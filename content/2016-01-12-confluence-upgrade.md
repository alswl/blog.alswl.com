Title: 一次艰难的 Wiki 升级
Author: alswl
Slug: confluence-upgrade
Date: 2016-01-12 22:53:55
Tags: confluence
Category: Efficiency

公司使用 [Confluence][_confluence] 管理自己的知识库，
现在使用的版本还是 3.0.1，而最新的 Confluence 版本已经是 5.4+。
新版本加入的一些现代化 Web 系统的新特性很吸引人，
在群众的强烈呼声下，我着手开始升级。

![201601/confluence_river.jpg](http://upload-log4d.qiniudn.com/upload_dropbox/201601/confluence_river.jpg)

<!-- more -->

官方的升级路线很扯，3.0.1 的升级路线是：

*   3.0.1 -> 3.5.17
*   5.0.3 -> 5.4.4

中间两次大版本升级，第一次原因不明，第二次是更新了 markup 渲染引擎，
改为 HTML 格式类型的渲染模式。

由于一些原因，我们系统还跑在 embedded 模式下（其实就是 HyperSQL），这种大版本升级，
需要先从内置库升级到外部数据库，比如 MySQL。

苦逼旅程就开始了。


## From embedded to MySQL

更新内之苦到外部库的操作流程：

*   导出当前的数据备份，包括附件，我导出后 1G+
*   使用当前同版本（3.0.1）安装一个全新的 wiki，注意下载 JDBC-connector
*   安装之后，配置好 MySQL，开始导入之前准备好的备份
*   悲剧上演

遇到了错误：

>   Import failed. Hibernate operation: could not insert: [com.atlassian.confluence.core.BodyContent#12028015]; SQL []; Duplicate entry '12028015' for key 'PRIMARY'; nested exception is com.mysql.jdbc.exceptions.jdbc4.MySQLIntegrityConstraintViolationException: Duplicate entry '12028015' for key 'PRIMARY'

官方文档 [https://confluence.atlassian.com/doc/troubleshooting-xml-backups-that-fail-on-restore-199034.html](https://confluence.atlassian.com/doc/troubleshooting-xml-backups-that-fail-on-restore-199034.html)
让修改重复键数据，好吧，我改，搜索一把重复主键，将备份里面的 `entities.xml` 弄出来。

```
# 格式化
awk '{s=s $0}END{gsub(/></,">\n<",s);s=gensub(/>([^ \n>]*)</,">\n\\1\n<","g",s);print s}' entities.xml > entities.xml.format
# 找重复主键 cat entities.xml.format G 'content" class="Page' -A 2 G -E '[0-9]+' | sort | uniq -c | sort -gr L cat entities.xml.format | grep 'name="id"' -A 1 -B 1 | grep -E '[0-9]+' -B 2 L
```

操作过程中，发现有数据就一条数据（grep entities.xml），还是插入重复（13238835）。
官方文档解释是，内置数据库的锁有时候会不灵，插入重复键。
于是决定再试试去掉主键约束方案，大不了那个数据我就不要了。

```
ALTER TABLE BODYCONTENT DROP PRIMARY KEY;
```

结果还有其他 PK 约束，我于是一条一条解开，然后……还是不行，真是作了一手的好死。

结论是，这数据错误了太多，已经无法手工修复。


## 横插一刀的 Emoji 😊😢💗

导入时候报了这么一个错误：

> Caused by: java.sql.SQLException: Incorrect string value: '\xF0\x9F\x8C\x8D\xE5\x9B...' for column 'BODY' at row 1 org.xml.sax.SAXException: Error while parsing 2015-10-19 23:14:13,108 ERROR [Importing data task] [confluence.importexport.impl.ReverseDatabinder] fromXML Error processing backup: -- referer: http://10.1.2.155:8087/setup/setup-restore-start.action | url: /setup/setup-restore-local.action | userName: anonymous | action: setup-restore-local org.xml.sax.SAXException: Error while parsing net.sf.hibernate.exception.GenericJDBCException: could not insert: [com.atlassian.confluence.core.BodyContent#12028161]

这是 Emoji 编码的问题，理论上 MySQL 换到 5.6+，更新 encoding 就可以了。

但是……Confluence 的建表 SQL 爆出了 255 varchar 超过 1000 限制的错误
，我尝试使用 [innodb_large_prefix](https://github.com/rails/rails/issues/9855)
似乎可以解决（因为重复键的问题，导致导入已经行不通）。

另外 innodb_large_prefix 是 5.6.3 才有的，只能升级 MySQL，
并且需要创建表时候使用 DYNAMIC 参数。

弄个 Emoji 这么绕，这导致我直接弃用了 MySQL。


如果是正常迁移，不遇到重复键，Emoji 的问题，可以参考官方的文档，完成平滑迁移：

*   https://confluence.atlassian.com/doc/migrating-to-another-database-148867.html
*   https://confluence.atlassian.com/doc/database-setup-for-mysql-128747.html
*   https://confluence.atlassian.com/doc/upgrading-confluence-4578.html
*   https://confluence.atlassian.com/doc/upgrading-confluence-manually-255363437.html
*   https://confluence.atlassian.com/conf56/confluence-user-s-guide/creating-content/using-the-editor/using-symbols-emoticons-and-special-characters


## 妈蛋，自己干

上面这么点东西，陆陆续续花了我两周的时间（晚上）。已经确认走不通平滑迁移，那就别怪我手段糙了。

使用 API 导出后直接导入，这种做法最大问题是不平滑，会丢掉 Wiki 修改的历史记录，
在和各个业务方沟通之后，最后达成了一致：可以暴力升级。

升级流程：

*   准备最新 Confluence 新站点
*   关停站点
*   导出数据，包括 Page、评论、附件
*   导入 Page，评论，附件
*   启动旧站点，开启只读模式
*   启用新站点

官方有一个 [Universal Wiki Converter](https://migrations.atlassian.net/wiki)，
我在 Bitbucket 上面找到了源码，但是已经不可工作了。
虽然宣称「The UWC will however save you 1-2+ weeks of scripting development time, compared with starting from scratch, for many of the most common conversion cases.」
但并没有卵用。

不行就自己随便搞搞好了，看了一下开发需要的 [Conflunce API](https://confluence.atlassian.com/display/CONF30/Remote+API+Specification+2.4#RemoteAPISpecification2.4-Page)，
和尤其贴心的新版本 [RESTful API](https://developer.atlassian.com/confdev/confluence-rest-api?continue=https%3A%2F%2Fdeveloper.atlassian.com%2Fconfdev%2Fconfluence-rest-api&application=dac)，就开始搞了。

写迁移代码，在这里 [atlassian-confluence-xxoo](https://github.com/duitang/atlassian-confluence-xxoo)，已经开源了，只使用过一次，成功的从 3.0.1 迁移到 5.4.4，
理论上，支持任意版本的 3.x/4.x Confluence 迁移到最新。

使用 `python app.py -h` 查看帮助，不行就看看代码。

希望有迁移需求的同学，搜索到这里能够获得一些帮助。
