---
title: "用OpenSSL生成证书"
author: "alswl"
slug: "using-openssl-to-generate-certificates"
date: "2009-03-15T00:00:00+08:00"
tags: ["c", "openssl", "ssl"]
categories: ["coding"]
---

这些命令虽然是linux下面的，但是在windows下面也能用

我遇到I am unable to access the ./demoCA/newcerts directory ./demoCA/newcerts: No
such file or directory 然后找到这篇文章，只要用生成相应的目录就可以了。

我遇到的第二个问题是TXT_DB error number 2 在redhat的网站[kbase.redhat.com/faq/docs/DOC-3624](http://kbase.redhat.com/faq/docs/DOC-3624)这篇文章。

我将原来index.txt里面的内容剪切出，然后重新签证，再把剪切出的内容粘贴到后来生成文件之前，就解决了那个问题。

下面是网上的资料：OpenSSL相关命令[hi.baidu.com/kobetec/blog/item/706fc0440ff3b44a510ffe0b.html](http://hi.baidu.com/kobetec/blog/item/706fc0440ff3b44a510ffe0b.html)

这个是一个不错的资料参考，就转载过来，谢谢原作者

命令操作：

　　1、生成普通私钥：

[weigw@TEST src]$ openssl genrsa -out privatekey.key 1024

Generating RSA private key, 1024 bit long modulus ....++++++ .......++++++ e
is 65537 (0x10001)


2、生成带加密口令的密钥：

  

[weigw@TEST src]$ openssl genrsa -des3 -out privatekey.key 1024

Generating RSA private key, 1024 bit long modulus ............++++++
.....................++++++ e is 65537 (0x10001) Enter pass phrase for
privatekey.key: Verifying - Enter pass phrase for privatekey.key:



在生成带加密口令的密钥时需要自己去输入密码。对于为密钥加密现在提供了一下几种算法：

-des encrypt the generated key with DES in cbc mode 

-des3 encrypt the generated key with DES in ede cbc mode (168 bit key) 

-aes128, -aes192, -aes256 encrypt PEM output with cbc aes


去除密钥的口令：

[weigw@TEST src]$ openssl rsa -in privatekey.key -out

privatekey.key Enter pass phrase for privatekey.key: writing RSA key



通过生成的私钥去生成证书：

  

[weigw@TEST src]$ openssl req -new -x509 -key privatekey.key -out cacert.crt
-days 1095

You are about to be asked to enter information that will be incorporated into
your certificate request.

What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank For some fields
there will be a default value, If you enter '.', the field will be left blank.

-----

Country Name (2 letter code) [GB]:CN

State or Province Name (full name) [Berkshire]:beijing

Locality Name (eg, city) [Newbury]:beijing

Organization Name (eg, company) [My Company Ltd]:wondersoft

Organizational Unit Name (eg, section) []:develop

Common Name (eg, your name or your server's hostname) []:WeiGW

Email Address []:weigongwan@sina.com

在生成证书的时候需要按照提示输入一些个人信息。


通过私钥生成公钥：

  

[weigw@TEST src]$ openssl rsa -in privatekey.key -pubout -out pubkey.key
writing RSA key


格式转换：（证书、私钥、公钥）（PEM <----->DER）

  

[weigw@TEST src]$ openssl x509 -in cacert.crt -inform PEM -out cacert.der
-outform DER

[weigw@TEST src]$

  

[weigw@TEST src]$ openssl rsa -in privatekey.key -inform PEM -out
privatekey.der -outform DER

writing RSA key

  

[weigw@TEST src]$ openssl rsa -pubin -in pubkey.key -inform PEM -pubout -out
pubkey.der -outform DER

writing RSA key


从DER格式转换成PEM格式一样，就是把inform的格式改成DERoutform的格式改成PEM即可。

  

下面是一个服务器和客户端认证的证书、私钥生成方法：（server.crt、client.crt、ca.crt）


第一步： 生成私钥


    [weigw@TEST bin]$ openssl genrsa -out server.key 1024    Generating RSA private key, 1024 bit long modulus .++++++ .. .........++++++ e is 65537 (0x10001)    [weigw@TEST bin]$ openssl genrsa -out client.key 1024    Generating RSA private key, 1024 bit long modulus ...++++++ ...... ..........++++++ e is 65537 (0x10001)    [weigw@TEST bin]$ openssl genrsa -out ca.key 1024  Generating RSA private key, 1024 bit long modulus ....... ..++++++ .........++++++ e is 65537 (0x10001)    [weigw@TEST bin]$

　　第三步： 申请证书（为请求文件签名）

[weigw@TEST bin]$ openssl ca -in server.csr -out server.crt -cert ca.crt
-keyfile ca.key

[weigw@TEST bin]$ openssl ca -in client.csr -out client.crt -cert ca.crt
-keyfile ca.key


如果在这步出现错误信息：

  

[weigw@TEST bin]$ openssl ca -in client.csr -out client.crt -cert ca.crt
-keyfile ca.key

Using configuration from /usr/share/ssl/openssl.cnf I am unable to access the
./demoCA/newcerts directory ./demoCA/newcerts: No such file or directory

[weigw@TEST bin]$


自己手动创建一个CA目录结构：

[weigw@TEST bin]$ mkdir ./demoCA

[weigw@TEST bin]$ mkdir demoCA/newcerts

创建个空文件：

[weigw@TEST bin]$ vi demoCA/index.txt

向文件中写入01：

[weigw@TEST bin]$ vi demoCA/serial


合并证书文件（crt）和私钥文件（key）：

  

[weigw@TEST bin]$ cat client.crt client.key > client.pem [weigw@TEST bin]$ cat
server.crt server.key > server.pem


合并成pfx证书：

  

[weigw@TEST bin]$ openssl pkcs12 -export -clcerts -in client.crt -inkey
client.key -out client.p12

Enter Export Password:

Verifying - Enter Export Password:

[weigw@TEST bin]$openssl pkcs12 -export -clcerts -in server.crt -inkey
server.key -out server.p12

Enter Export Password:

Verifying - Enter Export Password:


文本化证书：

  

[weigw@TEST bin]$ openssl pkcs12 -in client.p12 -out client.txt Enter Import
Password:

MAC verified OK

Enter PEM pass phrase: Verifying - Enter PEM pass phrase:

[weigw@TEST bin]$openssl pkcs12 -in server.p12 -out server.txt

Enter Import Password:

MAC verified OK

Enter PEM pass phrase: Verifying - Enter PEM pass phrase:


屏幕模式显式：（证书、私钥、公钥）

  

[weigw@TEST bin]$ openssl x509 -in client.crt -noout -text -modulus

[weigw@TEST bin]$ openssl rsa -in server.key -noout -text -modulus

[weigw@TEST bin]$ openssl rsa -in server.pub -noout -text -modulus


得到DH：

  

[weigw@TEST bin]$ openssl dhparam -out dh1024.pem 1024

  

