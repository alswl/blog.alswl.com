Title: IIS IE7 Opera Firefox 需要用户名和密码？【转载】
Author: alswl
Date: 2009-07-30 00:00:00
Tags: FireFox, IE7, Opera
Category: 综合技术
Summary: 

转载自《[IIS IE7 Opera Firefox 需要用户名和密码？ -
睿之工作室](http://www.ruizhisky.cn/article/Digest/207.htm)》（虽然从图片上来看是转载自多彩工作室```）

我先说几句：在FireFox about:config那里输入值时候，如果有多个网址应该用逗号隔开，如「localhost,
127.0.0.1」，这样比原文章中只添加localhost要更加方便。

转载的文字加灰色

Windows XP Professional IIS 5.1

原因：由于安全性能优越IE7.0的internet默认采用的「用户被询问是否允许带参数加载或编码控件」选项，也就是总是要验证用户是否有参数
加载，而IIS默认采用的匿名登录不进行任何验证，而前后的internet和IIS的设置矛盾，ie7的权限优先于iis所以冲突导致总是要密码验证。

![](http://www.i170.com/Attach/5DE1DA55-8E8E-4A0A-8768-DB93CD5E0E6A)

![](http://www.i170.com/Attach/2681B4F4-D11A-47ED-8FB9-E7B0BE76FC5A)

**Firefox**

Firefox 登录本地站点也需要用户名和密码的吧，用此办法即可解决

在Firefox地址栏中输入：about:config

然后在过滤器中输入：NTLM

双击network.automatic-ntlm-auth.trusted-uris,

在输入值中输入   localhost

重启FireFox,重新访问站点就可以解决这个问题了。

**Opera**

在Opera地址栏中输入：about:config

找到Network点击打开折叠

去掉Check Local Hostname后面的勾后保存

重启Opera,重新访问站点就可以解决这个问题了。

![](file:///C:/DOCUME%7E1/%E7%8B%84%E6%95%AC%E8%B6%85/LOCALS%7E1/Temp/moz-
screenshot.png)

