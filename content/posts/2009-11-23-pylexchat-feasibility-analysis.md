---
title: "PylexChat可行性分析"
author: "alswl"
slug: "pylexchat-feasibility-analysis"
date: "2009-11-23T00:00:00+08:00"
tags: ["flash", "air", "flex", "gae", "pylexchat"]
categories: ["coding"]
---

## PylexChat介绍

PylexChat取名自**Python**+**Flex**+**Chat**部
分缩写，这就意味着这个系统是基于Python+Flex的聊天系统。之所以做这个系统，源自我大学的最后一次课程设计，我不想浪费这最后一次可以供我发
挥自己想象力的机会。年后估计要参加工作了，毕业设计也不敢做这么有想法的课程设计。那就最后一次潇洒一下，做一个我完全没有接触过的东西。

我几乎不会Python，是最近一个月迷上这门强悍而简单的语言，我完全不会Flex，是最近1周时间才开始接触Flex。这意味着这次课程设计的
风险挺大。我花了几天的时间做了详细的可行性分析，分析了系统框架和GAE能够提供的服务和限制以及Flex/AIR能做的内容，否决了几个方案，最后总
结了一篇简单可行性分析（本文是一周时间慢慢形成的，并没有遵循正规的开发文档风格）。

## 几个基本的概念

内容出自[维基百科](http://zh.wikipedia.org/)

### Python

Python，是一种面向对象、直译式计算机程序设计语言，也是一种功能强大而完善的通用型语言，已经具有十多年的发展历史，成熟且稳定。

这种语言具有非常简捷而清晰的语法特点，适合完成各种高层任务，几乎可以在所有的操作系统中运行。

目前，基于这种语言的相关技术正在飞速的发展，用户数量急剧扩大，相关的资源非常多。

### Flex

Adobe Flex是最初由Macromedia公司在2004年3月发布的，基于其专有的Macromedia Flash平台，它是涵盖了支持RIA（Rich
Internet Applications）的开发和部署的一系列技术组合。

FLEX支持创建静态文件，该文件使用解释编译方式并且不需要购买服务器许可证就可以在线部署。

Flex的目标是让程序员更快更简单地开发RIA应用。在多层式开发模型中，Flex应用属于表现层。

Flex 采用GUI界面开发，使用基于XML的MXML语言。Flex 具有多种组件，可实现Web Services，远程对象，drag and
drop，列排序，图表等功能；FLEX内建动画效果和其它简单互动界面等。相对于基于HTML的应用（如PHP、ASP、JSP、ColdFusion
及CFMX等）在每个请求时都需要执行服务器端的模板，由于客户端只需要载入一次，FLEX应用程序的工作流被大大改善。FLEX的语言和文件结构也试图
把应用程序的逻辑从设计中分离出来。

Flex 服务器也是客户端和XML Web Services及远程对象（Coldfusion CFCs，或Java类，等支持Action Message
Format的其他对象）之间通讯的通路。

### AIR

dobe AIR（AIR＝Adobe Integrated Runtime），开发代号为Apollo，是一个跨操作系统runtime
environment用来建造RIA，使用Flash、Flex、HTML与AJAX，可能部署为桌面应用程式。

AIR是Adobe针对网络与桌面应用的结合所开发出来的技术，可以不必经由浏览器而对网络上的云端程式做控制，也由于这是Adobe所开发的技术，因此能很顺利的与
Adobe旗下的Photoshop、Flash、Firework等应用程式来进行开发。

### Google App Engine

Google App Engine是一个开发、托管网络应用程序的平台，使用Google管理的数据中心。它在2008年4月发布了第一个beta版本。

Google App Engine使用了云计算技术。它跨越多个服务器和数据中心来虚拟化应用程序。 其他基于云的平台还有Amazon Web
Services和微软的Azure服务平台等。

Google App Engine在用户使用一定的资源时是免费的。支付额外的费用可以获得应用程序所需的更多的存储空间、带宽或是CPU负载。

## 系统需要实现的功能

我简单罗列一下：登录、群聊、私聊、注册（功能实现优先级由高到低排列）。

功能着实有点简单，不过这个系统的亮点在于跨平台，而不是功能的强大。我在设计时候会尽量考虑多些东西，方便以后扩展。

## 数据交互实现方案

系统最主要也最难实现的部分是数据交互如何进行有效的交互。我总结了一下几种方法。

### 1.TCP/IP通信

一般的C/S模式程序都会考虑套接字连接方式，这是性能最高的交互方式。使用TCP/IP协议，能够有效的避免Python/Flex语言带来的数据交换问题。我查阅
了Flex文档，在`flash.net.Socket`下有套接字使用的API，这说明Flex在套接字支持上没有问题。接下来我查阅了GAE的文档，资料比较难找
，最后我查阅了[沙盒](http://code.google.com/intl/zh-CN/appengine/docs/java/runtime.html
#The_Sandbox)的定义、Python/Java在GAE的限制（参考文献-[Will it play in App
Engine](http://groups.google.com/group/google-appengine-java/web/will-it-play-
in-app-engine)），确定GAE不支持套接字和多线程。引用文字如下：[

](http://groups.google.com/group/google-appengine-java/web/will-it-play-in-
app-engine)

> #### 沙盒

>

> 为了使得 App Engine
能够跨多个网络服务器分配对于应用程序的请求，并且防止应用程序彼此干扰，请在受限制的"沙盒"环境中运行应用程序。在这种环境中，该应用程序可执行代
码；可存储和查询 App Engine 数据存储区中的数据；可使用 App Engine 邮件、网址抓取和用户服务；可检查用户的网络请求以及准备响应。

>

> App Engine 应用程序无法：

>

>   * 向文件系统写入。应用程序必须使用 [App Engine 数据存储区](http://code.google.com/appengine/doc
s/java/datastore/)存储永久数据。允许从文件系统中读取，并且可使用与该应用程序一起上传的所有应用程序文件。

>   * 打开套接字或直接访问另一主机。应用程序可使用 [App Engine
网址抓取服务](http://code.google.com/appengine/docs/java/urlfetch/)分别向端口 80 和 443
上的其他主机发出 HTTP 和 HTTPS 请求。

>   * 产生子进程或线程。必须在几秒钟内于单个进程中处理对应用程序的网络请求。响应时间很长的进程会被终止，以避免使网络服务器负载过重。

>   * 进行其他类型的系统调用。

>

> ##### 线程

>

> Java 应用程序无法新建 `java.lang.ThreadGroup` 或 `java.lang.Thread`。这些限制也适用于利用线程的 JRE
类。例如，应用程序无法新建 `java.util.concurrent.ThreadPoolExecutor` 或
`java.util.Timer`。应用程序可以对当前线程执行操作，如 `Thread.currentThread().dumpStack()`。

>

> ##### 文件系统

>

> Java 应用程序无法使用任何用来写入文件系统的类，如 `java.io.FileWriter`。应用程序可以使用诸如
`java.io.FileReader` 的类从文件系统中读取自己的文件。应用程序也可以通过例如 `Class.getResource()` 或
`ServletContext.getResource()` 来访问作为"资源"的自身文件。

>

> 只有视为"资源文件"的文件才可以由应用程序通过文件系统访问。默认情况下，WAR 中的所有文件都是"资源文件"。您可以使用 [appengine-
web.xml](http://code.google.com/intl/zh-
CN/appengine/docs/java/config/appconfig.html) 文件将文件从该组中排除出去。

>

> ##### java.lang.System

>

> 禁用不适用于 App Engine 的 `java.lang.System` 类的功能。

>

> 以下 `System` 方法在 App Engine
中不起作用：`exit()`、`gc()`、`runFinalization()`、`runFinalizersOnExit()`

>

> 以下 `System` 方法返回 `null`：`inheritedChannel()`、`console()`

>

> 应用程序无法提供或直接调用任何本机 JNI 代码。以下 `System` 方法引发
`java.lang.SecurityException`：`load()`、`loadLibrary()`、`setSecurityManager()`

>

> ##### 反射

>

> 允许应用程序对自己的类进行完全、无限制的反射访问。它可以查询任何私有成员，使用
`java.lang.reflect.AccessibleObject.setAccessible()`，以及读取/设置私有成员。

>

> 应用程序还可以对 JRE 和 API 类（如 `java.lang.String` 和 `javax.servlet.http.HttpServletR
equest`）进行反射。但是，它只可以访问这些类的公共成员，而不可以访问受保护成员或私有成员。

>

> 应用程序无法对不属于自己的任何其他类进行反射，也无法使用 `setAccessible()` 方法来避开这些限制。

>

> ##### 自定义类载入

>

> App Engine 完全支持自定义类载入。但是请注意，App Engine 将覆盖所有的
ClassLoader，以将相同的权限分配给所有由应用程序载入的类。如果执行自定义类载入，在载入不信任的第三方代码时要小心。

> #### 有没有 Google App Engine 不支持的 Python 库？

>

> 只有很少一部分本机 C python 模块以及本机 C python 模块的子集不受 Google App Engine 支持。详述了本机 C
Python 模块支持的完整列表可在[此处](http://code.google.com/intl/zh-
CN/appengine/kb/libraries.html)找到。被禁用的模块属于以下类别：

>

>   * 用于维护磁盘上数据存储区的库未在 Google App Engine 的 Python 中启用

>   * Google App Engine 禁用套接字

>   * 系统不允许您调用子进程，结果某些操作系统模块方法被禁用

>   * 线程不可用

>   * 由于安全方面的原因，大多数基于 C 的模块都被禁用

>   * 其他受限制的功能：

>     * 封送已禁用

>     * cPickle 又名 pickle

>     * 系统调用已禁用

>

> 请记住，使用以上任意一种功能的第三方包（如 mysql、postgresql 等）都将无法在 Google App Engine 上运行。

根据Google App Engine的文档描述，在云计算提供的服务器集群中，无法提供套接字和多线程的使用，这也是可以
遇见的，毕竟这么多服务器集群如果要实现套接字和多线程的同步，几乎是不可能完成的任务。

### 使用Web Service/XML通信

Flex对Web Service/XML提供了原生的支持，也支持RPC协议（[什么是RPC](http://zh.wikipedia.org/zh-
cn/RPC)），也可以使用一种AMF(Action Message Format)的一种二进制协议来交换数据。我查看了《Flex
3权威指南》的一些范例代码，实现这些协议需要的操作步骤略多，但是能支持复杂的对象传送。

考虑到我接触Python/Flex的时间和经验，这种方式显然风险很大，我只能略过这个方案。

### 使用Ajax Poiling方式通信

如果写过Ajax聊天室的童鞋们应该很轻松理解这种Poiling方式，即频繁的向服务器发送post请求（通常是1s），然后读取返回数据来进行数据交换。这种方式
适合数据格式简单的通信，不适宜大文件的传送。

这个方案简单易操作，加上我之前对Web前段也有一些学习，在技术上只要攻克Python/Flex难关，就有一定可行性了。

采用Ajax
Poiling方式完全是基于Http协议，这个GAE能够完美支持，Flex在`flash.net.*`下也有很多对应的方法进行操作，实现应该没有问题。

## 数据库的实现

在系统的后期，如果时间充裕，会考虑加入数据库的支持，实现简单的注册/登录和聊天记录存储。

GAE支持的数据库是BigTable，使用一种GQL的操作语言，与普通的关系型数据库还是有一些区别。下面是wiki的介绍

> BigTable is a compressed, high performance, and proprietary database system
built on Google File System (GFS), Chubby Lock Service, and a few other Google
programs; it is currently not distributed or used outside of Google, although
Google offers access to it as part of their Google App Engine.

直接加入BigTable支持我怕会导致整个项目拖延，所以如果顺利则加入数据库支持，如果不顺利则放到以后再实现。

## 相关链接

PylexChat in Google Project Host:
[http://code.google.com/p/pylexchat/](http://code.google.com/p/pylexchat/)

PylexChat in GAE:
[http://pylexchat.appspot.com/](http://pylexchat.appspot.com/)

先给出上面的网址，还没彻底部署好。

