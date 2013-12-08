Title: Subclipse1.2.x的一个Bug
Author: alswl
Slug: a-bug-of-subclipse1-2-x
Date: 2010-03-20 00:00:00
Tags: Subclipse, SVN
Category: 工欲善其事必先利其器

### 背景

在使用Eclipse开发项目，提交属性svn:ignore时候，SVN报出一个错误。

> Failed to execute WebDAV PROPPATCH

svn: Commit failed (details follow):

svn: At least one property change failed; repository is unchanged

整整花了3个小时的时间在这上面纠缠，终于在某个邮件论坛找到一点点线索。

在[Re: Failed to execute WebDAV PROPPATCH](http://marc.info/?l=subversion-
users&m=121478169326627&w=2)上面，有人提到Subclipse无法执行，但是Tortuial SVN没有问题

### 原因

我用的Subclispe还是07年在工作室时候安装的1.2.3版本，因为一直懒，所以没有更新。

### 解决

卸载老版本的Subclipse，使用新版的Subclipse

卸载方法：Help - Install New Soft -&nbsp_place_holder; What is already installed ->
Uninstall

安装新版本Subclipse，传送门->[Subclipse1.6.10](http://subclipse.tigris.org/files/docume
nts/906/47423/site-1.6.10.zip)

