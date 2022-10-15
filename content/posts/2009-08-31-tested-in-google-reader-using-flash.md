---
title: "测试在Google Reader下使用Flash"
author: "alswl"
slug: "tested-in-google-reader-using-flash"
date: "2009-08-31T00:00:00+08:00"
tags: ["建站心得", "html"]
categories: ["coding"]
---

发现我贴的Flash都不能在Google
Reader中显示，而[煎蛋](http://jandan.net)的可以，我FireBug了一下，发现它的Flash代码和我的略有区别。

我之前的Flash代码~ ` <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"
width="420" height="363" codebase="http://download.macromedia.com/pub/shockwav
e/cabs/flash/swflash.cab#version=6,0,40,0"><param name="allowFullScreen"
value="true" /><param name="allowscriptaccess" value="always" /><param
name="wmode" value="opaque" /><param name="src"
value="http://www.tudou.com/v/pO3E-u-qBPM" /><param name="allowfullscreen"
value="true" /><embed type="application/x-shockwave-flash" width="420"
height="363" src="http://www.tudou.com/v/pO3E-u-qBPM" wmode="opaque"
allowscriptaccess="always" allowfullscreen="true"></embed></object>`

这种代码是直接从土豆的「贴到博客或BBS」功能实现的，使用了object
Html元素。可能出于安全考虑，object并不在大多数的RSS订阅网站使用，也就播放不了使用object元素放置Flash的视屏。而煎蛋的代码如下：

`<embed width="480" height="400" align="middle" type="application/x-shockwave-
flash" wmode="transparent" allowscriptaccess="never"
src="http://player.youku.com/player.php/sid/XMTE1MDI5OTUy/v.txt"/>`

使用了embed元素（embed元素解释：embed可以用来插入各种多媒体，格式可以是
Midi、Wav、AIFF、AU、MP3等等，Netscape及新版的IE 都支持。url为音频或视频文件及其路径，可以是相对路径或绝对路径。）

如果要把土豆或者优酷等视频网站换成这种embed元素，只需要将`http://www.tudou.com/v/pO3E-u-qBPM`这种代码填入embed
元素的src位置即可，这个视屏地址可以从视频网站的「FLASH播放器的地址」这栏获得。

测试一下视频：

好吧，测试失败```(12:56)

