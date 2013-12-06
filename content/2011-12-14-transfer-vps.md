Title: 更换VPS
Author: alswl
Slug: transfer-vps
Date: 2011-12-14 00:00:00
Tags: VPS
Category: Linuxer
Summary: 

Log4D挂了整整一天，原因是因为VPS扩容导致系统无法启动。

我使用的VPS是[PhotonVPS](http://www.photonvps.com/billing/aff.php?aff=2188)的WARP.25
套餐。买时候套餐里面硬盘空间是2个G，前几天朋友告诉我新套餐变成了10G。我就发了ticket给客服，他们很快答应帮我升级VPS。我就将数据备份出来，静候升
级。

等了半天没反应，又咨询过后才知道新加入的硬盘空间需要重装系统才能启用。好吧，正好我想将CentOS 6换成Arch（Arch用的太顺手了）。

吭次吭次一阵捣鼓（其实重装系统就按一个按钮而已 ^_^），Arch装好了，然后发现系统无法启动了，悲剧鸟。

继续咨询客服，恩，这里插播一下，PhotonVPS的客服回复都是英文，但是可以发送中文过去，貌似有翻译助阵（不过英文文档看多了，简单的也能来两句，hiahi
a）。客服很快确认，Arch在目前VPS无法正常使用，坑爹阿。

我继续捣鼓，尝试Ubunt/Cent OS，发现都无法启动vps（症状是启动一下下之后立马又变成离线状态）。

继续找客服，最后客服给我重新分配了vps和ip，问题解决。

然我我又开始吭次吭次的装软件，最近系统装多了，手慢慢就熟了。

先升级一下系统`apt-get update upgrade`，然后创建用户，养成不使用root的好习惯。顺带装一些顺手工具vim/git/screen。

Ubuntu 11.04下面官方源里面带nginx/php5/php-fpm/php-mysql/mysql-
server，所以不用自己编译可以节省很多时间。

最后装上pptpd，不解释。

最近的装机事件频发，同志们阿，做好备份，备份才是王道阿。

