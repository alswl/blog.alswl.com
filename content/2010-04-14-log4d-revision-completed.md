Title: Log4D改版完成
Author: alswl
Slug: log4d-revision-completed
Date: 2010-04-14 00:00:00
Tags: 建站心得, WordPress
Category: Coding

![image](https://ohsolnxaa.qnssl.comm/2010/04/log4d_screenshot.png)新主题SimpleD也运行
了一段时间了，没出什么大Bug。其实从刚工作时候，也就是11月份，就一直说要自己写一个主题，拖啊拖，拖啊拖，拖到上个月才正式发布SimpleD
1.0版。现在缝缝补补到1.3了。

根据我的工作性质，我本身也算半个Web Designer，花这么长时间搞鼓一个主题是有原因的。最大的问题不是来自主题本身，毕竟我不是艺术家，问题大部分集中在
插件的测试和融合上。下面我就把制作我主题的预期目标和中间遇到问题的解决方案分享一下。

## 一、使用框架

第一件要做的事情是使用一套现有的WordPress主题框架。对于IT从业者来说，编码之前使用一个健壮灵活的框架是多么重要。这里推荐2个框架Sandbox 和
WordPress Basis Theme。

### 1.Sandbox

下载地址：[sandbox-theme - Project Hosting on Google Code](http://code.google.com/p
/sandbox-theme)

sandbox主题中文语言(汉化)包：[sandbox主题中文语言(汉化)包 - Kily's Blog](http://www.keelii.com
/sandbox-zh-cn-package/)

我使用的就是SandBox主题，模块分割比较清晰，默认是英文，可以找到第三方的中文语言包。

### 2.WordPress Basis Theme

不用wpbasis并不是说它不好，它甚至提供了基于HTML5的框架，但是问题的关键是，他默认输出是德文。如果是英文的话，我还能翻译成mo包，德文的话～～～呃
～～～

基本上，如果只是想尝鲜，wpbasis也挺适合，小巧，而且默认的css看上去也不错。

下载地址：[wp-basis-theme - Project Hosting on Google
Code](http://code.google.com/p/wp-basis-theme/)

除了框架，还有一些基本的WordPress自带函数和模板结构需要学习。如果真想做自己的主题，这一步是没法逃避的，强烈推荐水煮鱼的一套教程[
WordPress 主题教程 ](http://fairyfish.net/series/wordpress-theme-tutorials/)

## 二、难对付的插件

### 1.首先要保证的插件是邮件回复

我之前使用的是 MailToCommenter，因为最早时候的cn所在服务器不支持 Thread Comment，之久将就使用 MailToCommente
r。它不支持Ajax，使用和嵌套起来也比较麻烦，有些主题需要简单的修改源码。之前一直使用@单条回复方式，后来感觉嵌套式回复风格更人性化。
关于是否需要使用嵌套的讨论，详见mg12大大的 [WordPress 嵌套回复](http://www.neoease.com/wordpress-
thread-comments/)。

经过测试SandBox 和Wordpress Thread Comment 配合没有问题。

在移动手持上，G3自带浏览器中能够完美使用JavaScript。使用UCWeb for
Android，关闭JavaScript之后点击[回复]，会需要重新打开一次页面，但是回复输入框已经移动了，应该也没有问题。

### 2.代码高亮插件

这个是我需要换主题的根本原因，之前的使用了几个插件都和主题有些不适应，现在索性一步到位。

切换代码高亮插件还牵扯到编辑器的切换问题，所以又牵扯到到底使用哪个在线编辑器的问题。我之前使用的是Dean's FCKEditor 和 deans
fckeditor with pwwangs code plugin for
wordpress，都存在和代码高亮的不兼容情况（在使用html转义时候尤其会出现问题）。

我花了一个晚上对一些插件进行评估，要求如下"可以自由模式切换、兼容pre、插件不在仍然可以运行、自己控制转义符而不是自动转换，否则切换回带来问题、兼容CKE
ditor插件使用"，我还制作了一个xls文档。最后，我发现了一位老外的文章 [Travaganza Blog » Archive » Guide to
find a WordPress syntax highlighter that works
](http://www.travislin.com/2009/05/guide-to-find-a-wordpress-syntax-
highlighter-that-works/)

，解决了我长久以来一直的问题，我曾把这篇文章做了翻译 [WordPress代码高亮插件指南[译文]](http://log4d.com/2010/03
/guide-to-find-a-wordpress-syntax-highlighter-that-works-translation)

最后我选用了Syntax Highlighter and Code Colorizer for Wordpress，详情看我那篇翻译的文章。

### 3.内容编辑器

其实TinyMCE功能很强，可以媲美CKEditor，可以参看我自己在服务器上建立的完整的TinyMCE [http://e.log4d.com/tinym
ce.html](http://e.log4d.com/tinymce.html)，可惜WP和的TinyMCE被阉割的一塌糊涂，还会产生多余的照片缩略图。我
不得不投奔最强的文本编辑器CKEditor（FCKEditor）。

原先使用 Dean's FCKEditor With pwwang's Code Plugin For Wordpress ，是为了解决代码格式问题

现在代码问题解决了，使用 Dean's FCKEditor For Wordpress

如果需要使用原始WP的文件上传路径，需要修改一下Dean's FCKEditor For Wordpress 的js配置代码。

### 4.移动手持插件

最早时候用T-Wap这款国人制作的插件，支持域名重定向，但是会在根目录下生成一个多余的目录，生成的wap页面也不是很漂亮，后台界面很简陋。

#### Wordpress PDA & iPhone。

使用时候需要加入User-Agent:Android才能识别G3，功能比较强大，甚至能使用Add- this插件。

会和Cool-tags冲突，导致Cool-tag无法加载，可惜这款插件不是通过域名判断，而是通过User-
Agent来判断的，其实也不支持其他域名，恩，它不是我的菜。

下载地址：[WordPress › Wordpress PDA & iPhone « WordPress
Plugins](http://wordpress.org/extend/plugins/wp-pda/)

#### WPhone

只适合后台管理，很鸡肋

实话实说，后台功能做得的确比较强。

插件地址：[WordPress › WPhone « WordPress
Plugins](http://wordpress.org/extend/plugins/wphone/)

#### Mobile Pack（最后出现的显然是胜利者了）

完美达到我的要求，支持检测User-Agent或者绑定域名的双重显示方法。不过绑定域名时候遇到一些问题，插件没给太多的提示。如果选择
m.log4d.com的域名，cPanel创建子域默认是public/m，这是需要修改为public/才能使用Mobile
Pack，如果定位到public/m，插件无效。顾名思义，Mobile Pack其实是一种插件包的形式：Mobile Pack= Mobile Theme
+ Mobile Widgets + Mobile Switcher + mpexo。插件可以切换主题，自定义Wigget显示。

下载地址：[WordPress › WordPress Mobile Pack « WordPress
Plugins](http://wordpress.org/extend/plugins/wordpress-mobile-pack/)

## Last、

虽然版本增加到v1.3，但是很多东西都没有做到自定义，所以我暂时也不想把这个主题发布了。

需要参考的朋友可以到svn获取一下，地址在：[https://workspace4alswl.googlecode.com/svn/trunk/PHP/Si
mpleD](https://workspace4alswl.googlecode.com/svn/trunk/PHP/SimpleD)

