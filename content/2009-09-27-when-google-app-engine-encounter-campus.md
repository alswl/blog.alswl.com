Title: 当Google APP Engine遇上校内
Author: alswl
Slug: when-google-app-engine-encounter-campus
Date: 2009-09-27 00:00:00
Tags: GAE, 人人
Category: Python编程

昨天看《[程序员](http://www.csdn.net)》时候看到一篇讲开放接口的文章，是FaceBook的一个开发人员写的，讲了很多关于开放平台的东西
。其中提到Google App Engine的云计算支持，FaceBook的FBML（校内的称为XNML，一种标记性语言）。

## Google App Engine(GAE)

Google App Engine让用户可以在 Google 的基础架构上运行的网络应用程序。Google App Engine
应用程序易于构建和维护，并可根据用户的访问量和数据存储需要的增长轻松扩展。使用 Google App
Engine，将不再需要维护服务器：用户只需上传用户的应用程序，它便可立即为用户的用户提供服务。

通俗的说，App Engine就像是免费提供的一个500M高性能的空间，和一个appspot.com二级域名。在Google强大的云计算能力下，服务器的速度
和质量毋容置疑。现在App Engine支持Python和Java（似乎Java有些限制，具体的细节我没有看）。

## XNML

XNML（xiao nei market
language）是以种标记性语言，如果学过JavaEE，就会发现它和OGNL语言很像。XNML大概的形式是<xnml:iframe
….>这种形式，校内服务器会负责解析这种格式的语法生成相应的内容。其实这是把一些功能性内容封装成接口，为了安全和方便。

在校内提供的开发平台写应用需要自己的一个地址，肯定不能是192.168.0.X这种本机地址了。这时候Google App
Engine就派上了大用场，把应用的文件和数据存储在GAE里，那是相当的爽，可以放心的开发自己的第三方应用了。

我一直对开放平台的开发有兴趣，现在有了GAE这个利器，正好写一个自己的小应用玩玩，顺便练习练习自己的Python。

## 相关链接：

校内开发者（校内开发人员必须安装的应用）：[http://app.renren.com/developers/home.do](http://app.ren
ren.com/developers/home.do)

校内开放平台文档：[http://wiki.dev.renren.com/wiki/%E9%A6%96%E9%A1%B5](http://wiki.dev.
renren.com/wiki/%E9%A6%96%E9%A1%B5)

Google App Engine相关下载：[http://code.google.com/appengine/downloads.html](http:/
/code.google.com/appengine/downloads.html)

Google App Engine SDK for Python-Win：[GoogleAppEngine_1.2.5.msi](http://google
appengine.googlecode.com/files/GoogleAppEngine_1.2.5.msi)

Google App Engine SDK for Java：[appengine-java-
sdk-1.2.5.zip](http://googleappengine.googlecode.com/files/appengine-java-
sdk-1.2.5.zip)

Google App Engine Documentation：[google-appengine-
docs-20090921.zip](http://googleappengine.googlecode.com/files/google-
appengine-docs-20090921.zip)

最后一个小图标：![Powered by Google App
Engine](http://code.google.com/appengine/images/appengine-silver-
120x30.gif)，呵呵，Google的图标都那么帅

