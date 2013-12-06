Title: 用OpenSSL创建证书时用到的命令【原创】
Author: alswl
Slug: using-openssl-to-create-certificates-using-the-command
Date: 2009-03-17 00:00:00
Tags: OpenSSL, SSL
Category: C
Summary: 

这几天在弄OpenSSL需要使用的证书，翻了很多文档，找来一《本OpenSSL与网络信息安全-
基础、结构和指令》，书上的密码学和OpenSSL的基础介绍的很详细，但是缺少一些实例。

这证书死活做不出来，最后在《计算机网络高级软件编程技术》上第19章"利用OpenSSL实现安全的Web Server"中找到自己需要的内容，现在分享一下。

1.生成CA中心的私钥

>openssl req -newkey rsa:1024 -sha1 -keyout rootkey.pem -out rootreq.pem

2.生成CA中心的自签证书

>openssl x509 -req -in rootreq.pem -sha1 -extensions v3_ca -days 365 -signkey
rootkey.pem -out rootcert.pem

3.生成A分支机构的私钥和认证请求

>openssl req -newkey rsa:1024 -sha1 -keyout Akey.pem -out Areq.pem

PS:如果出现 Unable to load config info from c:/openssl/ssl/openssl.cnf
的错误提示，说明系统环境没有配置好，找不到Openssl.cnf配置文件

那么这时候可以把命令修改为： openssl req -newkey rsa:1024 -sha1 -keyout Akey.pem -out
Areq.pem -config D:StudyOpenSSLopenssl-0.9.8jappsopenssl.cnf

注意：这个 openssl.cnf 文件定位根据自己的OpenSSL位置修改。

4.由CA中心为A分支机构签发证书

>openssl x509 -req -in Areq.pem -sha1 -extensions usr_cert -CA rootcert.pem
-CAkey rootkey.pem -CAcreateserial -out Acert.pem

5.用x509命令查看生成的证书

>openssl x509 -subject -issuer -noout -in rootcert.pem

这样之后，Acert.pem就是所要使用的证书文件，Akey.pem是私钥文件，rootcert.pem是信任CA

供朋友们参考

