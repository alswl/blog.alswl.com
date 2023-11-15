

本文乃08-09校内日志存档，我一起给发布了，如果给大家阅读造成困难，我深感抱歉

这个系统我还是很得意的，是我大二时候学C#时候巅峰之作，那时候刚学完网络，
还没开任何网络编程，那时候第一次接触SourceForge，参考了好多英文资料。

----

# AzaChat管理系统 #
Powered by DDD & King ZD

## 系统功能 ##

* 登录，注册，群聊，私聊，踢人，聊天字体设置，字体颜色，图片插入，图文混编，音效播放，抖动窗体(模仿QQ)
* 聊天人员管理，数据库管理，数据库查找功能
* 皮肤更换功能

## 系统说明 ##

这个系统是我这个学期课程设计，花了我将近一个多月的时间(期末考试阶段，很忙 - -#)，在写之前，我完全不懂数据库和网络传输，C#和面向对象思想也是这学期刚开的。虽然Bug还很多，但我仍然写出来了，很是开心。

上传到CSDN，希望对大家有帮助。 
Aza的来源是因为一个笑话，一个女人是500只鸭子，我想到聊天室就应该那种AzaAza的聊天声音，嘿嘿。

代码我给，论文自己写。。。看懂了别人的代码就是你的，看不懂，还是我的。。。
写了很多注释，相信对大家有帮助的

## 版本 ##

我是在VS2008下面开发的，下载包里面自带转换器可以将项目文件转换到VS2005。
Sql server的版本是vs自带的sql server 2005 express

## 数据库说明 ##

1. 将自带的两个数据库文件User.mdf和Server_log附加到数据库
1. 将数据库登录方式打开为Windows身份验证和Sql Server验证
1. sa的密码可以自己改
1. 如果想在数据库服务器和聊天服务器分开的话，必须将数据库服务器的远程连接选项打开

更详细的设置方式可以去查CSDN

```
服务器帐号：sa
密码：123456

管理员帐号：admin
密码：admin

用户帐号：123
密码：123
```

更多帐号可以注册和去服务器端管理。

客户端普通帐号可以随时注册，服务器端必须是管理员帐号登录。
用起来很简单，登录进去就知道了。

PS:程序在.Net Framework2.0下写，请确保电脑已经有.Net Framework2.0或者更高版本，否则会报错

Powered by DDD

E-mail:alswlwangzi(a)163.com

## 更新 ##

2008.7.11更新

更新内容：

V1.3版本更新：修改图片传输大小限制Bug,增强数据管理删选功能，修改在线用户查看，增加查看对方IP地址和连接端口功能

V1.2」版本更新：加入远程数据库登录管理功能

V1.1版本更新：加入服务器数据管理，修改增加删除数据保存的一些Bug

![img](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/200910/A972857781312POT.jpg)

![img](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/200910/A983104784976POT.jpg)


![img](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/200910/A979487865902POT.jpg)

![img](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/200910/A976688814655POT.jpg)

![img](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/200910/A039328251736CUC.jpg)

![img](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/200910/A037255836541CUC.jpg)

![img](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/200910/A016564641801CUC.jpg)

![img](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/200910/A014442672895CUC.jpg)

![img](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/200910/A009044384619CUC.jpg)

![img](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/200910/A004793674766CUC.jpg)

![img](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/200910/A002612293529CUC.jpg)


终于写完了，虽然很累，不过真的很开心。

