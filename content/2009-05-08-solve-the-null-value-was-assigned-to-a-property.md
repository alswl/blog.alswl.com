Title: 解决 Null value was assigned to a property
Author: alswl
Slug: solve-the-null-value-was-assigned-to-a-property
Date: 2009-05-08 00:00:00
Tags: Hibernate, 贴吧
Category: Java编程和Java企业应用
Summary: 

晚上开始写贴吧分类，把class改成category，规避了关键字class，也显得更合理，百度的分类就是ct

然后在分类上遇到一个小问题，category_father在数据库是integer类型，可以为null，因为存在根分类，在这种情况下用Hibernate读取
Category时会产生错误

在jUnit单元测试中就通不过，错误为 org.hibernate.PropertyAccessException: Null value was
assigned to a property

Google后，发现Category中定义categoryFather为int类型，是不支持null的，需要改为Wrapper类Interger

有人说只需要设定setXXX和getXXX的Integer的类型和.hbm.xml文件中个Type="java.lang.Integer"就可以了

但是经过我测试发现，categoryFather 这个成员也要定义成Interger，否则会报错
org.hibernate.PropertyAccessException: Exception occurred inside setter of ...

晚上写完分类，感慨到：框架先行，功能其后，界面殿后。由于我home.jsp和category.jsp没有安排好，导致了很多问题。尽管有Eclipse的ren
ame功能，把class改为category依然很麻烦

