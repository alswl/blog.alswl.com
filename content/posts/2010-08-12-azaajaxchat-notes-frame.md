---
title: "AzaAjaxChat笔记-框架"
author: "alswl"
slug: "azaajaxchat-notes-frame"
date: "2010-08-12T00:00:00+08:00"
tags: ["php", "azaajaxchat", "cakephp", "thinkphp"]
categories: ["coding"]
---

1个月没有动PHP了，新装的系统甚至还没有配置PHP环境，今天看到BooguNote上有一个boo是专门记录AzaAjaxChat开发时候遇到的问题和解决办
法。于是把一些东西整理记录一下。

### 1. 从ThinkPHP开始

最早的AzaAjaxChat是基于ThinkPHP的，我当时在OpenSouce上看到ThinkPHP的介绍，有很多优点，看的我很心动：MVC模型，Ajax
支持，详细的文档和案例，国人开发的框架。我作为一个PHP新人一下子就被他吸引住了，决定用ThinkPHP做框架。

![image](../../static/images/upload_dropbox/201008/thinkphp.png)

随着系统开发的推进，我却感觉到一些不自在，遇到一些问题却找不好太好的解决办法。比如ThinkPHP的模块和分组两个概念，让我比较疑惑，花费了大量时间重组目录
结构，两种方法各有优劣，让我很难选择（有选择了反而难办了 ^_^）。

最让我恼火的是相对目录带来的路径混乱，在JSP开发中，静态内容习惯性放在webcontent文件夹中，而ThinkPHP的CSS、图片、JS引用让我很疑惑，
要区分App的和Model的静态文件。

在开发过程中，我也遇到过框架本身的Bug，让我对这个框架失去信心。在这里我没有贬低ThinkPHP或者ThinkPHP开发者的意思，他们的"大道至简、开发由
我"的理念很值得欣赏。只是作为初学者因为遇到的一些问题，带来了一定的开发难度，不得已放弃。

### 2. 选择CakePHP

在遇到数次挫折之后，我终于下定决心换框架。工作室之前有过一个项目是用CakePHP开发的，保存着一些资料，阿贵强烈推荐CakePHP。我Google了几篇框
架的评测文章后，考虑了一下AzaAjaxChat的规模，决定选择CakePHP。

![image](../../static/images/upload_dropbox/201008/cakephp.png)

CakePHP的脚手架(Scaffold)功能让我眼前一亮，让我脱离了大量CRUD繁琐的操作。而Cake Bake可以方便的根据数据库生成php代码，减少那
些没有逻辑意义的代码。AzaAjaxChat的定位是毕业设计，不是强健的产品，不会苛求太高的用户体验和安全特性，所以这个功能帮了我很多忙。

CakePHP能够处理关系型数据库之间的m-n关系，由于我的系统逻辑简单，并没复杂的多表操作，所以这里没有深究。从Cake
Baker的生成代码菜单上应该能够看出CakePHP还是能够处理一定的多表关联问题。

CakePHP也不是那么十全十美，最麻烦的是文档少，我指的是中文文档，英文资源还是比较丰富的。其次是对Ajax的支持不如ThinkPHP那么原生，我一开始使
用JSON方案，后来使用XML方案实现Ajax数据序列化。

### 3. CakePHP & ThinkPHP

使用的框架最大的目的是提高效率，大幅度缩短工作时间，这两个框架都是为此而诞生的。我这里不说孰优孰劣，如果感兴趣，可以Google查看相关比较。这两个框架都使
用Ruby On Rails的Active
Record理念进行开发，CakePHP更是被称为PHP版的RuR，我在编码中期还特意去图书馆查阅了RuR的相关资料，的确是高效的Web开发模型。

Active Record释义

> ActiveRecord也属于ORM层，由Rails最早提出，遵循标准的ORM模型：表映射到记录，记录映射到对象，字段映射到对象属性。配合遵循的命名和配
置惯例，能够很大程度的快速实现模型的操作，而且简洁易懂。

我在答辩的PPT中写选择CakePHP的原因有三：一站式的MVC框架、约定优于配置、更少的代码，其实这也是RuR的优势。

### 4. 相关连接

  * [Plod: [翻译]十款PHP开发框架横向比较  ](http://plod.popoever.com/archives/001110.html)

  * [ChinaUnix一位网友写的CakePHP入门（我觉得比官方教材好上手）  ](http://blog.chinaunix.net/tag.php?q=CakePHP)

  * [cakephp jquery ajax json_天知道_百度空间（CakePHP的Ajax操作方法）  ](http://hi.baidu.com/zsj1029/blog/item/8fa55e19502e6e4e42a9ad8c.html)

  * [老王的技术手册_博客_cakephp / zendframework_百度空间（挺多CakePHP相关资料）  ](http://hi.baidu.com/thinkinginlamp/blog/category/cakephp%20%26%2347%3B%20zendframework/index/0)

  * [IBM developerWorks 中国 : 使用 CakePHP 快速打造 Web 站点（IBM的CakePHP教程）  ](http://www.ibm.com/developerworks/cn/opensource/os-php-cake/)

