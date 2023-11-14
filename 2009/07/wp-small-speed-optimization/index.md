

今天实在无法忍受WP的速度，打开速度在10s-15s左右，好几个朋友反映，我咨询了一下小张，发现同一台服务器的网站速度都不错，那就是我的设置问题了。

参考了一下几篇速度优化博文，也对自己的博进行了简单的优化。

我没木木和万戈那样的本事，能几乎不用插件自己修改代码，我仅仅能稍微禁用一些插件，界面用的iNove，也不想做太多的改变。

我用FireBug查看了一下同服务器的其他网站，人家的连接数甚至高达80+，速度还比我快，我仔细检查，发现一些cnzz图片读取比较耗时。我在iNove的界面
下修改了end.php的代码，换上了文字代码，而不用去cnzz获取图片。

这样一来，似乎速度快了点。

我又删除了饭否的图片，这几天饭否也访问不了，留了也显示不出来。

我留下12个插件，分别是：Akismet, CodeColorer, Dagon Design Sitemap Generator, Google XML
Sitemaps, Mail To Commenter, Shutter Reloaded, Super Switch, WordPress Related
Posts, WP-PageNavi, WP-PostViews, WP-T-Wap, wp slug translate

我对插件看法和万戈大大的不一样，我还是觉得别人写好的东西，我没有必要学会操作php（尽管我是个程序员），也许懒人都是这么想法吧，呵呵……

最后我开启了DB Cache，这下捅了马蜂窝，DB Cache与WP2.8不兼容，界面完全空白，后台也空白，我只能还原数据库和文件，才返回原样。

这样下来，似乎只是删除了一个图片和一个wiggett，禁用了几个插件，速度就明显加快了（也许心理作用吧）。。。


