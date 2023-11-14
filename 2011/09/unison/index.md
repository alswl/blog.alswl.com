

## 1. 同步控

我是一个同步控，会妄想自己的文件遭遇不可修复性的毁灭， 因此经常丧心病狂的做备份。 比如每每备份到移动硬盘中，
比如每年一次的刻盘备份，又比如我现在要介绍的同步软件unison。

据我自己考察，这种对备份文件丢失的恐惧来自于小时候一次意外格式化F盘， 从而导致我搜集的所有《龙珠》漫画丢失而产生的。

另一个同步文件的需求来自于我的两台电脑：常驻家中的DELL 6400，是我的大房； 最近得宠的小蜜Thinkpad X201。其中6400是Win7系统，
而X200是Arch Linux主打的双系统，我希望两者的文件保持同步， 便于我两边使用时候都能检索资料。如何实现跨平台同步方案让我头疼了好久，
幸好有unison拯救了我。

## 2. 同步历史

很久很久以前，那时候我还喝三鹿，我开始用TotalCmd来做同步文件， 依稀记得那个功能是在 `命令` 里面的 `比较文件夹` 。
这个功能满足我当时简单粗糙的需求。只要把需要同步的文件夹分列TotalCmd两侧， 然后就可以通过命令自动查找相异的文件。

当时在我看来，尤其神奇的是文件过滤功能和按照 `日期` 、 `文件内容` 比较功能。 着实帮了我很大忙。

再过了几年，TotalCmd不能满足我了，我不想每次都选择需要同步的文件， 再用肉眼比对，同步功能也偏少。我搜寻到一款老牌的同步工具，
叫做[GoodSync](http://www.goodsync.com/)，这是一款商业软件，可以试用30天，
作为专业的同步软件，这个GoodSync的确是蛮适用：支持大小写屏蔽、 文件过滤等等。

GoodSync还可以支持网络映射硬盘，再通过Samba等协议支持，可以实现跨平台同步。
可惜GoodSync要收费，而且通过网络映射的方式也不慎完美，所以最后也弃用了。

## 3. unison

终于轮到[unison](http://www.cis.upenn.edu/~bcpierce/unison/)闪亮登场了。
unison解决了跨平台同步，文件过滤，断点续接，大小写同步等等各种问题。

官方介绍：

> Unison is a file-synchronization tool for Unix and Windows. It allows two
replicas of a collection of files and directories to be stored on different
hosts (or different disks on the same host), modified separately, and then
brought up to date by propagating the changes in each replica to the other.

>

> 

> Unison是一枚Unix和Windows通吃的文件同步工具。它允许不同电脑上（或者同一电脑上不同地方）的文件和目录之间惊心修改和同步更新。

>

> 

unison使用时候有服务器、客户机之分，客户机通过ssh连接到服务器端， 所以相对而言，数据通道还是安全的。

## 4. 安装

    
    sudo pacman -S unison

感谢众神赐予我们各种软件包，以上是Arch Linux的安装命令。 Ubuntu之类的也差不多apt-get了。

## 5. 配置

unison的传输通道用ssh，所以必须在同步的电脑上面配置好ssh， 服务端需要配置好sshd，另外最好配置好ssh公钥密钥，可以参考
[使用DDNS+SSH连通家庭/工作电脑](http://log4d.com/2011/06/ddns-ssh)。

unison使用 `~/.unison/*.prf` 的配置文件，默认应该会有一个 `default.prf` ， 我的 `default.prf`
配置如下。

    
    # Unison preferences file
    #root = /cygdrive/f
    #root = ssh://mm061.log4d.com//home/alswl

log = true

logfile = /home/alswl/.unison/.unison.log

#batch = true

#auto = true

#ignorecase = true

ignore = Name {Thumbs.db}

ignore = Path {music/iTunes}

其中 `root` 表示同步的两个目录，ssh开头的服务器端路径。 `log` 设定log文件位置， `batch` 指自动同步而不经过确认， `auto`
是同步之后列出同步建议清单， 选择 `yes` or `no` 即可。 `ignorecase` 是忽略大小写，在跨平台同步时候蛮有用。 `ignore`
指忽略文件列表，分为 `Name` 和 `Path` 。

我的default配置并不是一个可用配置，只是一个基础配置文件，用来给其他配置文件使用

    
    # Unison preferences file
    include default

root = /home/alswl

root = ssh://mm061.log4d.com//home/alswl

path = music

我使用 `include` 选项来加入 `default` 配置，就可以使用通用配置了。

## 6. 运行

终于到了激动人心的时刻了，我们使用下面命令同步文件夹。

    
    unison music

其中 `music` 就是之前配置好的 `music.prf` 。Papapa之后，就是各种选项了。

unison默认情况下面会依次提醒每个差异文件的差别，可以使用键盘命令查看具体差异。 依次查看文件会很烦，所以我习惯性使用 `auto` 命令来自动合并。
`auto` 会根据文件的状态，最后更新日期来选择合适的同步操作。

完了，没了，谢谢。

哦，对了，当时写那篇 [使用DDNS+SSH连通家庭工作电脑](http://log4d.com/2011/06/ddns-ssh)
大部分原因就是因为这个同步需求。而且经过我3个月来的使用，unison真是个好工具。


