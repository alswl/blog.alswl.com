Title: DDDSpace.com浴火重生了
Author: alswl
Slug: dddspace-com-bathed-in-fire-and-gave-birth-to
Date: 2009-12-24 00:00:00
Tags: 建站心得
Category: Coding

一大早过来，我就开始部署DDDSpace.com，上传文件和数据，修改数据库的域名，文章参考了["更换域名后应该做的事情 » Life Studio](http://wange.im/after-change-
domain.html)"。我原来的DDDSpace.cn所在的重庆主机还在停止80端口状态，域名管理器我也无法登录，所以不能做301修改了。

之后我索性更新到WordPress 2.9，出现了"wordpress Fatal error: Allowed memory size of
33554432 bytes
exhausted"这个错误，大意就是说内存超出指定大小。我在WordPress官方论坛找到了解决办法，原文在"[WordPress › Support »
Fatal error: Allowed memory size of 33554432 bytes exhausted (tried to
allocate](http://wordpress.org/support/topic/194370?replies=16)",解决办法是修改根目录下的
"wp-settings.php"，将内存限制由32M改到64M，直接搜索32M就可以了。

搜素数据库，一大堆DDDSpcae.cn，唉，还得慢慢测试慢慢改，还要重新申请各种域名上的服务。不过不管怎样，DDDSpace终于复活了。

同学们，赶紧修改你们的Feed地址啊！！！！

![image](https://4ocf5n.dijingchao.com/upload_dropbox/200912/phoenix.jpg)

感谢小张的支持，10号主机挺棒哦。

感谢GoDaddy支持支付宝，省了好多麻烦。

