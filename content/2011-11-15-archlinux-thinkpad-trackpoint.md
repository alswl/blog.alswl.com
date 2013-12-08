Title: Arch Linux下小红点中键
Author: alswl
Slug: archlinux-thinkpad-trackpoint
Date: 2011-11-15 00:00:00
Tags: arch, ThinkPad
Category: Linuxer

重要通知：Log4D的域名由 [http://dddspace.com](http://dddspace.com) 迁移到
[http://log4d.com](http://log4d.com) 。 订阅地址现在改为
[http://log4d.com/feed](http://log4d.com/feed) 和
[http://feeds.feedburner.com/dddspace](http://feeds.feedburner.com/dddspace)
。（FeedBurner的地址未发生变化） 请订阅我博客的朋友更新一下订阅地址。

## 关于Arch

Arch是一款优秀的Linux发行版，使用它可以快速的学习Linux操作技巧。 Arch崇尚的原则是"保持简单，且一目了然"，这也是我崇尚的风格。

保持简单的同时也会给我带来一些小小的困扰，比如配置一下Thinkpad上面的小红帽
中键都需要设定Xorg。Arch直接向我们展示了Linux美妙的侗体，没有任何遮掩。

好在Arch有最完善的[官方Wiki](https://wiki.archlinux.org/index.php/Main_Page)，
Thinkpad爱好者也组建了一个专门的
[ThinkWiki](http://www.thinkwiki.org/wiki/ThinkWiki)来为大家答疑解惑。
特别是官方Wiki，中文化做的非常好，是我见过最完善的中文linux wiki之一。

## 小红帽的中键

罗嗦完了，进入正题，我的环境是

  * arch(Linux version 3.1.0-4-ARCH)
  * Gnome3.2.1
  * X.Org X Server 1.11.2

根据 [How to configure the
TrackPoint](http://www.thinkwiki.org/wiki/How_to_configure_the_TrackPoint)
描述，配置小红帽的中键有6种办法， 我使用的是xinput配置（这是推荐方法）。

运行下列代码，即可启用小红帽中键上下滑动。

    
    xinput set-int-prop 12 "Evdev Wheel Emulation" 8 1
    xinput set-int-prop 12 "Evdev Wheel Emulation Button" 8 2
    xinput set-int-prop 12 "Evdev Wheel Emulation Timeout" 8 200

现在运行下面代码，启用左右滑动。

    
    xinput set-int-prop 12 "Evdev Wheel Emulation Axes" 8 6 7 4 5

创建自动脚本，在系统启动时候自动执行

    
    #!/bin/sh
    xinput list | sed -ne 's/^[^ ][^V].*id=\([0-9]*\).*/\1/p' | while read id
    do
            case `xinput list-props $id` in
            *"Middle Button Emulation"*)
                    xinput set-int-prop $id "Evdev Wheel Emulation" 8 1
                    xinput set-int-prop $id "Evdev Wheel Emulation Button" 8 2
                    xinput set-int-prop $id "Evdev Wheel Emulation Timeout" 8 200
                    xinput set-int-prop $id "Evdev Wheel Emulation Axes" 8 6 7 4 5
                    xinput set-int-prop $id "Evdev Middle Button Emulation" 8 0
                    ;;
            esac
    done

# disable middle button

xmodmap -e "pointer = 1 9 3 4 5 6 7 8 2"

我将这个bash放在 `~/.xinitrc` 里面执行。

PS：如果你使用这个方法有问题，建议检查一下当前环境。另外可以参考一下其他的设置方法 [How to configure the
TrackPoint](http://www.thinkwiki.org/wiki/How_to_configure_the_TrackPoint) 。

