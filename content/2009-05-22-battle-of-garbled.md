Title: 乱码之战
Author: alswl
Slug: battle-of-garbled
Date: 2009-05-22 00:00:00
Tags: Struts, 编码, 贴吧
Category: Java

今天重新设计了贴吧的数据库，参考了WordPress的无外键，设置default的值，我取消了两个外键，仅保留一个对应CategoryId的外键。

修改数据库时候发现MySQL的charset还是'latin'，就顺手修改成'utf-8'来保证统一，结果就出事了。

因为我修改了DAO，单元测试之后重新走一遍网页测试流程，结果发帖时候遇到乱码。

一回生两回熟，咱也不怕。

在Action里面设置logger，输出相应的数据，发现那里就是乱码，说明在Severlet或者Interceptor那里就出了问题。

仿照上次设置Tomcat字符集，详情见[Eclipse中开发的Jave EE项目在Tomcat的部署
](../2009/05/12238.html)，但是测试发现没有效果。

接着查看web.xml，发现里面还有Spring的filter，贴吧现阶段还没有加入Spring，删除，有一个编码过滤器org.apache.struts2
.dispatcher.FilterDispatcher，采用org.apache.struts2.dispatcher.FilterDispatcher可
以不适用，删除。

这么一删，就发现乱码问题解决了。

呵呵，只要人类还有很多语言，乱码仍然会存在，遇到了不要怕，慢慢调试就出来了

