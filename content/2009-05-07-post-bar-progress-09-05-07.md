Title: 贴吧进度-09-05-07
Author: alswl
Slug: post-bar-progress-09-05-07
Date: 2009-05-07 00:00:00
Tags: Struts, 贴吧
Category: Java编程和Java企业应用
Summary: 

今天写到创建帖子，在编码上遇到问题，jUnit下调用函数没有任何问题，那就表示问题出在Struts Filter捕获的文本上。

找了好几个方法都没有奏效。

游客登录情况下的Session还存在一点问题，原因是session类型转换上的问题，今天还没有好好的研究一下。

至此为止，登录注册写完了，静态校验写了一个毛胚，今天写完的现实帖子的列表，表现层用OGNL完成的，终于脱离开代码混杂的页面。

解决了一个tx.commit的错误，原来是《开发者突击》书上的代码有问题，我参考了Hibernate的官方文档，终于发现了错误的原因，tx.rollback
()应该在catch里面而不是final里面。

写着写着就感觉自己太多的不足，太多要学习的地方，加油！

