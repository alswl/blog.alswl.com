---
title: "python+django MTV框架 和php MVC框架"
author: "alswl"
slug: "python-django-mtv-framework-and-php-mvc-framework"
date: "2009-10-01T00:00:00+08:00"
tags: ["综合技术", "django", "mtv", "mvc"]
categories: ["coding"]
---

首先，祝福祖国60华诞，我爱这个国家。

刚才在GR读到[Here Comes The Sun](http://www.classicning.com)的[A shorten url app](http://www.classicning.com/blog/2009/09/a-shorten-url-app/-shorten-url-
app/)，其中提到了Python下Django框架的一些问题，我很感兴趣，搜索了一下MTV模型，资料很少。但有一篇我读后很有启发，现在转载如下。

原文链接：[python+django MTV框架 和php MVC框架的不同之处 - PHP+MYSQL+APACHE -ThinkPHP官方论坛](http://bbs.thinkphp.cn/viewthread.php?tid=5022)

作者：乔峰

******************残酷的分割线*****************

## python+django MTV框架 和php MVC框架的不同之处

最近学习了python语言和djangoMTV框架，感觉用的很爽啊。这里给大家粗略的介绍一下。

Django是一个开放源代码的Web应用框架，由Python写成。采用了MTV的设计模式，即模型M，模版T和视图控制器V。它最初是被开发来用于管理劳伦斯出版
集团旗下的一些以新闻内容为主的网站的。并于2005年7月在BSD许可证下发布。这套框架是以比利时的吉普赛爵士吉他手Django Reinhardt来命名的。

Django的主要目标是使得开发复杂的、数据库驱动的网站变得简单。Django注重组件的重用性和「可插拔性」，敏捷开发和DRY法则（Don't Repeat
Yourself）。在Django中Python被普遍使用，甚至包括配置文件和数据模型。

关键一点是Django框架把控制层(Ctronl layer)给封装了，无非与数据交互这层都是数据库表的读,写,删除,更新的操作.在写程序的时候，只要调用方
法就行了.感觉很方便.用户可以用很少的代码完成很多的事情.代码可读性强.运行的速度比php要快.

python是嵌入式的语言,它可以把C和JAVA语言的写的东西结合在一起.也难怪Google公司主导议语言用python,c++,java的比较多.大的公司
比较重视系统管理和总体的架构.

有人说最有发展的语言是python,不过都值得大家去探讨的.因为结果都很预料,前段时间闹的很热的是Ruby语言,Ruby刚出来时,传说也很了得,现在看起来也
不怎么行了.

## Python的前景

Python在编程领域的占有率一直处于稳步上升之中，根据最新的数据，Python排名第七。前六名分别是Java,C,VB,C++,PHP和Perl.
作为一个很年轻的语言，Python的位置已经相当令人振奋了。随着微软将Python纳入.Net 平台，相信Python的将来会更加强劲发展。Python
很可能会成为.Net平台快速开发的主流语言。

欲了解这方面情况，请参考Iron Python的相关信息.

著名的搜索引擎 Google 也大量使用Python。 现在中国的搜狐(sohu)网站邮箱系统也是用python开发的.更加令人吃惊的是，在Nokia智能手
机所采用的Symbian操作系统上，Python成为继C++,Java之后的第三个编程语言！可见Python的影响力之巨大。

我在学python语言和django MTV框架的一点体会,拿来教程,都说该语言如何简单易学,都是乱说,入门很简单,想要学深点,都不容易的.

个人感觉还是学PHP入门时最简单,不过现在弄出哪么框架,组件,也变得越来越不简单,PHP也越来越像JAVA的儿子JSP(当然PHP是C语言的儿子),个人觉得
他们越来越接近,但又有好多差异.

python语言不仅可以做WEB应用,而且可以做桌面,服务器软件和手机软件开发(有的诺基亚手机系统就是用python做的),而PHP专注做WEB 应用的,P
HP开发祖师也为PHP为什么不能转向照顾到做桌面,服务器软件和手机软件开发的应用听说也苦耐了好久,但最终没能成功转型.哪是因为他们在最初的底层定位搞死了(网
上评论观点).

不过我看到网上语言排名,PHP在Python之前,也说明PHP在近期表现不俗.

我喜欢用Python,Django,也很喜欢用php,thinkphp,特别是升级后的1.5版,但是可不可也做成MTV的框架模式呢.用精良的代码完成很多工作
.加快开发速度呢.大家都要努力哦.加油兄弟们.

### 2楼回复：

美國太空總署NASA使用Python，Google使用Python，Youtube使用Python.阿里巴巴也用python开发,搜狐邮箱是用python2
.6开发的

### 5楼回复：

MVC与MTV有什么不同呢.

大家都知道

MVC 中的M是代表MODLE层,V代表VIEW层,C代表Contrl层.

MTV 中的M是代表MODLE层,T代表Template(模板层),V代表VIEW层.

Django 是MTV模式框架,它把Control控制层容合到   Django 框架里边了,

程序员把  Control控制层东西交给Django自动完成了,  只需要编写非常少的代码完成很多的事情.所以,它比MVC框架考虑的问题要深一步.因为我们程
序员大都写程序在Contrl层,现在这个工作交给了框架,仅需写很少的调用代码,自然工作效率就提高了.

