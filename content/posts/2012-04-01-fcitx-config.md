---
title: "Fcitx 配置"
author: "alswl"
slug: "fcitx-config"
date: "2012-04-01T00:00:00+08:00"
tags: ["linuxer", "fcitx"]
categories: ["coding"]
---

## Fcitx

![Fcitx](../../static/images/upload_dropbox/201204/fcitx.png)

Fcitx 简介：

    
    小企鹅中文输入法（Free Chinese Input Toy for X，fcitx）
    是一个以 GPL 方式发布的输入法框架， 编写它的目是为桌面环境提供一个灵活的输入方案。

本程序目前可以支持XIM和GTK2，GTK3，QT4的IM Module，可为支持

XIM 的 X 应用程序提供输入服务。 fcitx 的源码包内提供了区位和全/简/双拼，

并支持基于码表的输入法（自带五笔、二笔和仓颉等输入码表）。

您可以从 http://fcitx.googlecode.com 下载最新的发布版本。

当年刚开始使用 Linux 时候，使用的是 iBus，随后发现 Fcitx 这个输入法， 试用了一下就发现自己所需要的 双拼 / 模糊音 / 自定义输入
功能都有提供， 遂转移阵地到 Fcitx。

## Fcitx 安装

大部分发行版软件源都有 Fcitx，Arch 下安装使用命令 `pacman -S fcitx` 即可安装最新版本。Ubuntu 的安装可以参考
[http://wiki.ubuntu.org.cn/Fcitx](http://wiki.ubuntu.org.cn/Fcitx) 。

## Fcitx 配置

详细的配置文档参见 [http://fcitx.github.com/handbook/fcitx.html](http://fcitx.github.co
m/handbook/fcitx.html)

## Fcitx 特殊符号

当我们需要输入特殊符号（数字符号、箭头等等）时候，往往需要去网上搜索对应的 unicode 码，然后拷贝过来。Fcitx
提供一个很方便的功能叫做「特殊符号输入」， 可以定义自己的特殊符号。

在 `/usr/share/fcitx/pinyin/pySym.mb` / `~/.config/fcitx/pinyin/pySym.mb`
（ps：我当前版本是4.2.1，所以是这个路径，老版本可能不是这个路径） 中定义需要使用的特殊符号，格式为 `<编码> <符号>` ，比如：

    
    yinyue ♩
    yinyue ♪
    yinyue ♫
    ...

那么，在 Fcitx 中输入 `yinyue` 就会出现如下候选框

![Fcitx 特殊符号](../../static/images/upload_dropbox/201204/fcitx-1.png)

`pySym.mb` 文件中，「编码」和「符号」均不允许出现空格，所以比较适合短小的符号，
而颜文字或者长句不适合在这里出现。颜文字以及其他较长的文字如何快速输入， 就要看 Fcitx 的「快速输入」功能了。

我在这里提供的配置文件包括了常用符号、数字、星座、箭头等等，喜欢可以直接拿去。
ps：我定义的「编码」是全拼，所以可能会混淆正常输入，建议全拼用户将「编码」略做 修改，添加前缀比如 `z` （文档中说 `v` 不能被使用为前缀）。

配置完成之后，使用 `fcitx -r` 重启 Fcitx（使用 Ctrl+5 可以刷新配置文件， 但并不能刷新全部配置文件，建议重启 Fcitx）。
待会配置「快速输入」之后，也需要重启 Fcitx 来让配置文件生效。

我的配置文件 [fcitx-config / pinyin / pySym.mb](https://github.com/alswl/fcitx-
config/blob/master/pinyin/pySym.mb)

## Fcitx 快速输入

Fcitx 的「快速输入」和「特殊符号」很类似，后者管理字符，前者管理自定义语句。

快速输入通过 `；` 按键启用，随后输入相应的「字符组合」，Fcitx 会自动补全。

编码对照文件存放在 `~/.config/fcitx/data/QuickPhrase.mb` 或 `share` 目录下对应的文件中，格式为
`<字符组合> <短语>` ，范例如下

    
    # 颜文字欢呼 （颜文字太需要了，卖个萌什么的太管用了）
    yhuanhu (/≥▽≤/)
    yhuanhu ヾ(o◕∀◕)ﾉ

在输入法中，键入 `；` 之后再输入 `yhuanhu` 就会出现下面候选框：

![Fcitx 快速输入](../../static/images/upload_dropbox/201204/fcitx-2.png)

从图中可以看出，Fcitx 还自动进行了「字符组合」补全。

我的 [fcitx-config / data / QuickPhrase.mb](https://github.com/alswl/fcitx-
config/blob/master/data/QuickPhrase.mb) 配置文件按类别收集了一些颜文字，可以直接拿过来使用。

参考链接：

  * [FCCTT推送特别篇----FCITX输入法快速输入表情](http://zhan.renren.com/fullcirclectt?tagId=163058&checked=true)
  * [颜文字收集整理╰(**°▽°**)](http://site.douban.com/widget/notes/4567539/note/197244464/)

## Fcitx 中文键位映射

很多朋友和我一样，喜欢使用「和」来替换"/"，至于为什么，知乎有一个回答就解释的很好
[为什么大家引用时常用直角引号（「」）而不是弯引号（""）？](http://www.zhihu.com/question/19589668)

Fcitx 完全可以通过配置中英文键位映射来修改中文状态下面的输入。全局配置文件在
`/usr/share/fcitx/data/punc.mb.zh_CN` 中， 个人配置文件在
`~/.config/fcitx/data/punc.mb.zh_CN` 这个对应位置。

我的配置 [fcitx-config / data / punc.mb.zh_CN](https://github.com/alswl/fcitx-
config/blob/master/data/punc.mb.zh_CN)

## 最后

关于 Fcitx，有 bug 可以到官网反馈，处理起来效率很高， 感谢作者们给大家带来这么优秀的开源软件。

Update:

  * 2012-03-02 感谢 @Weng Xuetian 指正 `Ctrl + F5` 是错误的，需要使用 `Ctrl + 5` 重载配置。

