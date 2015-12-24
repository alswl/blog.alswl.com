Title: ss with haproxy
Author: alswl
Slug: ss with haproxy
Date: 2015-11-27 20:23:24
Tags: SS, HAProxy
Category: Efficiency

![shadowsocks.png](http://upload-log4d.qiniudn.com/upload_dropbox/201512/shadowsocks.png)

以前用自己的 SS，Linode 美国，后来 Linode 日本，但是始终拼不过上海电信的国际带宽。
经常不稳定，丢一半的包。

于是买了 [SS](https://portal.shadowsocks.com/aff.php?aff=4215) 服务，
9 台服务器，自己挑觉得速度快的服务器。

但一直固定某台服务器也会偶尔出问题，导致邮件出不来，网页打不开。
需要手动切换一下服务器。
于是用 HA 做了一个本地代理，调整了一些参数，让 SS 总是有快速的服务器供选择。

结构：

```
+-----------------+                                                  +----------------+
|                 |                                                  |                |
|    Server 1     |>>>>v                                           >>|   Mail.app     |
|                 |    v                                           ^ |                |
+-----------------+    v                                           ^ +----------------+
                       v                                           ^
+-----------------+    v    |----------------+      +------------+ ^ +----------------+
|                 |    v    |                |      |            | ^ |                |
|    Server 2     |>>>>>>>>>|    HAProxy     |>>>>>>| SS-Client  |>>>|   Browser      |
|                 |    ^    |                |      |            | v |                |
+-----------------+    ^    +----------------+      +------------+ v +----------------+
                       ^                                           v   
+-----------------+    ^                                           v +----------------+
|                 |    ^                                           v |                |
|    Server 3     |>>>>^                                           v>|   Evernote...  |
|                 |                                                  |                |
+-----------------+                                                  +----------------+
```

配置：


```
global
    ulimit-n  4096


defaults
    log global
    mode    tcp
    timeout connect 1s
    timeout client 1s
    timeout server 1s


listen stats
    bind 127.0.0.1:12222
    mode http
    stats enable
    stats uri /
    stats refresh 8s


listen ss
    bind 127.0.0.1:1081
    mode tcp
    option tcpka
    #balance source
    balance roundrobin
    log global
    maxconn 1024

    timeout connect 200ms
    timeout client 600s
    timeout server 600s
    timeout check 80ms  # for office / home
    # timeout check 400ms  # for starbucks
    retries 1
    option redispatch
    option tcp-check

    server s1 host1:port maxconn 20 check inter 2s rise 30 fall 6 backup
    server s2 host2:port maxconn 20 check inter 2s rise 30 fall 6
    server s3 host2:port maxconn 20 check inter 1s rise 60 fall 6
```


挺稳定，很快速。

update: 2015-12-15，添加 `backup` 项，选一台最稳定的做 backup，避免所有连接都超时。
update: 2015-12-13，添加 `redispatch`  / `retries` 项，换机器重试，
大幅提高可用性，注意，可能在非幂等状态下面产生未知错误。

![haproxy.png](http://upload-log4d.qiniudn.com/upload_dropbox/201512/haproxy.png)

在跑的 node，有些延迟高，被干掉了。

![youtube.png](http://upload-log4d.qiniudn.com/upload_dropbox/201512/youtube.png)

看 1080P 也挺顺畅。

