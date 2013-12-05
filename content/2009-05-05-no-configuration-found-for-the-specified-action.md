Title: No configuration found for the specified action
Author: alswl
Date: 2009-05-05 00:00:00
Tags: Struts
Category: Java编程和Java企业应用
Summary: 

Tomcat 控制台打出如下警告：

WARN - No configuration found for the specified action: ‘xxxxx’in namespace:
‘/’. Form action defaulting to ‘action’ attribute’s literal value.

主要由于在写struts2表单时有给action指定全名，如:<s:form action=」xxxAction.do」…>,直接写成<s:form
action=」xxxAction」…>即可,因为在struts.xml中struts.action.extension属性有指定啦。

有一个关于在namespace上的设置在 [hi.baidu.com/mum0532/blog/item/128f9a64fa8594f5f6365457.
html](http://hi.baidu.com/mum0532/blog/item/128f9a64fa8594f5f6365457.html)
。这位朋友讲的很透彻很详细

关于Struts2 的 namespace 详细解释
[www.javaeye.com/topic/125743](http://www.javaeye.com/topic/125743)

