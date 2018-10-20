Title: 从 SQL Server 到 MySQL（二）：在线迁移，空中换发动机
Author: alswl
Slug: sql-server-migration-2
Date: 2018-05-21 11:24:36
Tags: SQLServer, MySQL, DB-Migration
Category: Coding

![flying-tanker](http://upload.log4d.com/upload_dropbox/201805/flying-tanker.png)

<smaill>（image via https://pixabay.com/en/military-stealth-bomber-refueling-602729/ ）</small>

在上篇文章
[从 SQL Server 到 MySQL （一）：异构数据库迁移 - Log4D](https://blog.alswl.com/2018/03/sql-server-migration-1/)
中，我们给大家介绍了从 SQL Server 到 MySQL 异构数据库迁移的基本问题和全量解决方案。
全量方案可以满足一部分场景的需求，但是这个方案仍然是有缺陷的：
迁移过程中需要停机，停机的时长和数据量相关。
对于核心业务来说，停机就意味着损失。
比如用户中心的服务，以它的数据量来使用全量方案，会导致迁移过程中停机若干个小时。
而一旦用户中心停止服务，几乎所有依赖于这个中央服务的系统都会停摆。

能不能做到无缝的在线迁移呢？系统不需要或者只需要极短暂的停机？
作为有追求的技术人，我们一定要想办法解决上面的问题。

<!-- more -->


## 在线迁移的原理和流程

针对 Oracle 到 MySQL，市面上已经有比较成熟的解决方案 - alibaba 的
[yugong](https://github.com/alibaba/yugong)
项目。
在解决 SQL Server 到 MySQL 在线迁移之前，我们先研究一下 yugong 是如何做到 Oracle
的在线迁移。

下图是 yugong 针对 Oracle 到 MySQL 的增量迁移流程：

![yugong-oracle.png](http://upload.log4d.com/upload_dropbox/201805/yugong-oracle.png)

这其中有四个步骤：

1.  增量数据收集 (创建 Oracle 表的增量物化视图)
2.  进行全量复制
3.  进行增量复制 (可并行进行数据校验)
4.  原库停写，切到新库

Oracle 物化视图（Materialized View）是 Oracle 提供的一个机制。
一个物化视图就是主库在某一个时间点上的复制，可以理解为是这个时间点上的 Snapshot。
当主库的数据持续更新时，物化视图的更新可以通过独立的批量更新完成，称之为 `refreshes`。
一批 `refreshes` 之间的变化，就对应到数据库的内容变化情况。
物化视图经常用来将主库的数据复制到从库，也常常在数据仓库用来缓存复杂查询。

物化视图有多种配置方式，这里比较关心刷新方式和刷新时间。
刷新方式有三种：

*   Complete Refresh：删除所有数据记录重新生成物化视图
*   Fast Refresh：增量刷新
*   Force Refresh：根据条件判断使用 Complete Refresh 和 Fast Refres

刷新机制有两种模式： Refresh-on-commit 和 Refresh-On-Demand。

Oracle 基于物化视图，就可以完成增量数据的获取，从而满足阿里的数据在线迁移。
将这个技术问题泛化一下，想做到在线增量迁移需要有哪些特性？
我们得到如下结论（针对源数据库）：

*   增量变化：支持增量获得增量数据库变化
*   延迟：获取变化数据这个动作耗时需要尽可能低
*   幂等一致性：变化数据的消费应当做到幂等，即不管目标数据库已有数据什么状态，都可以无差别消费

回到我们面临的问题上来，SQL Server 是否有这个机制满足这三个特性呢？
答案是肯定的，SQL Server 官方提供了 CDC 功能。



## CDC 的工作原理

什么是 CDC？
CDC 全称 Change Data Capture，设计目的就是用来解决增量数据的。
它是 SQL Server 2008 新增的特性，
在这之前只能使用 SQl Server 2005 中的 `after insert` / `after delete`
/ `after update` Trigger 功能来获得数据变化。

CDC 的工作原理如下：

![cdc-data-flow.png](http://upload.log4d.com/upload_dropbox/201805/cdc-data-flow.png)

当数据库表发生变化时候，Capture process 会从 transaction log 里面获取数据变化，
然后将这些数据记录到 Change Table 里面。
有了这些数据，用户可以通过特定的 CDC 查询函数将这些变化数据查出来。


## CDC 的数据结构和基本使用

CDC 的核心数据就是那些 Change Table 了，这里我们给大家看一下
Change Table 长什么样，可以有个直观的认识。

通过以下的函数打开一张表（fruits）的 CDC 功能。

```sql
-- enable cdc for db
sys.sp_cdc_enable_db;
-- enable by table
EXEC sys.sp_cdc_enable_table @source_schema = N'dbo', @source_name = N'fruits', @role_name = NULL;
-- list cdc enabled table
SELECT name, is_cdc_enabled from sys.databases where is_cdc_enabled = 1;
```

至此 CDC 功能已经开启，如果需要查看哪些表开启了 CDC 功能，可以使用一下 SQL：

```sql
-- list cdc enabled table
SELECT name, is_cdc_enabled from sys.databases where is_cdc_enabled = 1;
```

开启 CDC 会导致产生一张 Change Table 表 `cdc.dbo_fruits_CT`，这张表的表结构如何呢？

```sql
.schema cdc.dbo_fruits_CT
name            default  nullable  type          length  indexed
--------------  -------  --------  ------------  ------  -------
__$end_lsn      null     YES       binary        10      NO
__$operation    null     NO        int           4       NO
__$seqval       null     NO        binary        10      NO
__$start_lsn    null     NO        binary        10      YES
__$update_mask  null     YES       varbinary     128     NO
id              null     YES       int           4       NO
name            null     YES       varchar(255)  255     NO
```

这张表中以 `__` 开头的字段是 CDC 所记录的元数据，`id` 和 `name` 是 fruits 表的原始字段。
这意味着 CDC 的表结构和原始表结构是一一对应的。

接下来我们做一些业务操作，让数据库的数据发生一些变化，然后查看 CDC 的 Change Table：

```sql
-- 1 step
DECLARE @begin_time datetime, @end_time datetime, @begin_lsn binary(10), @end_lsn binary(10);
-- 2 step
SET @begin_time = '2017-09-11 14:03:00.000';
SET @end_time   = '2017-09-11 14:10:00.000';
-- 3 step
SELECT @begin_lsn = sys.fn_cdc_map_time_to_lsn('smallest greater than', @begin_time);
SELECT @end_lsn = sys.fn_cdc_map_time_to_lsn('largest less than or equal', @end_time);
-- 4 step
SELECT * FROM cdc.fn_cdc_get_all_changes_dbo_fruits(@begin_lsn, @end_lsn, 'all');
```

这里的操作含义是：

1.  定义存储过程中需要使用的 4 个变量
2.  begin_time / end_time 是 Human Readable 的字符串格式时间
3.  begin_lsn / end_lsn 是通过 CDC 函数转化过的 Log Sequence Number，代表数据库变更的唯一操作 ID
4.  根据 begin_lsn / end_lsn 查询到 CDC 变化数据

查询出来的数据如下所示：

```sql
__$start_lsn          __$end_lsn  __$seqval             __$operation  __$update_mask  id  name
--------------------  ----------  --------------------  ------------  --------------  --  ------
0000dede0000019f001a  null        0000dede0000019f0018  2             03              1   apple
0000dede000001ad0004  null        0000dede000001ad0003  2             03              2   apple2
0000dede000001ba0003  null        0000dede000001ba0002  3             02              2   apple2
0000dede000001ba0003  null        0000dede000001ba0002  4             02              2   apple3
0000dede000001c10003  null        0000dede000001c10002  2             03              3   apple4
0000dede000001cc0005  null        0000dede000001cc0002  1             03              3   apple4
```

可以看到 Change Table 已经如实的记录了我们操作内容，注意 `__$operation`
代表了数据库操作：

*   1  => 删除
*   2  => 插入
*   3  => 更新前数据
*   4  => 更新后数据

根据查出来的数据，我们可以重现这段时间数据库的操作：

*   新增了 `id` 为 1 / 2 的两条数据
*   更新了 `id` 为 2 的数据
*   插入了 `id` 为 3 的数据
*   删除了 `id` 为 3 的数据


## CDC 调优

有了 CDC 这个利器，终于意味着我们的方向是没有问题的，我们终于稍稍吁了一口气。
但除了了解原理和使用方式，我们还需要深入了解 CDC 的工作机制，对其进行压测、调优，
了解其极限和边界，否则一旦线上出现不可控的情况，就会对业务带来巨大损失。

我们先看看 CDC 的工作流程，就可以知道有哪些核心参数可以调整：

![Influence of capture job parameters](http://upload.log4d.com/upload_dropbox/201805/cdc-influence.png)

上图是 CDC Job 的工作流程：

*   蓝色区域是一次 Log 扫描执行的最大扫描次数：maxscans number（`maxscans`）
*   蓝色区域同时被最大扫描 transcation 数量控制：`maxtrans`
*   浅蓝色区域是扫描间隔时间，单位是秒：`pollinginterval`

这三个参数平衡着 CDC 的服务器资源消耗、吞吐量和延迟，
根据具体场景，比如大字段，宽表，BLOB 表，可以调整从而达到满足业务需要。
他们的默认值如下：

*   `maxscan` 默认值 10
*   `maxtrans` 默认值 500
*   `pollinginterval` 默认值 5 秒


## CDC 压测

掌握了能够调整的核心参数，我们即将对 CDC 进行了多种形式的测试。
在压测之前，我们还需要确定关键的健康指标，这些指标有：

*   内存：buffer-cache-hit / page-life-expectancy / page-split 等
*   吞吐：batch-requets / sql-compilations / sql-re-compilations / transactions count
*   资源消耗：user-connections / processes-blocked / lock-waits / checkpoint-pages
*   操作系统层面：CPU 利用率、磁盘 IO

出于篇幅考虑，我们无法将所有测试结果贴出来，
这里放一个在并发 30 下面插入一百万数据（随机数据）进行展示：

![cdc-metrics.png](http://upload.log4d.com/upload_dropbox/201805/cdc-metrics.png)

![cdc-system-load.png](http://upload.log4d.com/upload_dropbox/201805/cdc-system-load.png)

测试结论是，在默认的 CDC 参数下面：

CDC 的开启/关闭过程中会导致若干个 Process Block，
大流量请求下面（15k TPS）过程会导致约 20 个左右 Process Block。
这个过程中对服务器的 IO / CPU 无明显波动，
开启/关闭瞬间会带来 mssql.sql-statistics.sql-compilations 剧烈波动。
CDC 开启后，在大流量请求下面对 QPS / Page IO 无明显波动，
对服务器的 IO / CPU 也无明显波动， CDC 开启后可以在 16k TPS 下正常工作。

如果对性能不达标，官方有一些简单的优化指南：

*   调整 maxscan maxtrans pollinginterval
*   减少在插入后立刻插入
*   避免大批量写操作
*   限制需要记录的字段
*   尽可能关闭 net changes
*   没任务压力时跑 cleanup
*   监控 log file 大小和 IO 压力，确保不会写爆磁盘
*   要设置 filegroup_name
*   开启 sp_cdc_enable_table 之前设置 filegroup


## yugong 的在线迁移机制

OK，截目前位置，我们已经具备了 CDC 这个工具，但是这仅仅提供了一种可能性，
我们还需要一个工具将 CDC 的数据消费出来，并喂到 MySQL 里面去。

好在有 yugong。
Yugong 官方提供了 Oracle 到 MySQL 的封装，并且抽象了 Source / Target /
SQL Tempalte 等接口，
我们只要实现相关接口，就可以完成从 SQL Server 消费数据到 MySQL 了。

这里我们不展开，我还会花专门的一篇文章讲如何在 yugong 上面进行开发。
可以提前剧透一下，我们已经将支持 SQL Server 的 yugong 版本开源了。


## 如何回滚

数据库迁移这样的项目，我们不仅仅要保证单向从 SQL Server 到 MySQL 的写入，
同时要从 MySQL 写入 SQL Server。

这个流程同样考虑增量写入的要素：增量消费，延迟，幂等一致性。

MySQL 的 binlog 可以满足这三个要素，需要注意的是，MySQL binlog 有三种模式，
Statement based，Row based 和 Mixed。只有 Row based 才能满足幂等一致性的要求。

确认理论上可行之后，我们一样需要一个工具将 binlog 读取出来，并且将其转化为
SQL Server 可以消费的数据格式，然后写入 SQL Server。

我们目光转到 alibaba 的另外一个项目 Canal。
Canal 是阿里中间件团队提供的 binlog 增量订阅 & 消费组件。
之所以叫组件，是由于 Canal 提供了 Canal-Server 应用和 Canal Client Library，
Canal 会模拟成一个 MySQL 实例，作为 Slave 连接到 Master 上面，
然后实时将 binlog 读取出来。
至于 binlog 读出之后想怎么使用，权看用户如何使用。

我们基于 Canal 设计了一个简单的数据流，在 yugong 中增加了这么几个功能：

*   SQL Server 的写入功能
*   消费 Canal 数据源的功能

Canal Server 中的 binlog 只能做一次性消费，
内部实现是一个 Queue，
为了满足我们可以重复消费数据的能力，我们还额外设计了一个环节，将 Canal
的数据放到 Queue 中，在未来任意时间可以重复消费数据。
我们选择了 Redis 作为这个 Queue，数据流如下。

![canal.png](http://upload.log4d.com/upload_dropbox/201805/canal.png)


## 最佳实践

数据库的迁移在去 Windows 中，是最不容得出错的环节。
应用是无状态的，出现问题可以通过回切较快地回滚。
但数据库的迁移就需要考虑周到，做好资源准备，发布流程，
故障预案处理。

考虑到多个事业部都需要经历这个一个过程，我们项目组将每一个步骤都固化下来，
形成了一个最佳实践。我们的迁移步骤如下，供大家参考：


| 大阶段   | 阶段               | 事项                                                                                | 是否完成   | 负责人     | 耗时   | 开始时间   | 完成时间   | 备注   |
| -------- | ------------------ | ----------------------------------------------------------------------------------- | ---------- | ---------- | ------ | ---------- | ---------- | ------ |
| 白天     | 存量数据阶段       | 创建 MySQL 数据库，准备相关账号资源                                                 |            | DBA        |        |            |            |        |
|          |                    | 开启 CDC                                                                            |            | DBA        |        |            |            |        |
|          |                    | 从 Slave SQLServer dump 一份 snapshot 到 Backup SQL Server                          |            | DBA        |        |            |            |        |
|          |                    | Backup SQL Server 消费数据， ETL 到 MySQL                                           |            | DBA        |        |            |            |        |
|          | 增量数据阶段       | 确认 ETL 数据已经消费完成，检查数据总条数                                           |            | DBA        |        |            |            |        |
|          |                    | 从 Slave SQLServer 开始消费 CDC 数据，持续写入 MySQL                                |            | DBA        |        |            |            |        |
|          |                    | 使用 yugong 检查一天内数据的一致性                                                  |            | DBA        |        |            |            |        |
|          |                    | 检查不一致的数据，10 分钟之后人工进行检查，确认是 CDC 延迟带来的问题                |            | DBA        |        |            |            |        |
|          |                    | 检查数据总量条目                                                                    |            | DBA        |        |            |            |        |
|          |                    | 使用 yugong 对抽样表进行全量检查                                                    |            | DBA        |        |            |            |        |
| 凌晨     | 应用发布阶段       | 停止 SQL Server 的应用                                                              |            | 技术经理   |        |            |            |        |
|          |                    | 检查没有连接进入 SQL Server                                                         |            | DBA        |        |            |            |        |
|          |                    | 使用 yugong 检查一天内数据的一致性                                                  |            | DBA        |        |            |            |        |
|          |                    | 检查数据总量条目                                                                    |            | DBA        |        |            |            |        |
|          |                    | 启用基于 MySQL 的应用                                                               |            | 运维       |        |            |            |        |
|          | 测试阶段           | 测试应用是否正常，回归所有功能                                                      |            | QA         |        |            |            |        |
|          |                    | （临时新增）测试 ReadOnly DB 的应用访问情况                                         |            | QA         |        |            |            |        |
|          | 完成阶段           | 接入流量                                                                            |            | 运维       |        |            |            |        |
|          | （可选）回滚阶段   | 发现问题，直接将应用切回 SQL Server                                                 |            | 运维       |        |            |            |        |
|          |                    | 事后进行数据审计，进行新增数据补偿                                                  |            | DBA        |        |            |            |        |
|          |                    | （可选）回滚过程中，使用 Canal 读取 binlog，并使用 Canal Client 重放到 SQL Server   |            | DBA        |        |            |            |        |

## Reference

*   [Materialized View Concepts and Architecture](https://docs.oracle.com/cd/B10500_01/server.920/a96567/repmview.htm)
*   [Tuning the Performance of Change Data Capture in SQL Server 2008 | Microsoft Docs]( https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008/dd266396(v=sql.100) )
*   [alibaba/yugong: 阿里巴巴去Oracle数据迁移同步工具(全量+增量,目标支持MySQL/DRDS)](https://github.com/alibaba/yugong)
*   [alibaba/canal: 阿里巴巴mysql数据库binlog的增量订阅&消费组件 。阿里云DRDS( https://www.aliyun.com/product/drds )、阿里巴巴TDDL 二级索引、小表复制powerd by canal.](https://github.com/alibaba/canal)
