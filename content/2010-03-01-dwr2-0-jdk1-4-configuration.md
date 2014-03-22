Title: DWR2.0在JDK1.4下的配置
Author: alswl
Slug: dwr2-0-jdk1-4-configuration
Date: 2010-03-01 00:00:00
Tags: DWR, Weblogic
Category: Java

服务器的WebLogic版本是8.1，使用自带的JDK1.4

MyEclipse版本是6.6，项目文件的**Compiler compliance level**设置为1.4

MyEclipse自带Tomcat使用MyEclipse6.6自带的JDK5

开发时候系统运行无误。

部署到应用服务器之后，使用WebLogic自带的JDK1.4，登录之后的一些页面一旦访问，会导致服务器报错停止。我检查了一下错误信息。

> "ListenThread.Default" listening on port 7001, ip address *.*>

- DWR Version 2.0.5 starting.  
- - Servlet Engine: WebLogic XMLX Module 8.1 SP1 Fri Jun 20 23:06:40 PDT 2003 27  
1009 with

- - Java Version:&nbsp_place_holder;&nbsp_place_holder; 1.4.1_03  
- - Java Vendor:&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; Sun Microsystems Inc.  
- Line=19 The content of element type "dwr" must match "(init?,allow?,signatures  
?)".

  
Unexpected Signal : EXCEPTION_ACCESS_VIOLATION occurred at PC=0x6D3F8887

Function=JVM_RegisterPerfMethods+0x11C42

Library=C:beaJDK141~1jrebinclientjvm.dll

  
Current Java thread:

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&n
bsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; at
java.lang.Class.getName(Native Method)

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&n
bsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; at
org.apache.commons.logging.impl.LogFactoryImpl.getInstance(LogFactory

Impl.java:246)

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&n
bsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; at
org.apache.commons.logging.LogFactory.getLog(LogFactory.java:395)

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&n
bsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; at
org.directwebremoting.util.CommonsLoggingOutput.<init>(CommonsLogging

Output.java:35)

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&n
bsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; at
org.directwebremoting.util.Logger.<init>(Logger.java:62)

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&n
bsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; at
org.directwebremoting.util.Logger.getLogger(Logger.java:33)

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&n
bsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; at
org.directwebremoting.annotations.AnnotationsConfigurator.<clinit>(An

notationsConfigurator.java:335)

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&n
bsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; at
sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)

可以发现，错误是运行到DWR这里发生了报错，好，那么我们从这里下手。

狗狗之后，得知DWR 2.0需要的JDK是1.5+，如果使用JDK1.4则要换成DWR1.x。不过，随后我看到两篇文章提供了两种解决方案。

[在JDK1.4中正确使用 DWR AJAX框架_永无止境_百度空间](http://hi.baidu.com/mcjyellow/blog/item/7b
654d544dd0025ed109068f.html)中配置web.xml来添加一个init-param，我测试之后发现对我无效，原因会在下面贴出。

随后我在[DWR的BUG - 一点凉月的日志 - 网易博客](http://71322560.blog.163.com/blog/static/567209
75200919102327784/)看到标题为**在JDK1.4中运行和部署DWR2和hibernate3出现的问题**的文字，提供了删除annotati
ons的方法，经过我测试，的确有效，方法如下。（友情提醒，操作之前请记得备份哦）

> 在DWR2.0中提供了一些JDK5中才能使用的annotations的功能。然而，这个
功能在JDK1.4的环境中进行启动或者部署会发生错误。抱歉的是这个错误信息我没有及时记录，日后补上。这个错误在网上可以轻易地搜索到解决方案，即在
dwr.jar中删除掉org.directwebremoting.annotations.AnnotationsConfigurator这个类再
重新部署就可以了。

>

> 同样的问题出现在hibernate3中，hibernate3对annotations的 支持在JDK1.4中也可能出现异常
，解决的办法就是在部署文件中删除掉hibernate-annotations.jar就可以了。

>

> 另外值得说明的是，以上2个问题并不是每次都会出现的。它们就如同幽灵一样有时出现有时不出
现，因此我们并不需要总是删除这个类和jar包，只是在发生错误时才删除。

&nbsp_place_holder;按照上述所说操作，在加载DWR时候，服务器会提示**AnnotationsConfigurator is
missing. Are you running from within an IDE?**但是已经可以正常运行了。

为什么第一个无效，因为这个错误引起的原因是JDK5中才能使用的annotations的功能，就算在web.xml配置了java.lang.Object的cl
ass，依然没有办法找到annotations，错误依然会存在。

有朋友问怎么删除一个.jar的类，呵呵，其实直接用7-Zip或者WinRAR此类的工具打开jar文件，进去删除即可，jar文件本质上其实就是一个带Meta-
INF的zip压缩包。

