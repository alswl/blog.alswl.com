Title: 给WordPress加上robots.txt
Author: alswl
Slug: wordpress-to-add-robots-txt
Date: 2009-08-05 00:00:00
Tags: WordPress
Category: 建站心得
Summary: 

在Google搜索我的页面，能出来400+页面，但好多都是额外的页面，比如分页下的信息，比如说wap下的信息，最可怕的是甚至登录页面都暴露在Google搜索
结果中，这让我有点害怕了。

参考下面两篇文章《[善用 robots.txt 优化 Wordpress 博客 |
望月的博客](http://wangyueblog.com/2009/02/11/wordpress-robots-
txt/)》、《[总结一下Meta的用法及robot.txt的讲解 - SEO搜索引擎优化 -  ITOKIT.COM |WEB开发技术,站长交流论坛 -
Powered by Discuz!](http://www.itokit.com/bbs/viewthread.php?tid=45)》

为了优化WordPress的SEO效率，我们可以使用[robots.txt](http://log4d.com/robots.txt)文件来对搜索引擎搜索范
围进行限制。

下面是我的robots.txt内容：

    
    
    User-agent: *
    Disallow: /wp-
    Disallow: /feed/
    Disallow: /page/
    Disallow: /comments/feed
    Disallow: /index-wap.php/
    # BEGIN XML-SITEMAP-PLUGIN
    Sitemap: http://log4d.com/sitemap.xml.gz
    # END XML-SITEMAP-PLUGIN

其中屏蔽了page的分页、feed页面（据说feed容易引起baidu收录页面低下）、wp-页面（为了安全）、wap页面。

最后一句话为搜索引擎指出sitemap位置。

祝大家被Google/Baidu收录更多更有用的文章。

更新（09-08-12）：这段时间发现Google收录骤减，检查后发现很多以前日志没了，想了一下原因，发现下列代码阻止了蜘蛛爬以前的日志，造成收录减少，删除
下面的代码即可。

`Disallow: /page/`

