Title: 用户权限设计的问题
Author: alswl
Slug: design-of-user-rights
Date: 2009-06-25 00:00:00
Tags: 软件开发和项目管理
Category: Managment

### 问题

用户权限设计这一块，一直是一个我觉得比较难解决的问题。

以前我用了「伪继承」，虽然管理员继承了普通用户，但是数据库却是分开设计的。又或者压根没有继承关系，是两个不同的实体。

### 解决方案

这次在贴吧系统，有三个用户角色：普通用户、吧主、管理员，想设计的符合OO，但又要利于数据库的实现。就有几个问题需要解决：1.需要继承么；2.数据库怎么设计；
3.Hibernate怎么映射。最后参考几篇文章，设计成如下。

使用User类，Roll类，User具有一般用户属性，Roll负责角色，他们是1对1关系，最好在数据库有一张User-
Roll的对应关系表。来标明这个User具有哪个Roll。

在我这个系统，Roll类有三种，分别对应三种角色：普通用户，吧主和管理员。

这种独立出Roll角色类的方法被称为基于角色的用户权限设计方法。

[caption id="attachment_12439" align="alignnone" width="300" caption="User Roll UML类图"][![User Roll UML类图](https://ohsolnxaa.qnssl.com/upload_dropbox/200906/Snap2-300x148.jpg)](https://ohsolnxaa.qnssl.com/upload_dropbox/200906/Snap2.jpg)[/caption]

我给出的这个其实还不完善，完整的解决方案应该还包含ACL列表，可以定制Roll对应ACL列表的对应，来修改某一个角色的权限。因为我的系统角色固定，而且系统规
模比较小，我所说的三种发难已经能够满足我的要求了。

### 参考资料

用户权限设计<[猛击这里打开](http://blog.chinaunix.net/u1/42750/showart_359641.html)>

基于角色的用户权限设计问题<[猛击这里打开](http://blog.csdn.net/seapen/archive/2006/03/15/624734.a
spx)>

