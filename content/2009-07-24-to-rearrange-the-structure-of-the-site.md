Title: 重新整理网站的结构
Author: alswl
Slug: to-rearrange-the-structure-of-the-site
Date: 2009-07-24 00:00:00
Tags: 
Category: 建站心得

整理分为两个步骤：1.整理分类和标签。2.整理网页静态格式。

## 1.整理分类和标签

WordPress的分类和标签都是支持多对多形式的，也就是说一篇文章可以对应多个分类和多个标签，这样给作者带来了很大的方便，但同时也有了困惑，分类和标签到底
怎么区分。

千鸟志的大大在「[内容、标签和分类](http://blog.rexsong.com/?p=975)」中提到内容、标签和分类的三个阶段，其中一句话「标签(t
ags)的情况和分类类似，在传统组织方式中，分类必须创建于内容之前，而标签必须创建于内容之后。也就是说，分类和标签的根本区别在于创建先后顺序。」让我豁然开朗
。

我本身职业是程序员，所以我把我的标签定义为一些专业名词和一些特定名词，分类则是正常的分类。下面列举一下我的分类和标签。

分类：AJAX， C/C++， cinderella， Eclipse， FCKeditor， FireFox， Google， Hibernate， I,
Programer， IBM， Java， JavaScript， Linux， log4j， MFC， MySQL， Office， OGNL，
OpenSSL， PhotoShop， SSL， Struts2， Tomcat， Ubuntu， WinPcap， WordPress， WPF， 乱码，
五花八门， 保险， 关注互联网， 动漫， 友情链接， 娱乐着， 学海无涯， 工欲善其事必先利其器， 建站心得， 感悟， 数据库， 日记， 未分类， 校内，
游戏， 生活， 电脑相关， 碎碎念， 程序人生， 类库， 网络， 美工。

标签：乱码， 保险， 校内， 类库， 美食， 英语， 贴吧， AJAX， cinderella， Eclipse， FCKeditor， FireFox，
Google， Hibernate， IBM， log4j， MFC， MySQL， Office， OGNL， OpenSSL， PhotoShop，
Struts2， Tomcat， Ubuntu， WinPcap， WordPress， WPF

## 2.整理网页静态格式。

我最先的网址格式是 "/年/月/日/id.html"

后来改为 "/%year%/%monthnum%/%day%/%postname%.html"

现在比较后发现 "/%year%/%monthnum%/%postname%.html" 为最好

改网页静态格式带来的最大问题是会突然之间搜索引擎的结果全部转向404页面，所以如果可以不改，尽量不改。

对我而言，我既然网站结构大变动，就想全面整改。好在我的日访问量并不是很大。补救措施是在404页面加上相关解释，就能稍微起到一点引导性作用。

[我的404未找到页面](http://log4d.com/404.html)

