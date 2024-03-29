---
title: "char nchar varchar nvarchar 区别"
author: "alswl"
slug: "difference-between-char-nchar-varchar-nvarchar"
date: "2010-07-16T00:00:00+08:00"
tags: ["综合技术"]
categories: ["coding"]
---

在开发时候，发现数据库的一个字段用的是nchar(16)，让我感觉很奇怪，我知道nvarchar可以变长，nchar会用空格填充，这在存取时候需要Trim(
)操作，所以我一直不用nchar。而现在在产品中发现nchar的使用，不由觉得很奇怪。

私底下认为是效率的问题，一番Google之后发现一段文章详述了几种数据库文字类型存储的差异。

原文出处：[char nchar varchar nvarchar 区别 - Rainbow - 博客园](http://www.cnblogs.com/yoyozhou/archive/2008/11/21/1338452.html)

联机帮助上的：

char(n)

定长

索引效率高 程序里面使用trim去除多余的空白

n 必须是一个介于 1 和 8,000 之间的数值,存储大小为 n 个字节

varchar(n)

变长

效率没char高 灵活

n 必须是一个介于 1 和 8,000 之间的数值。存储大小为输入数据的字节的实际长度，而不是 n 个字节

text(n)

变长

非Unicode数据



nchar(n)

定长

处理unicode数据类型(所有的字符使用两个字节表示)

n 的值必须介于 1 与 4,000 之间。存储大小为 n 字节的两倍

nvarchar(n)

变长

处理unicode数据类型(所有的字符使用两个字节表示)

n 的值必须介于 1 与 4,000 之间。字节的存储大小是所输入字符个数的两倍。所输入的数据字符长度可以为零

ntext(n)

变长

处理unicode数据类型(所有的字符使用两个字节表示)



## 1、CHAR。

CHAR存储定长数据很方便，CHAR字段上的索引效率级高，比如定义char(10)，那么不论你存储的数据是否达到了10个字节，都要占去10个字节的空间,不足
的自动用空格填充，所以在读取的时候可能要多次用到trim（）。

## 2、VARCHAR。

存储变长数据，但存储效率没有CHAR高。如果一个字段可能的值是不固定长度的，我们只知道它不可能超过10个字符，把它定义为 VARCHAR(10)是最合算的。
VARCHAR类型的实际长度是它的值的实际长度+1。为什么"+1"呢？这一个字节用于保存实际使用了多大的长度。从空间上考虑，用varchar合适；从效率上考
虑，用char合适，关键是根据实际情况找到权衡点。

## 3、TEXT。

text存储可变长度的非Unicode数据，最大长度为2^31-1(2,147,483,647)个字符。

## 4、NCHAR、NVARCHAR、NTEXT。

这三种从名字上看比前面三种多了个"N"。它表示存储的是Unicode数据类型的字符。我们知道字符中，英文字符只需要一个字节存储就足够了，但汉字众多，需要两个
字节存储，英文与汉字同时存在时容易造成混乱，Unicode字符集就是为了解决字符集这种不兼容的问题而产生的，它所有的字符都用两个字节表示，即英文字符也是用两
个字节表示。nchar、nvarchar的长度是在1到4000之间。和char、varchar比较起来，nchar、nvarchar则最多存储4000个字符
，不论是英文还是汉字；而char、varchar最多能存储8000个英文，4000个汉字。可以看出使用nchar、nvarchar数据类型时不用担心输入的字
符是英文还是汉字，较为方便，但在存储英文时数量上有些损失。

所以一般来说，如果含有中文字符，用nchar/nvarchar，如果纯英文和数字，用char/varchar

我把他们的区别概括成：

CHAR，NCHAR 定长，速度快，占空间大，需处理

VARCHAR，NVARCHAR，TEXT 不定长，空间小，速度慢，无需处理

NCHAR、NVARCHAR、NTEXT处理Unicode码

