Title: Struts2的编码问题
Author: alswl
Date: 2009-05-08 00:00:00
Tags: Struts, 编码
Category: Java编程和Java企业应用
Summary: 

继续昨天的编码问题 我一直全部采用UTF-8格式，而且在jUnit测试中并没有问题，说明是在Struts进行数据收集时候出错。

Google之后，根据网上一些建议修改web.xml struts.xml 但都没有效果。

网上建议在web.xml中添加 ：

    
    
    <filter>
    	<filter-name>struts-cleanup</filter-name>
    	<filter-class>org.apache.struts2.dispatcher.ActionContextCleanUp
    	</filter-class>
    </filter>
    <filter-mapping>
    	<filter-name>struts-cleanup</filter-name>
    	<url-pattern>/*</url-pattern>
    </filter-mapping>

来设定本地化和编码，然后在struts.xml中添加过滤器

    
    
    <constant value="UTF-8" name="struts.i18n.encoding"></constant>
    <constant value="UTF-8" name="struts.locale"></constant>

根据我测试，都没有效果。

我检查完JSP页面编码和本地文件编码，也都不存在问题。
最后我在一片帖子中看到讲WebWork2和Struts2的一些过滤器不一样，那位高手遇到和我几乎一样的问题，然后他使用另外一个Filter ：

    
    
    <filter>
    	<filter-name>struts2</filter-name>
    	<filter-class>org.apache.struts2.dispatcher.FilterDispatcher
    	</filter-class>
    </filter>

在Struts2中War文件解压出来的.xml中使用的是
org.apache.struts2.dispatcher.ng.filter.StrutsPrepareAndExecuteFilter
我并不清楚两者的区别，但是在采用 org.apache.struts2.dispatcher.FilterDispatcher 之后，问题迎刃而解。
然后查看手头的Struts2书，上面也是用的org.apache.struts2.dispatcher.FilterDispatcher
嗯，自己水平实在太菜，继续努力。

-技术改变世界，创新驱动中国-

