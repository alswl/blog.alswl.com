---
title: "Arch Linux装机软件"
author: "alswl"
slug: "linux-application"
date: "2011-12-11T00:00:00+08:00"
tags: ["linuxer", "arch"]
categories: ["coding"]
---

重要通知：Log4D的域名由 [http://dddspace.com](http://dddspace.com/) 迁移到
[http://log4d.com](../) 。

订阅地址现在改为 [http://log4d.com/feed](../feed) 和
[http://feeds.feedburner.com/dddspace](http://feeds.feedburner.com/dddspace)
。（FeedBurner的地址未发生变化）

<strike>http://feed.dddspace.com</strike> 弃用

请订阅我博客的朋友更新一下订阅地址。

前天将arch32位换成64位的系统，想充分利用4G内存。 在mountpoint时候，我mount了 `/root` 和`/home`
盘，然后arch问需要 `(re)create` 分区么。 选项有 `Yes` 和 `No` ，看上去不选 `No` 就进行不下去，我就点了一下。

结果就悲剧了有没有！！！！！！！！！

`home` 盘有150G左右有木有！！！！！！！！

日本岛国文化都有70G有木有！！！！！！！！六七年的心血有木有！！！！！

上次备份是2个月前有木有，就算有Dropbox/github/cvs等等，还会丢失变更有木有！！

两个月的数据变化阿，各种文档，照片和音乐阿！！！！！！

你妹的arch格式化之前通知能不能明显一点，弄个 `format` 字眼吓不死我的！！！！

上次备份是放在Dell笔记本里面的，主板坏了打不开有木有！！！！！！！

最后我用移动硬盘装载老电脑的硬盘，勉强把数据恢复过来。

又是一次苦逼的装机路，我一一记录下来。

下面是官方指导文档配置完成之后的软件，在Arch官方库和ARU里面有。

## 常用工具

  * tilda 一个小巧的Terminal Emulator
  * fcitx 好用的输入法

## 应用软件

  * asciidoc
  * gnucash #财务软件
  * libreoffice
  * foxitreader #yaourt
  * bc #计算器
  * text-live-core #LaTex

## 网络应用

  * firefox
  * firefox-i18n-zh-cn
  * chromium
  * dropbox #yaourt
  * wakoopa #跟踪系统软件的工具 yaourt
  * wireshark-gtk #抓包用的wireshark
  * thunderbird
  * telepathy #empathy依赖
  * nmap #网络工具

## 媒体软件

  * kid3 #mp3 idv2/idv3编辑器
  * gimp
  * smplayer #播放器
  * rhythmbox #音乐播放器
  * audacity #音频编辑器
  * k3b #cd刻录

## 开发应用

  * gvim
  * git/svn/mercurial/cvs
  * ctags
  * jdk #yaourt sun官方jdk
  * mysql
  * mysql-workbench #mysql wrokbench
  * nginx
  * php
  * php-fpm
  * python-virtualenv #python版本管理
  * python-virtualenvwrapper #pytohn版本管理增强工具
  * memcached

## 系统工具

  * net-tools #包含ifconfig/route，这个包现在不在BASE中，默认不安装
  * inetutils #包含ftp/telnet，同上
  * networkmanager-openconnect #networkmanager相关的插件
  * networkmanager-openvpn
  * networkmanager-pptp
  * networkmanager-dispatcher-sshd
  * virtualbox
  * virtualbox-addtitions #virtualbox 增强包
  * qt
  * unrar zip unzip
  * flashplugin
  * bash-completion #bash自动完成
  * nautilus-open-terminal
  * avant-window-navigator #dock
  * hardinfo #设备信息
  * gpaste #多剪贴板 yaourt
  * gstreamer0.10-ffmpeg #预览
  * gparted #分区工具
  * conky #系统运行状态
  * ntp #网络时间校准工具
  * dnsmasq #本地dns缓存

## gnome相关

  * gnome-tweak-tool-3.2.2-2

## gnome shell扩展

在 [https://extensions.gnome.org/](https://extensions.gnome.org/) 可以下载Gnome3扩展。

  * Alternative Status Menu
  * gTile #桌面多窗口分割
  * Places Status Indicator
  * Workspace Navigator

