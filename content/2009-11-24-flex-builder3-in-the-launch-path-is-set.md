Title: Flex Builder3中的launch path设置
Author: alswl
Slug: flex-builder3-in-the-launch-path-is-set
Date: 2009-11-24 00:00:00
Tags: Flash, Flex, Flex Builder
Category: Coding

在Flex
Builder3中，想运行或者调试一个Flex项目，有Run/Debug/Profile三种运行方式。当我点击这三种方式的按钮时，都会报出一下警告：

> Flash Player Not Found

Flex Builder cannot locate the required version of Flash Player. You might
need to install Flash Player 9 or reinstall Flex Builder.

Do you want to try to run your application with the current version?

大意就是说没有找到Flash
Player，有两个选项Yes/No。如果是Yes，则开启FireFox打开一个html页面，其中内嵌着swf文件。这个警告框还给出一个"`Adobe
Flash Player downloads`"的下载链接。我下载安装后依然无法解决这个问题。

每次点一下倒并不是很麻烦，可恶的是如果这样，就无法对项目进行调试，`trace()`输出也不会在Console输出。

经过我尝试，我发现问题其实是出在项目的执行方式上，修改一下几个地方就可以了。

点击菜单栏的`Run->Run Configurations`，在打开的对话框中找到`Main`中的`URL or Path to
launch`，里面默认是`Use defaults`，现在我们把Debug/Profile/Run手工改成项目文件夹下对应的swf文件即可。

[![flex_launch_path](https://ohsolnxaa.qnssl.com/2009/11/flex_launch_path.jpg)](https://ohsolnxaa.qnssl.com/2009/11/flex_launch_path.jpg)

这样修改之后，无论是运行还是调试，都能在一个Flash Player中进行，比在Firefox中方便的多了。

