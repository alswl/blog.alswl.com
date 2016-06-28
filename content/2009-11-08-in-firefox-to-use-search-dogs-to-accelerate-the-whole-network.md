Title: 在FireFox下使用搜狗全网加速
Author: alswl
Slug: in-firefox-to-use-search-dogs-to-accelerate-the-whole-network
Date: 2009-11-08 00:00:00
Tags: 技术达人, FireFox
Category: Efficiency

搜狗浏览器加速功能很讨喜，尤其对我们这种6毛电信，2毛钱跑教育网的用户来说。但是我更喜欢火狐环境，想在FireFox环境下使用搜狗代理服务器，于是就有了此文
。

原文链接：[firefox使用搜狗教育网代理 | 二月鸟的天空](http://dan.febird.net/2008/12/firefox.html)

我没能成功地用bat运行子进程，所以只能开着搜狗浏览器使用加速功能。在FireFox下使用FoxyProxy进行代理管理，相当方便。

上图：

[![firefoxinsogou](http://upload-log4d.qiniudn.com/2009/11/firefoxinsogou.jpg)](http://upload-log4d.qiniudn.com/2009/11/firefoxinsogou.jpg)

*********************************正文终于开始拉**********************************

就只想用用Sogou的代理，本人还是更喜欢 firefox的，所以分析了Sogou程序的进程之后上个 国外网站就找到解决方法了。

其实Sogou代理的原理原理设这样的，首先如果你设置了 「启用教育网代理」，那么你的sogou会新建一个子进程，专门做代理使用的，用Process
Explorer 可以看到 这个子进程的命令行：

    
    "C:Program FilesSogouExplorerSogouExplorer.exe"  -proxy
       "C:Program FilesSogouExplorerat1.dll"
       "CNC" "C760E475E7821B9EDA873346AC0C76D3

(可以将改行文件写成 .cmd 或者 .bat 直接执行)

在TCP/IP 选项卡还可以看到 该进程在 8081和8082两个端口 LISTENING。

最末尾的是和机器相关的识别码，可能每个人都不一样，如果你运行这个程序后，就自动在本地有了一个代理了。使用其他浏览器，就可以轻松使用这个代理突破教育网了。

代理地址是 127.0.0.1:8081 类型 http将下面文本保存为 REG 文件，双击导入即可开机自动启动Sogou代理

    
    Windows Registry Editor Version 5.00
    [HKEY_LOCAL_MACHINESOFTWAREMicrosoftWindowsCurrentVersionRun]
    "Sogou Proxy"="C:Program FilesSogouExplorerSogouExplorer.exe" -proxy
    "C:Program FilesSogouExplorerat1.dll" "CNC" "C760E475E7821B9EDA873346AC0C76D3

注意替换后面的识别码

这种方法同样可以使用于其他浏览器，只要在相应的浏览器中设置代理即可。Good Luck!!

