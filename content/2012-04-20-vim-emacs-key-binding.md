Title: Vim 下模拟 Emacs 键绑定
Author: alswl
Date: 2012-04-20 00:00:00
Tags: Emacs, Readline, Shell, Vim
Category: Linuxer, 工欲善其事必先利其器
Summary: 


Vimer 需要 Emacs 键绑定？看上去很蛋疼的需求吧。其实不然，大部分的 Shell / Readline 默认绑定的是 Emacs 键位绑定（处于输入状态下，Emacs 的键位很好用）。Vim 的模式切换很牛逼，但是 Insert 模式下面，只有寥寥几个快捷键，我修改了配置文件，绑定需要的 Emcas 按键到 Vim 中来。

Github 中搜索关键字 Vim Emcas key bind，出来一些结果，不是很完美，我又慢慢调教了几个星期，放出我的 .vimrc。

``` bash
" 模拟 Emacs 键绑定
" Move
inoremap <C-a> <Home>
inoremap <C-e> <End>
"inoremap <C-p> <Up>
"inoremap <C-n> <Down>
inoremap <C-b> <Left>
inoremap <C-f> <Right>
inoremap <M-b> <C-o>b
inoremap <M-f> <C-o>w
" Rubout word / line and enter insert mode
" use <Esc><Right> instead of <C-o>
inoremap <C-w> <Esc>dbcl
" delete
inoremap <C-u> <Esc>d0cl
inoremap <C-k> <Esc><Right>C
inoremap <C-d> <Esc><Right>s
inoremap <M-d> <C-o>de
```

需要的朋友请取用，我的 Vim 配置文件和插件在 [https://github.com/alswl/dotfiles](https://github.com/alswl/dotfiles) 。