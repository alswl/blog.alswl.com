Title: 美化postviews
Author: alswl
Date: 2009-05-21 00:00:00
Tags: WordPress
Category: 建站心得
Summary: 

很多朋友用postviews这个插件，的确很适合国人的风格，但是如果单纯的添加到页面中，会显得很突兀，难看，我做了几个美化工作。

首先，在用到postviews函数时候都定义span id，比如在single.php中修改，在下面代码

    
    <span><?php the_author_posts_link(); ?></span><?php endif; ?>

后面跟上一段显示浏览次数的代码

    
    <span><?php the_author_posts_link(); ?></span><?php endif; ?>

这样就可以显示浏览次数。

然后修改style.css文件，我的是inove主题，在382行附近修改

    
    .post .date,
    .post .author,
    .post .postviews,
    .post .editpost,
    .post .comments,
    .post .addcomment,
    .post .addlink,
    .post .editlinks {
    background:url(img/icons.gif) no-repeat;
    padding-left:22px;
    height:16px;
    line-height:16px;
    display:block;
    font-size:12px;
    }

增加一个".post .postviews,"，然后再在后面的.post .author，如下

    
    .post .author {
    background-position:0 0;
    margin-right:15px;
    float:left;
    }

后面添加

    
    .post .postviews {
    float:left;
    }

这样就能显示合适的大小。

此时间距还有问题，修改".post .author"

    
    .post .author {
    background-position:0 0;
    margin-right:15px;
    float:left;
    }

此时位置就修改好了。

如果想添加我这样的心形符号，就得修改wordpresswp-
contentthemesinoveimg下面的icons.gif，在合适的地方添加一个自己喜欢的图像，然后修改style.css

    
    .post .postviews {
    background-position:0 -18px;
    float:left;
    }

如果喜欢我的心形，可以直接下载我的修改好的图像，[icons.gif](http://log4d.com/wp-
content/themes/inove/img/icons.gif)，覆盖原来的就可以了。

开始以为PS不能制作.gif，所以用了png，但png在IE下不正常，后来Google了，才学会用PS生成透明背景的gif

