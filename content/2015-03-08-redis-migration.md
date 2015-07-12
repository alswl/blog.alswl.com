Title: Redis 集群迁移
Author: alswl
Slug: redis-migration
Date: 2015-03-08 15:33:49
Tags: Redis
Category: Coding
Status: Draft


几乎每一个网站都需要用户登录系统，其中核心是存储 Session 的用户登录状态存储系统。
它的特点是读取频率极高，对吞吐量、响应速度、容量要求都很苛刻，
用户的每次点击都需要进行身份认证，量大，期望响应速度快，
否则看着 loading 那个小圈圈转啊转，肯定会疯掉。
目前主流的实现使用 Redis 存储用户登录信息，Redis 特点是功能简单、无依赖、
存储结构丰富（虽然一般只会用到简单 key-value 存取）、有持久化功能。
我大堆糖的使用的 Session 存储系统也正是 Redis。

可是 Redis 也不是什么问题没有，Redis 自身没有 Sharding 功能，Replication
也是在逐步完善完善过程中
（2.4 支持 `Replication`，2.8 加入 `Replication partial resynchronization` 功能）。
纵观当下流行的 DB 系统，哪个不是自带这两个特性，这两个分布式特性应该成为新出产的 DB 系统的标配。
而且作者还经常发布延期，放烟雾弹，不知道 Redis 自带 Sharding 特性要等到何年马月。

吐槽归吐槽，日子还是要过，随着业务规模的扩大，单台 Redis 实例不能满足需求。
考虑到 Redis 也是久经考验的战士，替换掉他成本比较高，那就来扩容吧。

扩容的基本要求是，扩大系统容量，业务不中断，保证原始数据的可用性。
本着这几个基本要求，想着我遇到的问题别一定遇到过，就开始 Google 了。

虽然搜索到的信息比较少，最后还是在 Github 搜到了好心人提供的解决方案
[https://github.com/idning/redis-mgr](https://github.com/idning/redis-mgr)
和 Codis 这个项目。

研究了这两项目的代码之后，发现前者存在几个问题：没有估算系统容量，需要停机进行操作。
后者是一个 Proxy，虽然有动态加入节点功能，只能用来参考实现方法。
