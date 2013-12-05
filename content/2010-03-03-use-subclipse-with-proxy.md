Title: 使用subclipse代理
Author: alswl
Date: 2010-03-03 00:00:00
Tags: Eclipse, Subclipse, SVN
Category: 工欲善其事必先利其器
Summary: 

&nbsp_place_holder;公司网络必须使用代理，今天更新自己写的一个Utils到Google Project
Host时候，出现无法打开SVN服务器的现象，我在浏览器测试了那几个目录，都没有问题，猜到是代理连接的问题。

Eclipse的代理设置在"**General-Network Connections**"中设置，很明显，Subclipse不在这里设定。

PS：在写的是一个DataBase->Java 3层代码生成器，想仿照[**动软.NET生成器**](http://www.maticsoft.com/)那
样写，今天刚写完生成Bean的一些版本，自己计划在半年时间内写一个beta版。

下面是解决办法，来自 [百亩森林 »
解决windows下subclipse穿过代理连接subversion服务器](http://blog.baimusenlin.com/83.html)

×××××&&以下原文&&×××××

解决windows下subclipse穿过代理连接subversion服务器

1、cmd命令提示符输入 echo %APPDATA%

2、进入第一步输出的目录下，并找到Subversion目录(如C:Documents and
SettingsAdministratorApplication DataSubversion)，注意此目录为隐藏目录。

3、在servers文件中的最后[global]后增加

    
    http-proxy-host =192.168.1.1
    http-proxy-port =80
    http-proxy-username =username
    http-proxy-password =password

