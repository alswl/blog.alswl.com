Title: OpenSSL中的BIO【转载】
Author: alswl
Slug: openssl-s-bio
Date: 2009-03-19 00:00:00
Tags: OpenSSL, SSL
Category: C
Summary: 

SSL类型的BIO

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; ---根据openssl
doccryptobio_f_ssl.pod翻译和自己的理解写成

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; （作者：DragonKing,
Mail: wzhah@263.net ,发布于：http://openssl.126.com 之openssl专业论坛）

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; 从名字就可以看出，这是一个非常重要的BI
O类型，它封装了openssl里面的ssl规则和函数，相当于提供了一个使用SSL很好的有效工具，一个很好的助手。其定义（opensslbio.h,opens
slssl.h）如下：

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
BIO_METHOD *BIO_f_ssl(void);

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
#define BIO_set_ssl(b,ssl,c) BIO_ctrl(b,BIO_C_SET_SSL,c,(char *)ssl)

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
#define BIO_get_ssl(b,sslp) BIO_ctrl(b,BIO_C_GET_SSL,0,(char *)sslp)

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
#define BIO_set_ssl_mode(b,client) BIO_ctrl(b,BIO_C_SSL_MODE,client,NULL)

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
#define BIO_set_ssl_renegotiate_bytes(b,num)
BIO_ctrl(b,BIO_C_SET_SSL_RENEGOTIATE_BYTES,num,NULL);

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
#define BIO_set_ssl_renegotiate_timeout(b,seconds)
BIO_ctrl(b,BIO_C_SET_SSL_RENEGOTIATE_TIMEOUT,seconds,NULL);

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
#define BIO_get_num_renegotiates(b)
BIO_ctrl(b,BIO_C_SET_SSL_NUM_RENEGOTIATES,0,NULL);

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
BIO *BIO_new_ssl(SSL_CTX *ctx,int client);

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
BIO *BIO_new_ssl_connect(SSL_CTX *ctx);

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
BIO *BIO_new_buffer_ssl_connect(SSL_CTX *ctx);

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
int BIO_ssl_copy_session_id(BIO *to,BIO *from);

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
void BIO_ssl_shutdown(BIO *bio);

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
#define BIO_do_handshake(b) BIO_ctrl(b,BIO_C_DO_STATE_MACHINE,0,NULL)

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
该类型BIO的实现文件在sslbio_ssl.c里面，大家可以参看这个文件得到详细的函数实现信息。

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; 【BIO_f_ssl】

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
该函数返回一个SSL类型的BIO_METHOD结构，其定义如下：

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; static BIO_METHOD
methods_sslp=

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; {

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
BIO_TYPE_SSL,"ssl",

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
ssl_write,

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
ssl_read,

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
ssl_puts,

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
NULL, /* ssl_gets, */

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
ssl_ctrl,

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
ssl_new,

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
ssl_free,

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
ssl_callback_ctrl,

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
};

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
可见，SSL类型BIO不支持BIO_gets的功能。

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; BIO_read和BIO_write函数
调用的时候，SSL类型的BIO会使用SSL协议进行底层的I/O操作。如果此时SSL连接并没有建立，那么就会在调用第一个IO函数的时候先进行连接的建立。

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
如果使用BIO_push将一个BIO附加到一个SSL类型的BIO上，那么SSL类型的BIO读写数据的时候，它会被自动调用。

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; BIO_reset调用的时候，会调用SS
L_shutdown函数关闭目前所有处于连接状态的SSL，然后再对下一个BIO调用BIO_reset，这功能一般就是将底层的传输连接断开。调用完成之后，SS
L类型的BIO就处于初始的接受或连接状态。

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
如果设置了BIO关闭标志，那么SSL类型BIO释放的时候，内部的SSL结构也会被SSL_free函数释放。

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; 【BIO_set_ssl】

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
该函数设置SSL类型BIO的内部ssl指针指向ssl，同时使用参数c设置了关闭标志。

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; 【BIO_get_ssl】

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
该函数返回SSL类型BIO的内部的SSL结构指针，得到该指针后，可以使用标志的SSL函数对它进行操作。

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; 【BIO_set_ssl_mode】

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
该函数设置SSL的工作模式，如果参数client是1，那么SSL工作模式为客户端模式，如果client为0，那么SSL工作模式为服务器模式。

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
【BIO_set_ssl_renegotiate_bytes】

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; 该函数设置需要重新进行session协商
的读写数据的长度为num。当设置完成后，在没读写的数据一共到达num字节后，SSL连接就会自动重新进行session协商，这可以加强SSL连接的安全性。参数
num最少为512字节。

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
【BIO_set_ssl_renegotiate_timeout】

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
该函数跟上述函数一样都是为了加强SSL连接的安全性的。不同的是，该函数采用的参数是时间。该函数设置重新进行session协商的时间，其单位是秒。当SSL
session连接建立的时间到达其设置的时间时，连接就会自动重新进行session协商。

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
【BIO_get_num_renegotiates】

&nbsp_place_holder;&nbsp_place_holder;
该函数返回SSL连接在因为字节限制或时间限制导致session重新协商之前总共读写的数据长度。

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; 【BIO_new_ssl】

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
该函数使用ctx参数所代表的SSL_CTX结构创建一个SSL类型的BIO，如果参数client为非零值，就使用客户端模式。

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
【BIO_new_ssl_connect】

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
该函数创建一个包含SSL类型BIO的新BIO链，并在后面附加了一个连接类型的BIO。

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; 方便而且有趣的是，因为在filter类型
的BIO里，如果是该BIO不知道（没有实现）BIO_ctrl操作，它会自动把该操作传到下一个BIO进行调用，所以我们可以在调用本函数得到BIO上直接调用BI
O_set_host函数来设置服务器名字和端口，而不需要先找到连接BIO。

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
【BIO_new_buffer_ssl_connect】

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
创建一个包含buffer型的BIO，一个SSL类型的BIO以及一个连接类型的BIO。

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
【BIO_ssl_copy_session_id】

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; 该函数将BIO链from的SSL
Session
ID拷贝到BIO链to中。事实上，它是通过查找到两个BIO链中的SSL类型BIO，然后调用SSL_copy_session_id来完成操作的。

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; 【BIO_ssl_shutdown】

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
该函数关闭一个BIO链中的SSL连接。事实上，该函数通过查找到该BIO链中的SSL类型BIO，然后调用SSL_shutdown函数关闭其内部的SSL指针。

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; 【BIO_do_handshake】

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; 该函数在相关的BIO上启动SSL握手过程
并建立SSL连接。连接成功建立返回1，否则返回0或负值，如果连接BIO是非阻塞型的BIO，此时可以调用BIO_should_retry函数以决定释放需要重试
。如果调用该函数的时候SSL连接已经建立了，那么该函数不会做任何事情。一般情况下，应用程序不需要直接调用本函数，除非你希望将握手过程跟其它IO操作分离开来。

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
需要注意的是，如果底层是阻塞型（openssl帮助文档写的是非阻塞型,non blocking,但是根据上下文意思已经BIO的其它性质，我个人认为是阻塞型，
blocking才是正确的）的BIO，在一些意外的情况SSL类型BIO下也会发出意外的重试请求，如在执行BIO_read操作的时候如果启动了session重
新协商的过程就会发生这种情况。在0.9.6和以后的版本，可以通过SSL的标志SSL_AUTO_RETRY将该类行为禁止，这样设置之后，使用阻塞型传输的SSL
类型BIO就永远不会发出重试的请求。

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; 【例子】

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
1.一个SSL/TLS客户端的例子，完成从一个SSL/TLS服务器返回一个页面的功能。其中IO操作的方法跟连接类型BIO里面的例子是相同的。

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
BIO *sbio, *out;

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
int len;

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
char tmpbuf[1024];

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
SSL_CTX *ctx;

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
SSL *ssl;

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
ERR_load_crypto_strings();

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
ERR_load_SSL_strings();

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
OpenSSL_add_all_algorithms();

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
//如果系统平台不支持自动进行随机数种子的设置，这里应该进行设置(seed PRNG)

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
ctx = SSL_CTX_new(SSLv23_client_method());

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
//通常应该在这里设置一些验证路径和模式等，因为这里没有设置，所以该例子可以跟使用任意CA签发证书的任意服务器建立连接

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
sbio = BIO_new_ssl_connect(ctx);

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
BIO_get_ssl(sbio, &ssl);

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
if(!ssl) {

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
fprintf(stderr, "Can't locate SSL pointern");

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; }

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
/* 不需要任何重试请求*/

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
SSL_set_mode(ssl, SSL_MODE_AUTO_RETRY);

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
//这里你可以添加对SSL的其它一些设置

