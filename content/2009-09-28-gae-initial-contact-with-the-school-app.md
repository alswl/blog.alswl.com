Title: GAE+校内App初接触
Author: alswl
Slug: gae-initial-contact-with-the-school-app
Date: 2009-09-28 00:00:00
Tags: Python, GAE, Google, 人人
Category: Coding

下午刚有了在Google App Engine上写校内（人人网）App的想法，下午就迫不及待的开始动手。下面我以一个简单的Hello
World来介绍一个开发步骤。

## 1.创建GAE应用

建立一个Google App Engine空间，需要一个Google帐号，仅此而已。拥有帐号，进入 ![App
Engine](https://www.google.com/accounts/ah/ah20x20.gif) [App
Engine](http://code.google.com/appengine/) ，激活这个服务，就可以[创建新的应用](https://appengi
ne.google.com/)。如何创建不是我这里要讲的重点，现在GAE支持简体中文版本，应该没有任何问题。

![image](http://upload-log4d.qiniudn.com/2009/09/image3.png) 一个简单的App控制台

## 2.部署GAE App

刚才建立的GAE App其实还是空的，如果访问xxx.appspot.com时候，你会发现什么都出不来（按理应该是404页面，但是由于连404页面都没有设置
，所以Nothing,检查http状态会发现返回的是404状态）。

这时候我们就要开始部署这个GAE App了：1.下载一个[Google App Engine SDK for Python-Win](http://goog
leappengine.googlecode.com/files/GoogleAppEngine_1.2.5.msi)，这样就可以在本地测试项目，然后发布到
GAE。

用这个GAE Launcher在本地创建了一个Application，注意标识符和你网上申请的要一致。然后会自动生成一个包含"」Hello
Word!「的main.py和app.yaml的文件夹。其中app.yaml的内容是用来配置项目的。

相关链接：[app.yaml的具体设置](http://code.google.com/intl/zh-
CN/appengine/docs/python/config/appconfig.html)

![xnapp_gae_launcher](http://upload-
log4d.qiniudn.com/2009/09/xnapp_gae_launcher2.jpg)
我创建了一个名为jasontidemo的App，并且启动服务器，可以进行浏览。

在一切没有问题之后，我们就可以惦记Deploy部署这个项目了，这时候要输入帐号和密码，然后出现console控制台等待信息。出现下面提示时候，就说明上传成功
了。

    
    Closing update: new version is ready to start serving.
    Uploading index definitions.
    Password for alswlwangzi@gmail.com: 2009-09-27 16:00:36 (Process exited with code 0)

这时候我们就可以打开xxx.appspot.com查看刚才部署的网站。

## 3.校内应用

拥有校内帐号，就可以创建校内应用。第一步是需要安装一个名为「[开发者](http://app.renren.com/developers/home.do)」
的应用。通过这个应用，可以链接到其他一些有帮助的内容：[开放平台文档](http://wiki.dev.renren.com/wiki/)、[测试工具](h
ttp://dev.renren.com/center/tools.do)、[讨论区](http://group.renren.com/GetTribe.d
o?id=237768885)。

第二步是创建一个新的应用，按部就班的填上相关资料。

[![image](http://upload-log4d.qiniudn.com/2009/09/image5.png)](http://upload-
log4d.qiniudn.com/2009/09/image51.png)

校内开发者，右上角可以申请开发应用（看讨论区貌似童鞋们都不满意这个开发平台呢）

[![xnapp_main](http://upload-log4d.qiniudn.com/2009/09/xnapp_main.jpg)](http
://upload-log4d.qiniudn.com/2009/09/xnapp_main2.jpg)

我的应用程序，在这里可以编辑应用的属性

创建之后，就可以填上Canvas的基本选项中的「应用展示地址」和「Canvas Callback
URL」，后者就是实际的地址，我们将填上刚才的xxx.appspot.com这种形式的网址。

[![xnapp_config](http://upload-
log4d.qiniudn.com/2009/09/xnapp_config.jpg)](http://upload-
log4d.qiniudn.com/2009/09/xnapp_config2.jpg)

最后测试自己的应用，也就是刚才「应用展示地址」，形式类似于apps.renren.com/xxx/，就可以看到我们的应用了，这时候基本框架就差不多了。

## 4.噩耗

此时当满天欢喜时候打开刚才的「应用展示地址」，你会惊奇的发现校内居然报错了，直接报了405错误。什么是405错误，就是服务器没有权限访问。

我花了一下午时间才解决这个问题，因为问题可能出在校内，也可能是GAE的功能限制上。

在appspot上测试这个应用是没有任何问题的

[![xnapp_show_ori](http://upload-
log4d.qiniudn.com/2009/09/xnapp_show_ori.jpg)](http://upload-
log4d.qiniudn.com/2009/09/xnapp_show_ori1.jpg)

显示的源码，其中的xnml校内服务器自己可以解析出来的，这段代码在校内测试工具也能通过

调试之后，终于把问题锁定在get
和post上，具体原因是因为校内发起请求GAE服务器用的是Post方法，而我们的main.py中目前只相应get方法，导致了校内请求GAE
Post方法，服务器没有这个方法调用，就返回了405错误。

修复这个问题只给main.py的MainHandler这个类加上post方法

    
    class MainHandler(webapp.RequestHandler):

def head(self, *args):

return self.get(*args)

def post(self):

self.response.out.write'Hello world!')

## 5.结合

最后我加上一个简单的<xn:profile-pic />来展示一下整个App

下面我发布我的这个简单的Hello World!（其实因为要使用XNML，所以已经不是单纯的打出Hello World了）

app.yaml：定义了main.py和404页面

    
    application: jasontidemo
    version: 1
    runtime: python
    api_version: 1

handlers:

- url: /  
script: main.py

- url: /index.html  
script: main.py

- url: /.*  
script: not_found.py main.py：我把post 和get写的比较Dirty，其实可以封装在一个函数里的。

    
    import wsgiref.handlers
    from google.appengine.ext import webapp

class MainHandler(webapp.RequestHandler):

def head(self, *args):

return self.get(*args)

def post(self):

self.response.out.write('''<b>使用者的名称及其大中小三种头像：</b>

<div style="text-align: center;">

图片：

<xn:profile-pic uid="loggedinuser" linked="true" size="tiny"/>

<xn:profile-pic uid="loggedinuser" linked="true" size="normal"/>

<xn:profile-pic uid="loggedinuser" linked="true" size="main"/>

<br />

姓名：

<xn:name uid="loggedinuser" linked="true" shownetwork="true" />

</div>''')

def get(self):

self.response.out.write('''<b>使用者的名称及其大中小三种头像：</b>

<div style="text-align: center;">

图片：

<xn:profile-pic uid="loggedinuser" linked="true" size="tiny"/>

<xn:profile-pic uid="loggedinuser" linked="true" size="normal"/>

<xn:profile-pic uid="loggedinuser" linked="true" size="main"/>

<br />

姓名：

<xn:name uid="loggedinuser" linked="true" shownetwork="true" />

</div>''')

def main():

application = webapp.WSGIApplication([('/.*', MainHandler)], debug=True)

wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':

main() not_found.py：自定义的404页面，其实就是简单的在MainHandler里面的get加入简单的文本。

    
      def get(self):
        self.response.out.write('404 Not Found')

把这个GAE App部署，然后就可以在校内的apps.renren.com/xxx/使用这个应用了。

[![xnapp_show](http://upload-log4d.qiniudn.com/2009/09/xnapp_show.jpg)](http
://upload-log4d.qiniudn.com/2009/09/xnapp_show1.jpg)

我的头像，按理应该有三个，我怀疑是校内的一个服务器出问题了，只刷出来两张。

[![xnapp_sidebar](http://upload-
log4d.qiniudn.com/2009/09/xnapp_sidebar.jpg)](http://upload-
log4d.qiniudn.com/2009/09/xnapp_sidebar1.jpg)

可以收藏这个应用，看到侧边栏的海绵宝宝了么？呵呵

