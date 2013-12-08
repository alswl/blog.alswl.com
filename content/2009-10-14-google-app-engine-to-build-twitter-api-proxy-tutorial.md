Title: Google App Engine搭建Twitter API Proxy教程
Author: alswl
Slug: google-app-engine-to-build-twitter-api-proxy-tutorial
Date: 2009-10-14 00:00:00
Tags: GAE, Twitter
Category: 关注互联网

来源：[Google App Engine搭建Twitter API
Proxy教程](http://www.williamlong.info/archives/1956.html)

alswl:今天我本来想使用[GAppProxy](http://gappproxy.googlecode.com/)搭建自己的[服务器](http://j
asontiproxy.appspot.com/fetch)，不过失败了，似乎客户端有些问题，也可能是我配置的问题。之后就正好看到月光大大的这篇文章，欣喜之
极，搭建了[自己的Twitter birdnest服务器](http://jasontitwitter.appspot.com/api/)，并转载之。

本文将介绍如何通过Google App Engine搭建基于Python
2.5的BirdNest环境，建好的BirdNest可以在TwitterFox或twhirl中使用。

### 环境准备：Google App Engine

先要[注册Google App Engine](http://www.williamlong.info/archives/1357.html)，注册地址
[http://appengine.google.com/](http://appengine.google.com/) ，然后建立一个applicatio
n，目前第一次使用需要验证用户手机，输入手机号码就收验证码即可，之后，就可以用yourid.appspot.com来访问你的app应用。

此外，还需要下载安装Google APP Engine的开发环境，注意Python的版本，需要是2.5系列的，不能使用2.6或更高的版本，否则运行会出错。

Google App Engine SDK 下载地址 [http://code.google.com/intl/zh-
CN/appengine/downloads.html](http://code.google.com/intl/zh-
CN/appengine/downloads.html)

Python 2.5.4 下载地址 [http://www.python.org/download/releases/2.5.4/](http://www.
python.org/download/releases/2.5.4/)

关于Google App Engine的详细使用说明请参见[这个地址](http://www.williamlong.info/archives/1880.
html)，这里我就不再累赘。

### 环境准备：BirdNest

下载birdnest要注意是下载[分支branches/gae](http://birdnest.googlecode.com/svn/branches/g
ae)，别下载主干trunk，否则更新到GAE上也不能用，会报错。可以使用一个SVN工具下载。例如[TortoiseSVN](http://www.will
iamlong.info/archives/1878.html)等。将其放到一个目录中，进入目录，编辑app.yaml文件，将第一行的application
里的参数修改为自己的应用名。（alswl:我使用Eclipse获取了SVN的内容）

### 发布应用到GAE

准备好了上面的一切后，就可以发布这个应用到自己的Appspot上了，执行 appcfg.py update
目录名，中间会要求输入Gmail的用户名和密码，之后就可以使用了。你创建的API地址应该是yourid.appspot.com/api/ 。

### 使用BirdNest

在twhirl里的使用方法是，打开账号管理Accounts manager，选择laconi.ca账户类型，输入：[你的twitter帐号名]@yourid
.appspot.com，密码为Twitter密码，即可使用。（alswl:我使用的是twhirl，需要安装Adobe AIR环境）

在twitterfox里的使用方法是，打开 C:Documents and SettingsAdministratorApplication
DataMozillaFirefoxProfiles 随机信息
.defaultextensionstwitternotifier@naan.netcomponents目录，编辑
nsTwitterFox.js文件，找不到的话直接在Documents and
Settings中搜索nsTwitterFox.js文件，编辑该文件的38行，将其修改为 var TWITTER_API_URL =
http://yourid.appspot.com/api/ 即可。

