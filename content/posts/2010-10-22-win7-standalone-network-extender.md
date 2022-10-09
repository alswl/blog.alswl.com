---
title: "在Win7上面使用Standalone Network Extender"
author: "alswl"
slug: "win7-standalone-network-extender"
date: "2010-10-22T00:00:00+08:00"
tags: ["技术达人", "win7"]
categories: ["efficiency"]
---

用Win7大概1个月了，的确很不错，本来试用的心态变成了完全不想回到XP时代了。

Win7的UAC比Vista已有很大的进步，至少不是那么烦心了，但是仍然很多场合都不能与以前旧版本的一些软件配合默契。

比如公司用的这款VPN软件-Standalone Network Extender。

这款软件是Billion BiGuard公司推出的SSL产品，通过IE载入一个Active插件来连接公司内网。我在以前XP时候很轻松连入，先在却死活无法连接
成功。我看了一下版本：build:Sep 7 2009-14:06:08，在[Billion
BiGuard公司](http://www.biguard.com)的主页也没有找到适合Win7的新版本。

我猜测VPN软件需要修改系统底层参数，可能需要管理员权限，就试用管理员权限打开IE，果然，顺利连接成功。

嗯，以后使用古董遇到一些比较怪异的问题，如果它是安全可靠的，就可以试试管理员权限了。我是不推荐关闭UAC的，权限机制虽然烦，但是可以保证一些系统权限不被开放
。

