Title: FMS的80端口占用
Author: alswl
Slug: fms-80-port-used
Date: 2010-05-22 00:00:00
Tags: FMS
Category: Flash编程
Summary: 

AzaAjaxChat 的语音聊天需要使用的Flex的流媒体传输，我在评估的方案有两套：1.使用原声Socket在客户端进行连接，2.使用FMS
流媒体服务器进行数据传输。

FMS （Flash Media Server）在安装时候，有一个选项是端口使用哪个，默认是1935 和
80端口，安装之后发现在使用两个Apache在80端口发生冲突（FMS使用的也是Apache服务器），需要将这个端口修改。

Google后，发现修改 Flash Media Server 3conffms.ini 删除80留下1935即可。

    
    # IP address and port(s) Flash Media Server should listen on
    # For example:
    #    ADAPTOR.HOSTPORT = :1935,80
    #
    ADAPTOR.HOSTPORT = :1935

唔～继续搞鼓Flex的流媒体传输了，头疼蛋大啊。。。

相关链接：[Flash Media Server 开发版下载](http://www.adobe.com/cfusion/tdrc/index.cfm?pr
oduct=flashmediaserver&loc=zh_cn)，容量有上线，支持10个用户并发操作

