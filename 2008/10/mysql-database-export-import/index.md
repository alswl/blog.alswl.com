

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

