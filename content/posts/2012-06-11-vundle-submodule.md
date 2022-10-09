---
title: "Vundle 和 Submodule"
author: "alswl"
slug: "vundle-submodule"
date: "2012-06-11T22:07:00+08:00"
tags: ["工欲善其事必先利其器", "git", "vundle"]
categories: ["efficiency"]
---


## 问题背景 ##

Vundle 是个好东西，可以用来管理 vim 配置和 vim 插件。Vundle
会将所有插件管理在 `.vim/bundle/` 中，详情可看
[使用 Vundle 管理 Vim 插件](/2012/04/vundle/)。

官方安装 Vundle 方法如下：

``` bash
$ git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle
```

我的 Vundle 的版本是 `59bff0c457f68c3d52bcebbf6068ea01ac8f5dac`，
git 版本是 `git version 1.7.10.2` 。
使用 `BundleInstall` 可以安装 `.vimrc` 中配置的插件，

我使用 git 控制 `.vim` 和 `.vimrc` 版本。在 `BundleInstall`
之后会导致 vundle 目录项目状态混乱，要么形成一个无法追踪的
submodule 比如 `.vim/bundle/The-NERD-Commenter (untracked content)`
，要么变成一个普通的文件夹 `.vim/bundle/vim-markdown`。

<!-- more -->

## 使用 Submodule 管理 插件 ##

为了解决这个问题，我们需要先了解一点 Git 中 Submodule 的知识，详情可以查看
[Git Book 中文版 - 子模块](http://gitbook.liuhui998.com/5_10.html)。

用 Submodule 来初始化 Vundle ，使用下面的语句：

``` bash
git submodule add  https://github.com/gmarik/vundle.git .vim/bundle/vundle

git submodule status # 查看子模块状态
 59bff0c457f68c3d52bcebbf6068ea01ac8f5dac .vim/bundle/vundle (0.9.1-18-g59bff0c)
```

Submodule 的映射是被记录在 .gitmodules 文件中的，初始化完 Vundle 之后如下：

``` ini .gitmodules
[submodule ".vim/bundle/vundle"]
        path = .vim/bundle/vundle
        url = https://github.com/gmarik/vundle.git
```

## 最佳实践 ##

使用 Submodule 能够很完美的控制 Vundle 管理下的 Vim 插件。
可惜 Vundle 无法自动帮我们初始化插件的 Submodule。曾经也有热心用户建议 Vundle
加上这个功能：[https://github.com/gmarik/vundle/pull/41](Init/update submodules in git bundles)。
不过 Vundle 的作者很残暴的拒绝了，他认为 Vim 插件可能需要深入定制，
因此不希望使用 Submodule 来管理插件。

我崇尚自动化构建，甚至宁愿牺牲一些所谓的定制，
少量的修改我可以放弃 Vundle 而手工管理。我琢磨了一下我的最佳实践：

使用 Submodule 来初始化 `.vim/bundle/vundle`，然后在使用 `BundleInstall`
来安装其它插件。两个步骤分别为：

``` bash
git submodule add  https://github.com/gmarik/vundle.git .vim/bundle/vundle
vim +BundleInstall
```

大功告成，既能享受插件升级带来的优势，又可以使用 Vundle 统一管理，管理 vim
环境甚为方便。我的 Vim 配置文件在
[https://github.com/alswl/dotfiles](alswl / dotfiles)，还包括 Awesome
/ 按键映射等等配置。
