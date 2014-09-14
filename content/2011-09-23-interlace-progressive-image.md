Title: 网页渐进式载入图片
Author: alswl
Slug: interlace-progressive-image
Date: 2011-09-23 00:00:00
Tags: WebFront, zhihu
Category: Coding

## Question

为什么有的网页打开图片是从上到下逐行打开，有的则是先显示低分辨率图片再逐渐加入细节？

## Answer

感谢@吴亚桐
回答给我找到线索，感谢提问者的好问题，我为这个问题曾经困惑了多年。这种渐进式载入方法容易和其他渐进式载入混淆。&nbsp_place_holder;

我这里小总结一下几种渐进式载入办法。&nbsp_place_holder;

  * js延迟载入，当浏览器滚动条拉到下面时候才显示出图片，参考&nbsp_place_holder;[http://www.neoease.com/lazy-load-jquery-plugin-delay-load-image/&nbsp_place_holder;](http://www.neoease.com/lazy-load-jquery-plugin-delay-load-image/ )  

  * 使用两张一大一小照片，小的先显示，等大图片完全下载好之后再载入。参考 [http://blog.rexsong.com/?p=929&nbsp_place_holder;](http://blog.rexsong.com/?p=929 )  

  * 图片渐进式技术，也就是本问题。&nbsp_place_holder;  

  * 大图片切割成小图片，逐个载入，这是互联网早期方式，现在已经几乎看不到了。太浪费http连接了。

&nbsp_place_holder;下面是答案&nbsp_place_holder;

* * *

浏览器下载图片的时候渐进式载入，这样下载完一张图可以看到它的样子，只不过只是不清楚的图，这样可以减少你等待看它的时间。&nbsp_place_holder;

实际上有两种方式可以实现这种渐进式效果，一种是图像隔行扫描（**Interlace**），中文可以成为交错，另外一种叫做图像渐进式扫描（**Progress
ive**）。&nbsp_place_holder;

  1. 隔行扫描可以在gif/png中实现。隔行GIF是指图像文件是按照隔行的方式来显示的，比如先出奇数行，再出偶数行，造成图像是逐渐变清楚的。将图像文件保存成隔行GIF格式的方法是，在 Photoshop中进行保存时，选择"Interlaced"（不要选择"Normal"），在Paint Shop Pro中进行保存时，点击"Option…"按钮，选择"Interlaced"（不要选择"Non Interlaced"）。&nbsp_place_holder;  

  2. 渐进式扫描在在jpg中实现。逐级JPG文件可以让图像先以比较模糊的形式显示，随着图像文件数据不断从网上传过来，图像会逐渐变清晰。这样做的好处是图像可以尽快地显示出来，虽然图像不很完美，但是却让浏览者看到了希望，并且图像在不断地变好。将图像文件保存成逐级JPG格式的方法是，在Photoshop中进行保存时，选择"Progressive"，在Paint Shop Pro中进行保存时，点击"Option…"按钮，选择"Progressive encoding"。

参考&nbsp_place_holder;

[http://blog.csdn.net/greenerycn/article/details/1458231&nbsp_place_holder;](h
ttp://blog.csdn.net/greenerycn/article/details/1458231 )

[http://www.libpng.org/pub/png/pngintro.html](http://www.libpng.org/pub/png/pn
gintro.html)

## via

[http://www.zhihu.com/question/19773824](http://www.zhihu.com/question/1977382
4)

