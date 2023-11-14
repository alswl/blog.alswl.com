

贴吧1.0差不多可以完成了，进入界面美化，我服务器验证写完之后，开始用jQuery写js。

使用了jQuery的UI，后来想加入Ajax验证，但是遇到了问题：

09-05-23 07:53 WARN [org.apache.struts2.dispatcher.Dispatcher] - Could not
find action or result

There is no Action mapped for namespace / and action name AjaxLogin. -
[unknown location]

我整整找了一个多小时，曾以为是action name的问题或者是package name, package namespace
的问题，为此我特意重新学习了一下他们的使用方法，但是仍然没有效果。

最后，终于在Google找到了一些资料：

[struts2 json jquery 集成详解](http://huqilong.blog.51cto.com/53638/136802)来自
户起龙的博客

我本来以为Struts/lib下面的json-lib-2.1.jar就可以了，而且启动Tomcat没有任何报错，居然要另外一个jar，叫做json-
plugin

下载地址：[猛击这里下载](http://code.google.com/p/jsonplugin/downloads/list)

使用这个插件之后，本以为轻松搞定，但是仍然还是这个错误！！！

怎么可能？！我怒了，翻开Struts2的文档，文档用的是DWR，已经使用taglib封装了，再查看json-plugin的文档，仍然未果！！

最后逼急了，使用这篇文章 《在Struts 2中使用JSON Ajax支持》[猛击这里打开](http://webservices.ctocio.com.cn/tips/424/7670924.shtml)，重新写了一个Action和一个简单的jsp页面，使用最淳朴的<submit>提交。终于可以成功了，数据交
换能够明显的在FireBug下看到。

这种情况的话，据我猜测，应该是我原来使用的<s:form>标签的问题，如果使用简单的<form>就应该可以避免了。

09_05_24修正

之前说是<s:form>的问题，而用<form>可以解决，结果我发现<form>也不行，直接返回当前页面，这就比较郁闷了，最后，我把<form>去除，只留下
<input type="submit">就可以了，不好意思，让Strut2蒙冤了。


