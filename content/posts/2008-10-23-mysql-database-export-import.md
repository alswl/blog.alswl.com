---
title: "mysql 数据库导出/导入"
author: "alswl"
slug: "mysql-database-export-import"
date: "2008-10-23T00:00:00+08:00"
tags: ["综合技术", "database", "mysql"]
categories: ["coding"]
---

正在学JSP，用的TomCat和MySQL，没有用CSV控制，所以数据库靠导出导入

导出：

```
cd bin;
mysqldump -uroot -proot xxx > xxx.sql;
导入：
cd bin;
create xxx;
source xxx.sql;

```
