Title: OpenSSL初接触
Author: alswl
Date: 2009-03-05 00:00:00
Tags: OpenSSL, SSL
Category: C/C++编程
Summary: 

Boss昨个儿说，这两天把SSL上面的相关东西给他去看一下

苦命啊，最近都在做Ajax，SSL几乎没有什么动静。唉，今天中午没吃饭，没睡觉，就开始做SSL

耗费了很多时间，才正确的编译完OpenSSL

要做的东西是基于C#的、利用OpenSSL开源代码完成的SSL分级服务器，很是麻烦，要用C#来调用C程序，而且OpenSSL本来就很难使用，唉，残念啊。

下面把我今天的成果分享一下：

[[C#]用HttpWebRequest加载证书建立SSL通道时发生异常的解决办法- 旁观
...](http://www.cnblogs.com/zhengyun_ustc/archive/2005/04/11/135821.aspx)

[OpenSSL- .net，C++/CLI语言的一次实践](http://i.cn.yahoo.com/suntongo/blog/p_2/)

[OpenSSL: The Open Source toolkit for SSL/TLS](http://www.openssl.org/)

[使用OpenSSL API
进行安全编程](http://www.ibm.com/developerworks/cn/linux/l-openssl.html)

[在C#工程中使用OPENSSL](http://www.cnblogs.com/sleepingwit/archive/2008/11/03/132333
4.html)

[本文介绍在VC 6.0中编译和使用OpenSSL的过程- 微光的闪现-
博客园](http://www.cnblogs.com/gleam/archive/2008/05/07/1187154.html)

[深信服SSL VPN M4.0正式发布](http://www.sinfors.com/cn/news/913.htm)

这些是我使用的资料，搜集了好几天的

关于OpenSSL编译，源码文件夹下的INSTALL.W32就说的很清楚

[本文介绍在VC 6.0中_编译_和使用_OpenSSL_的过程- 微光的闪现-
博客园](http://www.cnblogs.com/gleam/archive/2008/05/07/1187154.html)

[_openssl编译_步骤- 太郎之石的专栏-
CSDNBlog](http://blog.csdn.net/gofishing/archive/2006/04/10/658203.aspx)

[在Windows下使用汇编方式_编译OpenSSL_方法- rabbit729的专栏-
CSDNBlog](http://blog.csdn.net/rabbit729/archive/2008/06/03/2506514.aspx)

[在Windows下_编译OpenSSL_（VS2005） - shootingstars -
博客园](http://shootingstars.cnblogs.com/archive/2006/02/17/332276.html)

之前我按照官方做法编译失败了，后来安装了VS2005之后就成功了，可能是环境配置的问题，如果VC6.0的朋友遇到和我一样的原因，可以换Visual
Studio下面的"Visual Studio 2005 命令提示"试试

