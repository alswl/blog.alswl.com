Title: dbevent2gc v0.1发布
Author: alswl
Slug: dbevent2gc-v0-1-released
Date: 2011-11-25 00:00:00
Tags: Python编程, coffee-time-project, dbevent2gc, GAE, github, iCalendar, Mako, OpenSource, web.py
Category: Coding

重要通知：Log4D的域名由 [http://dddspace.com](http://dddspace.com) 迁移到
[http://log4d.com](http://log4d.com) 。

订阅地址现在改为 [http://log4d.com/feed](http://log4d.com/feed) 和
[http://feeds.feedburner.com/dddspace](http://feeds.feedburner.com/dddspace)
。（FeedBurner的地址未发生变化）

<strike>http://feed.dddspace.com</strike> 弃用

请订阅我博客的朋友更新一下订阅地址。

![dbevent2gc](http://upload-log4d.qiniudn.com/2011/11/dbevent2gc.png)

## 关于dbevent2gc

A application to sync douban.com events to Google Calendar.

dbevent2gc是一个GAE应用，它将豆瓣同城的活动同步到Google Calendar的日历， 允许用户订阅活动而知道最近几周周边将发生活动。

dbevent2gc是基于Python/web.py/mako/iCalendar的，源代码地址在
[https://github.com/alswl/dbevent2gc](https://github.com/alswl/dbevent2gc)

## 使用方法

目前dbevent2gc运行在GAE上面，地址是 http://dbevent2gc.appspot.com （墙外）
[http://dbevent2gc.log4d.com/](http://dbevent2gc.log4d.com/) （我做的本地反向代理）
登录这个地址可以选择需要订阅的城市和活动类型，然后会生成一个按钮， 点击这个按钮可以直接将选择的活动订阅到Google日历。

如果你无法翻墙，可以使用 [http://dbevent2gc.appspot.com/event/location/beijing?type=all](h
ttp://dbevent2gc.appspot.com/event/location/beijing?type=all) 这样的地址添加到你的Google
Calender里面。

接受的参数：

  * 城市（把最后的beijing替换成你想要的城市拼音， 更多城市拼音查看[这里](http://www.douban.com/location/world/?others=true)
  * 活动类型 type，支持all, commonweal, drama, exhibition, film, music, others, party, salon, sports, travel. 可选参数,默认为all

## 安装方法

如果想自己搭建GAE应用，也很简单，直接使用 `git://github.com/alswl/dbevent2gc.git` 就可以获取最新代码，
然后嘛去GAE注册一个应用，上传即可运行了。

dbevent2gc看上去可以用了，我昨晚发布了v0.1版本。

感兴趣的同学可以试试，现在的问题是获取的活动可能太多了，<strike>我后期会加上过滤功能</strike>（update
2011-11-26，我已经添加了活动类型选择功能）。

