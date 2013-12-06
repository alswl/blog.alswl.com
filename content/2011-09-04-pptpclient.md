Title: 使用pptpclient连接vpn网络[译文]
Author: alswl
Slug: pptpclient
Date: 2011-09-04 00:00:00
Tags: arch, pptp, VPN, 译文
Category: Linuxer
Summary: 

最近在ddwrt配置vpn，参考了arch的pptpclient配置文档[Microsoft VPN client setup with pptpclien
t](https://wiki.archlinux.org/index.php/Microsoft_VPN_client_setup_with_pptpcl
ient)，同时顺便花了一点时间翻译成中文，正文如下（使用[wiky.js](https://github.com/tanin47/wiky.js)转换pe
diawiki到html，原文会有更多的wiki模板样式便于查看，有问题请参照原文）。

pptpclient是一个实现Microsoft PPTP协议的程序。因此它能够被用来接入另一个Microsoft VPN网络，比如学校和单位。

### 安装PPTPClient

pptpclient由安装包pptpclient提供，运行下列命令可以安装：

# pacman -S pptpclient

### 配置

你需要从网络管理员获取以下信息来配置pptpclient:

  * VPN服务器的ip或者域名
  * VPN隧道名称
  * Windows域（不是所有网络都需要）
  * VPN用户名
  * VPN密码

## 编辑配置文件

用你称手的编辑器打开/etc/ppp/options.pptp。这个文件为你的VPN连接启用了一系列默认安全设置。如果你连接时候出现问题，你可以自定义配置。
你的options.pptp文件最少需要包含以下内容：

    
    lock
    noauth
    nobsdcomp
    nodeflate
    

## 编辑密码文件

下一步，打开或者创建/etc/ppp/chap-
secrets。我们将在这个文件里面存储你的密码，记得修改权限让除root之外所有用户不能访问它。这个文件的格式如下：

    
    <DOMAIN>\<USERNAME> PPTP <PASSWORD> *

如果你的服务器不要求域，则配置如下：

    
    <USERNAME> PPTP <PASSWORD> *
    

替换掉上文中范例中的占位符。注意，如果你的密码包含特殊字符，比如"$"，你需要用双引号把它们包起来。

## 命名你的VPN隧道

用你称手的编辑器创建类似/etc/ppp/peers/的文件，把这里替换成你的VPN连接名。这个文件设置之后看起来如下：

    
    pty "pptp <SERVER> --nolaunchpppd"
    name <DOMAIN>\<USERNAME>
    remotename PPTP
    require-mppe-128
    file /etc/ppp/options.pptp
    ipparam <TUNNEL>

{{Note|跟刚才一样，如果你的连接不要求域，忽略范例中的"\"}} {{Note|PPTP远程主机使用Chap-Secrets文件中的}}

是VPN服务器的地址，是你所属的域，是你将要用来连接服务器的用户名，是连接的名称。

{{Note|如果你不需要使用MPPE，你应当从/etc/ppp/options.pptp中移除require-mppe-128这个选项}}

创建你的连接

用root执行以下命令来确保配置是正确的： # pon $TUNNEL debug dump logfd 2 nodetach
如果一切都配置好了，pon命令应当不会自动结束。一旦你感觉差不多OK了，就可以终止这个命令。 {{Note|另一个用来确保配置正确的命令是ifconfig
-a，看看里面时候有一个名叫ppp0的新驱动，并且还是可用的}} 执行以下命令来连接VPN隧道： # pon
是你之前命名过的VPN隧道名称。注意使用root命令执行。

## 配置路由

一旦你成功连接上VPN，你就可以和VPN服务器交互了。当然在此之前，咱们需要添加一个新的路由到你的路由表，从而可以接入远程网络。

{{Note|根据你的环境配置，你可能需要每次都重复添加路由信息}}

你可以阅读[PPTP Routing Howto](http://pptpclient.sourceforge.net/routing.phtml)来获得更
多如何添加路由的信息，里面还有很多范例。 &nbsp_place_holder;

## 选择路由

对我来说，只有传输到VPN网络的数据包才应该走VPN连接，所以我添加如下路由条目： # route add -net 192.168.10.0
netmask 255.255.255.0 dev ppp0 这将路由所有目的地址为191.168.10.xxx的数据到VPN连接。
&nbsp_place_holder;

## 配置为默认路由

如果你想要所有数据从VPN连接走，下面这条命令包你爽： # route add default dev ppp0
{{Note|所有数据从VPN连接走的话会比正常连接慢一些}} &nbsp_place_holder;

### 断开连接

下面这条命令用来断开VPN连接： # poff  是你VPN连接的名称。

### 把一个VPN连接配为默认启动

你可以在rc.d创建一个快捷命令来实现自动在后台连接VPN网络。

{{Note|和平常一样，是你隧道的名字，是你加入路由表的命令。}}

    
    #!/bin/bash

. /etc/rc.conf

. /etc/rc.d/functions

DAEMON=<TUNNEL>-vpn

ARGS=

[ -r /etc/conf.d/$DAEMON ] && . /etc/conf.d/$DAEMON

case "$1" in

start)

stat_busy "Starting $DAEMON"

pon <TUNNEL> updetach persist &> /dev/null && <ROUTING COMMAND> &>/dev/null

if [ $? = 0 ]; then

add_daemon $DAEMON

stat_done

else

stat_fail

exit 1

fi

;;

stop)

stat_busy "Stopping $DAEMON"

poff MST &>/dev/null

if [ $? = 0 ]; then

rm_daemon $DAEMON

stat_done

else

stat_fail

exit 1

fi

;;

restart)

$0 stop

sleep 1

$0 start

;;

*)  
echo "usage: $0 {start|stop|restart}"

esac

注意，我们可以使用updetach和persist这两个附加命令在pon上。updetach保证pon阻塞知道连接被建立。另外一个命令persist保证网络
自动重练。如果需要开机自动启动，则添加@-vpn到rc.conf的DAEMONS中去。

### 注意

你可以在[pptpclient website](http://pptpclient.sourceforge.net/)查到更多关于pptpclient的配
置信息。Ubuntu的帮助手册也有一些帮助你配置的信息。这些范例能够很轻松的稍加变换从而添加到daemons中去，从而帮助你自动化运行。
&nbsp_place_holder;

