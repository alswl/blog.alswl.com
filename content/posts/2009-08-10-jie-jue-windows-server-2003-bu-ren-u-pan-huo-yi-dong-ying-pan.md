---
title: "解决windows server 2003不认U盘或移动硬盘"
author: "alswl"
slug: "jie-jue-windows-server-2003-bu-ren-u-pan-huo-yi-dong-ying-pan"
date: "2009-08-10T00:00:00+08:00"
tags: ["技术达人", "windows"]
categories: ["efficiency"]
---

今天总监给我配了一台电脑，是HP的服务器，志强的X3210处理器。这样以后再也不用背着电脑翻墙了~

在这台服务器里发现了Visual Studio 2008 Team System，这好东西啊，不用自己下，我赶紧找移动硬盘来考它。

试了好一会，Windows Server
2003都没有认出这个移动硬盘，显示正确的，就是不出现盘符。我一度认为自己的移动硬盘又出了事情，最好发现原来是Windows Server
2003使用移动硬盘盒Linux一样，需要加载一下。

相关链接《[解决windows server 2003不认U盘或移动硬盘_蓝色天空](http://hi.baidu.com/cheng_allen/blo
g/item/5a46d307004a05c97a894746.html)》

### 快速解决的2个办法:

#### 一、U盘以及移动硬盘自动装载也是一样的，WINDOWS2003具体配置方法如下：

1、进入命令提示符环境(也就是DOS)

2、进入DISKPART程序

3、输入AUTOMOUNT ENABLE指令

4、OK，下次USB硬盘接入后就可以像XP 一样自动装载了。

#### 二、在我的电脑上右健－－管理－－磁盘管理－－你会看到你的移动硬，右健为你的移动硬盘

指定一个盘符就认出来了。

如有特殊或其它情况：

1:供电不足,把两个接头全插上.

2:没有分配盘符. 在桌面我的电脑上点右键--管理--存储--磁盘管理 里面给你的移动硬盘分配盘符.

