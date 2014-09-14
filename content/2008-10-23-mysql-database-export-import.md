Title: mysql 数据库导出/导入
Author: alswl
Slug: mysql-database-export-import
Date: 2008-10-23 00:00:00
Tags: 综合技术, Database, MySQL
Category: Coding

正在学JSP，用的TomCat和MySQL，没有用CSV控制，所以数据库靠导出导入

导出：

cd bin;

mysqldump -uroot -proot xxx > xxx.sql;

导入：

cd bin;

create xxx;

source xxx.sql;

