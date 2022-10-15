---
title: "aMSN中文报错解决办法"
author: "alswl"
slug: "amsn-zh-cn-error-solution"
date: "2010-03-15T00:00:00+08:00"
tags: ["技术达人", "msn"]
categories: ["efficiency"]
---

转载，不解释。

原文链接：[解决amsn0.98.1选择中文报错_gnn77的空间_百度空间](http://hi.baidu.com/gnn77/blog/item/3c
0ce113931ac4cda6ef3fb0.html)

××××-------×××××

amsn默认的语言是英文，如果选择语言为简体中文就会报如下错误。

> TK has brought an error, there is a bug in aMSN, please report it by
clicking the Report button. You can click Details to see more informations
about the bug or click Ignore to continue chatting with aMSN.

解决的方法是编辑amsn安装目录下share/amsn/langlist文件（Windows下面是aMSNscriptslanglist）。

    
    <lang>
    <langcode>zh-CN</langcode>
    <name>Chinese - Simplified (简体中文)</name>
    <version>1.2</version>
    <encoding>gb18030</encoding>
    </lang>

改为

    
    <lang>
    <langcode>zh-CN</langcode>
    <name>Chinese - Simplified (简体中文)</name>
    <version>1.2</version>
    <encoding>gb2312</encoding>
    </lang>

