---
title: "Ubuntu8.04的教育网源"
author: "alswl"
slug: "the-education-network-ubuntu8-04-source"
date: "2009-05-27T00:00:00+08:00"
tags: ["linuxer", "ubuntu"]
categories: ["coding"]
---

Google的话有很多源，北大的宣称5M，结果我都连不上，交大的宣称2M，我发现只有20kb/s，连更新语言包都超级慢。

最后经过我的测试，是成都电子科技大学的最快，2M左右，推荐使用。

特别注意，这是8.04的源，虽然8.10大部分能用，但会出现某些软件包找不到，请大家使用前做好备份。

速度的话，还是得自己测试，我只是推荐，下面的内容都是我复制过来自带的，不是我增加的。（PS:晚上时候我用官方的Mirror也3M/s）

` #北京市清华大学更新服务器（教育网，推荐校园网和网通用户使用）：

deb http://mirror9.net9.org/ubuntu/ hardy main multiverse restricted universe

deb http://mirror9.net9.org/ubuntu/ hardy-backports main multiverse restricted
universe

deb http://mirror9.net9.org/ubuntu/ hardy-proposed main multiverse restricted
universe

deb http://mirror9.net9.org/ubuntu/ hardy-security main multiverse restricted
universe

deb http://mirror9.net9.org/ubuntu/ hardy-updates main multiverse restricted
universe

deb-src http://mirror9.net9.org/ubuntu/ hardy main multiverse restricted
universe

deb-src http://mirror9.net9.org/ubuntu/ hardy-backports main multiverse
restricted universe

deb-src http://mirror9.net9.org/ubuntu/ hardy-proposed main multiverse
restricted universe

deb-src http://mirror9.net9.org/ubuntu/ hardy-security main multiverse
restricted universe

deb-src http://mirror9.net9.org/ubuntu/ hardy-updates main multiverse
restricted universe`

#沈阳市东北大学更新服务器（教育网，推荐校园网和网通用户使用）：

deb ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/ hardy main
multiverse restricted universe

deb ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/ hardy-backports
main multiverse restricted universe

deb ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/ hardy-proposed main
multiverse restricted universe

deb ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/ hardy-security main
multiverse restricted universe

deb ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/ hardy-updates main
multiverse restricted universe

deb-src ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/ hardy main
multiverse restricted universe

deb-src ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/ hardy-backports
main multiverse restricted universe

deb-src ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/ hardy-proposed
main multiverse restricted universe

deb-src ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/ hardy-security
main multiverse restricted universe

deb-src ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/ hardy-updates
main multiverse restricted universe

#厦门大学更新服务器（教育网服务器）：

deb ftp://ubuntu.realss.cn/ubuntu/ hardy main restricted universe multiverse

deb ftp://ubuntu.realss.cn/ubuntu/ hardy-backports restricted universe
multiverse

deb ftp://ubuntu.realss.cn/ubuntu/ hardy-proposed main restricted universe
multiverse

deb ftp://ubuntu.realss.cn/ubuntu/ hardy-security main restricted universe
multiverse

deb ftp://ubuntu.realss.cn/ubuntu/ hardy-updates main restricted universe
multiverse

deb-src ftp://ubuntu.realss.cn/ubuntu/ hardy main restricted universe
multiverse

deb-src ftp://ubuntu.realss.cn/ubuntu/ hardy-backports main restricted
universe multiverse

deb-src ftp://ubuntu.realss.cn/ubuntu/ hardy-proposed main restricted universe
multiverse

deb-src ftp://ubuntu.realss.cn/ubuntu/ hardy-security main restricted universe
multiverse

deb-src ftp://ubuntu.realss.cn/ubuntu/ hardy-updates main restricted universe
multiverse

#成都市 电子科技大学更新服务器（教育网，推荐校园网和网通用户使用）：

deb http://ubuntu.uestc.edu.cn/ubuntu/ hardy main multiverse restricted
universe

deb http://ubuntu.uestc.edu.cn/ubuntu/ hardy-backports main multiverse
restricted universe

deb http://ubuntu.uestc.edu.cn/ubuntu/ hardy-proposed main multiverse
restricted universe

deb http://ubuntu.uestc.edu.cn/ubuntu/ hardy-security main multiverse
restricted universe

deb http://ubuntu.uestc.edu.cn/ubuntu/ hardy-updates main multiverse
restricted universe

deb-src http://ubuntu.uestc.edu.cn/ubuntu/ hardy main multiverse restricted
universe

deb-src http://ubuntu.uestc.edu.cn/ubuntu/ hardy-backports main multiverse
restricted universe

deb-src http://ubuntu.uestc.edu.cn/ubuntu/ hardy-proposed main multiverse
restricted universe

deb-src http://ubuntu.uestc.edu.cn/ubuntu/ hardy-security main multiverse
restricted universe

deb-src http://ubuntu.uestc.edu.cn/ubuntu/ hardy-updates main multiverse
restricted universe

deb http://ubuntu.dormforce.net/ubuntu/ hardy main multiverse restricted
universe

deb http://ubuntu.dormforce.net/ubuntu/ hardy-backports main multiverse
restricted universe

deb http://ubuntu.dormforce.net/ubuntu/ hardy-proposed main multiverse
restricted universe

deb http://ubuntu.dormforce.net/ubuntu/ hardy-security main multiverse
restricted universe

deb http://ubuntu.dormforce.net/ubuntu/ hardy-updates main multiverse
restricted universe

deb-src http://ubuntu.dormforce.net/ubuntu/ hardy main multiverse restricted
universe

deb-src http://ubuntu.dormforce.net/ubuntu/ hardy-backports main multiverse
restricted universe

deb-src http://ubuntu.dormforce.net/ubuntu/ hardy-proposed main multiverse
restricted universe

deb-src http://ubuntu.dormforce.net/ubuntu/ hardy-security main multiverse
restricted universe

deb-src http://ubuntu.dormforce.net/ubuntu/ hardy-updates main multiverse
restricted universe

#上海市上海交通大学更新服务器（教育网，推荐校园网和网通用户使用）：

deb http://ftp.sjtu.edu.cn/ubuntu/ hardy main multiverse restricted universe

deb http://ftp.sjtu.edu.cn/ubuntu/ hardy-backports main multiverse restricted
universe

deb http://ftp.sjtu.edu.cn/ubuntu/ hardy-proposed main multiverse restricted
universe

deb http://ftp.sjtu.edu.cn/ubuntu/ hardy-security main multiverse restricted
universe

deb http://ftp.sjtu.edu.cn/ubuntu/ hardy-updates main multiverse restricted
universe

deb-src http://ftp.sjtu.edu.cn/ubuntu/ hardy main multiverse restricted
universe

deb-src http://ftp.sjtu.edu.cn/ubuntu/ hardy-backports main multiverse
restricted universe

deb-src http://ftp.sjtu.edu.cn/ubuntu/ hardy-proposed main multiverse
restricted universe

deb-src http://ftp.sjtu.edu.cn/ubuntu/ hardy-security main multiverse
restricted universe

deb-src http://ftp.sjtu.edu.cn/ubuntu/ hardy-updates main multiverse
restricted universe

#中国科学技术大学更新服务器（教育网，推荐校园网和网通用户使用）：

deb http://debian.ustc.edu.cn/ubuntu/ hardy main multiverse restricted
universe

deb http://debian.ustc.edu.cn/ubuntu/ hardy-backports main multiverse
restricted universe

deb http://debian.ustc.edu.cn/ubuntu/ hardy-proposed main multiverse
restricted universe

deb http://debian.ustc.edu.cn/ubuntu/ hardy-security main multiverse
restricted universe

deb http://debian.ustc.edu.cn/ubuntu/ hardy-updates main multiverse restricted
universe

deb-src http://debian.ustc.edu.cn/ubuntu/ hardy main multiverse restricted
universe

deb-src http://debian.ustc.edu.cn/ubuntu/ hardy-backports main multiverse
restricted universe

deb-src http://debian.ustc.edu.cn/ubuntu/ hardy-proposed main multiverse
restricted universe

deb-src http://debian.ustc.edu.cn/ubuntu/ hardy-security main multiverse
restricted universe

deb-src http://debian.ustc.edu.cn/ubuntu/ hardy-updates main multiverse
restricted univers

