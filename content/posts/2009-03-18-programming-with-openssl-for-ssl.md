---
title: "用openssl进行SSL编程【转载-月光】"
author: "alswl"
slug: "programming-with-openssl-for-ssl"
date: "2009-03-18T00:00:00+08:00"
tags: ["c", "openssl", "ssl"]
categories: ["coding"]

---

主要介绍openssl进行SSL通信的一些函数以及过程，主要是初始化过程，至于数据的接收以及后续处理可以具体问题具体分析。

load所有的SSL算法

OpenSSL_add_ssl_algorithms();

建立SSL所用的method

SSL_METHOD *meth=SSLv23_method();

初始化上下文情景

SSL_CTX *ctx=SSL_CTX_new(meth);

ret->quiet_shutdown=1;默认的是ret->quiet_shutdown=0;他相当于SSL_set_shutdown函数将参数设置为SS
L_SENT_SHUTDOWN|SSL_RECEIVED_SHUTDOWN

当设置为1时，假如关闭后，不通知对方，这样不适合TLS标准

SSL_CTX_set_quiet_shutdown(ctx,1);

ctx->options|=SSL_OP_ALL，SSL/TLS有几个公认的bug,这样设置会使出错的可能更小

SSL_CTX_set_options(ctx,SSL_OP_ALL);

设置cache的大小，默认的为1024*20=20000，这个也就是可以存多少个session_id，一般都不需要更改的。假如为0的话将是无限

SSL_CTX_sess_set_cache_size(ctx,128);

SSL_CTX_load_verify_locations用于加载受信任的CA证书，CAfile如果不为NULL，则他指向的文件包含PEM编码格式的一个或多
个证书，可以用e.g.来简要介绍证书内容

CApath如果不为NULL，则它指向一个包含PEM格式的CA证书的目录，目录中每个文件包含一份CA证书，文件名是证书中CA名的HASH值

可以用c-rehash来建立该目录，如cd /some/where/certs（包含了很多可信任的CA证书） c_rehash .。返回一成功，0
失败。SSL_CTX_set_default_verify_paths找寻默认的验证路径，在这里肯定找不到的。

这里主要set cert_store

char *CAfile=NULL,*CApath=NULL;

SSL_CTX_load_verify_locations(ctx,CAfile,CApath);

当需要客户端验证的时候，服务器把CAfile里面的可信任CA证书发往客户端。

if(CAfile !=NULL
)SSL_CTX_set_client_CA_list(ctx,SSL_load_client_CA_file(CAfile));

设置最大的验证用户证书的上级数。

SSL_CTX_set_verify_depth(ctx,10);

当使用RSA算法鉴别的时候，会有一个临时的DH密钥磋商发生。这样会话数据将用这个临时的密钥加密，而证书中的密钥中做为签名。

所以这样增强了安全性，临时密钥是在会话结束消失的，所以就是获取了全部信息也无法把通信内容给解密出来。

static unsigned char dh512_p[]={

0xDA,0x58,0x3C,0x16,0xD9,0x85,0x22,0x89,0xD0,0xE4,0xAF,0x75,

0x6F,0x4C,0xCA,0x92,0xDD,0x4B,0xE5,0x33,0xB8,0x04,0xFB,0x0F,

0xED,0x94,0xEF,0x9C,0x8A,0x44,0x03,0xED,0x57,0x46,0x50,0xD3,

0x69,0x99,0xDB,0x29,0xD7,0x76,0x27,0x6B,0xA2,0xD3,0xD4,0x12,

0xE2,0x18,0xF4,0xDD,0x1E,0x08,0x4C,0xF6,0xD8,0x00,0x3E,0x7C,

0x47,0x74,0xE8,0x33,

};

static unsigned char dh512_g[]={0x02,};

DH *dh=DH_new();

dh->p=BN_bin2bn(dh512_p,sizeof(dh512_p),NULL);

dh->g=BN_bin2bn(dh512_g,sizeof(dh512_g),NULL);

SSL_CTX_set_tmp_dh(ctx,dh);

下面加载服务器的证书和私钥，私钥可以和证书在一个文件之中。判断私钥和证书是否匹配。

char *s_cert_file="server.pem";

char *s_key_file=NULL;

SSL_CTX_use_certificate_file(ctx,s_cert_file,SSL_FILETYPE_PEM);

获取私钥之前先把私钥的密码给写上

char *pKeyPasswd="serve";

SSL_CTX_set_default_passwd_cb_userdata(ctx, pKeyPasswd);

SSL_CTX_use_PrivateKey_file(ctx,s_cert_file,SSL_FILETYPE_PEM);

SSL_CTX_check_private_key(ctx);

设置一个临时的RSA，在出口算法中，有规定需要这么做的。

RSA *rsa=RSA_generate_key(512,RSA_F4,NULL,NULL);

SSL_CTX_set_tmp_rsa(ctx,rsa);

用于设置验证方式。s_server_verify是以下值的逻辑或

SSL_VERIFY_NONE表示不验证，SSL_VERIFY_PEER用于客户端时要求服务器必须提供证书，用于服务器时服务器会发出证书请求消息要求客户端提
供证书，但是客户端也可以不提供

SSL_VERIGY_FAIL_IF_NO_PEER_CERT只适用于服务器且必须提供证书。他必须与SSL_VERIFY_PEER一起使用

当SSL_VERIFY_PEER被设置时verify_callback可以控制验证的行为。任何一个验证失败信息都会终止TLS连接

static int s_server_verify=SSL_VERIFY_NONE;

SSL_CTX_set_verify(ctx,SSL_VERIFY_PEER,NULL/*verify_callback*/);

为了从自己本身的程序中产生一个session_id，所以要给本程序设定一个session_id_context，否则程序从外部获取session_id_co
ntext来得到session_id，那很容易产生错误

长度不能大于SSL_MAX_SSL_SESSION_ID_LENGTH

const unsigned char s_server_session_id_context[100]="1111asdfd";

SSL_CTX_set_session_id_context(ctx,s_server_session_id_context,sizeof
s_server_session_id_context);

return ctx;

