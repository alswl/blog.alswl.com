Title: 添加FireFox下的边框圆角
Author: alswl
Date: 2009-12-31 00:00:00
Tags: WordPress
Category: 建站心得, 技术达人
Summary: 

起因是换了DDDSpace.com 这个域名，需要测试邮件回复情况，我发现在在iGoogle的GMail小窗口显示着实有些难看，就修改了一下样式，添加了圆角
、增加了`padding`值，唔，这个**圆角不对IE系列有效果**。

增加圆角的部分如下：

    
    -moz-border-radius: 10px;
    -khtml-border-radius: 10px;
    -webkit-border-radius: 10px;
    border-radius: 10px;

修改之后的Mail To Commenter 模板如下

    
    <div style="border: 1px solid rgb(183, 183, 183); margin: 1em 40px; padding: 5pt 15px; background-color: #CCFFFF; color: rgb(17, 17, 17);-moz-border-radius: 10px; -khtml-border-radius: 10px; -webkit-border-radius: 10px; border-radius: 10px;">
      <p>Hi！<strong>%user%</strong>，你在 <strong>%post_title%</strong> 上的评论有了新回复</p>
    </div>
    <div style="border: 1px solid rgb(183, 183, 183); margin: 1em 40px; padding: 5pt 15px; background-color: #CCFFFF; color: rgb(17, 17, 17);-moz-border-radius: 10px; -khtml-border-radius: 10px; -webkit-border-radius: 10px; border-radius: 10px;">
      <p>>><strong>你</strong> 说：<br/>
        %your_comment%
      <p>>> <strong>%comment_author%</strong> 回复说： <br/>
        %reply_comment%
      <p>>> 查看原文，请至： <a href="%comment_link%" target="_blank">%comment_link%</a></p>
      <p style="float: right;"> ---- From <a target="_blank" href="%blog_link%/"><strong>%blog_name%</strong></a></p>
    </div>
    

&nbsp_place_holder;效果演示如下

Hi！**%user%**，你在 **%post_title%** 上的评论有了新回复

>>**你** 说：

%your_comment%

>> **%comment_author%** 回复说：

%reply_comment%

>> 查看原文，请至： [%comment_link%](%comment_link%)

---- From [**%blog_name%**](%blog_link%/)

&nbsp_place_holder;

一下是转载自胡戈戈的"[ CSS3圆角属性在Firefox,Chrome,Safari的实现 |
胡戈戈](http://hugege.com/2008/11/09/css3-firefox-chrome-safari/)"，关于圆角的使用很详细。

~~~~~~~圣诞节的分割线~~~~~~~

今天在aw那里看到他的博客用了Firefox专有的圆角属性，另外WordPress的后台也使用了，于是我自己也就试一下来用了。目前IE还未支持圆角属性，IE
8我还不清楚支不支持，或许我们以后只要使用`border-radius`这个CSS3属性就能轻松地在现代浏览器实现这个困扰很多小盆友的问题了，希望这一天的到
来不会太遥远。目前我们已经可以在Firefox,Chrome,Safari实现这个功能了，但他们也还是使用私有属性来实现，用法上略有区别。

**先说一下Firefox的圆角属性：**  
`-moz-border-radius: {1,4} | inherit`

如果你想设置四个角都是一样圆角的话，可以像这样子直接设置`-moz-border-radius:5px;`

也可以单独设置元素的上左、上右、下右、下左四个角的值，分别用`-moz-border-radius-topleft`、`-moz-border-
radius-topright`、`-moz-border-radius-bottomright`、`-moz-border-radius-
bottomleft`来设置。

也可以用合并起来一起设置，如我目前的主题暂时设置的`-moz-border-radius:5px 0 5px 0;`

**对chrome、Safari这两个webkit内核的浏览器来说，是用`-webkit-border-radius`来实现的。**  
`-webkit-border-radius：{1,2} | inherit;`

如果你想设置四个角都是一样圆角的话，依然可以像这样子直接设置`-moz-border-radius:3px;`

如果是单独设置四个角的话，需要采取这种方式

    
    -webkit-border-top-left-radius:5px 10px;
    -webkit-border-top-right-radius:5px 10px;
    -webkit-border-bottom-right-radius:5px 10px;
    -webkit-border-bottom-left-radius:5px 10px;

如果是要合并的话，只支持`-webkit-border-radius:3px;`或者是这样子`-webkit-border-radius:3px
4px;`**使用`-webkit-border-radius:5px 0 5px 0;`将不会有任何效果。**

**著名皮肤制作人[utom](http://utombox.com/new-lastfm/)总结了圆角属性不同浏览器下的运用**
    
    -moz-border-radius: 5px;
    -khtml-border-radius: 5px;
    -webkit-border-radius: 5px;
    border-radius: 5px;

更多详细的请大家自己查看以下链接：

[mozilla 和webkit的 CSS圆角](http://weibin.org/html/moz-border-radius-webkit-
border-radius_28.html)

[ https://developer.mozilla.org/en/CSS/-moz-border-
radius](https://developer.mozilla.org/en/CSS/-moz-border-radius)

[ apple_ref/doc/uid/TP30001266-webkit-border-bottom-left-radius](http://develo
per.apple.com/documentation/AppleApplications/Reference/SafariCSSRef/Articles/
StandardCSSProperties.html#//apple_ref/doc/uid/TP30001266--webkit-border-
bottom-left-radius)

