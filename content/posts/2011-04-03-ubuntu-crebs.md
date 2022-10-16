---
title: "Ubuntu桌面自动换背景"
author: "alswl"
slug: "ubuntu-crebs"
date: "2011-04-03T00:00:00+08:00"
tags: ["linuxer", "desktop", "ubuntu"]
categories: ["coding"]
---

GNOME桌面系统可以使用一系列的图片作为背景，每过一段时间能够自动更换。这个功能核Win7下面自动换背景效果一致。不过很可惜，系统自带的可自动更换图片集只
有几张，也找不到什么按钮可以直接设定。

下图就是系统自带的两个图片集（第二行第一组和第二组）。

![image](/images/upload_dropbox/201104/appearance_preferences.png)

我们可以通过撰写xml自己制作图片集，xml格式模板在`/usr/share/gnome-background-properties/cosmos.xml`
，实际的xml存放在类似于`/usr/share/backgrounds/cosmos/background-1.xml`的配置文档里面。

除了手工撰写xml，我们还可以通过crebs小软件来自动生成xml文件。

官方介绍如下：

> A background slideshow creator for the GNOME desktop wallpaper.

The GNOME desktop is able to use a sequence of images for its background
wallpaper, changing them automatically over time, but does not include an
interface for specifying which images should constitute such a slideshow.
Create Background Slideshow (CreBS) is a small Python/GTK application that
provides such an interface, saving users from having to manually edit XML
files.

安装方法是运行如下apt-get命令

    
    sudo add-apt-repository ppa:crebs/ppa
    sudo apt-get update
    sudo apt-get install crebs

在shell里面运行crebs即可召唤出GUI界面，导入自己喜欢的图片保存，即可在背景设定程序里面看见刚刚保存的动态桌面拉。

PS：很赞Launchpad.net的界面风格，非常简洁漂亮。

