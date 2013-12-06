Title: 在Eclipse3.5下使用Flex Builder 3
Author: alswl
Slug: the-eclipse3-5-using-flex-builder-3
Date: 2009-11-18 00:00:00
Tags: AIR, Eclipse, Flex, Flex Builder
Category: 工欲善其事必先利其器
Summary: 

这次课程设计是我大学最后一次了，毕业设计会需要谨慎，所以这次课程设计我决定做一个新潮的系统。

我将系统命名为PylexChat，是一个基于**Python**+**Flex**的聊天系统，架构在**GAE**+**AIR**环境，支持多平台（**Wi
ndows+Linux+Web+手机**）客户端登录。开发IDE为**Eclipse**+**Flex Builder3**插件，我的**Eclipse
Gelileo**(v3.5)。在安装Flex Builder 3过程中就弹出需要3.4一下环境，我没在意，继续安装了。

安装之后出现了问题，Eclipse插件根本没有加载，我在[Getting Flex Builder 3 plugin to survive a new
Eclipse Version](http://greylurk.com/index.php/2009/06/getting-flex-builder-3
-plugin-to-survive-a-new-eclipse-version/)找到了相应解决方案。

在`Eclipselinks`目录下面建立`com.adobe.flexbuilder.feature.core.link`文件，编辑内容为`d:/Stud
y/Flex Builder 3 Plug-in`（记得修改目录），这样就可以正常加载并编写项目了。

在使用过程中，如果代码没有写好，会出现`An internal error occurred during: "Removing compiler
problem markers...".`这样的提示，此时无论我做如何动作，保存代码/清理项目/新建文件，都会出现如上错误，根本没法继续。经过我尝试，除了将
项目删除重新建立，没有其他的办法彻底解决这个问题。

这里有一个Adobe 官方论坛的讨论帖[http://forums.adobe.com/thread/90415](http://forums.adobe.
com/thread/90415)，似乎这个问题在当时Flex Builder 2就出现，现在出现在Eclpse 3.5 + Flex Builder
3下面。

看来得等Flex Builder3之后的版本发布才能修复这个Bug，否则的话，还是得换回Eclpse 3.4……

悲剧了，我刚使用Galileo一周时间……

