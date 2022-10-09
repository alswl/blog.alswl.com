---
title: "Vim中缩进和空格的使用"
author: "alswl"
slug: "vim-indentation-and-space-config"
date: "2010-03-09T00:00:00+08:00"
tags: ["工欲善其事必先利其器", "vim"]
categories: ["efficiency"]
---

原文链接：[WindStorm的技术空间: vim中缩进与空格的设置介绍](http://windwithstorm.blogspot.com/)（Blog
Spot）

对于使用vim的程序员来说，`shiftwidth`，`tabstop`，`softtabstop`绝对是经常接触的三个缩进因素。能否有方便美观的，整体化的
缩进，主要是由他们相互间的配合决定。在经过一段时间试用后，总结一下我的设置经验。

## 1 shiftwidth

这个是用于程序中自动缩进所使用的空白长度指示的。一般来说为了保持程序的美观，和下面的参数最好一致。同时它也是符号移位长度的制定者。

## 2 tabstop

定义tab所等同的空格长度，一般来说最好设置成8，因为如果是其它值的话，可能引起文件在打印之类的场合中看起来很别扭。除非你设置了
`expandtab`模式，也就是把tabs转换成空格，这样的话就不会一起混淆，不过毕竟制表符为8是最常用最普遍的设置，所以一般还是不要改。

## 3 softtabstop

如果我们希望改变程序中的缩进怎么办？`shiftwidth`和`tabstop`不一样的话，你会发现程序比较难看的。这时候，`softtabstop`就起作
用了。可以从vim的说明中看到，一旦设置了`softtabstop`的值时，你按下tab键，插入的是空格和tab制表符的混合，具体如何混合取决于你设定的`s
ofttabstop`，举个例子，如果设定softtabstop=8, 那么按下tab键，插入的就是正常的一个制表符;如果设定
softtabstop=16,那么插入的就是两个制表符；如果softtabstop=12,那么插入的就是一个制表符加上4个空格；如果 `softtabsto
p`=4呢？那么一开始，插入的就是4个空格，此时一旦你再按下一次tab，这次的四个空格就会和上次的四个空格组合起来变成一个制表符。换句话说，`softtab
stop`是"逢8空格进1制表符",前提是你`tabstop=8`。

## 4 关于expandtab

举个例子，在多人一起开发项目时，为了使代码风格尽量保持一致，一般不允许在代码使用TAB符，而以4个空格代之。我们可以编辑一个文件，包含下面的内容：

    
    set shiftwidth=4
    set expandtab

然后把下面的命令加入到.vimrc中：

    
    autocmd FileType c,cpp set shiftwidth=4 | set expandtab

就可以只在编辑c和cpp文件时实行这种设置了。

