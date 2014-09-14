Title: 给MoinMoin写插件
Author: alswl
Slug: the-write-the-plugins-for-moinmoin
Date: 2012-02-10 00:00:00
Tags: Python, image2attach, MoinMoin
Category: Coding

## 1. 使用 MoinMoin

前些日子，我写了一篇[使用MoinMoin作为个人KMS](../2011/12/moinmoin-kms)
大赞MoinMoin的各种好处。MoinMoin的其中一个好处是基于GPL的开源，
我们可以方便的给MoinMoin撰写自己的插件（当然也可以去官方的wiki上获取大量现成插件）。

  * [MoinMoin开发者wiki地址](http://moinmo.in/MoinDev)
  * [MoinMoin开发API文档（这个官方wiki居然很少提及）](http://docs.moinmo.in/)
  * [MoinMoin的多国语翻译组wiki地址](http://moinmo.in/MoinDev/Translation)

我在使用MoinMoin过程中，有一个急迫需要的功能：

> 保存一篇网页时候，要将里面的图片保存到本地，而不是使用外链接方式保存， 因为由于各种不可预测的原因，原始图片数据很有可能丢失或者无法连接。

这个功能对于将Wiki产品转化为KMS应用非常需要，可惜MoinMoin官方并没有提供，
我也没在MoinMoin的开发者插件库中找到类似功能，就自己写了一个插件image2attach。

  * [MoinMoin插件库](http://moinmo.in/MoinMoinExtensions)
  * [image2attach在MoinMoin官方Wiki的地址](http://moinmo.in/ActionMarket/Image2Attach)

现在我分享一下如何写MoinMoin插件，技术大牛可以直接移步官方开发文档， 我这里只是写一些简单的内容，帮助像我一样的同学。

以下内容需要Python编程基础～

## 2. MoinMoin 系统结构

MoinMoin的UML图：

![MoinMoin](http://upload-log4d.qiniudn.com/2012/02/MoinMoinArchitecture.png)

## 3. MoinMoin 常用对象

### 3.1. request

这个request和普通jsp/asp中request很类似（实际上这个request就是继承
[werkzeug](http://werkzeug.pocoo.org/)的Request）。

除了正常的web request功能，Moin的request还带了Wiki自身的信息。

  * request.getText # 多国语函数，经常使用 `_ = request.getText` 来简化代码
  * request.dicts # 获取定义在页面中的Dict，参见http://moinmo.in/HelpOnDictionaries
  * request.groups # 获取权限管理中的组别
  * request.user.may # 检查用户权限

### 3.2. Page

Page是最常见的类，它代表某个Wiki页面，通过它可以获取某个页面所有信息。 age本身是只读的，如果需要编辑需要使用PageEditor。

  * Page.exists() # 是否存在
  * Page.getRevList() # 版本列表
  * Page.current_rev() # 当前版本
  * Page.getPagePath() # 存储路径
  * Page.get_raw_body() # 获取存储的数据
  * Page.send_page() # 发送格式化好页面

### 3.3. PageEditor

上面说到Page是只读的，那当我们需要编辑页面时候，就要用到PageEditor类了。

  * PageEditor.saveText() # 保存内容
  * PageEditor.deletePage() # 删除页面

### 3.4. AttachFile

顾名思义，AttachFile用来管理页面附件。

  * AttachFile.exists() # 检查附件是否存在
  * AttachFile.getAttachDir() # 获取附件存放的本地目录
  * AttachFile.getAttachUrl() # 获取附件url

### 3.5. wikiutil

wikiutil 是MoinMoin提供的一个帮助类，包含一些常用的小功能。

  * wikiutil.escape() # html转义
  * wikiutil.createTicket() # 生成一串唯一key，用来页面验证
  * wikiutil.checkTicket() # 检查ticket
  * wikiutil.invoke_extension_function() # 注入脚本类插件
  * wikiutil.version2timestamp() # 将MoinMoin时间转换成UNIX时间戳
  * wikiutil.timestamp2version() # 参考楼上
  * wikiutil.renderText() # 将wiki text转换成html来展现

### 3.6. user

用户类，CRUD操作，不解释。

### 3.7. formatter

formatter将输出展现类，将wiki text转换为各种预定义的格式。 需要和parser配合使用（两者关系看上去像抽象工厂模式）。

  * formatter.text() # 格式化为普通文本
  * formatter.img() # 格式化为图片
  * formatter.number_list() # 格式化为有序列表
  * formatter.bullet_list() # 格式化为无序列表
  * formatter.listitem() # 格式化为列表项

### 3.8. parser

formatter完成的工作是展现解析后的wiki内容，而负责解析的就是parser了。

流程是这样的：

    
    wiki -> parser -> formatter

每一个parser都对应一个或者多个formatter。系统内置的 parser/formatter 有：

  * docbook
  * html
  * plain
  * python
  * rst
  * cvs

## 4. MoinMoin 运行流程

  1. cgi.py
  2. 通过url获取pagename和action，然后调用对应的Page方法和Action对象  

    1. Page().send_page()创建普通页面
    2. MoinMoin.action.getHandler()用来获取对应action

## 5. MoinMoin 开发配置

### 5.1. 禁用pyc缓存

MoinMoin 为了提高系统效率，会为 python 文件生成pyc缓存，如果放任它们的话。
每次修改python源码效果都得不到立即体现。所以我们要在开发阶段禁用系统缓存。

在文件 `/usr/lib/python2.7/site-packages/MoinMoin/config/multiconfig.py`
的第815行左右，修改 `options_no_group_name` 中的 `cache` 时间。

当改为0时候，就不使用 `pyc` 缓存，这样就不用重启服务器来清楚缓存了。

    
    options_no_group_name = {
            # ...
            #'cache': (600, 30), # cache action is very cheap/efficient
            'cache': (0, 0), # cache action is very cheap/efficient #XXX alswl
            # ...
    }

## 6. image2attach 范例

image2attach这个插件功能很简单，就是读取wiki文本内容，找出所有图片，
然会将这些图片从互联网上下载到本地，并将文中的图片链接改为MoinMoin的附件链接。

### 6.1. 创建插件文件

在 `data/plugin/action/` 目录下创建文件Image2Attach.py。
（请使用大写文件，Moin会自动识别大写开头的Python文件为插件）

### 6.2. 基本框架

  1. `execute()` ：hook函数，用来给上层调用，签名必须是 `def execute(pagename, request)`
  2. `Class Image2Attach` ：主要类，处理逻辑。  

    1. `process() / process_line()` ：处理每行wiki text，会抓取<a>和<img>
    2. `process_transclude() / process_link()` ：分别处理<a> / <img>
    3. `fetch_image()` ：下载图片
    4. `add_attachment()` ：将图片作为附件加入到wiki
    5. `write_file()` ：写入wiki text

总的来说，开发Moin插件还是比较方便的，官方提供了详尽（但不够顺畅）的教程和
[API文档](http://docs.moinmo.in/moin/1.9/)。 我大部分时间在看Moin的API文档，
Moin作为一款久经考研的Wiki系统，开放的代码也有很多地方可以学习。

