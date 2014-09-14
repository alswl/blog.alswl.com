Title: Ubuntu8.10下MySQL的安装
Author: alswl
Slug: ubuntu8-10-under-the-mysql-installation
Date: 2009-05-27 00:00:00
Tags: Linuxer, MySQL, Ubuntu
Category: Coding

Ubuntu下的MySQL安装本应该很简单，但是如果因为修改了软件源的话，反而变得麻烦起来。

为了加快更新一些组件的速度，我加入了清华的、交大等大学的源，是8.04下Ubuntu版本的，这个直接导致了之后安装MySQL的问题。

当选择Mysql-server之后，需要一堆组建，要手动安装，基本上出现这种提示，就没戏了，硬着头皮查找软件包，最后到一个perl-
api的软件包这里就再也进行不下去了。

Google了好一会，才有一个人的答案正确，说是8.10下用8.04的源就会有这种问题，我换成原始的备份了的源

下面就是原始的源，使用这个找到MySQL之后就一次成功了 ` # deb cdrom:[Ubuntu 8.10 _Intrepid Ibex_ -
Release i386 (20081029.5)]/ intrepid main restricted

# See http://help.ubuntu.com/community/UpgradeNotes for how to upgrade to

# newer versions of the distribution.`

deb http://mirror.rootguide.org/ubuntu/ intrepid main restricted

deb-src http://mirror.rootguide.org/ubuntu/ intrepid main restricted

## Major bug fix updates produced after the final release of the

## distribution.

deb http://mirror.rootguide.org/ubuntu/ intrepid-updates main restricted

deb-src http://mirror.rootguide.org/ubuntu/ intrepid-updates main restricted

## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu

## team. Also, please note that software in universe WILL NOT receive any

## review or updates from the Ubuntu security team.

deb http://mirror.rootguide.org/ubuntu/ intrepid universe

deb-src http://mirror.rootguide.org/ubuntu/ intrepid universe

deb http://mirror.rootguide.org/ubuntu/ intrepid-updates universe

deb-src http://mirror.rootguide.org/ubuntu/ intrepid-updates universe

## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu

## team, and may not be under a free licence. Please satisfy yourself as to

## your rights to use the software. Also, please note that software in

## multiverse WILL NOT receive any review or updates from the Ubuntu

## security team.

deb http://mirror.rootguide.org/ubuntu/ intrepid multiverse

deb-src http://mirror.rootguide.org/ubuntu/ intrepid multiverse

deb http://mirror.rootguide.org/ubuntu/ intrepid-updates multiverse

deb-src http://mirror.rootguide.org/ubuntu/ intrepid-updates multiverse

## Uncomment the following two lines to add software from the 'backports'

## repository.

## N.B. software from this repository may not have been tested as

## extensively as that contained in the main release, although it includes

## newer versions of some applications which may provide useful features.

## Also, please note that software in backports WILL NOT receive any review

## or updates from the Ubuntu security team.

# deb http://cn.archive.ubuntu.com/ubuntu/ intrepid-backports main restricted
universe multiverse

# deb-src http://cn.archive.ubuntu.com/ubuntu/ intrepid-backports main
restricted universe multiverse

## Uncomment the following two lines to add software from Canonical's

## 'partner' repository. This software is not part of Ubuntu, but is

## offered by Canonical and the respective vendors as a service to Ubuntu

## users.

# deb http://archive.canonical.com/ubuntu intrepid partner

# deb-src http://archive.canonical.com/ubuntu intrepid partner

deb http://mirror.rootguide.org/ubuntu/ intrepid-security main restricted

deb-src http://mirror.rootguide.org/ubuntu/ intrepid-security main restricted

deb http://mirror.rootguide.org/ubuntu/ intrepid-security universe

deb-src http://mirror.rootguide.org/ubuntu/ intrepid-security universe

deb http://mirror.rootguide.org/ubuntu/ intrepid-security multiverse

deb-src http://mirror.rootguide.org/ubuntu/ intrepid-security multiverse

