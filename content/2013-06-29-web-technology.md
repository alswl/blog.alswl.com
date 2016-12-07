Title: 读《大规模Web服务开发技术》
Author: alswl
Slug: web-technology
Date: 2013-06-29 00:17
Tags: 综合技术, 读书笔记
Category: Coding


年前看了这本书《大规模Web服务开发技术》，当时给的评价是：

> 很好，让我这个渣渣看的很感动，数据翔实，经历可靠，翻译的也不错，我给 4.2 分

现在经历过 Python / Django / 烂代码的阵痛，开始有更多的想法，
在整理这些粗糙的想法之前，我又把这本书翻了一遍，写个流水帐读书笔记。

![大规模Web服务开发技术](https://ohsolnxaa.qnssl.com/upload_dropbox/201306/s6818566.jpg)


《大规模Web服务开发技术》@豆瓣： [http://book.douban.com/subject/6758780/](http://book.douban.com/subject/6758780/)


规模
----

小规模 / 大规模 /
超大规模的侧重点各不相同：保持扩展性/保持冗余/低成本运维/开发合作方便

内存、磁盘、负载
----------------

内存快，磁盘慢，ＩＯ 速度的差异

数据分布式
----------

1.  使用局部分布式，热数据独立出来。
2.  Partition 分布式，按模块分割数据。
3.  按 ID 分割，比如 a-g, h-z
4.  按访问类型，一般请求 / feed / 图像（\#毒药计划的原理）

<!-- more -->

索引
----

索引，B 树（是一颗平衡树，log n 速度查找，顺序读取，插入，删除） / Ｂ+
树（节点只保存子节点指针，叶子保存数据）

使用 MySQL 索引的语句：

- where
- order by
- group by

多个查询时候要使用复合索引，每次查询只会走单一一个索引。

算法
----

感受算法 log n, 线性的差距。

### 字符匹配

正则到 Trie

### 贝叶斯匹配

### 全文搜索

逆向索引

基础设施
--------

- 云 / 自己构建
- 评估服务器性能极限
- 负载跟踪：平均负载 / 内存 / CPU 信息

冗余
----

- Web 服务器冗余
- DB 冗余
- 存储系统

维稳
----

- 功能增加 / 内存泄漏
- 特定 URL 的地雷，资源循环
- 访问暴增
- 数据量增加
- 外部 API 稳定（新浪等）
- 硬件故障

### 对策

- 保持余量， 在 70% 极限内运行
- 异常时候的自动重启 / 自动中止耗时查询

虚拟化
------

- 解除物理限制
- 软件层面主机控制

番外： 寻找瓶颈
--------------

调优的意义：「找出负载原因并去除」

- 查看平均负载
 -  top / uptime
- 确认 CPU、 I/O 瓶颈
 - sar / vmstat 检查交换区状态

番外： 负载
----------

负载的含义：等待 CPU / IO 资源的进程数。 知道了负载还要知道如何看 CPU
还是 IO 负载。

番外：sar
--------

- sar-P ALL
- sar -u
- sar -q
- sar -r

番外：Henata 的选择
------------------

队列系统：

- [TheSchwartz](/TheSchwartz)
- Gearman

DB 类型：

- Key Value： memcached / [TokyoTyrant](/TokyoTyrant)
- MyISAM / InnoDB

文件系统：

- MogileFS
- NFS
- WebDAV
- DRBD
- HDFS

缓存系统：

- Squid
- Vanish

计算集群：

- Hadoop
