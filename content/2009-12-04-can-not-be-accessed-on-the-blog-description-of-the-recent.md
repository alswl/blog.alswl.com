Title: 关于博客最近无法访问的说明
Author: alswl
Slug: can-not-be-accessed-on-the-blog-description-of-the-recent
Date: 2009-12-04 00:00:00
Tags: 日记
Category: Life

呃，由于某些原因，服务器所在的江西机房停止了IDC服务，我今天晚上刚更换了服务器。我向在这段时间访问我博客却发现404错误的童鞋们报以10万分抱歉~

网上搜索相关新闻，原来很多机房有非法信息和未备案网站，被叫停了，我所在的江西景德镇服务器属于重灾区。幸好那天早晨备份了数据库和文件，基本没有造成什么损失。花
了1个多小时搬家，除了一个Share-This插件工作不正常，貌似没有发现其他问题。

Share-This的这个插件在[http://log4d.com/wp-content/plugins/share-this/share-this.php?akst_action=css](http://log4d.com/wp-content/plugins/share-this/share-this.php?akst_action=css)路径上会返回500内部服务器错误，搜索结果为文件权限问题，我之后设定为755/777都没有效
果。没办法，暂时停用这个插件了。

Update:09_12_04-23:29：这个问题我已经解决，问题出在wp-content/wp-include文件夹的权限当初被我错误的设定为777，正
确的应该为755，导致读取错误，就有了内部服务器500错误。用Ftp工具对这两个文件夹及其子文件夹进行轮询修改为755，问题即可解决。

ps:感慨到，搬家果然难啊~

附：近期被封机房名单

  
上海怒江移动（1号楼的基本没多少恢复的 到目前也没有解封）

上海漕河泾网通

上海漕宝路电信（开始封杀小段，现在封杀大段）

浙江金华电信

浙江金华网通

浙江绍兴电信（这个知道两家大的代理被封，保守估计超过4000台）

江西景德镇电信（直接停止IDC服务 最惨的就是他了）

河北网通（什么机房不知道）

江苏电信扬州机房

安徽合肥电信IDC机房

北京亦庄网通机房

  
2009-12-02 中国电信景德镇分公司终止与所有IDC业务合作

但愿上述的机房能够尽快恢复工作，也希望那些没有备案或者有异常内容的站点为大家的利益着想，千万不要再出现这样的事件了。

Update:测试上传图片的权限

[![image](http://upload.log4d.com/upload_dropbox/200912/xiaobai_wifi.jpg)](http://upload.log4d.com/upload_dropbox/200912/xiaobai_wifi.jpg)

