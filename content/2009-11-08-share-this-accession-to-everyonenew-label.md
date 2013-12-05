Title: 给Share this加入人人、豆瓣新标签
Author: alswl
Date: 2009-11-08 00:00:00
Tags: WordPress
Category: 建站心得
Summary: 

## Share this

Share this是给博文加上分享按钮，基于prototype的一款WordPress插件。 Share this
中文，从名字你就已经知道，这个Share
this插件的中文版本。当然，我想先告诉你的是，这并不是汉化，而是中文化（本土化）。还辨别不清楚吗？那就是这个插件将更适合于中文用户使用了。 Share
this 由[幸福收藏夹](http://www.happinesz.cn/archives/328/)修改。
[点击这里下载](http://www.happinesz.cn/file/share-this.zip)（此为Share this
中文原版，为了方便，我们以下所用版本都是该版本，请不要升级你的Share this插件，否则会还原为英文） share-this唯一遗憾是用的prototy
pe，这个js比较大，网上有[jQuery版本的第三方修改版](http://www.thunderguy.com/semicolon/2007/07/30
/share-this-jquery-a-wordpress-plugin/)，不过最好还是自行实现js。

## 增加新的按钮

下载的Share this 中文还是07年11月份的产品，很多新的Web2.0网站，比如人人、豆瓣还没有相应的分享按钮。在这里，我就把他们添上去。 1
.打开share-this.php，你会惊喜的发现里面有很多sofish的注释，使修改变得异常简单。在112行左右加入新的代码。

`, 'renren' => array(

    'name' => '人人网'

    , 'url' =>
'http://share.renren.com/share/buttonshare.do?link={url}&title={title}'

) , 'douban' => array(

    'name' => '豆瓣网'

    , 'url' =>
'http://www.douban.com/recommend/?url={url}&title={title}&sel=&v=1'

)`

2.加入网站图片，你可以保存![](http://log4d.com/wp-content/plugins/share-this/renren.gif)
和![](http://log4d.com/wp-content/plugins/share-this/douban.gif) 并上传到share-
this.php同一文件夹下。 3.刷新页面，你会发现新的按钮出来了。

## 加入更多按钮

其实加入按钮的关键在于相应url，这个url怎么获取呢。其实我们可以从对应网站[人人网分享](http://share.renren.com/)、[豆瓣网分
享](http://www.douban.com/service/bookmarklet)加入自己的浏览器。然后随便通过这些按钮收藏一个网页，如百度。那么就
会弹出一个收藏页面。 [![douban_share](http://upload-
log4d.qiniudn.com/2009/11/douban_share.jpg)](http://upload-
log4d.qiniudn.com/2009/11/douban_share.jpg)
这时候获取图中的网页地址，然后修改其中真实的url和title，替换为{url},{title}，这两个标记供share-this插件识别
。再将相应代码加入share-this.php，就大功告成了。
图片的获取可以使用FireFox的查看页面信息，其中媒体页面可以获得favicon.ico，转换为.gif格式上传即可。

## 相关下载

懒人来下载这个吧，都是经过修改的，不过第一个jQuery没汉化...我懒了...如果英语不好就下载第二个吧 [share-this_jquery](http
://upload-log4d.qiniudn.com/2009/11/share-this_jquery.zip)（Share this
jQuery版本，Jason Ti本地化+未汉化+已经汉化） [share-this_prototype](http://upload-
log4d.qiniudn.com/2009/11/share-this_prototype.zip)（Share this
prototype版本，sofish本地化+汉化） 哦，最后，如果觉得本文不错，你也可以分享哦，谢谢咯。

