Title: MySQL Command Line Client乱码问题及解决方案
Author: alswl
Date: 2009-07-06 00:00:00
Tags: Database, MySQL, 编码
Category: 综合技术
Summary: 

以前用MySQL时候都是可视化界面，如MySQL Admin使用，现在学着使用MySQL Command Line client，初次接触，就遇到乱码问题。

乱码是中文字符串的，Google后，找到一些解决方案。摘录如下：

引用自今天去祸害哪家的闺女呢？<[猛击这里打开](http://leonel.javaeye.com/blog/315090)>

1:改变数据库的默认编码配置，在MYSQL的安装目录中，找到my.ini，修改默认编

码为：default-character-set=utf8

2:建立数据库时，CREATE DATABASE ms_db CHARACTER SET utf8 COLLATE

utf8_general_ci;

3:执行脚本：指定编码格式set names utf8(注意，不是UTF-8)

4:如果你采用的是外部接入的方式，在连接中确定请求的编码格式如：

jdbc:mysql://localhost:3306 /ms_db?

useUnicode=true&characterEncoding=UTF-8(不要出现任何空格，否则出错)

我使用的是第3种方法，由于我的数据库是Hibernate生成的，所以编码集改为utf8依然乱码，使用gbk就可以了。

