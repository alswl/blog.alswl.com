

最近工作比较忙，自由上网的时间被大幅度减少，加上在啃.net的书，所以能够分享的东西就不多了。公司所在的部门需要将PMS和KMS整合在一起，正在对KMS进行
选型，我就趁这个机会把我使用知识管理系统的经验分享一下。

## 一、知识管理系统（KMS）

简单说一下知识管理的定义：指个人或团体通过工具建立知识体系并不断完善，进行知识的收集、消化吸收和创新的过程，这其中使用的工具也就是KMS。KMS应该帮助我们
队只是进行采集、精炼、索引、分类、检阅、检索、搜索的功能。

不多解释KMS了，省的看大段文字心烦，想做理论深入的去最下面的相关链接查找吧。

## 二、我想要的KMS

我理想中的KMS应该能够满足一下几点要求。

### 1、数据保存格式

数据的保存格式关系到知识的完整性和呈现方式，这是我最看重的一条。我理想中的保存格式是能够内嵌媒体信息，可以自定义内容的样式，最好是用大家比较习惯的文档体系，
比如h1/h2/h3/p/br/ol/li。在内嵌媒体内容的同时也要能够在知识点外挂其他类型文件，比如Excel、知识导图，甚至exe可执行文件。

数据保存格式也要考虑数据的移植性，因为一旦我们的KMS需要换一个系统，就会带来大量个工作，这个极其讨厌。使用xml/doc/excel/mm这些通用数据类型
存储信息可以在一定条件下解决这个问题。

数据存储的形式最好使用文件形式，尽量不要使用数据库，什么MySQL/MSSQL/SQLite，一旦知识数量到了一个规模，这反而会成为限制（我可不想为了一个小
小KSM而开一个后台服务器进程）。

### 2、数据采集方式

数据采集方式关系到采集是否顺手。所谓顺手，就是说我看到某个资源（文字 / 图片 /
网页），都可以通过尽可能少的步骤保存到我自己的KMS，比如通过常驻后台的托盘程序，又或者监视剪贴板指定格式内容。

相应的解决办法有从源获取，比如说可以直接读取我Google
Reader中打上星号的内容，从某个Feed获取内容，从我当前正在浏览的网页获取我所需要的内容（不保存那些广告和垃圾信息）。

### 3、数据索引

能够对所有的信息进行无限制分类和打标签，支持1->N分类和1->N标签即可，没有太多的花样了。

能够根据分类、标签、标题、正文多层次搜索，支持高级查找，比如说AND条件和OR条件。

### 4、数据同步和安全

能够将KMS的数据同步到网上，哦~换一个流行的说法，支持云同步。考虑到在家庭和工作电脑之间进行切换，这点还是需要的。

有一个剑走偏锋的办法，使用现在很多的同步软件，比如说DropBox、DBank和快盘，就可以把那些以文件形式保存数据的KMS信息进行同步。

KMS可能涉及到很多安全和隐私信息，所以必须建立对应帐户和安全机制。允许用户对分享、二次分享、隐私、禁止同步等选项进行详细设置。

### 5、协同工作

能够针对于部门小组进行知识管理，这属于企业级产品，不在今天讨论范围之内。其实对于团队来说，Wiki也是一个不错的选择，KMS太过于个性化了。

## 三、我使用的KMS-WizKnowledge

废话了这么多，终于进入重点了，我现在使用的KMS系统-WizKnowledge。

[![image](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/201009/wiz1.jpg)](../../static/images/upload_dropbox/201009/wiz1.jpg)

这款Wiz是我最早在[Louis](http://louishan.com)那里看到这篇文章《[Wiz(为知个人知识管理)正式版发布- Louis Han
Life Log](http://louishan.com/articles/wiz-personal-knowledge-
management.html)》，当时没有立即试用。之后在看到**同步控**也发布了相关的一篇日志《[WizKnowledge -
支持同步的个人知识整理工具 |
同步控](http://www.syncoo.com/wizknowledge-1988.htm)》，最后又看到xDash的一篇《[我的个人知识管理工具
[PKM] | 同步控](http://www.syncoo.com/my-pkm-tools-2038.htm)》，终于忍不住诱惑去下了试用。

现在用Wiz也大概一个多月了，我对应我上面的要求对Wiz进行一下品评一下。

### 1、优点

Wiz使用.ziw格式保存文件，其实这就是zip wiz的缩写，其内质是zip压缩的html文档。这种保存方式可以妥善的保存上文提到的内嵌式媒体，而且内部使
用html+css，能够方便数据展现和迁移。对于大部分选用KMS的朋友来说，使用html+css也不会带来学习曲线。

Wiz使用树形目录保存文件，这样就无法做到任意指定分类，但是带来好处是以文件夹方式保存知识内容，所以总体来说这算是优点。

![image](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/201009/wizcat.jpg)

![image](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/201009/wiz_path.jpg)

Wiz的每个文档都支持外接任意类型附件，并将其保存到.ziw中，这对于mm/doc/xls这些特殊类型来说特别有用。

Wiz支持多平台，其中有WM平台，还有Android版本。我试用过Android版本，很弱，问题很多。对我来说，移动手持上面的软体不需要太多功能，可以方便的
查看即可。

Wiz还支持第三方插件，目前官方发布版本集成的有导入文件、导入Google
Docs/日历、博客下载器、发布到博客。其中导入文件支持"*.htm;*.html; *.mht;*.nws; *.eml; *.txt;*.ini;
*.bat;*.inf; *.swf;*.bmp; *.jpg;*.jpeg; *.gif;*.png; *.doc;*.docx;
*.rtf;*.ppt;*.pptx; *.xls;*.xlsx;*.ziw; *.zip;*.cpp;*.hpp; *.cxx;*.c;*.h;
*.pas;*.dpr;*.java; *.js;*.cs;*.vbs; *.sql;*.oraclesql; *.idl;*.console;
*.shell;*.pl; *.php"这么多类型。

Wiz给每个注册用户提供300M的网络空间（从1.0.3不限制总空间大小，限制每月流量）。这点在同类产品中比较少见，极其方便了用户。

Wiz提供一个名为WizNote的小工具进行信息采集，同时会在IE中装插件。FireFox下面也有自己的.xpi小插件（功能有些问题，我还是使用FireBu
g获取innerHtml的方式操作）。

![image](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/201009/wiznote.png)

Wiz还附带一个一个WIzCalendar小工具，可以在日历上面布置知识点，这点对于有些同学来说比较方便，可以实现GTD功能。（因为我依赖于Google
Calendar，所以我不使用这个功能）

[![image](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/201009/wizcal.png)](../../static/images/upload_dropbox/201009/wizcal.png)

### 2、缺点

Wiz的缺点不多，说起来就是刚发行到正式版，还不是特别完善，比如安全机制，比如采集机制（我现在喜欢用FireBug获取元素的innerHtml直接复制到Wi
z的编辑器源码里）。

Wiz开发团队承诺永久免费，从他们的其他几款产品"网文快捕"等来看，还是比较有运营能力的，尤其是支持第三方插件，这在KMS中间不多见。

## 四、其他几款KMS

我选择Wiz不适没用试用其他KMS，这里我说一下不选择他们的原因。

### 1、EverNote

![image](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/201009/evernote.png)

EverNote是最近最火的同步工具，是的，它是同步工具，不是KMS。而且现在的EverNote基于.net
3.5，我直接崩溃。虽然我是.net程序员，但是我反感CS程序使用.net，尤其还是3.5sp1，天哪，我的2G电脑跑起来都觉得卡。

同事EverNote保存的文件格式也不适合做KMS，更多有关EverNote的信息可以看[善用佳软EverNote专题](http://xbeta.info
/tag/evernote)。

PS：EverNote是不错的同步工具，但是善用佳软的宣传力度也太大了吧~

### 2、OneNote

微软的办公软件体系好大哦，OneNote是Office 2007之后逐渐变得比较重要的部分。OneNote存放时本地的，似乎在OneNote
2010的正版用户支持数据同步。

因为OneNote体积比较大，我追求速度和体积，加之没有使用Offcie全系列，所以没有选用OneNote。准确来说，Outlook+SharePoint+
OneNote是一整套的企业级KMS，OneNote更注重于收集。

我使用OneNote用的不多，感兴趣的朋友到这里[OneNote爱好者](http://www.onenoter.com/)可以看到更多信息。

PS：[OneNote 2010试用版下载地址](http://microsoft-office-onenote.softonic.cn/download)

### 3、PKM

PKM = Pin Knowledge Managerment，说起来这款软件挺早的，使用KMS比较早的朋友们应该都知道这款软件。我使用这款软件的第一印象是
：好山寨的界面啊，居然可以选取工具栏，虽然是VB写的，但也不至于如此吧~

[![image](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/201009/pinE1.jpg)](../../static/images/upload_dropbox/201009/pinE1.jpg)

我使用时候还遇到了诸多问题，比如附件无法拖入，网页到html无法转换成功，甚至开启PKM之后，我的QQ2010聊天界面的Alt键无法使用，真是诡异。

![image](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/201009/pinE2.jpg)

![image](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/201009/pinE3.jpg)

PKM的功能看上去很强大，似乎比Wiz更专业，作者给了很多教程。但是最不喜欢的是居然用doc保存文档，这搞毛啊，无论是大小还是速度都是我不能忍受的。同时PK
M分为免费版和专业版，专业版需要花票票购买。

PKM在KMS的普及上做了相当多的工作，这点上我很佩服和感谢作者，详情可见[PKM全民推广系列一：PKM定义 - 专业个人知识管理软件研究 -
博客园](http://www.cnblogs.com/pinpkm/archive/2007/10/16/925606.html)。

### 4、其他一些KMS

Google Docs其实也能做成KMS，还支持团队协作，但是，你懂的……

![image](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/201009/maiku.jpg)

盛大推出了线上KMS-[麦库](http://note.sdo.com/)，我支持盛大的这次向KMS进军，可惜线上……你懂的……这不是我的菜……

再其他……我就不懂了……

## Last

好啦，介绍到这里，总算是大功告成，一篇博文搞了两天，真是吃力~


