---
title: "Eclipse代码统计插件"
author: "alswl"
slug: "statistics-eclipse-plug-in-code-to"
date: "2009-06-30T00:00:00+08:00"
tags: ["工欲善其事必先利其器", "eclipse"]
categories: ["efficiency"]
---

贴吧快完成主要功能了，想统计一下代码量，找到这么一个插件

我 自己试用了一下，发现需要注意两个地方：1.必须在JAVA透视图下使用才能有效；2.必须为项目的选项下的Metrics选择启动Metrics才能统
计；3.这个插件原意是分析代码质量、复杂性的，在分析结果中包含了代码量统计。4.只统计java代码，不统计jsp文件。

最后，Metrics可以以图形化的形式显示包的依赖关系，很好玩，大家可以试试。

转载自：三亩地<[猛击这里打开](http://www.alexadaman.cn/program/eclipse-dai-ma-tong-ji-cha-jian.html/comment-page-1#comment-292569)>，谢谢作者

***********************以下为原文*************************

Metrics插件可以从多个角度对Eclipse中的代码进行统计：

[![metrics](/images/upload_dropbox/201612/404.png)](http://image-001.yo2cdn.com/wp-content/uploads/0/38/2008/08/metrics.png)

**官方网站**：[http://metrics.sourceforge.net/](http://metrics.sourceforge.net/)

**添加方法**：Run Eclipse, go to Help menu -> Software Updates -> Find and Install ... On the opening dialog choose Search for new features to install. Add a new Remote site with the following url **http://metrics.sourceforge.net/update** and follow the instructions for installation.

**使用方法**：To start using the Metrics View, use Windows -> Show View -> Other and navigate to the Metrics View, as shown in the next image.

