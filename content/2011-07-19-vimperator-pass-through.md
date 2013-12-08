Title: Vimperator的Pass through
Author: alswl
Slug: vimperator-pass-through
Date: 2011-07-19 00:00:00
Tags: FireFox, Vim, Vimperator
Category: 技术达人

作为 vim 的拥护者，我同时也喜欢使用 Vimperator 这款 Firefox 下面的插件，这款插件可以帮助实现 Firefox 的纯键盘操作。

我同时也是 GMail / Google Reader 的深度用户，他们在网页端也支持纯键盘操作，这样就和 Vimperator 产生了冲突。键盘按键事件被
Vimperator 拦截了，导致键盘操作在这些应用上面不起作用。

还好，Vimperator 提供了一种名为 Pass through 的模式，按 `CTRL+Z` 进入这种模式，在这种模式下面，Vimperator
将不响应键盘操作，全部放行到 Web 页面。

在某一次版本更新之后， Pass through 的快捷键 `CTRL+Z` 似乎不起作用了，我翻遍了用户手册也没有找到解决办法。

就在昨天，我无意中不知道按了什么键，命令栏里面出现了 `IGNORE ALL KEYS (Press <S-Esc> or <INSERT> to
exit)` 这行提示信息。在这种状态下面，我测试了 GMail 的快捷键，果然又起作用了。

好吧，我终于找回了丢失的 `CTRL+Z` ，新版的 Vimperator 使用 `Shift+Esc` 或者 `INSERT` 键来进入原来的 Pass
through 模式。

------残念的分割线-----

之前按 `<-` 键时候，按成了 ThinkPad 的回退键，导致文章没有保存，纠结啊。

