Title: CodeColorer的Html转义
Author: alswl
Slug: the-html-escape-codecolorer
Date: 2009-09-07 00:00:00
Tags: 
Category: 建站心得
Summary: 

刚开始写博客时候我用的CodeColorer进行WordPress的代码高亮。后来，我觉得这个插件在格式上有些不满意的地方，于是就停用了。之后写的文章都是直
接包在WordPress的Code元素内。

几天之后，我发现了这个问题，大部分的代码在这两种模式下还算正常，但是如果是遇到html下的一些转义字符，就变得麻烦了。CodeColorer的html代码添
加是在编辑器的HTML模式下编辑，编辑后不能切换到可视化编辑器下，否则代码会被编辑器格式化。HTML代码的转义靠CodeColorer自动完成。

在使用WordPress自己的code元素后，也就是关闭了CodeColorer插件，代码转义靠在可视化编辑器下就进行了转义。

像我这个博客，前半段代码存放的是直接html代码，而后来的存放了几篇经过转义的html代码，造成了代码显示混乱。

## 症状

[caption id="attachment_12631" align="alignnone" width="345"
caption="开启CodeColorer+可视化界面编辑结果"][![Snap2](http://upload-
log4d.qiniudn.com/2009/09/Snap2.jpg)](http://upload-
log4d.qiniudn.com/2009/09/Snap2.jpg)[/caption]

[caption id="attachment_12632" align="alignnone" width="304"
caption="关闭CodeColorer+HTML编辑结果在首页显示"][![关闭CodeColorer+HTML编辑结果](http
://upload-log4d.qiniudn.com/2009/09/Snap3.jpg)](http://upload-
log4d.qiniudn.com/2009/09/Snap3.jpg)[/caption]

[caption id="attachment_12633" align="alignnone" width="312"
caption="关闭CodeColorer+HTML编辑结果在内容页"][![关闭CodeColorer+HTML编辑结果在内容页](http
://upload-log4d.qiniudn.com/2009/09/Snap4.jpg)](http://upload-
log4d.qiniudn.com/2009/09/Snap4.jpg)[/caption]

[caption id="attachment_12634" align="alignnone" width="365"
caption="正确显示"][![正确显示](http://upload-
log4d.qiniudn.com/2009/09/Snap5.jpg)](http://upload-
log4d.qiniudn.com/2009/09/Snap5.jpg)[/caption]

## 解决方法

CodeColorer开着和关着都成问题，要么影响我之前的代码，要么影响我后来的代码。所以必须有第三种方法解决，我检查了CodeColorer源码
，发现了在codecolorer-core.php一段代码。

`if ($options['escaped']) {

$text = html_entity_decode($text);

}`

大意是如果选项有escaped的话，就对text进行html转换。

（其实我觉得把if给注释了，直接用转义，可以更好的使用，省的每段代码加入escaped="true"）

果然，我在官方的[Frequently Asked Questions](http://kpumuk.info/projects/wordpress-
plugins/codecolorer/#faq)中找到这么一段话：

Q. I see &lt; instead of < (or other HTML entities like >, &, ") in my code.

A. You should use [cc escaped="true"] or [cce] in the visual editor when
inserting code into the post.

就是说在<code>标签中加入escaped="true"就可以防止Html被转义。

我坚持使用code标签，以防在没有CodeColorer的环境下[cc]解析出现错误。

