Title: 关于 NetworkManager / PolicyKit / ConsoleKit 的那些屌事
Author: alswl
Slug: networkmanager-policykit-consolekit
Date: 2012-05-17 09:07
Tags: Linuxer, NetworkManager, PolicyKit, ConsoleKit, GDM, Gnome
Category: Coding


在使用 Awesome 的过程中，我又遇到了一个老问题「NetworkManager 在非 Gnome
环境启动后，会无法 添加 / 删除 / 编辑 无线连接」。明眼人一看就知道，
这是权限的问题。

## 问题描述 ##

我的环境是 **ArchLinux / xmonad 0.10 / awesome v3.4.11 / GDM 3.4.1 / NetworkManager 0.9.4.0**，
下面我用 awesome 做示例，其他非 Gnome WM 也应该是类似配置。


我的 WM 启动流程是：
通过 GDM 启动 xmonad / awesome，启动 xsession 是 `/usr/share/xsessions/awesome.desktop`，
内容如下

<!-- more -->

``` ini
[Desktop Entry]
Name=Awesome
Comment=This session logs you into Awesome
Type=Application
Exec=ck-launch-session dbus-launch $HOME/.start-session.sh awesome
TryExec=/usr/bin/awesome
```

`$HOME/.start-session.sh` 中的作用是启动 **nm-applet** 和 **exec awesome**。

启动之后的情况是 NetworkManager 无线 编辑/删除 按钮变灰无法点击，或者可以点击，
但是会发生 **insufficient privileges** 错误。

![insufficient privileges](http://upload-log4d.qiniudn.com/2012/05/insufficient-privileges.png)


## 问题原因 ##

这个问题是由 PolicyKit 和 ConsoleKit 启动不当引起的。

PolicyKit 是：

> PolicyKit allows fine-tuned capabilities in desktop enviroment. Traditionally only privilaged user (root) was allowed to configure network. However while in server enviroment it is reasonable assumption it would be too limiting to not allowed to connect to hotspot on laptop. Still however you may not want to give full privilages to this person (like installing programs) or you want to limit options for some people (for example on your children laptops only 'trusted' networks with parential filters can be used). As far as I remember it works like:
> 
> * Program send message to daemon via dbus about action
> * Daemon uses PolicyKit libraries/configuration (in fact PolicyKit daemon) to determine if user is allowed to perform action. It may happen that the certain confition must be fullfilled (like entering password or hardware access).
> * Deamon performs action according to it (returns auth error or perform action)

ConsoleKit 是：

> In short consolekit is service which tracks user sessions (i.e. where user is logged in). It allows switching users without logging out [many user can be logged in on the same hardware at the same time with one user active]. It is also used to check if session is "local" i.e. if user have direct access to hardware (which may be considered more secure then remote access).

参考：[What are ConsoleKit and PolicyKit? How do they work?](http://unix.stackexchange.com/questions/5220/what-are-consolekit-and-policykit-how-do-they-work)

所以简而言之，ConsoleKit 是用来管理用户会话的，PolicyKit 是用来处理用户申请特殊权限的，
他们两个经常工作在一起。

有个 PolicyKit 认证 API 教程可以一看：

* [使用 PolicyKit 进行身份认证（上）](http://www.kissuki.com/blog/2009/03/10/policykit/)
* [使用 PolicyKit 进行身份认证（中）](http://www.kissuki.com/blog/2009/03/12/policykit/)
* [使用 PolicyKit 进行身份认证（下）](http://www.kissuki.com/blog/2009/03/13/policykit/)

我的这个问题就是由于 PolicyKit 无法正确授权引起的。

## 问题解决 ##

我开始吭次吭次的 Google，一会就找到了 Arch Wiki 中 [NetworkManager](https://wiki.archlinux.org/index.php/NetworkManager#Set_up_PolicyKit_permissions) 的解决办法：

``` bash
exec ck-launch-session dbus-launch wm
```

写的很清楚，使用 **ck-launch-session** 和 **dbus-launch** 来加载 WM。但是我已经使用
`ck-launch-session` 来启动 WM 了。

随后我把怀疑的目光放到 `/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1`
这个程序给系统提供 PolicyKit 权限认证，请求时候会让用户输入密码，如下图：

![PolicyKit Agent](http://upload-log4d.qiniudn.com/2012/05/policykit-agent.png)

可惜还是不行。

我甚至还参考[Using gnome keyring in xmonad](http://blog.san-ss.com.ar/2011/03/using-gnome-keyring-in-xmonad.html)
试图手工建立一个 Gnome Keyring。事实证明，Gnome Keyring 和这个问题无关。

最后，我用 `ck-list-sessions` 命令查看运行的用户 Session，发现同时运行着两个，
一个处于 `Active`，一个不处于 `Active`，这下真相大白了：GDM 启动时候会自己启动
`ck-launch-session`，不用自己手动启动，否则会造成两个会话而无法正确授权。

```
Session2:
	unix-user = '1000'
	realname = 'Jason Ti'
	seat = 'Seat1'
	session-type = ''
	active = TRUE
	x11-display = ':0'
	x11-display-device = '/dev/tty7'
	display-device = ''
	remote-host-name = ''
	is-local = TRUE
	on-since = '2012-05-17T00:54:31.706019Z'
	login-session-id = '2'
Session3:
	unix-user = '1000'
	realname = 'Jason Ti'
	seat = 'Seat1'
	session-type = ''
	active = False
	x11-display = ':0'
	x11-display-device = '/dev/tty7'
	display-device = ''
	remote-host-name = ''
	is-local = TRUE
	on-since = '2012-05-17T00:54:33.3465302Z'
	login-session-id = '2'
```

修正 `/usr/share/xsessions/awesome.desktop` 如下：

``` ini
[Desktop Entry]
Name=Awesome
Comment=This session logs you into Awesome
Type=Application
Exec=$HOME/.start-session.sh awesome
TryExec=/usr/bin/awesome
```

事实上，在启动完 GDM 还没进入 WM 之前，`Ctrl+Alt+F1` 切换到命令行下面，查看进程会发现

```
root       637     1  0 08:44 ?        00:00:00 /usr/lib/polkit-1/polkitd --no-debug
root      1072     1  0 08:44 ?        00:00:00 /usr/sbin/console-kit-daemon --no-daemon
rtkit     1260     1  0 08:45 ?        00:00:00 /usr/lib/rtkit-daemon
```

果不其然，PolicyKit 和 ConsoleKit 已经在运行了。

实测 Awesome / Xmonad 已经可以正常授权 NetworkManager 来编辑无线了。
