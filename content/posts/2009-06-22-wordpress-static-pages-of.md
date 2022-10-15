---
title: "WordPress页面静态化"
author: "alswl"
slug: "wordpress-static-pages-of"
date: "2009-06-22T00:00:00+08:00"
tags: ["建站心得", "wordpress"]
categories: ["coding"]
---

其实以前也使用了静态化，但是只是显示文章别名为数字的固定链接，这个对搜索引擎不太友好，也不是很容易识别。

今天我安装了一个插件wp-slug-
translate，是偶爱偶家出品的<[猛击这里打开](http://blog.2i2j.com/)>，感觉这位大大出了好几个很有用的插件，很是实用。

这个插件的作用是会自动把文章名转换为英文表示的名称，是通过Google翻译来做的，基本还是没有什么出入的，当然，也可以自己手动修改文章名。

我重新修改了一下固定链接的表示，修改成/%year%/%monthnum%/%day%/%postname%.html，这样看上去就像是伪静态了，例如本文的
地址为http://log4d.com/2009/06/22/wordpress-static-pages-of.html

这个插件一个缺点是不能修改已经存在的文章，那么如果要全部修改的话，只能自己手动修改，我用Google翻译一个一个修改，大约花了5分钟时间。如果自己的文章被别
人引用的比较多，那么建议不要修改以前的地址，否则会产生很多无效链接的。

