

早在去年时候，我就发现有个叫做 [Raspberry Pi][] 的玩意，
已经忘了是从那里得知这个东西。这个卡片大小的电路板是可以运行
Debian 的主机，提供了一个发挥自己想象的平台。13 年 [南京极客行动][]
时候，Michael 好像还拿了一个板子参加比赛。

![RaspberryPi.jpg](https://e25ba8-log4d-c.dijingchao.com/upload_dropbox/201407/RaspberryPi.jpg)

我对这个东西充满了兴趣，仅售 $39 的主机，小巧的机身，
可以充分发挥自己的想象力：离线下载，动作片播放器，家庭分享中心，
给侄子学习编程~想到这些可以发挥自己的创造力，
就迫不及待的要去采购并去尝试。

不过我还是理智的压抑住自己的情感，手头老是有更重要的事情要去做，实在不能再给自己多找一个精力分散的方向。
于是，我这么一压抑，就压抑了一年。

后来在 InnoSpae 看到 [SegmentFault][] 的姜尚用 [Arduino][]
写了一个播放超级玛丽音乐的程序，又让我重新燃烧起使用硬件创造一些小玩意的热情。

![4f42dcf03f067e12fe5c156e2af1373b.image.538x354.jpg](https://e25ba8-log4d-c.dijingchao.com/upload_dropbox/201407/4f42dcf03f067e12fe5c156e2af1373b.image.538x354.jpg)

碰巧的是，现在有一个非常适合的场景需要这样的工具：前段时间，团队在优化发布流程，也就是将工程师写好的代码发布到正式环境的过程。其中有一个重要环节是需要需求方对提出的功能进行验证。而需求方往往验证的不及时，就需要一个方法来通知需求方。使用 QQ 群效果不好，喊又太累，就想了一个歪主意，在办公室播放音乐。

简而言之，就是用 Raspberry Pi 播放音乐。几个方案确定之后，发现用 AirPlay 的方式最适合我们：每个人都有控制内容的权利；方案使用方便，一个苹果手机即可；内容来源多，豆瓣、网易、虾米都可以播放。

分分钟搞定这个方案，一个需要 5 个步骤。

1. 从淘宝买 RaspBerry Pi、无线网卡、SD 卡。
1. 从 [Raspberry Pi Download][] 搞一个 Raspbian，然后 `dd` 到 SD 卡，看官方文档操作，很详细（Mac 需要考虑使用高速写入 `/dev/rdisk1`）
1. SSH 登录到 `pi@192.168.1.x`，`git clone https://github.com/juhovh/shairplay.git` 然后阅读 [Shairplay][] 文档安装
1. 运行 Shairplay `shairplay -a 3DAir`
1. 在 **同一个** 局域网连着的手机播放音乐，从底向上拉 iPhone 菜单，就会发现多了一个 AirPlay 标记「3DAir」，点击即可播放。

上图：

![2014-07-15 19.43.16.jpg](https://e25ba8-log4d-c.dijingchao.com/upload_dropbox/201407/2014-07-15%2019.43.16.jpg)

![2014-07-16 19.25.33.png](https://e25ba8-log4d-c.dijingchao.com/upload_dropbox/201407/2014-07-16%2019.25.33.png)

哈哈，以后办公室开 Party，周末关怀，生日会什么的，再不不用担心放音乐问题了~

[Raspberry Pi]: http://www.raspberrypi.org/

[SegmentFault]: http://segmentfault.com/
[南京极客行动]: http://geekon.geekstack.org/
[Arduino]: http://www.arduino.cc/
[Raspberry Pi Download]: http://www.raspberrypi.org/downloads/
[Shairplay]: https://github.com/juhovh/shairplay

