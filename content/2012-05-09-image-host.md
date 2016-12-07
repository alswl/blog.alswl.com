Title: 使用独立图床子域名
Author: alswl
Slug: image-host
Date: 2012-05-09 16:21
Tags: 建站, minigal nano, CF Image Host Script
Category: Coding


最近在将 Wordpres 切换到 OctoPress，顺便将图片统一放到[Upload4D](https://ohsolnxaa.qnssl.comm)管理。

我挑选图床管理程序有下面几个需求，需求由强到弱排列：

* 开源
* 简单
* 不需数据库支持
* 支持分目录
* 允许上传图片
* 支持后台直接操作文件
* 支持用户管理，不允许其他人上传
* 页面美观
* 不要生成缩略图等文件
* 软件持续更新

于是我踏上了「考古之旅」，先后试用了 MiniGal Nano / MG2 /
CF Image Host Script / minishowcase 等等图床软件，评测记录如下。

<!-- more -->

## 参赛选手 ##

### [MiniGal Nano](http://www.minigal.dk/minigal-nano.html) ###

![MG Nano](https://ohsolnxaa.qnssl.comm/2012/05/mg-nano.png "MiniGal Nano")

* 没有上传功能
* 没有后台管理功能
* 2010年最后更新

### [MG2](http://www.minigal.dk/mg2.html) ###

![MG2 前台](https://ohsolnxaa.qnssl.comm/2012/05/mg2-front.png)
![MG2 管理界面](https://ohsolnxaa.qnssl.comm/2012/05/mg2-admin.png)

* 假目录，其实所有照片在同一目录下面
* 界面丑
* 09年更新

### [美优网 Meiu Studio|php相册系统](http://meiu.cn/) ###

* 国产
* 需要 MySQL

### [CF Image Hosting Script v1.4.2](http://www.codefuture.co.uk/projects/imagehost/) ###

![CF Image Hosting](https://ohsolnxaa.qnssl.comm/2012/05/cf-image-host.png)

* 据说煎蛋在使用
* 无法用户控制
* 无目录

### [Minishowcase](http://minishowcase.net/) ###

* 没看见上传功能
* 没看见目录功能
* 丑
* 2009年更新

### [Qdig](http://qdig.sourceforge.net/) ###

![Qdig](https://ohsolnxaa.qnssl.comm/2012/05/qdig.png)

* 无法上传
* 丑
* 2006年更新

### [iFoto, CSS-based GD2 photo gallery](http://sourceforge.net/projects/ifoto/) ###

![iFoto](https://ohsolnxaa.qnssl.comm/2012/05/ifoto.png)

* 无法上传
* 丑
* 2006年更新

### [Encode Explorer](http://encode-explorer.siineiolekala.net/) ###

![Encode Explorer](https://ohsolnxaa.qnssl.comm/2012/05/encode-explorer.png)

* 这其实是一个文件管理器
* 支持预览
* 不支持多文件上传
* 其他要求全部达到

## 最终选择 ##

最后，我选择了 Encode Explorer，坑爹吧，获胜者居然是一个文件管理软件，
而不是一个图床软件。

Encode Explorer 是单文件程序，代码一共3k多行，我看了一下，还能支持多语言，
我就加上了中文支持，并且修正了新建目录/新建文件的权限 bug，改为目录755,
文件644，并且这两个模式可以在配置文件修改。

修改之后的 Encode Explorer 可以在
[alswl / encode-explorer](https://github.com/alswl/encode-explorer) 找到。

既然已经不单纯是图床了，那我也把以前的一些附件放到这个子域名下，域名也要由
img.log4d.com 改为 upload.log4d.com 。

我用 sed 命令将原来的图片和附件命令批量修改，命令如下
`sed -i 's/log4d.com\/wp-content\/uploads/upload.log4d.com/g' ./_posts/*`。

ps:今天是我博客独立3周年纪念日，本来想在今天之前把 Wordpress 迁移到
OctoPress，可惜最近太忙，就耽误了。
