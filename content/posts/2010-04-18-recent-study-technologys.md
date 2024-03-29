---
title: "最近在学的技术"
author: "alswl"
slug: "recent-study-technologys"
date: "2010-04-18T00:00:00+08:00"
tags: ["java", "esb", "ibatis", "jaas", "javase", "mule", "testing", "tiles"]
categories: ["coding"]
---

根据这篇日志的题目，必然是一篇水文，我思量再三，还是把它放出来，这些技术的接触把我带入了另一个广阔的天堂。这是我学Java以来的第二个里程碑。

使用Java1年半，1年前开始JSP编程，一直是我和周围的朋友自己摸索，学校没有开Java课，也没有参加什么培训课程，面对庞大的Java开源分支，我一直摸索
，不能登堂入室。

万分感谢倪经理这1个月来的教导，他给了我一个不一样的Java。

### iBatis

如果说Hibernate是一款自动化的导弹，那么iBatis则是一款轻型的半自动步枪，简介、高效、方便配置。加上iBator这个神器，iBatis可以使开发
效率几倍提升。

年前开始学习iBatis，想借其思想自己完成一个简单的ORM系统，3月份时候，公司的一个新框架采用了iBatis，更是给我提供了一个绝佳的Playgroun
d。Hibernate和iBatis有各自的适合使用的领域，不能单纯的说谁好谁不好，不过iBatis绝对值得尝试。

动软的.net生成器使用的DAL接入层也是使用的iBats.net做数据接入。

### Jaas

我对权限控制的理解，从最早的单表用户字段管理，到贴吧的基于角色权限控制，直到后来公司使用的基于权限+菜单控制，最好到现在的Jaas提供的资源-角色-权限-
菜单 控制体系。细化到原子级的权限控制带来了莫大的好处，这个很大程度归功于Jaas。

> Java Authentication Authorization Service（JAAS，Java验证和授权API）提供了灵活和可伸缩的机制来保证客
户端或服务器端的Java程序。Java早期的安全框架强调的是通过验证代码的来源和作者，保护用户避免受到下载下来的代码的攻击。JAAS强调的是通过验证谁在运行
代码以及他／她的权限来保护系统面受用户的攻击。它让你能够将一些标准的安全机制，例如Solaris NIS（网络信息服务）、Windows
NT、LDAP（轻量目录存取协议），Kerberos等通过一种通用的，可配置的方式集成到系统中。

我对这套权限系统的学习还不透彻，还有很多地方需要琢磨和研究，学无止境啊。

### ESB

很惭愧，知道现在才知道这个名词，ESB的思想其实在很多地方得到了灌输，我一直自认经常会跟进主流技术，现在才发现果然还是自己道行不够。

> ESB全称为Enterprise Service
Bus，即企业服务总线。它是传统中间件技术与XML、Web服务等技术结合的产物。ESB提供了网络中最基本的连接中枢，是构筑企业神经系统的必要元素

>

> ESB的出现改变了传统的软件架构，可以提供比传统中间件产品更为廉价的解决方案，同时它还可以消除不同应用之间的技术差异，让不同的应用服务器协调运作，实现了
不同服务之间的通信与整合。从功能上看，ESB提供了事件驱动和文档导向的处理模式，以及分布式的运行管理机制，它支持基于内容的路由和过滤，具备了复杂数据的传输能
力，并可以提供一系列的标准接口。

### Mule

Mule是一个企业服务总线(ESB)消息框架，也就是上面所说的ESB的一个开源框架实现。Mule的优势体现在：

1.基于J2EE1.4的企业消息总线(ESB)和消息代理(broker).

2.可插入的连接性:比如 Jms,jdbc,tcp,udp,multicast,http,servlet,smtp,pop3, file,xmpp等.

3.支持任何传输之上的异步，同步和请求响应事件处理机制.

4.支持Axis或者Glue的Web Service.

5.灵活的部署结构 [Topologies]包括Client/Server, P2P, ESB 和Enterprise Service Network.

6. 与Spring 框架集成:可用作ESB 容器，也可以很容易的嵌入到Spring应用中.

7.使用基于SEDA处理模型的高度可伸缩的企业服务器.

8.强大的基于EIP模式的事件路由机制等.

Mule发布最新版本1.1，这个发布包括集成了JBI，对 BPEL的支持,还增加一些新的传输器(transport)Quartz,FTP,RMI与EJB等。

### Tiles

我之前认识是<include>已经是一种比较好的页面实现方式，Tiles的出现粉碎了我的认识。Tiles框架提供了一种模板机制，模板定义了网页的布局，同一模
板可以被多个Web页面共用。通过配置文件进行协调，把页面文件的分层应用到极致。

> Apache Tiles 是一个创建简单的网络应用用户界面的模板框架，Tiles让用户可以在运行中使用定义好的小模块装配成完整的页面。

>

> 采用基本的JSP语句创建复合式网页 -> 采用JSP的include指令创建复合式网页 -> 采用Tiles:Insert标签创建复合式网页 ->
采用Tiles模板创建复合式网页

### Web压力测试

这是我在翻阅大学里软件工程课孙老师给05届毕业生的PPT时候发现的内容。PPT体面推荐了3种Web压力测试工具。

Web Application Stress Tool, Microsoft

[JMeter, Java Apache Project](http://jakarta.apache.org/jmeter/)

[LoadItUp, BroadGun Software](http://www.broadgun.com)

上述三种，我只试用了JMeter，还在继续研究中。

### Web测试自动化

这也是从那堆PPT中学习的东西，我把他们列到我的GTD计划中，还没来得及实现。

#### [Watir

](http://wtr.rubyforge.org/)

一个使用 Ruby 实现的开源Web 自动化测试框架。

#### [Selenium

](http://selenium.openqa.org/)

ThoughtWorks 专门为 Web 应用而开发的自动化测试工具，适合进行功能测试、验收测试 。

#### [jWebUnit

](http://jwebunit.sourceforge.net/)

为 Web 应用程序创建测试用例的一个开源框架，它可以容易地插入到大多数 Java IDE 中。

### Last

啥也不说了，埋头学习吧～

路漫漫其修远兮，吾将上下而求索。

