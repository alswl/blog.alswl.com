---
title: "通过Mail For Exchange实现S60 Google Calendar同步"
author: "alswl"
slug: "through-the-mail-for-exchange-to-achieve-s60-google-calendar-sync"
date: "2009-11-08T00:00:00+08:00"
tags: ["移动手持", "google", "symbian"]
categories: ["efficiency"]
---

原文出处：[通过Mail For Exchange实现S60 Google Calendar同步 | iMobApps-
手机应用软件](http://imobapps.com/2009/10/mail-for-exchange-s60-google-
calendar.html)

我测试了GooSync，开始收费了，而且半天没收到配置信息，然后就索性测试Mail For Exchange（貌似说有风险，我暂时没碰到，不过最好备份）

顺便说一下，[iMobApps](http://imobapps.com/)是一个很不错的手机咨询站点

******************************华丽的星星*************************

对于S60手机的Google
Calendar同步，之前本站介绍过[GooSync](http://imobapps.com/2009/05/goosync-s60-google-
calendar-sync.html)和[CalSyncS60](http://imobapps.com/2008/09/calsyncs60-two-
way-synchronization-between-nokia-s60-phone-and-google-calendar.html)，CalSyncS
60早早就开始收费，GooSync也与昨日宣布将[终止免费版服务](http://imobapps.com/2009/10/goosync-
lite.html)，好在可以通过[Mail For Exchange](http://www.google.com/mobile/products/syn
c.html#p=nokia_smart)来实现Email，Contacts和Calendar的同步。之前没有使用Mail For
Exchange主要是因为使用Mail For Exchange之后，你不能使用其他方式来实现同步。

具体设置可以看下图： ![image](/images/upload_dropbox/200911/tlu16djx.jpg)
![image](/images/upload_dropbox/200911/fwjcuuge.jpg)

![image](/images/upload_dropbox/200911/siait7ew.jpg)
![image](/images/upload_dropbox/200911/g3qei8kl.jpg)

安装时会提示：**在设备上安装并使用 Mail for Exchange 之后，您不应使用任何其他方法 (例如诺基亚 PC 套件)
来同步联系人、日历项或任务。 同时使用其他方法同步将会导致数据丢失、重复或损坏。**

**Mail For Exchange的连接设置：**

  * Exchange的服务器是 m.google.com，
  * 安全连接选「是」。
**证书设置：**

  * 用户名：你的Gmail邮件地址
  * 密码：你的Gmail密码
  * 域：m.google.com
**同步日程**： 

  * 可以选择手动同步或者自动同步；
**日历：**

  * 同步日历回溯：可以设置2周，一个月或者一年；
  * 初次同步：如果你希望保留手机上的Calendar内容，请务必选择「保留手机项目」
Mail For
Exchange还可以实现Contacts和Email的同步，不过个人觉得[Gmail的客户端](http://imobapps.com/2008/09
/gmail-mobile-client.html)也不错，并不追求Mail的实时Push，Contacts我通过[Google Sync](http://
www.williamlong.info/archives/1690.html)同步，所以对我个人而言，同步Calendar就足够了。

**注**：如果你只想同步Calendar的话，需要确保电邮、任务和联系人的同步设为「否」

**以防设置不当导致同步中出现资料丢失，强烈建议你在同步前对手机进行备份！！！**

经试验，单独同步Calendar的话还是可以实现和PC套件的同步。

[Mail For Exchange下载](http://www.nokia.com.cn/get-support-and-
software/software/mail-for-exchange/compatibility-and-download)
|[本站下载](http://www.boxcn.net/shared/xbtyu83yd8)（1.75Mb）

