---
title: "配置SVN服务端"
author: "alswl"
slug: "svn-server-setup"
date: "2010-03-02T00:00:00+08:00"
tags: ["工欲善其事必先利其器", "svn"]
categories: ["efficiency"]
---

实在忍受不了VSS了，下决心自己在虚拟机配置一个SVN服务器，然后再在服务器上安装一个SVN服务器端。以前都是使用现成的SVN服务器，或者使用Google
Code提供的Project Host，今天就自己动手，丰衣足食吧。

话说VSS的确过时了，好多特性很麻烦，也难怪Louis嘲笑我Eclipse用VSS了～

## 什么是SVN服务器

**Subversion**，简称**SVN**，是一个开放源代码的版本控制系统（SCM），相对于的RCS、CVS，采
用了分支管理系统，它的设计目标就是取代CVS。互联网上越来越多的控制服务从CVS转移到Subversion。（via
[wiki](http://zh.wikipedia.org/zh-cn/Subversion)）

关于SVN / VSS / CVS等源代码管理系统已经有很多比较的文章了，我这里推荐几篇

[Better SCM Initiative : Comparison](http://better-
scm.berlios.de/comparison/comparison.html)
这篇是老外写的一篇各种SCM比较，内容相当翔实，可以作为论文参考资料了都

[SVN对比VSS,不知这样够了没 - 哥不是传说，是寂寞 -
博客园](http://www.cnblogs.com/yansc/archive/2008/09/27/1300954.html) 国人的一篇比较

## SVN服务端安装

Subversion官网已经迁移到Apache项目组下了，点击[Apache Subversion](http://subversion.apache.or
g/)访问Subversion官网，上面提供各个操作系统的版本下载，Windows环境下面分了**CollabNet **/ **Tigris.org
**/ **SlikSVN **/ **VisualSVN** 四个链接，我选择Tigris.org进行下载。

点击[Setup-
Subversion-1.6.6.msi](http://subversion.tigris.org/files/documents/15/46906
/Setup-Subversion-1.6.6.msi)下载截至2010-03-02的最新版

下载完之后，一路Next就可以安装完毕，使用 **svn --version** 测试一下能不能显示以下信息，如果可以，则说明安装没有问题了。

> C:Documents and SettingsAdministrator>svn --version

svn，版本 1.6.6 (r40053)

 编译于 Oct 26 2009，20:14:36

  
版权所有 (C) 2000-2009 CollabNet。

Subversion 是开放源代码软件，请参阅 http://subversion.tigris.org/ 站点。

此产品包含由 CollabNet(http://www.Collab.Net/) 开发的软件。

  
可使用以下的版本库访问模块:

  
* ra_neon : 通过 WebDAV 协议使用 neon 访问版本库的模块。  
 - 处理"http"方案

 - 处理"https"方案

* ra_svn : 使用 svn 网络协议访问版本库的模块。 - 使用 Cyrus SASL 认证  
 - 处理"svn"方案

* ra_local : 访问本地磁盘的版本库模块。  
 - 处理"file"方案

* ra_serf : 通过 WebDAV 协议使用 serf 访问版本库的模块。  
 - 处理"http"方案

 - 处理"https"方案

## SVN服务端的配置

1.手动创建一个文件夹，作为存储数据的地方，比如"`**c:repository**`"

2.在命令提示符下面输入`svnadmin create
c:repository`，如果执行正确的话，会在repository文件夹下形成4个文件夹2个文件。

3.执行`svnserve.exe -d -r c:repository`
来启动服务，在外部就能通过TortoiseSVN这些SVN客户端进行访问。关于TortoiseSVN使用，我会在之后的文章中整理出来。

使用上述第3个步骤运行SVN服务器会很麻烦，必须开着一个CMD窗口，通常，我们后将这个功能作为Windows的一个服务载入，这样就可以开机自动启动，不用人去
维护了。

执行脚本 `sc create svn binpath= ""C:Program FilesSubversionbinsvnserve.exe"
--service -r"C:repository"" displayname= "Subversion Server" depend= Tcpip
start= auto` 就可以将svnserve程序作为服务载入。关于sc命令，可以点击[这里](http://baike.baidu.com/view/
1367668.htm)查看更多。

## SVN服务器用户管理

设定SVN服务器用户的权限，需要修改 confsvnserve.conf 文件，如下所示

    
    [general]
    # password-db = passwd
    # anon-access = none
    # auth-access = write
    # authz-db = authz
    # realm = My First Repository 

去之每行开头的#，其中第二行是指定身份验证的文件名，即passwd文件.a access = none
是匿名用户不能访问，必须要有用户名和密码。（注意：问这，一定要注意格式去掉注释后要顶格不能有空）

用户管理相当简单，只需要在confpasswd中打开相应的权限，之后在confpasswd 加入用户就可以了。

    
    [users]
    # harry = harryssecret
    # sally = sallyssecret
    alswl = alswl
    jason = jason

格式为"用户名 = 密码"，如可插入一行：mm = mm，即为系统添加一个mm，密码为mm的用户。（注意顶格写不要有空隙）

用户权限管理，如果是简单模式，可以直接将 confsvnserve.conf 中的 **authz-db = authz** 前面加上 #
即可，关于详细的权限分组管理，我现在还一知半解，等我搞明白再分享…… --_--#

## 参考链接

[SVN服务端的配置 - Svn中文网](http://www.svn8.com/svnsy/20090606/6224.html)
我今天所有看的文章中最详细准确的一篇

[Subversion 安装与配置 - Panda -
CSDN博客](http://blog.csdn.net/songrun/archive/2008/11/29/3410428.aspx)

[windows安装基于Apache的SVN服务器(包括SSL配置)[2007-8-19更新] - Windows下Subversion安装使用 -
SVN中文论坛](http://www.iusesvn.com/bbs/thread-158-1-1.html) 这篇虽然老，但是条理很清晰

## 参考书籍

[使用Subversion进行版本控制](http://www.subversion.org.cn/svnbook/)

> 这是使用Subversion进行版本控制在 Subversion中文站的在线主页，本书的在线主页在[http://svnbook.red-
bean.com/](http://svnbook.red-bean.com/)。 这是一本关于
[Subversion](http://subversion.tigris.org/)的 [自
由](http://www.subversion.org.cn/svnbook/1.4/svn.copyright.html)图书
[Subversion](http://subversion.tigris.org/)，Subversion
被设计为CVS的替代产品。你可能从本页的布局上也猜到了，本书通过[O'Reilly
Media](http://www.oreilly.com/catalog/0596004486/)出版。

传送门-[PDF版本下载](http://www.subversion.org.cn/svnbook/1.4/svnbook.pdf)

