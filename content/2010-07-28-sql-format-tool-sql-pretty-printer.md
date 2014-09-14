Title: SQL格式化工具-SQL Pretty Printer
Author: alswl
Slug: sql-format-tool-sql-pretty-printer
Date: 2010-07-28 00:00:00
Tags: 工欲善其事必先利其器, SQL Pretty Printer
Category: Efficiency

### 背景

最近写了一些SQL，数据库用的是MS-SQL，而SQL Server Management
Studio是不自带代码格式化功能的，这让我用起来很郁闷，PL/SQL Developer格式起来多爽啊。

在网上找了一下SQL格式化工具，只有一个用起来还不错的[在线版本](http://www.dpriver.com/pp/sqlformat.htm)，我测试
了一下，功能强大，可惜不支持中文，注释的中文会被打上？？

### SQL Pretty Printer

我在那个在线网站看到了Desktop Version的菜单，进去一看，哦，原来这个网站本身就在做一款SQL格式化工具的产品，叫做 SQL Pretty
Printer。

[![](http://upload-log4d.qiniudn.com/2010/07/spp_app.jpg)](http://upload-
log4d.qiniudn.com/2010/07/spp_app.jpg)

SQL Pretty Printer 的桌面版本

![](http://upload-log4d.qiniudn.com/2010/07/spp_code.jpg)

格式化好之后的代码

### 功能

SQL Pretty Printer目前提供4种使用方式，桌面版本，SSMS(SQL Server Management
Studio)插件，VS插件，和提供API接口。

[![](http://upload-log4d.qiniudn.com/2010/07/spp_ssms.jpg)](http://upload-
log4d.qiniudn.com/2010/07/spp_ssms.jpg)

SSMS(SQL Server Management Studio)插件版本

![](http://upload-log4d.qiniudn.com/2010/07/spp2code.jpg)

可以将SQL转化成代码格式，支持数种语言

![](http://upload-log4d.qiniudn.com/2010/07/spp2html.jpg)

可以将SQL转化成HTML格式

### 获取

使用版本只能提供30次，而且桌面版本的无法将代码复制出来，我使用的是SSMS插件版本，可以直接在查询器里面格式化，试用版的限制比较多。

翻遍SQL Pretty Printer的网站，终于发现了Get SQL Pretty Printer Desktop Version For
Free信息，作者说可以通过4种途径获取免费的授权码。

>   * 1.If you are a technical/software blogger or journalist willing to write
us up (honest reviews are the most useful to us) [email us](mailto:support@dpr
iver.com?subject=I%20want%20to%20review%20sql%20pretty%20printer%20on%20my%20s
oftware%20blog%21) a short blurb with the link to your blog and we'll send you
a license, FREE of charge, so that you can evaluate sql pretty printer
properly.

>   * 2.If you are willing to demo SQL Pretty Printer to an audience of at
least 15 people (at a user group, a conference, a BarCamp), [email us](mailto:
support@dpriver.com?subject=I%20want%20to%20demo%20SQL%20Pretty%20Printer%21)
your info and we'll give you two licenses, one for you to keep and one to give
away at the event, FREE of charge.

>   * 3.If you teach a high-school class, [email
us](mailto:support@dpriver.com?subject=I%20teach%20high-school%21) the name of
your school and your class, plus the number of students in your class. We will
send you a license for all of them.

>   * 4.A note to university students and professors: we currently do not
offer free licenses to universities, but we'll be happy to offer you an
additional 50% off any orders of 10 or more licenses. [Let us
know](mailto:support@dpriver.com?subject=Student%20Discount) if you're
interested and we'll set up a discount code for you.

很幸运，我有自己的软件博客，写完这篇文章之后，我就会向作者发出申请邮件。

### 最后

说说这个软件的弊病吧，那就是功能太单一。现在大部分的查询器都有格式化功能，只是M$这边没有加入这个功能，从该软件的产品线来看，很依赖于SSMS和VS，一旦他
们加入格式化功能，这个软件的使用价值就大大降低了。

### Links

下载链接：[http://www.dpriver.com/dlaction.php](http://www.dpriver.com/dlaction.php
)

在线版本（不支持中文）：[http://www.dpriver.com/pp/sqlformat.htm](http://www.dpriver.com/p
p/sqlformat.htm)

获取免费的授权码：[http://www.dpriver.com/products/sqlpp/getforfree.php](http://www.dpr
iver.com/products/sqlpp/getforfree.php)

### Others

WP Keyword Link这个插件在更新到版本 1.5.2之后会让正文中图片无法显示，出现类似http://log4d.com/****的URL，导致图
片显示失败，停用这个插件之后即可，期待作者下个版本修复这个问题。

### Update-2010-7-29

下午作者就给了答复，问我要哪一个版本的Key，第二天早晨拿到了SSMS版本的Licence。作者叫James
Wang，而且工作组叫GuduSoft，我怀疑作者是华人

再次感谢作者的慷慨~

