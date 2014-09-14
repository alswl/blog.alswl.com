Title: 在 Python 中使用 epoll[译文]
Author: alswl
Slug: python-epoll
Date: 2013-01-12 00:01
Tags: Python, 译文
Category: Coding


原文地址： [http://scotdoyle.com/python-epoll-howto.html][source] ，
我这里取精简内容翻译过来。

============ 正文开始 ============ 

## 介绍 ##

Python 从 2.6 开始支持 [epoll][]。现在我们用 Python3 来写基于这些 API
的 epoll 范例。

<!-- more -->

## 阻塞的 Socket 通信范例 ##

``` python
import socket

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
response  = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
response += b'Hello, world!'

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('0.0.0.0', 8080))
serversocket.listen(1)

try:
   while True:
      connectiontoclient, address = serversocket.accept()
      request = b''
      while EOL1 not in request and EOL2 not in request:
          request += connectiontoclient.recv(1024)
      print('-'*40 + '\n' + request.decode()[:-2])
      connectiontoclient.send(response)
      connectiontoclient.close()
finally:
   serversocket.close()
```

这个范例中的代码在 `accept()` 、 `recv()` 和 `send()` 时候会发生阻塞，
导致其他连接无法完成。

通常情况下，在我们使用阻塞模型时候，会专门建立一个主线程来进行监听，
将建立成功的连接交给其他线程操作，然后继续在主线程上面监听。
这样一来，就不会受单次请求阻塞的限制。

[C10K][] 问题描述了其他处理高并发方法，比如异步 Socket，
通过监听事件来触发预设的响应。异步 Socket 可以是单线程，也可以是多线程。

Python 的 API 中包含了 select / poll / epoll，具体的可用性依赖于操作系统。
他们的效率是 epoll > poll > select，从这个 [性能测试文章][] 就可以看出来。

## epoll 异步编程范例 ##

epoll 的流程是这样的：

1. 创建 epoll 实例
1. 告诉 epoll 去监听哪几种类型事件
1. 向 epoll 查询最近已监听事件的变化
1. 根据不同的类型做不同的处理
1. 让 epoll 修改监听列表
1. 重复 3-5 直到结束
1. 消灭 epoll 实例

范例代码：

``` python
import socket, select

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
response  = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
response += b'Hello, world!'

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('0.0.0.0', 8080))
serversocket.listen(1)
serversocket.setblocking(0)

epoll = select.epoll()
epoll.register(serversocket.fileno(), select.EPOLLIN)

try:
   connections = {}; requests = {}; responses = {}
   while True:
      events = epoll.poll(1)
      for fileno, event in events:
         if fileno == serversocket.fileno():
            connection, address = serversocket.accept()
            connection.setblocking(0)
            epoll.register(connection.fileno(), select.EPOLLIN)
            connections[connection.fileno()] = connection
            requests[connection.fileno()] = b''
            responses[connection.fileno()] = response
         elif event & select.EPOLLIN:
            requests[fileno] += connections[fileno].recv(1024)
            if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
               epoll.modify(fileno, select.EPOLLOUT)
               print('-'*40 + '\n' + requests[fileno].decode()[:-2])
         elif event & select.EPOLLOUT:
            byteswritten = connections[fileno].send(responses[fileno])
            responses[fileno] = responses[fileno][byteswritten:]
            if len(responses[fileno]) == 0:
               epoll.modify(fileno, 0)
               connections[fileno].shutdown(socket.SHUT_RDWR)
         elif event & select.EPOLLHUP:
            epoll.unregister(fileno)
            connections[fileno].close()
            del connections[fileno]
finally:
   epoll.unregister(serversocket.fileno())
   epoll.close()
   serversocket.close()
```

最关键的几行如下：

* 16：注册感兴趣的事件
* 23：如果发现是监听 socket，则创建连接
* 30：读事件处理
* 33：读事件完成后，修改 epoll 对应的状态到写事件
* 35：写事件
* 41：释放对应的连接

Epoll 分边缘触发（edge-triggered）和水平触发（level-triggered）两种，
前者只被内核触发一次通知（除非状态被改变为未就绪），后者在触发后如果不做操作，
以后仍然会收到内核的触发通知。

## 更多优化 ##

### 连接等待池大小 ##

我们之前的代码直接使用 `listen()` 建立连接，可以通过设定一个队列大小，
在队列满了时候，就不再接受新的连接，从而保证已经接受的连接顺利完成。

### TCP 选项 ###

使用 [TCP\_CORK][] 功能，可以将小数据包封装成大包传输，提高效率。

[TCP\_NODELAY][] 则作用相反，将大包分成小包发送出去。比较适合实时应用比如 SSH。

（译者：[Linux下高性能网络编程中的几个TCP/IP选项][]介绍这几个 HTTP，写的不错。

范例中的源码在 [source code][] 下载。


[source]: http://scotdoyle.com/python-epoll-howto.html
[epoll]: http://linux.die.net/man/4/epoll
[C10K]: http://www.kegel.com/c10k.html
[性能测试文章]: http://lse.sourceforge.net/epoll/index.html
[TCP\_CORK]: http://www.baus.net/on-tcp_cork
[TCP\_NODELAY]: http://www.techrepublic.com/article/tcpip-options-for-high-performance-data-transmission/1050878
[Linux下高性能网络编程中的几个TCP/IP选项]: http://www.uplook.cn/blog/8/81276/
[source code]: http://scotdoyle.com/python-epoll-examples.tar.gz
