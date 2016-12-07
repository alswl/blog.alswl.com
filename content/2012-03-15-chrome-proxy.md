Title: Chrome 独立代理设置
Author: alswl
Slug: chrome-proxy
Date: 2012-03-15 00:00:00
Tags: 技术达人, Chrome, Privoxy, SwitchySharp
Category: Efficiency

Chrome 在2011年4月份时候，加入了两个新的实验性扩展分支，分别是 Web Navigation Extension API 以及 Proxy
Extension API， 通过他们，可以让 Chrome 使用自己独立的代理。

借助这个新功能，我们可以通过 SwitchySharp 使用某个 list 完成部分网址代理。

我的环境： Arch Linux / Chromiun(17.0.963.78) / Proxy SwitchySharp 1.9.38。

## 安装 Proxy SwitchySharp

由于 [SwitchyPlus](http://code.google.com/p/switchyplus/) 停止维护， 因此这里我使用 [Proxy
SwitchySharp](http://code.google.com/p/switchysharp/)。

Proxy SwitchySharp 介绍如下：

    
> 轻松快捷地管理和切换多个代理设置。基于 "Proxy Switchy!" 和 "SwitchyPlus" 开发。
> 使用 SwitchySharp 和 GFW List 的图文教程（一次成功，无需重启）  http://is.gd/swap2
> 
> **注意！我无法在这个页面回复你的提问。如果有任何故障反馈、求助、建议，请移步项目主页，谢谢！=> http://code.google.com/p/switchysharp/issues/entry**
> 
> 特色：
> 
> * 使用 Chrome 代理 API，只修改浏览器代理设置，不修改系统代理设置。
> * 支持自动切换模式，可根据 URL 使用不同的代理情景模式。
> * 可导入、导出设置。
> * 支持在线列表，且能兼容 GFW List 。
> * 使用事件监视代理更改，更高效准确。
> * 支持改进的快速切换模式，随意在代理之间切换。
> 
> 为什么我要做这个扩展？ =>
> 
> 由于 @gh05tw01f 停止支持和更新 SwitchyPlus 项目，我决定自己对其代码进行修改。
> 
> 在自己用的同时，本着开源的精神，我也将项目使用 GPL 授权，并上传至商店方便各位使用。
> 
> 为什么你应该从 SwitchyPlus 转移到 SwitchySharp ？=>
> 
> 最重要的原因是， SwitchyPlus 项目已经不再更新，作者也不提供支持。而本项目还在开发过程中，提供支持和更新。
> 
> 其次，此扩展支持设置的导入导出，这是 SwitchyPlus 中没有的功能。
> 
> 最后，此扩展修复了 SwitchyPlus 中的很多 bug ，且增加了很多激动人心（？）的新功能，如一键切换中使用自动切换模式等。

相关链接：[安装地址](https://chrome.google.com/webstore/detail/dpplabbmogkhghncfbfdeeok
oefdjegm?hl=zh_CN)

## 配置 Proxy SwitchySharp

  * 在Chrome地址栏输入 about:flags 找到"实验性扩展程序 API"启用并重启浏览器。 （新版本可以不勾选）
  * 勾选在隐身模式下启用。

配置主界面如下：

[ ![SwitchySharp config](https://ohsolnxaa.qnssl.com/2012/03/switchysharp_1.png) ](https://ohsolnxaa.qnssl.com/2012/03/switchysharp_1.png)

其中的 HTTP 代理和端口，根据自己的需要填写。

相关链接： [让Chrome浏览器用上独立的代理 | 非诚勿扰](http://youcan.hourb.com/archives/19)

## Socks 用户的福音

Chrome 是不支持 socks 类型的代理服务器的（[bug
地址](http://code.google.com/p/chromium/issues/detail?id=29914)），所以类似 `ssh -D`
建立的 socks 连接都会无法使用，我们需要通过 Privoxy 来将 socks 转换到 http。

Arch Linux 下安装 Privoxy，其他发行版也是类似。
  
    pacman -S privoxy

配置 Privoxy，修改 `/etc/privoxy/config` 添加一行：

    
    forward-socks5 / 127.0.0.1:7070 .

注意上面的空格和末尾的点。

配置好 Privoxy 后，重启服务，Privoxy 默认在 8118 端口提供服务，可以使用 `127.0.0.1:8118` 来访问代理服务器。

参考链接：

* [ssh socks5 转 http « 细节的力量](http://xijie.wordpress.com/2009/12/08/ssh-
socks5-%E8%BD%AC-http-3/) * [Privoxy - Home Page](http://www.privoxy.org/)


## 使用某个 list

这事不能说太细，看图说话。

[ ![SwitchySharp config](https://ohsolnxaa.qnssl.com/2012/03/switchysharp_2.png) ](https://ohsolnxaa.qnssl.com/2012/03/switchysharp_2.png)

注意将某 list 加入切换规则，否则会无法获取 appspot 中的内容。

参考链接：https://autoproxy.org/zh-CN/node/61 （自备梯子）

