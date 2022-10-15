---
title: "FireFox下WordPress上传频繁崩溃解决方法"
author: "alswl"
slug: "firefox-frequently-collapse-under-the-wordpress-upload-solution"
date: "2009-06-06T00:00:00+08:00"
tags: ["建站心得", "firefox", "wordpress"]
categories: ["coding"]
---

今天修改了数据库option中上传的路径，终于可以使用上传了，很开心，可是又遇到在FireFox下WordPress上传导致FireFox崩溃的问题。

情况是这样，在后台点上传图片，出现上传面板的Loding界面，结果FireFox就崩溃了，查看崩溃信息，并没有什么特殊的显示。在IE下则完全没有这个问题。

Google后几篇文章说是FireFox中Firebug的问题，[猛击这里打开该文章](http://www.tvwz.com.cn/html/computer-repaire/firebug-leads-to-firefox-to-collapse.html)，我也算是个网页开发者，FireBug是必装的，禁止FireBug后重新尝试，依然失败。证明该文章问题和我并不一样。

我一次尝试关闭Web Developer, FlashGot, Adblock Plus，都没有效果，直到最后关闭Google
Gears，才发现崩溃终于停止了。

那么问题就应该是在Google Gears上，这个Google Gears是FireFox的一个插件，用来对本地文件进行暂存的，我的系统也装了Google
Gears，这两个Google Gears不是同一个，系统下的Google
Gears可以对IE进行缓存加速，而IE并没有崩溃，说明问题出在FireFox下的Google Gears。

那么，只要把这个组件关闭就可以了，问题就解决了。

我又尝试了删除Google Gears缓存，崩溃依旧，重新更新Word Press缓存，崩溃依旧，没办法，只能舍弃这个优秀的组件了。

之前使用这两个软件都没有问题，到现在还不知道什么问题导致的，目前只能暂时禁用，我会继续尝试设置这两个工具的。

