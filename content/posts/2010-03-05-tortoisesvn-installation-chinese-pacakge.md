---
title: "TortoiseSVN中文版安装"
author: "alswl"
slug: "tortoisesvn-installation-chinese-pacakge"
date: "2010-03-05T00:00:00+08:00"
tags: ["工欲善其事必先利其器", "svn", "tortoisesvn"]
categories: ["efficiency"]
---

虽然大部分情况下我都是用Subclipse连接SVN服务器，但是为了让整个团队在Delphi下使用上SVN，就需要使用SVN的客户端了，TortoiseSV
N是目前比较流行的SVN客户端，目前最新版是1.6.7。

传送门之-[TortoiseSVN-1.6.7.18415-win32-svn-1.6.9.msi](http://downloads.sourceforg
e.net/tortoisesvn/TortoiseSVN-1.6.7.18415-win32-svn-1.6.9.msi?download)

下面是一片TortoiseSVN中文版的安装方法，转载过来。

原文出处：[TortoiseSVN 中文版 安装 -Svn中文网](http://www.svn8.com/svnpz/20090622/6696.html)

××××______××××[](http://www.svn8.com/svnpz/20090622/6696.html)

TortoiseSVN 是 Subversion 版本控制系统的一个免费开源客户端，可以超越时间的管理文件和目录。

如果是新安装,可以到
[http://tortoisesvn.net/downloads](http://tortoisesvn.net/downloads)
下载最新版本.一般32位安装版和64位安装版.另外按安装方式来分会分为msi与GnuPG.
GnuPG这东西对于很多人来说不怎么熟识.而且在windows下,我只下载msi的安装文件

先把TortoiseSVN安装好.安装基本上是点下一步就完成了.所以在这里就赘述了。

安装包里面默认语言是英语,对于很多中国人来说使用英语还是不怎么习惯. 不过TortoiseSVN是多语言软件,他会有一个中文包,还是在
[http://tortoisesvn.net/downloads](http://tortoisesvn.net/downloads)
下载下了需要的语言包安装.安装完后,不用重启,可以在setting里面的语言设计里找到刚才安装的语言.

可能出现的问题

1,安装语言包失败 或者 安装语言包后没有中文选项

如果没有选项就是代表安装失败,原因可能是版本不对,例如我下载的TortoiseSVN的安装文件名是TortoiseSVN-
1.6.2.16344-win32-svn-1.6.2.msi,就是说我安装的文件我是1.6.2版本,然后更新版本号是16344.语言包的安装文
件也是类似这样.LanguagePack_1.6.2.16344-win32-zh_CN.msi,软件版是1.6.2,更新版本号是16344.只
要软件版跟更新版对得上.基本上不会出现问题.所以安装前先确认这两个版号.

2,对于已经安装旧版的TortoiseSVN的人来说,可能已经找不到语言包的安装了.

不过没有关系,可以自己重写一下载的url http://sourceforge.net/project/downloading.php?groupname=tortoisesvn&filename=LanguagePack_1.6.2.16344-win32-zh_CN.msi&use_mirror=nchc
看url很容易 看出来filenamer=后面的就是我们需要下载的文件名.而且文件名都很有规则.

只要TortoiseSVN的 about us里就会看到以下的内容了。

我的TortoiseSVN的版是TortoiseSVN 1.5.1, Build 13563 - 32 Bit 。我只需要把上面的url改成下面的就可以了 
http://sourceforge.net/project/downloading.php?groupname=tortoisesvn&filename=
LanguagePack_1.5.1.13563-win32-zh_CN.msi&use_mirror=nchc

