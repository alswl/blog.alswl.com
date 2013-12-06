Title: 让 Octopress 支持 RSS2.0
Author: alswl
Slug: support-rss
Date: 2012-05-22 16:18
Tags: Octopress, Jekyll, Squlid, 人人网
Category: Ruby 编程
Summary: 


土鳖人人网的 **日志导入** 功能仅支持 RSS2.0，而 Octopress 输出的订阅格式是 Atom1.0。
于是为了让人人网的同学能看见我那些技术宅，又或非技术宅的文章，
我只能昧着良心，给 Octopress 加上过时的 RSS2.0 输出。

在 `source/` 下创建新文件 `rss.xml` ，内容如下：

{% gist 2767610 %}

然后，访问 `http://site.url/rss.xml` 即可。
我的 RSS2.0 地址是 [http://log4d.com/rss.xml](http://log4d.com/rss.xml)。

最后，再让我吐槽一下人人网的工程师们：「导入日志后格式处理的一塌糊涂，几乎不能看」，真土鳖。