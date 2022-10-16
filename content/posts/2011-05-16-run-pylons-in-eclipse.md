---
title: "Eclipse中运行Pylons"
author: "alswl"
slug: "run-pylons-in-eclipse"
date: "2011-05-16T00:00:00+08:00"
tags: ["python", "eclipse", "pylons"]
categories: ["coding"]
---

官方中pylons都是通过在shell中运行paster serve --reload
development.ini来运行应用实例。而整天在任务栏跑着一个黑乎乎的shell很碍眼，通过一下步骤可以在Eclipse中运行pylons。

配置Run Configuration - Python Run如下。

Main页签中Main Module指向paster-script.py，可以使用绝对路径。

![image](/images/upload_dropbox/201105/eclipse-main.png)

配置Arguments页签的参数，添加serve --reload development.ini，后面的ini配置文件可以使用绝对路径。

![image](/images/upload_dropbox/201105/eclipse-arguments.png)

勾选Common下的Allocate Console来进行paster调试信息输出。

在Windows - Preference - Pydev - Interpreter - Python中的PYTHONPATH加入pylons目标环境
，报过site-packages目录和site-packages目录下面的egg文件（理解为jar包，称之为蟒蛇蛋）。

不出意外的话，就可以通过Run跑起整个应用了。

很可惜的是，这样做还是不能对应用进行Debug，pylons的debug依然依赖于pylons的"交互调试页面"。

参考[http://stackoverflow.com/questions/147650/debug-pylons-application-through-
eclipse](http://stackoverflow.com/questions/147650/debug-pylons-application-
through-eclipse)

