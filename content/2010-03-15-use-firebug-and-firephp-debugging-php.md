Title: 使用Firebug和FirePHP调试PHP[译文]
Author: alswl
Slug: use-firebug-and-firephp-debugging-php
Date: 2010-03-15 00:00:00
Tags: PHP, Firebug, FirePHP, 译文
Category: Coding

这是我第一篇译文，在写WordPress 主题时候偶尔看到的FirePHP插件，看都这篇文章，不知道为什么，动了翻译的念头。

原文链接：[Debug PHP with Firebug and
FirePHP](http://www.sitepoint.com/blogs/2010/02/09/debug-php-firebug-firephp/)

译言的链接：[译言网 |
使用Firebug和FirePHP调试PHP](http://article.yeeyan.org/view/119553/94520)

×××××以下译文××××××

![image](https://ohsolnxaa.qnssl.com/upload_dropbox/201612/404.png)

如果你和我一样，你会在开发网页项目时候完全无法离开[FireBug](http://getfirebug.com/)。这个小巧的"臭虫"是一个神奇而有用的H
TML/CSS/JavaScript/Ajax调试器。但是你也许不知道这个还可以用来调试PHP，没错，它可以，感谢一款名为FirePHP的FireFox插件
。

通过一个小小的服务端库，和这款在Firebug上的插件，你的PHP脚本能够发送调试信息到浏览器，轻易的通过HTTP相应头编码。一旦你设置，你可以在Fiire
bug的控制台获得PHP脚本警告和错误，就感觉像直接调试JavaScript一样

使用这个工具，首先你需要安装[FirePHP插件](https://addons.mozilla.org/en-US/firefox/addon/6149)
。这个插件需要你已经安装FireBug。装好FirePHP之后，重新打开Firebug面板时候，你会看到新加了一个蓝色的臭虫图标。点击这个图标会出现一个开启
或者关闭FirePHP的菜单。

![FirePHP Menu](https://ohsolnxaa.qnssl.com/upload_dropbox/201612/404.png)



当然，这时候我们还无法做任何事，你还需要安装FirePHP的服务端，点击[这里](http://www.firephp.org/HQ/Install.htm
)下载。这是一个独立的版本，你可以手动下载或者使用PEAR。装后之后，你可是轻松的将这个库加入你的代码。它被设计了很多版本来整合入多个框架或者管理系统，比如
[WP-FirePHP plugin for WordPress](http://wordpress.org/extend/plugins/wp-
firephp/) 和 [JFirePHP plugin for Joomla](http://joomlacode.org/gf/project/kune
na/frs/?action=FrsReleaseView&release_id=11823)。暂时不管这些，我们将把精力集中在独立的功能上。

一旦你在你服务器上部署了FirePHP库，你还需要在你的代码中加入以下的代码：

`require_once('FirePHPCore/fb.php');`

这是因为FirePHP通过HTTP头发送记录的数据，你需要缓存你的代码产生的输出，从而来响应头信息从这里获取代码生成的内容。这个可以通过在代码头部的`ob_
start`来实现。

`ob_start();`

当这些步骤完成后，你可以开始使用FirePHP了。你需要做的只是调用`fb`函数在任何你想要记录的地方。同时你也可以使用一个可选的标签和常量去定义预定义信息
，一个错误，一个警告，或者一条信息。

$var=array('a'=>'pizza',&nbsp_place_hold
er;'b'=>'cookies','c'=>'celery');

fb($var);

fb($var,"Anarray");

fb($var,FirePHP::WARN);

fb($var,FirePHP::INFO);

fb($var,'Anarraywith&
nbsp_place_holder;anErrortype',&nbsp_pla
ce_holder;FirePHP::ERROR);

    
    $var = array('a'=>'pizza', 'b'=>'cookies', 'c'=>'celery');fb($var);fb($var, "An array");fb($var, FirePHP::WARN);fb($var, FirePHP::INFO);fb($var, 'An array with an Error type', FirePHP::ERROR);

这些代码将在Firebug控制台输出如下所示

![FirePHP Console Output](https://ohsolnxaa.qnssl.com/upload_dropbox/201612/404.png)

你也可以使用FirePHP来跟踪你程序的执行情况：通过使用`FirePHP::TRACE常量，你可以在` `fb被调用的地方查看``行数、类名和方法名`

1

functionhello(){

2

fb('HelloWorld!',&nbs
p_place_holder;FirePHP::TRACE);

3

}

4

functiongreet(){

5

hello();

6

}

7

greet();

    
    function hello() { fb('Hello World!', FirePHP::TRACE);}function greet() { hello();}greet();

产生的输出如下

![FirePHP Trace Output](http://www.sitepoint.com/blogs/wp-
content/uploads/2010/02/Screen-shot-2010-02-09-at-3.00.40-PM.png)

这个跟踪功能可以完美的调试更复杂的代码，让你精确的知道你的方法是在哪里被调用的。

当然，别忘了你需要在你代码发布之前移除你的调试语句。

这里还有很多FirePHP的内容没有涉及到。我只是向你简单展示一下FirePHP的API，还有很多高级的面向对象API。你可以获得更多相关内容在
[FirePHP site](http://www.firephp.org/HQ/Use.htm)，要记得看它哦～

