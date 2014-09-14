Title: 关于WordPress中TinyMCE空格
Author: alswl
Slug: about-wordpress-spaces-in-tinymce
Date: 2009-09-09 00:00:00
Tags: 建站心得, TinyMCE, WordPress
Category: Coding

在FireFox下，粘贴到WordPress编辑器中的内容会被自动去掉空格，这对于像Python这种靠缩进控制代码段的code就是毁灭性的打击。而同时作为一
个FireFox用户，我又不愿意为了这个看上去很小的问题切换到IE下。

我开始漫长的征途。

相关链接：

[TinyMCE-Advanced-WP插件 | 80](http://blog.hi1980.com/2009/04/01/tinymce-
advanced-wp-plugins.html)

[「不聪明」的wordpress在线编辑器-Dean... For Wordpress |
素食勤俭敬老孝慈](http://veryi.com/w/104.html)

[TinyMce对火狐不太好 - 我的博客 - 真空实验室 VLab
2.2](http://blog.tgb.net.cn/index.php?load=read&id=161)

[F2blog和Wordpress的空格那点事 - 我的博客 - 真空实验室 VLab
2.2](http://blog.tgb.net.cn/index.php?load=read&id=615)

我又考虑FireFox粘贴的问题，考虑是不是这个原因，给FireFox取消了粘贴限制。

[关于firefox粘贴问题的解决方法 - 愿得一心人，白首不相离 -
博客大巴](http://chifanhezhou.blogbus.com/logs/1406504.html)

还是无用。

最后我求助了Google in English，又尝试了几种方法。

[TinyMCE:Configuration/entity encoding - Moxiecode Documentation Wiki](http://
wiki.moxiecode.com/index.php/TinyMCE:Configuration/entity_encoding)

[TinyMCE wipes out non-breaking space characters (&nbsp;) |
drupal.org](http://drupal.org/node/72570)

依然失败。

我下载了TinyMCE原装的版本，发现它完全能在FireFox3下完美粘贴……

前前后后大概试了4小时，仍然没有什么进展，算了，我被征服了```。

还是感谢以上这些链接文章的作者贡献。

无奈之下，我拿起Vim，它提供一个输出为Html的功能，用那个直接拷贝吧...

