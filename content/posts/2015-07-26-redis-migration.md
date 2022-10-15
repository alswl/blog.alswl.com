---
title: "Redis 集群扩容"
author: "alswl"
slug: "redis-migration"
date: "2015-07-26T15:33:49+08:00"
tags: ["redis"]
categories: ["coding"]
---


几乎每一个网站都需要用户登录状态系统，其中核心是存储 Session 的用户登录状态存储系统。
主流的实现之一是使用 Redis 存储用户登录信息，Redis 特点是功能简单、无依赖、
存储结构丰富、有持久化功能。
我大堆糖的 Session 存储系统也正是基于 Redis。

可是 Redis 也存在一些问题，比如 Redis 自身没有 Sharding 功能，Replication
也是在逐步完善完善过程中
（2.4 支持 `Replication`，2.8 加入 `Replication partial resynchronization` 功能）。
纵观当下流行的 DB 系统，哪个不是自带这两个特性，这两个分布式特性应该成为新出产的 DB 系统的标配。
而且作者还经常发布延期，放烟雾弹，不知道 Redis 自带 Sharding 特性要等到何年马月。

随着业务规模的扩大，单台 Redis 实例不能满足需求。
考虑到 Redis 也是久经考验的战士，替换掉他成本比较高，那就对 Redis 进行扩容。

扩容的基本要求是：

* 扩大系统容量，成为分布式系统，未来有横向扩展
* 业务不中断
* 保证原始数据的可用性


Google 了一下，有两个项目可以参考：
[https://github.com/idning/redis-mgr][REDIS_MGR]
和豌豆荚的 [Codis][CODIS]。

研究了这两项目的代码之后，发现前者存在几个问题：
需要停机进行操作。
后者提供了完整一套解决方案，Server/Proxy/Config Manage，对我这次迁移来说，太重了，
而且项目比较新，风险高，只能用来参考实现方法。

最后我决定参考 redis-mgr 的方案，然后使用两种方式同步数据：
系统运行中打上 patch 完成数据的动态迁移；后台跑迁移数据脚本。


## 方案的关键词


### `dump` / `restore` / `pttl`

核心的操作流程是：
使用 `dump` 命令导出数据，`restore` 命令恢复数据，`pttl` 命令获取设置 TTL。


### Presharding

Redis 官方没有 sharding 方案，但提供一种策略 presharding。
Redis 作者写了一篇[Redis Presharding][PRE_SHARDING]。核心是：
提前做 2^n 个实例，避免扩容时候数据迁移，一般使用 2^n 个实例，
目的是为了能够自然地乘以 2 进行拆分。
这些实例可以分开放，也可以放在同一台机器上面。

我这次操作，将 `OLD_CLUSTER` 的一个实例拆分为了 `NEW_CLUSTER` 的 32 个实例，
跑在 4 台服务器上面。

### Twemproxy

Redis 的 经典款 Proxy，用来实现对多个 Redis 实例 sharding，
Twitter 出品，[链接][TWEMPROXY]。


### 一致性 Hash

传统的 Hash 方法是 `hash(key) = value % nodes.length`，
当加入、减少 Hash 节点时候，会导致 `hash(key)` 的全部失效。
典型的一致性 Hash 算法，[Ketama][KETAMA] 通过环状 node 分布，解决了这个问题。

Twemproxy 还提供 `modula` 和 random 两种分布式方案。


### db 大小预估

Redis 只能查看整个实例内存尺寸。不能查看单个 db。
使用 `ramdomkey` 做抽样检查，取 1% key 抽样，估计单个 key 大小，
然后做 benchmark 估算操作性能，估算操作时间。


### 动态迁移数据

为了在迁移过程中保证服务可用，需要将数据兼容 Redis 集群 `OLD_CLUSTER` / `NEW_CLUSTER`，
业务代码必须同时支持访问两个集群，做法也很简单

* 访问 `NEW_CLUSTER`
* 有数据则继续操作，无数据则访问 `OLD_CLUSTER`，获取数据 `DATA`
* 将数据和 TTL 保存到 `NEW_CLUSTER`

将这个逻辑封装成一个 client，替换掉原来 Redis Client 即可。

注意，这个点可能产生幻读，读取 key 和写入 key 有个时间差，
但是我处理的 session 是 immutable 数据，不会出现问题。
而如果将 Redis 用作 Persistence，就要评估对业务的影响了。


### 后台迁移数据

依赖用户访问来进行迁移，效率太低了，这个迁移时间和最长 TTL 时间相当，
需要主动将这个数据从 `OLD_CLUSTER` 迁移到 `NEW_CLUSTER`。

方案也很简单，使用 `randomkey` 获取一批数据，然后按动态迁移数据方法进行迁移。


### pipeline

如果在业务逻辑中使用了 PIPELINE，就会遇到问题，需要改写掉业务方案，
待迁移完成之后，再进行恢复。


### multikey

`mget` / `mset` 等多键操作方法需要注意拆解 key，然后一一 `dump` / `restore` /
`ttl`。


## 正式操作

线上操作的数据：

```
# 0.483 g db0
12:05:19,444 - __main__ - INFO - v, dumps keys 1014/1375371/..., time: 974.183676004
# 4.552 g db1
17:38:36,422 - __main__ - INFO - v, dumps keys 1392/7711834/..., time: 3076.41647506
```

附上 Migration Script：[https://blog.alswl.com/2015/07/redis-migration/ Redis Cluster Migration](https://gist.github.com/alswl/e96a5308ebac4f69f809f9ba56dfe168)


[REDIS_MGR]: https://github.com/idning/redis-mgr
[CODIS]: https://github.com/wandoulabs/codis
[PRE_SHARDING]: http://oldblog.antirez.com/post/redis-presharding.html
[KETAMA]: https://github.com/RJ/ketama
[TWEMPROXY]: https://github.com/twitter/twemproxy
