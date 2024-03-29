---
title: "常见证书格式和转换【转载】"
author: "alswl"
slug: "common-certificate-format-and-conversion"
date: "2009-03-15T00:00:00+08:00"
tags: ["c", "ssl"]
categories: ["coding"]
---

这些文字都是转来转去，都找不到原作者是谁，唉````

仍然感谢作者的贡献....

PKCS 全称是 Public-Key Cryptography Standards ，是由 RSA
实验室与其它安全系统开发商为促进公钥密码的发展而制订的一系列标准，PKCS 目前共发布过 15 个标准。 常用的有：

PKCS#7 Cryptographic Message Syntax Standard

PKCS#10 Certification Request Standard

PKCS#12 Personal Information Exchange Syntax Standard

X.509是常见通用的证书格式。所有的证书都符合为Public Key Infrastructure (PKI) 制定的 ITU-T X509 国际标准。

PKCS#7 常用的后缀是： .P7B .P7C .SPC

PKCS#12 常用的后缀有： .P12 .PFX

X.509 DER 编码(ASCII)的后缀是： .DER .CER .CRT

X.509 PAM 编码(Base64)的后缀是： .PEM .CER .CRT

.cer/.crt是用于存放证书，它是2进制形式存放的，不含私钥。

.pem跟crt/cer的区别是它以Ascii来表示。

pfx/p12用于存放个人证书/私钥，他通常包含保护密码，2进制方式

p10是证书请求

p7r是CA对证书请求的回复，只用于导入

p7b以树状展示证书链(certificate chain)，同时也支持单个证书，不含私钥。

一 用openssl创建CA证书的RSA密钥(PEM格式)：

openssl genrsa -des3 -out ca.key 1024

二用openssl创建CA证书(PEM格式,假如有效期为一年)：

openssl req -new -x509 -days 365 -key ca.key -out ca.crt -config openssl.cnf

openssl是可以生成DER格式的CA证书的，最好用IE将PEM格式的CA证书转换成DER格式的CA证书。

三 x509到pfx

pkcs12 -export -in keys/client1.crt -inkey keys/client1.key -out
keys/client1.pfx

四 PEM格式的ca.key转换为Microsoft可以识别的pvk格式。

 pvk -in ca.key -out ca.pvk -nocrypt
-topvk

五 PKCS#12 到 PEM 的转换

openssl pkcs12 -nocerts -nodes -in cert.p12 -out private.pem

验证 openssl pkcs12 -clcerts -nokeys -in cert.p12 -out cert.pem

六 从 PFX 格式文件中提取私钥格式文件 (.key)

openssl pkcs12 -in mycert.pfx -nocerts -nodes -out mycert.key

七 转换 pem 到到 spc

openssl crl2pkcs7 -nocrl -certfile venus.pem -outform DER -out venus.spc

用 -outform -inform 指定 DER 还是 PAM 格式。例如：

openssl x509 -in Cert.pem -inform PEM -out cert.der -outform DER

八 PEM 到 PKCS#12 的转换，

openssl pkcs12 -export -in Cert.pem -out Cert.p12 -inkey key.pem

