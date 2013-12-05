Title: Postfix 基本配置[译文]
Author: alswl
Date: 2013-11-09 14:59
Tags: Postfix
Category: Linuxer
Summary: 


原文地址：[Postfix Basic Configuration ](http://www.postfix.org/BASIC_CONFIGURATION_README.html#syntax)。
有少许编译。

## 介绍 ##

Postfix 的配置文件 [main.cf][] 有数百个配置参数，
幸运的是，所有参数都有合理的默认配置项。
大部分时候，只需要配置两三个参数即可。

安装 Postfix 的方法可以参见 [安装方法]。

特殊场景用途的配置方式，如邮件中枢，防火墙，拨号环境客户端的说明可以在
[标准配置说明][] 里面查看。

<!--more-->

## Postfix 配置语法 ##

Postfix 的配置文件默认在 `/etc/postfix`。主力配置文件是 [main.cf][] 和
[master.cf][]。用户权限必须是 root 的。

`/etc/postfix/main.cf` 配置语法有两个要点：不用引号，可以使用 `$` 来引用参数。

```
# 定义一个参数
/etc/postfix/main.cf:
    parameter = value
# 引用一个已有参数
/etc/postfix/main.cf:
    other_parameter = $parameter
```

引用参数时候，可以再定义之前先引用（Postfix 使用延迟计算技术）。

Postfix 使用数据文件来控制接入权限。详情请看 [DATABASE 介绍][]，一般这样配置：

```
/etc/postfix/main.cf:
    virtual_alias_maps = hash:/etc/postfix/virtual
```

修改 `main.cf` 或者 `master.cf` 之后，需要 `postfix reload` 重新载入配置文件。


## 配置对外发送域名 ##

[myorigin][] 参数指定邮件中显示的发送域名，默认使用当前机器名 `$myhostname`。
一般来说，我们会把 `myorigin` 设置成顶级域名 `$mydomain`。

范例：

```
/etc/postfix/main.cf:
    myorigin = $myhostname (default: send mail as "user@$myhostname")
    myorigin = $mydomain   (probably desirable: "user@$mydomain")
```

## 配置接收域名 ##

[mydestination][] 参数配置了本地直接接收的域名，而不会再对外发送。

这个参数可以使用文件配置，也可以使用 `type:table`，比如 hash / btree / ldap
/ mysql 等等。

范例：

```
# 默认配置
/etc/postfix/main.cf:
    mydestination = $myhostname localhost.$mydomain localhost

# 对整个域名生效
/etc/postfix/main.cf:
    mydestination = $myhostname localhost.$mydomain localhost $mydomain

# 对多个 DNS 域名生效
/etc/postfix/main.cf:
    mydestination = $myhostname localhost.$mydomain localhost 
        www.$mydomain ftp.$mydomain
```

## 配置允许从哪些地方接收 ##

默认情况下面，Postfix 仅发送信任网络的邮件。信任网络配置在 [mynetworks][] 参数中。

范例（使用下列任意一个）：

```
/etc/postfix/main.cf:
    mynetworks_style = subnet  (default: authorize subnetworks)
    mynetworks_style = host    (safe: authorize local machine only)
    mynetworks = 127.0.0.0/8   (safe: authorize local machine only)
    mynetworks = 127.0.0.0/8 168.100.189.2/32 (authorize local machine) 
```

还可以这样配置：

```
/etc/postfix/main.cf:
    mynetworks = 168.100.189.0/28, 127.0.0.0/8
```

## 配置允许发送到的域名 ##

默认情况下，非信任网络仅仅被允许从发送邮件到特定域名。默认值是
[mydestination][] 下面的所有域名（包括子域名）。

```
/etc/postfix/main.cf:
    relay_domains = $mydestination (default)
    relay_domains =           (safe: never forward mail from strangers)
    relay_domains = $mydomain (forward mail to my domain and subdomains)
```

## 配置递送方式：直接或间接 ##

默认情况下，Postfix 会直接递送邮件到因特网。有时候你的服务器在防火墙后面或者
无法直接连接互联网，那就需要将邮件递送到另外一个 [relay host][]。

范例：

```
/etc/postfix/main.cf:
    relayhost =                   (default: direct delivery to Internet)
    relayhost = $mydomain         (deliver via local mailhub)
    relayhost = [mail.$mydomain]  (deliver via local mailhub)
    relayhost = [mail.isp.tld]    (deliver via provider mailhub)
```

## 配置报告错误 ##

可以通过配置 [aliases][] 来将错误报告邮件转发给其他人。

范例：

```
/etc/aliases:
    postmaster: you
    root: you
```

默认情况下面，只会报告严重错误（资源错误和软件错误）：

```
/etc/postfix/main.cf:
    notify_classes = resource, software
```

其他错误还有：bounce 拒收 / 2bounce 错误报告拒收 / delay 延迟 / policy 策略未通过
/ protocol 协议错误 / resouce 资源错误 / software 软件错误

## 代理/NAT 配置 ##

有时候需要通过代理或者 NAT 连接互联网。参考 [proxy_interfaces][]

范例：

```
/etc/postfix/main.cf:
    proxy_interfaces = 1.2.3.4 (the proxy/NAT external network address)
```

## Postfix 日志分布情况 ##

日志路径配置在 `/etc/syslog.conf` 中：

```
etc/syslog.conf:
    mail.err                                    /dev/console
    mail.debug                                  /var/log/maillog
```

建议经常这样做日志审核：

```
# postfix check
# egrep '(reject|warning|error|fatal|panic):' /some/log/file
```

## 在 chorooted 状态下运行 Postfix ##

初学者就不用管这个了。

## 配置机器名 ##

[myhostname][] 手工指定了 FQDN。它被其他好几个域名相关的地方引用。

一般来说，如果指定了 `mydomain`，就会自动通过它生成 `myhostname`。

范例：

```
/etc/postfix/main.cf:
    myhostname = host.local.domain (machine name is not FQDN)
    myhostname = host.virtual.domain (virtual interface)
    myhostname = virtual.domain (virtual interface)
```

## 配置域名 ##

使用 [mydomain][] 配置，这个参数被很多地方引用。

范例：

```
/etc/postfix/main.cf:
    mydomain = local.domain
    mydomain = virtual.domain (virtual interface)
```

## 配置网络地址 ##

[inet_interfaces][] 配置监听网络。

默认配置：

```
/etc/postfix/main.cf:
    inet_interfaces = all
```

多个虚拟邮件服务器配置：

```
/etc/postfix/main.cf:
    inet_interfaces = virtual.host.tld         (virtual Postfix)
    inet_interfaces = $myhostname localhost... (non-virtual Postfix)
```

注意，这项参数配置完之后需要重启。


 [main.cf]: http://www.postfix.org/postconf.5.html
 [master.cf]: http://www.postfix.org/master.5.html
 [安装方法]: http://www.postfix.org/INSTALL.html
 [标准配置说明]: http://www.postfix.org/STANDARD_CONFIGURATION_README.html
 [DATABASE 介绍]: http://www.postfix.org/DATABASE_README.html
 [myorigin]: http://www.postfix.org/postconf.5.html#myorigin
 [mydestination]: http://www.postfix.org/postconf.5.html#mydestination
 [mynetworks]: http://www.postfix.org/postconf.5.html#mynetworks
 [mydestination]: http://www.postfix.org/postconf.5.html#mynetworks
 [relay host]: http://www.postfix.org/postconf.5.html#relayhost
 [aliases]: http://www.postfix.org/aliases.5.html
 [proxy_interfaces]: http://www.postfix.org/postconf.5.html#proxy_interfaces
 [myhostname]: http://www.postfix.org/postconf.5.html#myhostname
 [mydomain]: http://www.postfix.org/postconf.5.html#mydomain
 [inet_interfaces]: http://www.postfix.org/postconf.5.html#inet_interfaces