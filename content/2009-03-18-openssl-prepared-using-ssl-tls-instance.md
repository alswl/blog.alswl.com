Title: 用openssl编写ssl,tls程序实例【转载-作者：yawl(yawl@nsfocus.com) 】
Author: alswl
Slug: openssl-prepared-using-ssl-tls-instance
Date: 2009-03-18 00:00:00
Tags: C, OpenSSL, SSL
Category: Coding

◆ 用openssl编写ssl,tls程序

作者：yawl(yawl@nsfocus.com)

日期：2000-8-15

一:简介:

ssl(secure socket layer)是netscape公司提出的主要用于web的安全通信标准,分为2.0版和3.0版.tls(transport
layer security)是ietf的tls工作组在ssl3.0基础之上提出的安全通信标准,目前版本是1.0,即rfc2246.ssl/tls提供的安全
机制可以保证应用层数据在互联网络传输不被监听,伪造和窜改.

openssl(www.openssl.org)是sslv2,sslv3,tlsv1的一份完整实现,内部包含了大量加密算法程序.其命令行提供了丰富的加密,验
证,证书生成等功能,甚至可以用其建立一个完整的ca.与其同时,它也提供了一套完整的库函数,可用开发用ssl/tls的通信程序. apache的https两种
版本mod_ssl和apachessl均基于它实现的.openssl继承于ssleay,并做了一定的扩展,当前的版本是0.9.5a.

openssl的缺点是文档太少,连一份完整的函数说明都没有,man page也至今没做完整:-(,如果想用它编程序,除了熟悉已有的文档(包括ssleay,m
od_ssl,apachessl的文档)外,可以到它的maillist上找相关的帖子,许多问题可以在以前的文章中找到答案.

编程:

程序分为两部分,客户端和服务器端,我们的目的是利用ssl/tls的特性保证通信双方能够互相验证对方身份(真实性),并保证数据的完整性,私密性.

1.客户端程序的框架为:

/*生成一个ssl结构*/

meth = sslv23_client_method();

ctx = ssl_ctx_new (meth);

ssl = ssl_new(ctx);

/*下面是正常的socket过程*/

fd = socket();

connect();

/*把建立好的socket和ssl结构联系起来*/

ssl_set_fd(ssl,fd);

/*ssl的握手过程*/

ssl_connect(ssl);

/*接下来用ssl_write(), ssl_read()代替原有的write(),read()即可*/

ssl_write(ssl,"hello world",strlen("hello world!"));

2.服务端程序的框架为:

/*生成一个ssl结构*/

meth = sslv23_server_method();

ctx = ssl_ctx_new (meth);

ssl = ssl_new(ctx);

/*下面是正常的socket过程*/

fd = socket();

bind();

listen();

accept();

/*把建立好的socket和ssl结构联系起来*/

ssl_set_fd(ssl,fd);

/*ssl的握手过程*/

ssl_connect(ssl);

/*接下来用ssl_write(), ssl_read()代替原有的write(),read()即可*/

ssl_read (ssl, buf, sizeof(buf));

根据rfc2246(tls1.0)整个tls(ssl)的流程如下:

client server

clienthello -------->

serverhello

certificate*

serverkeyexchange*

certificaterequest*

<-------- serverhellodone

certificate*

clientkeyexchange

certificateverify*

[changecipherspec]

finished -------->

[changecipherspec]

<-------- finished

application data <-------> application data

对程序来说,openssl将整个握手过程用一对函数体现,即客户端的ssl_connect和服务端的ssl_accept.而后的应用层数据交换则用ssl_re
ad和ssl_write来完成.

二:证书文件生成

除将程序编译成功外,还需生成必要的证书和私钥文件使双方能够成功验证对方,步骤如下:

1.首先要生成服务器端的私钥(key文件):

openssl genrsa -des3 -out server.key 1024

运行时会提示输入密码,此密码用于加密key文件(参数des3便是指加密算法,当然也可以选用其他你认为安全的算法.),以后每当需读取此文件(通过openssl
提供的命令或api)都需输入口令.如果觉得不方便,也可以去除这个口令,但一定要采取其他的保护措施!

去除key文件口令的命令:

openssl rsa -in server.key -out server.key

2.openssl req -new -key server.key -out server.csr

生成certificate signing
request,生成的csr文件交给ca签名后形成服务端自己的证书.屏幕上将有提示,依照其指示一步一步输入要求的个人信息即可.

3.对客户端也作同样的命令生成key及csr文件:

openssl genrsa -des3 -out client.key 1024

openssl req -new -key client.key -out client.csr

4.csr文件必须有ca的签名才可形成证书.可将此文件发送到verisign等地方由它验证,要交一大笔钱,何不自己做ca呢.

首先生成ca的key文件:

openssl -des3 -out ca.key 1024

在生成ca自签名的证书:

openssl req -new -x509 -key ca.key -out ca.crt

如果想让此证书有个期限,如一年,则加上"-days 365".

("如果非要为这个证书加上一个期限,我情愿是..一万年")

5.用生成的ca的证书为刚才生成的server.csr,client.csr文件签名:

可以用openssl中ca系列命令,但不是很好用(也不是多难,唉,一言难尽),一篇文章中推荐用mod_ssl中的sign.sh脚本,试了一下,确实方便了不少
,如果ca.csr存在的话,只需:

./sigh.sh server.csr

./sign.sh client.csr

相应的证书便生成了(后缀.crt).

现在我们所需的全部文件便生成了.

其实openssl中还附带了一个叫ca.pl的文件(在安装目录中的misc子目录下),可用其生成以上的文件,使用也比较方便,但此处就不作介绍了.

三:需要了解的一些函数:

1.int ssl_ctx_set_cipher_list(ssl_ctx *,const char *str);

根据ssl/tls规范,在clienthello中,客户端会提交一份自己能够支持的加密方法的列表,由服务端选择一种方法后在serverhello中通知服务端
,从而完成加密算法的协商.

可用的算法为:

edh-rsa-des-cbc3-sha

edh-dss-des-cbc3-sha

des-cbc3-sha

dhe-dss-rc4-sha

idea-cbc-sha

rc4-sha

rc4-md5

exp1024-dhe-dss-rc4-sha

exp1024-rc4-sha

exp1024-dhe-dss-des-cbc-sha

exp1024-des-cbc-sha

exp1024-rc2-cbc-md5

exp1024-rc4-md5

edh-rsa-des-cbc-sha

edh-dss-des-cbc-sha

des-cbc-sha

exp-edh-rsa-des-cbc-sha

exp-edh-dss-des-cbc-sha

exp-des-cbc-sha

exp-rc2-cbc-md5

exp-rc4-md5

这些算法按一定优先级排列,如果不作任何指定,将选用des-
cbc3-sha.用ssl_ctx_set_cipher_list可以指定自己希望用的算法(实际上只是提高其优先级,是否能使用还要看对方是否支持).

我们在程序中选用了rc4做加密,md5做消息摘要(先进行md5运算,后进行rc4加密).即

ssl_ctx_set_cipher_list(ctx,"rc4-md5");

在消息传输过程中采用对称加密(比公钥加密在速度上有极大的提高),其所用秘钥(shared
secret)在握手过程中中协商(每次对话过程均不同,在一次对话中都有可能有几次改变),并通过公钥加密的手段由客户端提交服务端.

2.void ssl_ctx_set_verify(ssl_ctx *ctx,int mode,int (*callback)(int,
x509_store_ctx *));

缺省mode是ssl_verify_none,如果想要验证对方的话,便要将此项变成ssl_verify_peer.ssl/tls中缺省只验证server,如
果没有设置ssl_verify_peer的话,客户端连证书都不会发过来.

3.int ssl_ctx_load_verify_locations(ssl_ctx *ctx, const char *cafile,const
char *capath);

要验证对方的话,当然装要有ca的证书了,此函数用来便是加载ca的证书文件的.

4.int ssl_ctx_use_certificate_file(ssl_ctx *ctx, const char *file, int type);

加载自己的证书文件.

5.int ssl_ctx_use_privatekey_file(ssl_ctx *ctx, const char *file, int type);

加载自己的私钥,以用于签名.

6.int ssl_ctx_check_private_key(ssl_ctx *ctx);

调用了以上两个函数后,自己检验一下证书与私钥是否配对.

7.void rand_seed(const void *buf,int num);

在win32的环境中client程序运行时出错(ssl_connect返回-1)的一个主要机制便是与unix平台下的随机数生成机制不同(握手的时候用的到).
具体描述可见mod_ssl的faq.解决办法就是调用此函数,其中buf应该为一随机的字符串,作为"seed".

还可以采用一下两个函数:

void rand_screen(void);

int rand_event(uint, wparam, lparam);

其中rand_screen()以屏幕内容作为"seed"产生随机数,rand_event可以捕获windows中的事件(event),以此为基础产生随机数.
如果一直有用户干预的话,用这种办法产生的随机数能够"更加随机",但如果机器一直没人理(如总停在登录画面),则每次都将产生同样的数字.

这几个函数都只在win32环境下编译时有用,各种unix下就不必调了.

大量其他的相关函数原型,见cryptorandrand.h.

8.openssl_add_ssl_algorithms()或ssleay_add_ssl_algorithms()

其实都是调用int ssl_library_init(void)

进行一些必要的初始化工作,用openssl编写ssl/tls程序的话第一句便应是它.

9.void ssl_load_error_strings(void );

如果想打印出一些方便阅读的调试信息的话,便要在一开始调用此函数.

10.void err_print_errors_fp(file *fp);

如果调用了ssl_load_error_strings()后,便可以随时用err_print_errors_fp()来打印错误信息了.

11.x509 *ssl_get_peer_certificate(ssl *s);

握手完成后,便可以用此函数从ssl结构中提取出对方的证书(此时证书得到且已经验证过了)整理成x509结构.

12.x509_name *x509_get_subject_name(x509 *a);

得到证书所有者的名字,参数可用通过ssl_get_peer_certificate()得到的x509对象.

13.x509_name *x509_get_issuer_name(x509 *a)

得到证书签署者(往往是ca)的名字,参数可用通过ssl_get_peer_certificate()得到的x509对象.

14.char *x509_name_oneline(x509_name *a,char *buf,int size);

将以上两个函数得到的对象变成字符型,以便打印出来.

15.ssl_method的构造函数,包括

ssl_method *tls

发表者：colorrain

/*****************************************************************************
**********

* eof - cli.cpp

***************************************************************************************/

/*****************************************************************************
**********

*ssl/tls服务端程序win32版(以demos/server.cpp为基础)

*需要用到动态连接库libeay32.dll,ssleay.dll,

*同时在setting中加入ws2_32.lib libeay32.lib ssleay32.lib,

*以上库文件在编译openssl后可在out32dll目录下找到,

*所需证书文件请参照文章自行生成.

***************************************************************************************/

#include <stdio.h>

#include <stdlib.h>

#include <memory.h>

#include <errno.h>

#include <sys/types.h>

#include <winsock2.h>

#include "openssl/rsa.h"

#include "openssl/crypto.h"

#include "openssl/x509.h"

#include "openssl/pem.h"

#include "openssl/ssl.h"

#include "openssl/err.h"

/*所有需要的参数信息都在此处以#define的形式提供*/

#define certf "server.crt" /*服务端的证书(需经ca签名)*/

#define keyf "server.key" /*服务端的私钥(建议加密存储)*/

#define cacert "ca.crt" /*ca 的证书*/

#define port 1111 /*准备绑定的端口*/

#define chk_null(x) if ((x)==null) exit (1)

#define chk_err(err,s) if ((err)==-1) { perror(s); exit(1); }

#define chk_ssl(err) if ((err)==-1) { err_print_errors_fp(stderr); exit(2); }

int main ()

{

int err;

int listen_sd;

int sd;

struct sockaddr_in sa_serv;

struct sockaddr_in sa_cli;

int client_len;

ssl_ctx* ctx;

ssl* ssl;

x509* client_cert;

char* str;

char buf [4096];

ssl_method *meth;

wsadata wsadata;

if(wsastartup(makeword(2,2),&wsadata) != 0){

printf("wsastartup()fail:%dn",getlasterror());

return -1;

}

ssl_load_error_strings(); /*为打印调试信息作准备*/

openssl_add_ssl_algorithms(); /*初始化*/

meth = tlsv1_server_method(); /*采用什么协议(sslv2/sslv3/tlsv1)在此指定*/

ctx = ssl_ctx_new (meth);

chk_null(ctx);

ssl_ctx_set_verify(ctx,ssl_verify_peer,null); /*验证与否*/

ssl_ctx_load_verify_locations(ctx,cacert,null); /*若验证,则放置ca证书*/

if (ssl_ctx_use_certificate_file(ctx, certf, ssl_filetype_pem) <= 0) {

err_print_errors_fp(stderr);

exit(3);

}

if (ssl_ctx_use_privatekey_file(ctx, keyf, ssl_filetype_pem) <= 0) {

err_print_errors_fp(stderr);

exit(4);

}

if (!ssl_ctx_check_private_key(ctx)) {

printf("private key does not match the certificate public keyn");

exit(5);

}

ssl_ctx_set_cipher_list(ctx,"rc4-md5");

/*开始正常的tcp socket过程.................................*/

printf("begin tcp socket...n");

listen_sd = socket (af_inet, sock_stream, 0);

chk_err(listen_sd, "socket");

memset (&sa_serv, , sizeof(sa_serv));

sa_serv.sin_family = af_inet;

sa_serv.sin_addr.s_addr = inaddr_any;

sa_serv.sin_port = htons (port);

err = bind(listen_sd, (struct sockaddr*) &sa_serv,

sizeof (sa_serv));

chk_err(err, "bind");

/*接受tcp链接*/

err = listen (listen_sd, 5);

chk_err(err, "listen");

client_len = sizeof(sa_cli);

sd = accept (listen_sd, (struct sockaddr*) &sa_cli, &client_len);

chk_err(sd, "accept");

closesocket (listen_sd);

printf ("connection from %lx, port %xn",

sa_cli.sin_addr.s_addr, sa_cli.sin_port);

/*tcp连接已建立,进行服务端的ssl过程. */

printf("begin server side ssln");

ssl = ssl_new (ctx);

chk_null(ssl);

ssl_set_fd (ssl, sd);

err = ssl_accept (ssl);

printf("ssl_accept finishedn");

chk_ssl(err);

/*打印所有加密算法的信息(可选)*/

printf ("ssl connection using %sn", ssl_get_cipher (ssl));

/*得到服务端的证书并打印些信息(可选) */

client_cert = ssl_get_peer_certificate (ssl);

if (client_cert != null) {

printf ("client certificate:n");

str = x509_name_oneline (x509_get_subject_name (client_cert), 0, 0);

chk_null(str);

printf ("t subject: %sn", str);

free (str);

str = x509_name_oneline (x509_get_issuer_name (client_cert), 0, 0);

chk_null(str);

printf ("t issuer: %sn", str);

free (str);

x509_free (client_cert);/*如不再需要,需将证书释放 */

}

else

printf ("client does not have certificate.n");

/* 数据交换开始,用ssl_write,ssl_read代替write,read */

err = ssl_read (ssl, buf, sizeof(buf) - 1);

chk_ssl(err);

buf[err] = ;

printf ("got %d chars:%sn", err, buf);

err = ssl_write (ssl, "i hear you.", strlen("i hear you."));

chk_ssl(err);

/* 收尾工作*/

shutdown (sd,2);

ssl_free (ssl);

ssl_ctx_free (ctx);

return 0;

}

/*****************************************************************

* eof - serv.cpp

*****************************************************************/

五.参考文献

1.ssl规范(draft302)

2.tls标准(rfc2246)

3.openssl源程序及文档

4.ssleay programmer reference

5.introducing ssl and certificates using ssleay

