

今天开始AzaAjaxChat的视频聊天模块，拖FMS的福，实现起来很轻松，不过后来在JavaScript和Flash的交互上遇到了问题。

Flash在各个浏览器中的实现始终是个麻烦的事情，什么Object Embed~，似乎没有什么标准的格式，一般都要做一些浏览器Hack，我对这些深痛恶绝，在
泡了一下午前端相关的论坛后，偶然发现一款JavaScript交互的神器。

![image](/images/upload_dropbox/201005/swfobject_logo.gif)

## SWFObject: 基于Javascript的Flash媒体版本检测与嵌入模块

SWFObject是一个用于在HTML中方面插入Adobe Flash媒体资源（*.swf文件）的独立、敏捷的JavaScript模块。该模块中的JavaS
cript脚本能够自动检测PC、Mac机器上各种主流浏览器对Flash插件的支持情况。它使得插入Flash媒体资源尽量简捷、安全。而且它是非常符合搜索引擎优
化的原则的。此外，它能够避免您的 HTML、XHTML中出现object、embed等非标准标签，从而符合更加标准。

（即：通过text/html应答页面， 而非application/xhtml+xml）

官方在Google Project Host中，下载的代码包中有一个简单的Example，也包含了SWFObject的源码，感兴趣的同学可以研究一下。

相关链接：

[swfobject - Project Hosting on Google Code](http://code.google.com/p/swfobject)

[SWFObject中文的帮助文档](http://www.awflasher.com/flash/articles/swfobj.htm)

如果你也像我这样为Flash发愁，不妨试试这个小巧的js~


