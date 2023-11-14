


前段时间学习 Redis 时候，听到 hiredis 的大名，正好也在做异步的学习，就找来代码学习一下。
我几乎不太会 C，仅限于最简单的语法，完全没有在生产环境中写过，
所以先看个 Client 简单代码，下次看 Memcached 代码应该会更顺畅一些。

Hiredis 是用 C 写的 Redis 客户端，对 Redis 协议进行了简单的封装，
同时提供了同步和异步的两种 API。Hiredis 的代码位于
[https://github.com/redis/hiredis](https://github.com/redis/hiredis)。

<!-- more -->

## 一分钟使用入门 ##

同步 API 的调用方法：

```
redisContext *context = redisConnect("127.0.0.1", 6379);
reply = redisCommand(context, "SET foo %s", value);	
printf("PING: %s\n", reply->str);
freeReplyObject(reply)
redisFree(context);
```

Redis ae 异步 API 的调用方法，使用 Redis 自己的 ae 事件库，
至于为什么 Redis 没有使用 libevent 或者 libev，可以参考
[Reason](http://groups.google.com/group/redis-db/browse_thread/thread/b52814e9ef15b8d0/)，
[中文翻译](http://blog.csdn.net/archimedes_zht/article/details/6909074)：

```
void connectCallback(const redisAsyncContext *c, int status) {
    printf("Connected...\n");
}

void disconnectCallback(const redisAsyncContext *c, int status) {
    printf("Disconnected...\n");
}
void getCallback(redisAsyncContext *c, void *r, void *privdata) {
    redisReply *reply = r;
    if (reply == NULL) return;
    printf("argv[%s]: %s\n", (char*)privdata, reply->str);
    redisAsyncDisconnect(c);
}

redisAsyncContext *c = redisAsyncConnect("127.0.0.1", 6379);
loop = aeCreateEventLoop();
redisAeAttach(loop, c);
redisAsyncSetConnectCallback(c,connectCallback);
redisAsyncSetDisconnectCallback(c,disconnectCallback);

redisAsyncCommand(c, getCallback, (char*)"end-1", "GET key");
```

Libev 异步 API 调用，因为 `adapters/*.h` 封装的好，所以几乎和 ae 调用一致：

```
void connectCallback(const redisAsyncContext *c, int status) {
    printf("Connected...\n");
}
void disconnectCallback(const redisAsyncContext *c, int status) {
    printf("Disconnected...\n");
}
void getCallback(redisAsyncContext *c, void *r, void *privdata) {
    redisReply *reply = r;
    if (reply == NULL) return;
    printf("argv[%s]: %s\n", (char*)privdata, reply->str);

    /* Disconnect after receiving the reply to GET */
    redisAsyncDisconnect(c);
}

redisAsyncContext *c = redisAsyncConnect("127.0.0.1", 6379);
redisLibevAttach(EV_DEFAULT_ c);
redisAsyncSetConnectCallback(c,connectCallback);
redisAsyncSetDisconnectCallback(c,disconnectCallback);
redisAsyncCommand(c, getCallback, (char*)"end-1", "GET key");
```

Hiredis 还支持使用 libevent，我就不列出来了。

详细的使用 example 可以看
[https://github.com/redis/hiredis/tree/master/examples](https://github.com/redis/hiredis/tree/master/examples)。

## 主要结构 ##

* redisReply
* redisReader
* redisContext

## 流程 ##


### 同步连接 ###

同步连接的代码在 `hiredis.c` 和 `net.c` 中。

`redisConnect` / `redisConnectWithTimeout` / `redisConnectNonBlock` 都调用了
`net.c` 里面的 `redisContextConnectTcp`。使用 `fcntl(fd, F_SETFL, flags)`
设置是否阻塞连接。

`O_NONBLOCK` 即 Socket 非阻塞模式，但仍然是同步的哦。

事实上，无论阻塞还是非阻塞，hiredis 都会使用非阻塞（poll）来
`connect` 连接服务器，会返回 -1，并且 `errno`
为 `EINPROGRESS`，这是非阻塞模式正常的表现。
为什么阻塞模式也会强制使用非阻塞的 `poll` 连接？其实是为了能够支持 timeout 功能。
hiredis 在连接成功之后，按照之前需求重新设定为阻塞或者非阻塞模式。

关于如何设计超时功能，可以参考 [http://blog.csdn.net/ast_224/article/details/2957294](http://blog.csdn.net/ast_224/article/details/2957294)。

### 命令 ###

使用 va\_list 解决变参问题（C 也支持变长参数，被惊呆了，我果然是 C 盲啊）。
```
int redisFormatCommand(char **target, const char *format, ...) {
	va_list ap;
	int len;
	va_start(ap,format);
}
```

`redisvCommand` 用来执行阻塞Redis 命令，它会调用 `__redisBlockForReply`，
内部调用 `redisBufferWrite` 从 socket 写 buffer，然后同步等待，从
`redisBufferRead` 读数据，用 `redisGetReplyFromReader` 解析返回数据。

### 异步连接 ###

异步调用的代码在 `async.c` 中，我先看 ae 库。

重要的结构是 `redisAsyncContext` 和 `redisAeEvents`，前者重要的方法是注册回调函数：
`addRead` / `delRead` / `addWrite` / `delWrite`，后者是用来存放 loop / fd / event stream
的。

异步连接时候，仍然使用 `redisContextConnectTcp` 来发起到服务器的非阻塞连接。

使用 `aeCreateEventLoop` 创建一个事件循环，然后使用 `redisAeAttach` 给
`context` 注册事件，比如说 `aeCreateFileEvent(loop,e->fd,AE_READABLE,redisAeReadEvent,e)`
就注册了一个 `read` 事件，并将 callback 调用设置到 `redisAeReadEvent`，
`redisAeReadEvent` 再将这个事件托管给 `redisAsyncHandleRead`（定义在 async.c 里面，
被三个 event 库调用）。

所以，hiredis 通过 adapter 的封装，屏蔽了 ae / libevent / libev 的 API 差异，
从而可以灵活的选择。据说 ae 是从两个 libevent 库重写过来的，可是我觉得 ae
的风格和 libev 比较像，而 libevent 的风格比较好理解。

如果拿这段代码的复杂度和 Tornado 的 IOLoop 进行对比，真实感觉 Tornado 那段 API
封装太人性化了，C 的代码写起来好复杂，系统 API、资源控制、错误控制都挺麻烦。

Redis ae 事件库的分析可以参考 [http://my.oschina.net/u/917596/blog/161077#OSC_h4_6](http://my.oschina.net/u/917596/blog/161077#OSC_h4_6)。
Libevent 的一个简单教程 [http://www.wangafu.net/~nickm/libevent-book/01_intro.html](http://www.wangafu.net/~nickm/libevent-book/01_intro.html)。

## 关于 C ##

作为 C 渣的我，勉强读完 hiredis，感觉那点 C 基础完全不够用，
稍微将学习过程中疑惑的地方罗列一下：

* `IFDEF` 使用，可以防止重复导入同一个头文件定义，这里有一个详细的解释
[http://faculty.cs.niu.edu/~mcmahon/CS241/c241man/node90.html](http://faculty.cs.niu.edu/~mcmahon/CS241/c241man/node90.html)
* `__cplusplus`: C++ 里面定义了这个变量，而 C 没有定义，所以当 C++ 编译器识别
source 时候，通过这个加上 `ifdef` 来使用 `extern` 编译 C 代码。
* long long: long 只能存放 32 位，long long 可以存放 64 位长度，即 0 - 2^64-1。
* `c->flags |= REDIS_BLOCK` / `c->flags &= ~REDIS_BLOCK;` 简洁的位操作。
* sds（simple dynamic string）是 Redis 自己实现的 C String 字符串结构。
* `((void)fd)` 好像是将 fd 指针转成无类型的指针，不知道有什么用处。

