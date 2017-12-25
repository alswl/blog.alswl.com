Title: 图片批量加入水印
Author: alswl
Slug: volume-by-adding-a-watermark-image
Date: 2009-07-20 00:00:00
Tags: 建站心得, PhotoShop
Category: Coding

在群里聊天，偶尔提及图片水印问题，呃，我居然一直忘了做这一块内容。

图片加水印，无非3个办法：1.插件自动处理。2.专业加水印软件。3.用PS等修图软件自己动手。

我不太喜欢用太多插件，于是就测试了一下自己电脑上的几个图片编辑软件：PhotoCap3,
HyperSnap，发现他们水印功能都不是那么理想。我不想专门为一个水印去安装一个软件，最后决定用Photoshop写一个Acion动作自己批处理。

参考这篇文章：《[PS制作水印的简单教程_ps制作实例-photoshop](http://www.16xx8.com/photoshop/zhizuoshili/photoshop-4274.html)》和《[Photoshop批量处理动作的录制与运用  - 21CN.COM - IT频道](http://i
t.21cn.com/software/pingmian/adobe/2006/01/19/2441838.shtml)》，基本步骤为（我使用的PhotoS
hopCS3精简版）：

1.制作一个80×80的小Logo,主意背景透明，文本设为30%透明度，讲文字45°倾斜放置。

2.讲制作好的Logo全选保存为图案「编辑-定义图案」

3.填充需要加入水印的图片，「编辑-填充」，选择刚才保存的图案。

可以将第三步保存为一个Action动作，以后就可以不用手工修改了，直接使用「文件-自动-批处理」就可以一步到位了。

图片效果可以参考我之前的图片，效果略微稍挤，我以后会继续修改的。

[caption id="attachment_12362" align="alignnone" width="500"
caption="龙珠·改"][![龙珠·改](https://ohsolnxaa.qnssl.com/2009/06/2009050421141455.jpg)](https://ohsolnxaa.qnssl.com/2009/06/2009050421141455.jpg)[/caption]

09_07_21更新： [小丑](http://loli-ta.com/)同学提了一个建议：不需要大量水印，如果原创有版权的，加上水印无所谓，非原创的就不用加水印了。

我感觉的确很有道理，修改了部分图片（有些源图片已经删除，无法修改了…）。

如果只增加一个角落的水印，可以使用「图案印章」工具，选择之前使用的图案，一样可以达到水印效果。

[![naruto_xiaoyin_cubao](https://ohsolnxaa.qnssl.com/2009/07/snapshot20090720180858.jpg)](https://ohsolnxaa.qnssl.com/2009/07/snapshot20090720180858.jpg)

