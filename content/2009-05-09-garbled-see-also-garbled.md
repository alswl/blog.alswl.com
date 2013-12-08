Title: 乱码！又见乱码！
Author: alswl
Slug: garbled-see-also-garbled
Date: 2009-05-09 00:00:00
Tags: Hibernate, Struts, 编码, 贴吧
Category: Java编程和Java企业应用

今天解决了贴吧发帖的问题，可以正确的发送到正确的分类了。

随后遇到的问题是发帖完毕返回 Category.action 时候，无法读取争取的贴吧分类数据，经过在 struts.xml
里的Category.action 里的 result 后面的url加入参数，可以读取正确categoryId了

本来想在result中加入param元素而不是在url后面加 ？categoryId=0来实现，但是尝试了好久，Google和官方文档都没有什么解决方案

其中遇到的一个问题是「&」这个符号不能直接使用，需要进行转义，用「&amp;」来替代。

最后是categoryName的问题了，本来以为很简单，却遇到了编码问题，之前从Home.action转到Category.action能正确编码，像 ht
tp://localhost:8080/PostBar/Category.action?categoryId=4&categoryName=%E9%9F%B
3%E4%B9%90 ，而现在的categoryName后面却有乱码

最恨乱码问题，整整花了我将近2小时，仍然没有完美解决方法，只能勉强在PostTopic.action转到Category.action时进行Encode编码
，但是这十足dirty work，而且不方便再次读取categoryName。

我尝试在struts.xml用OGNL语言进行转换，但是却无法运行，找不出问题。

实在没有办法了，现在我准备用Baidu这种url形式，只传递categoryId，而在此用Hibernate读取数据库去除categoryName来获得内容

当初之所以考虑多次传递时怕读取数据库会导致性能大幅度下降，今天又学习了一下Hibernate的缓存机制，感觉是我多虑了，二级缓存应该能大大缓解多次读取的问题
。

