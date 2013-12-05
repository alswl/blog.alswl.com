Title: 使用MoinMoin作为个人KMS
Author: alswl
Date: 2011-12-26 00:00:00
Tags: image2attach, KMS, MoinMoin, nginx, uwsgi, wiz
Category: Linuxer, Python编程, 工欲善其事必先利其器
Summary: 

去年9月份时候，我写过一篇《[我所使用的知识管理系统](http://log4d.com/2010/09/my-kms)》
来介绍我使用的KMS系统。当时经过我层层筛选之后，我选用了Wiz作为我的KMS。

一年多过去了，Wiz在Windows下面工作的非常不错，Wiz团队里陆续推出了iOS / Android /
[Web](http://service.wiz.cn/web/)版本。我的Wiz收藏的内容也增加到近1000篇。

此时我遇到了KMS再选型的问题，原因很简单：我全线转换到Linux平台， Wiz不符合我的要求了。

我重新整理一下我要求KMS的特性：

  * 跨平台：Linux / Web / iOS / Android / Windows
  * 数据保存格式：移植方便，将图片保存到本地
  * 数据采集方式：支持网络直接拷贝复制
  * 数据索引：支持分类 + tag
  * 协同工作：方便的分享机制
  * 免费

经过我历时N月的搜寻筛选，MoinMoin Wiki中标了！

## 1. 关于MoinMoin

MoinMoin是使用Python编写的Wiki实现，MoinMoin当前版本1.9。

MoinMoin的优点是：

  * 安装简单;
  * 支持中文全文检索；
  * 汉化较好；
  * 不依赖外界的数据库, 使用纯文本保存, 备份非常容易, 直接复制即可。
  * 支持从html转换到MoinMoin Wiki格式，纯文本的wiki格式比html来的更纯粹，只保存需要的数据，而不保存冗余的样式，MoinMoin这点做的非常好，支持几乎全部html标记的转换。

## 2. 安装MoinMoin

MoinMoin基于Python，因此安装比基于php的MediaWiki麻烦一点。

你也可以参考[官方安装指导（英文）](http://moinmo.in/HowTo)，里面有 Ubuntu / CentOS / SuSE
等系统的安装方法。

### 2.1. 使用MoinMoin桌面版（最简单）

好在有MoinMoin下载包里面包含了简单的可执行版本，只需3个步骤就可以运行了。

  1. 下载MoinMoin [http://moinmo.in/MoinMoinDownload](http://moinmo.in/MoinMoinDownload)
  2. 解压缩到合适的目录（安装目录）
  3. 运行目录下面的 `wikiserver.py`
    1. Linux/Unix：在命令行里面运行 `wikiserver.py`
    2. Mac：在 `wikiserver.py` 上面点击右键，选择 `open with...` - `All Applications` - `Always Open With` - `Terminal.app`
    3. Windows：下载 [Python](http://www.python.org/download/) （2.5-2.6）， 安装之后双击 `wikiserver.py` 运行。

安装好之后，打开浏览器，在地址栏输入 [http://localhost:8080/](http://localhost:8080/) 即可访问。

PS：如果你将MoinMoin安装的优盘，甚至可以做成移动知识库哦~

更多可以参考 [官方DesktopEdition帮助文档（英文）](http://moinmo.in/DesktopEdition)

### 2.2. nginx+uWsgi方式（程序员适用）

`wikiserver.py` 虽然可以运行，但是作为开发者，我当然要使用效率更高的方式。 运行Python Web应用需要 `Appach / ngnix
+ CGI / FastCGI / uWSGI` 环境。 我这里使用nginx + uWSGI进行环境配置。

Google了N多资料之后，这篇 [ArchLinux 下使用 Nginx + uWSGI 部署
MoinMoin](http://typedef.me/2011/08/30/archlinux-nginx-uwsgi-moinmoin-setup)
最是详细，另外还可以参考 [运行在 nginx 与 uwsgi 之上的 moinmoin](http://garfileo.is-
programmer.com/2011/4/24/run-moinmoin-on-uwsgi-and-nginx.26347.html)。

我将主要步骤和我的一些修改列出来。

#### 2.2.1. 安装需要软件

我当前系统是Arch，运行一下命令安装，其他系统也类似

    
    pacman -S nginx moinmoin
    yaourt uwsgi

#### 2.2.2. 配置MoinMoin

默认情况下，moinmoin 被安装在了 `/usr/lib/python2.7/site-packages/MoinMoin` 和
`/usr/moin/share` 这两个目录下。

    
    cd /usr/share/moin/
    ln -s /usr/share/moin/server/moin.wsgi .
    ln -s /usr/share/moin/config/wikiconfig.py .

#### 2.2.3. 配置nginx

在上文的基础上，我做了一些小修改，我的nginx站点配置如下，我没有使用端口9090 作为uwsgi的监听端口，而是使用了UNIX
Sock，这样相对安全一些。

ps：貌似这个版本的uwsgi 0.9.9.2有点小问题，无法在 `/var/run` 里面创建sock， 我只能将 `uwsgi.sock` 放在
`/tmp` 里面

    
    server {
            listen       80;
            server_name  wiki.localhost;
            location /{
                    include uwsgi_params;
                    #uwsgi_pass 127.0.0.1:9090;
                    uwsgi_pass unix:/tmp/uwsgi.sock;
                    uwsgi_param UWSGI_PYHOME /usr/lib/python2.7/site-packages/MoinMoin;
                    uwsgi_param UWSGI_CHDIR /usr/share/moin;
                    uwsgi_param UWSGI_SCRIPT moin_wsgi;
            }
    }

# vim: set ft=conf:

#### 2.2.4. 配置启动文件

因为使用 UNIX Sock 连接，所以 `/etc/rc.d/uwsgi` 启动文件也略做修改（ Ubunt 的启动配置文件在
`/etc/init.d/` 下面）， 加入了 `SOCK` ，同时我为 uwsgi 指定运行用户 `http` ，避免root启动带来的安全隐患。

    
    #!/bin/bash

#PORT=9090

SOCK=/tmp/uwsgi.sock

PROCESSES=4

USER=http

LOG=/var/log/uwsgi.log

PID=`pidof -o %PPID /usr/bin/uwsgi`

. /etc/rc.conf

. /etc/rc.d/functions

case "$1" in

start)

stat_busy "Starting uwsgi"

if [ -n "$PID" ]; then

stat_busy "uwsgi is already running"

stat_die

else

#uwsgi --uid $USER -s ":$PORT" -M -p $PROCESSES -d $LOG &> /dev/null # use
socket port

uwsgi --uid $USER --socket $SOCK -M -p $PROCESSES -d $LOG &> /dev/null # use
unix sock

add_daemon uwsgi

stat_done

fi

;;

stop)

stat_busy "Stopping uwsgi"

killall -QUIT uwsgi &> /dev/null

rm_daemon uwsgi

stat_done

;;

restart)

$0 stop

sleep 1

$0 start

;;

*)  
echo "usage: $0 {start|stop|restart}"

esac

exit 0

## 3. Image2Attach

去年我选择Wiz而不选择Wiki类产品时候，是考虑到一个图片保存本地化的问题。 即保存一篇网页时候，要将里面的图片保存到本地，而不是使用链接方式保存，
因为由于各种不可预测的原因，原始图片数据很有可能丢失或者无法连接。

Wiz使用的方案是使用mht格式将图片保存在问题，而大部分 Wiki，包括 MoinMoin 都以 文本的形式保存数据，那就无法保存远程图片了。

经我研究，MoinMoin 中有附件的方法可以保存文件，并且当这种附件存放的是图片文件时， 也可以直接使用 `{{attachment:xxx.jpg}}`
这样的 Wiki 语法来查看图片。

我尝试在 MoinMoin 插件库里面找将远程图片本地化的插件未果，于是就花了一个星期左右 时间写了一个实现这样功能的插件 Image2Attach。

更多使用可以参考这篇文章 [MoinMoin plugin: image2attach v0.0.2
released](http://log4d.com/2011/12/moinmoin-plugin-image2attach)

所以说，当程序员就是好，功能没有就自己实现呗。

## 4. MoinMoin的简单上手

[@张刚](http://zhanggang.net/) 同学发邮件给我和我交流了两个问题，我顺便整理到这里。（2011-12-28更新）

### 安装语言包

  * 首先请确保当前登录账户是超级用户，超级用户设置在 `/usr/share/moin/wikiconfig.py` （可能路径有所差异）里面的 `superuser = [u"yourid"]` ，加入你需要设定的用户id
  * 中文界面会根据浏览器语言设定获取，而相应的中文帮助文件默认没有安装，我建议安装。安装步骤如下：  

    * 访问http://localhost/LanguageSetup，里面有安装文档链接http://localhost/LanguageSetup?action=language_setup
    * 在http://wiki.localhost/LanguageSetup?action=language_setup中，选择 `Simplified_Chinese` 点击最下面 `all_pages`
    * 同时我也建议安装英文版本的 `all_pages` ，因为中文有一些翻译不全。

更多的中文信息你可以访问[MoinMoin主版本中文网站](http://master.moinmo.in/%E9%A6%96%E9%A1%B5)。

### 如何加入内容

下面是我自己总结的步骤，目前工作的还不错。

  * 进入新页面http://localhost/newpage，如果不存在就会创建新页面
  * 默认是文本模式编辑器，切换到图形编辑模式（默认编辑器可以在个人设置里面修改）
  * 从某个网页粘帖内容到图形编辑模式（这个图形编辑器是CKEditor的精简版）。
  * 查看图形编辑器原始码，再返回"所见即所得"状态（这个步骤可以去除一些空格）
  * 返回文本模式编辑器，MoinMoin会自动转换html->wiki（目前我遇到3个bug，中文开头空格/BR换行/fieldset，前两个我已经修 复，diff文件在[http://upload-log4d.qiniudn.com/2011/12/moinmoin.diff](http://upload-log4d.qiniudn.com/2011/12/moinmoin.diff)）
  * 人工审核一下wiki，也顺便仔细看看文章内容
  * 加入Category，预览，保存

## 5. MoinMoin的一些修改

在使用MoinMoin这段时间，我发现了一些小问题，就对源码做了一些小修改。 当然如果你觉得麻烦，不做这些修改也一样可以使用的很好。

我修改了 `/usr/lib/python2.7/site-
packages/MoinMoin/converter/text_html_text_moin_wiki.py` 这个文件。点击 [diff文件](http
://upload-log4d.qiniudn.com/2011/12/moinmoin.diff)下载。

## 6. wiz转MoinMoin经验

Wiz中数据存储格式其实是mht，微软的鸟东西，数据转换颇为不方便。

第一种方法是借助Wiz Web服务，Wiz小组推出的 [Web服务](http://service.wiz.cn/web) 可以很方便的查看所有同步
过的内容，里面就是标准的html代码了，直接可以复制粘帖。Wiz的Web端图片也不用 Cookie认证，取到图片地址就可以抓取了。

另一种办法就是使用Wiz的导出功能，导出成mht格式， 然后使用MoinMoin站点提供的插件
[Word2Moin](http://moinmo.in/MicrosoftWordConverter) 脚本进行转换。

我使用的方法是第一种。

