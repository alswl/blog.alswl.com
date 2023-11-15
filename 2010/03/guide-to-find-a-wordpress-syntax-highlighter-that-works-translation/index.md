

这是我第二篇译文，第一篇见这里 [使用Firebug和 FirePHP调试PHP[译文]](http://log4d.com/2010/03/use-firebug-and-firephp-debugging-php)

关注我博客的作者可能知道，我在年前就在做自己的主题，但是因为种种原因，一直到现在才完成beta1.0，不仅仅是主题的原因，还有各种插件的匹配，最让我头疼的两
个"回复插件"和"代码着色插件"。

这篇文章做了一个很好的评测，自此我找到了真正好用的代码着色软件。

关于博客改版的一些经验，我会在稍后的日志中总结出来。

原文链接：[Guide to find a WordPress syntax highlighter that works · Geek Out](http://geekout.travislin.com/guide-to-find-a-wordpress-syntax-highlighter-that-works/)

原文作者：Travis

译者：[alswl](http://log4d.com)

----

[之前](http://www.travislin.com/2009/05/autonomy-of-syntax-highlighter/)，我曾经抱怨过我
多么需要一个代码高亮插件但是却没有收到好的建议…我亲自测试审核了一些我在[插件目录](http://wordpress.org/extend/plugins/)找到较为的流行插件。这些被我列出的插件满足下列的要求：

支持WordPress 2.7.1

在2009年有过更新

我寻找代码高亮插件的标准除了以上两点上还有：

代码在切换可视化模式和HTML代码模式后没有变化

下载后立即可以使用，不需要配置或者少量的配置即可

[SyntaxHighlighterEvolved](http://wordpress.org/extend/plugins/syntaxhighlighter/)

上次更新: 2009-5-4 (Version 2.1.0)

标记: 可视化的. Eg/ `[php]`, `[javascript]`

SyntaxHighlighter Evolved 的一个功能是它有一个漂亮的工具栏在代码快的转角处，允许你使用下列功能：在一个弹出窗体内查看代码、复制代码
到剪贴板和打印代码。出于某些原因Syntaxhighter Evolved喜欢去掉我的代码里缩进（空格）（译者按：这可能是WordPress自带TinyMC
E在FireFox下的Bug）。如果我尝试在HTML模式保存，我会收到PHP警告同时我的代码在我的文章中消失。总之，这个插件不是我想要的。

[![p06-syntax-highlighter-evolved](http://www.travislin.com/wp-content/uploads/2009/05/p06-syntax-highlighter-evolved-300x269.gif)](http://www.travislin.com/wp-content/uploads/2009/05/p06-syntax-highlighter-evolved.gif)

[![p06-syntax-highlighter-evolved-02](http://www.travislin.com/wp-content/uploads/2009/05/p06-syntax-highlighter-evolved-02-300x157.gif)](http://www.travislin.com/wp-content/uploads/2009/05/p06-syntax-highlighter-evolved-02.gif)

### Syntax Highlighter Plus

[Syntax Highlighter Plus](http://wordpress.org/extend/plugins/syntaxhighlighter-plus/)

上次更新: 2009-2-11 (Version 1.0b2)

标记: 可视化的. Eg/ `[sourcecode language='css']`

就像_Syntax Highlighter_家庭的其他插件，这款插件也有一个工具条，并且和Syntax Highlighter
Evolved一样，它也因为在我尝试保存到HTML模式时候丢失了我代码的缩进而失败。

[![p06-syntax-highlighter-plus](http://www.travislin.com/wp-content/uploads/2009/05/p06-syntax-highlighter-plus-287x300.gif)](http://www.travislin.com/wp-content/uploads/2009/05/p06-syntax-highlighter-plus.gif)

### Google Syntax Highlighter for WordPress

[Google Syntax Highlighter for WordPress](http://wordpress.org/extend/plugins/google-syntax-highlighter/)

上次更新: 2007-8-14 (Version 1.5.1)

标记: HTML. Eg/ `<pre name="code" class="php">`

尽管它已经快2年没有更新了，Google Syntax Highlighter似乎还是博主们的流行选择，所以我决定把它放到测试中来。Google
Syntax Highlighter 有一个文本化的工具栏，没有Syntax Highlighter家族那么花俏但是却功能一样。这个插件在代码行比较长时候会
遇到样式的问题，不过没什么大关系。直到我在切换可视模式和HTML模式时候失败了，又是一位让人失望的候选者。

[![p06-google-syntax-lighlighter](http://www.travislin.com/wp-content/uploads/2009/05/p06-google-syntax-lighlighter-275x300.gif)](http://www.travislin.com/wp-content/uploads/2009/05/p06-google-syntax-lighlighter.gif)

[![p06-google-syntax-lighlighter-02](http://www.travislin.com/wp-content/uploads/2009/05/p06-google-syntax-lighlighter-02-300x162.gif)](http://www.travislin.com/wp-content/uploads/2009/05/p06-google-syntax-lighlighter-02.gif)

### WP-Chili

[WP-Chili](http://wordpress.org/extend/plugins/wp-chili/)

上次更新: 2008-7-24 (Version 1.1)

标记: HTML. Eg/ `<code class="php">`

WP-Chili 是另外一位比较特殊的候选者，它在[another WordPress syntax highlighterreview](http://www.cagintranet.com/archive/the-definitive-guide-on-wordpress-syntax-highligher- plugins/)进行过评测，我依然给它一个测试机会。和之前的几位候选者不同的是，它需要手动字符转义。我使用[Elliot's postablescript](http://www.elliotswan.com/postable/)
(推荐)来完成这个工作。它的样式有些简单，可能需要一些调整（比如说修正长换行、附加背景和边框颜色以便从正常的段落中区分出来）。WP-
Chili可以可视模式和HTML模式切换下工作，遗憾的是代码缩进在数次保存之后丢失了……难道没有一个插件接受我的空格缩进？！

[![p06-wp-chili](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/201612/404.png)](http://www.travislin.com/wp-content/uploads/2009/05/p06-wp-chili.gif)

### Code Colorer

[Code Colorer](http://wordpress.org/extend/plugins/codecolorer/)

上次更新: 2009-1-27 (Version 0.7.3)

标记:可视化的&HTML . Eg/ `<code lang="php">`, `[cc lang="php"]`。

我在插件目录找到了一个新的插件。由于某些原因，我不能正确获取代码，尽管使用Firebug能查看到HTML代码。（译者按：我之前有使用过Code
Colorer，在切换也存在问题，但能正常显示）

[![p06-code-colorer](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/201612/404.png)](http://www.travislin.com/wp-content/uploads/2009/05/p06-code-colorer.gif)

### Dojox Wordpress Syntax Highlighter

[Dojox Wordpress Syntax Highlighter](http://wordpress.org/extend/plugins/wp-dojox-syntax-highlighter/)

上次更新: 2009-1-27 (Version 0.7.3)

标记: HTML. Eg/ `<pre><code class="php">`

Dojox 是第一个通过测试的插件：代码在数次不同模式切换下仍然保存。Dojox使用双重标记并且需要手动编码转义。虽然背景颜色也许需要修改一下来适应博客的主
题，但除此之外，最终这是一个可以工作的插件。

[![p06-dojox](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/201612/404.png)](http://www.travislin.com/wp-content/uploads/2009/05/p06-dojox.gif)

### Syntax Highlighter and Code Colorizer for Wordpress

[Syntax Highlighter and Code Colorizer for Wordpress](http://wordpress.org/extend/plugins/syntax-highlighter-and-code-prettifier/)

上次更新: 2009-5-5 (Version 2.0.296)

标记: HTML. Eg/ `<pre class="brush:php">`

很显然这款插件也称作代码美化插件。代码美化默认自动执行，同时作为Syntax Highlighter家族的成员它也会会有一个工具栏在右上角。不同于这个家族其
他成员，它的确能够正常使用！无论在切换可视化或者HTML模式时候都没有问题。当然，你得自己手动转义你的代码。

[![p06-code-colorizer](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/201612/404.png)](http://www.travislin.com/wp-content/uploads/2009/05/p06-code-colorizer.gif)

### WP-SynHighlight

[WP-SynHighlight](http://wordpress.org/extend/plugins/wp-synhighlight/)

上次更新: 2009-1-27 (Version 0.91)

标记: 可视化的. Eg/ `[codesyntax lang="php"]`

这是我能找到的唯一一个使用可视化标记并且在不同模式之间切换还能工作的插件。一旦你在可视化模式粘贴代码，不需要加上转义字符，这是在可视化编辑模式下的优势。但是
当我使用它自带的例子时，不管我怎么做，我都没有办法通过WP-SynHightlight为代码着色。

[![p06-wp-synhighlight](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/201612/404.png)](http://www.travislin.com/wp-content/uploads/2009/05/p06-wp-synhighlight.gif)

### 结论

**Syntax Highlighter and Code Colorizer for Wordpress** 
赢的了我的评选，它简单强大而且确实在工作。这个插件是现成的，意味着我不需要在CSS中修改为他重新着色以保证和我主题匹配。我知道我会享受我的选择的。


