---
title: "IE XML 缓存问题"
author: "alswl"
slug: "ie-xml-cache-problem"
date: "2010-06-02T00:00:00+08:00"
tags: ["webfront", "azaajaxchat", "ie", "javascript"]
categories: ["coding"]
---

明天开始上交毕业设计初稿，其中有一节是遇到的问题和解决办法。我把平时在BooguNote 中的琐碎片段整理出来，便有了此文。

PS:之前已经有过3篇相关毕设的文章：

[CakePHP的全局变量](http://log4d.com/2010/05/cakephp-global-variables)

[FMS的80端口占用](http://log4d.com/2010/05/fms-80-port-used)

[SWFObject 一款JavaScript的Flash检测与插入模块](http://log4d.com/2010/05/swfobject)

---- 正文开始 ----

## 问题背景

系统要实现一个操作，即每次向同一个url 请求一个GET方法获取一个xml文件，这个xml文件记录着聊天数据并且是即时生成的。当用FireFox或者Chro
me请求时候都能获得正确的数据，而IE则常常出现无法获取实时的XML数据。

而如果在地址栏中填入 http://localhost/AzaAjaxChat/src/Chat/getXml?messageId=41
这个原始的XML文件地址，就可以获取正确的XML文件。并且在下次IE 的 HTTPRequest请求时候就正常了。看来问题出在IE自身的缓存上面。

## 解决方法

### 1.使用URL参数随机事件

在AJAX请求的页面后加个随机函数,我们可以使用随机时间函数，在javascript发送的URL后加上t=Math.random()。

当然，不是直接把t=Math.random()拷贝到URL后面,应该像这样:


    url = url + "& amp;" + "t=" + Math.random();

### 2.修改Header缓存时间

在XMLHttpRequest发送请求之前加上 XMLHttpRequest.setRequestHeader("If-Modified-
Since","0")。一般情况下,这里的 XMLHttpRequest 不会直接使用。

你应该可以找到这样的代码

XXXXX.send(YYYYYY);

那么,就把它变成

XXXXX.setRequestHeader("If-Modified-Since","0");

XXXXX.send(YYYYYY);

## a Sample

我选择的是第一种方法，我觉得这种更为直观。我的具体代码如下（使用jQuery）：


    jQuery.get("http://localhost/AzaAjaxChat/src/Chat/getXml", {
    	messageId: aacGlobal.currentMessageId,
    	version: Math.random()
    }, getRemoteDataCallBack);

