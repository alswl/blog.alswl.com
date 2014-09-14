Title: 管理WebLogic服务
Author: alswl
Slug: manage-weblogic-service
Date: 2010-03-06 00:00:00
Tags: Java, Weblogic
Category: Coding

## 注册WebLogic成 windows服务

1、执行Domain目录下的 `installService.cmd [USER_NAME]
[PASSWORD]`命令，就会在windows服务中生成一个`beasvc
domainname_adminservername`的服务启动类型为"自动"，手动将它设置为启动就可以每次开机自动启动了。

2、在创建新的域的时候有这个选项的，服务名字为beasvc domainname-servername。

## 删除WebLogic服务

1.执行Domain目录下的 `stopWebLogic.cmd`命令就可以删除服务

2.删除服务之后，可以直接删除Domain下的所有文件～

