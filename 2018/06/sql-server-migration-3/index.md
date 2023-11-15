

该系列三篇文章已经全部完成：

*   [从 SQL Server 到 MySQL（一）：异构数据库迁移 - Log4D](https://blog.alswl.com/2018/03/sql-server-migration-1/)
*   [从 SQL Server 到 MySQL（二）：在线迁移，空中换发动机 - Log4D](https://blog.alswl.com/2018/05/sql-server-migration-2/)
*   [从 SQL Server 到 MySQL（三）：愚公移山 - 开源力量 - Log4D](https://blog.alswl.com/2018/06/sql-server-migration-3/)

![201806/refactor.png](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/201806/refactor.png)

我们用了两章文章
[从 SQL Server 到 MySQL（一）：异构数据库迁移](https://blog.alswl.com/2018/03/sql-server-migration-1/)
/
[从 SQL Server 到 MySQL（二）：在线迁移，空中换发动机](https://blog.alswl.com/2018/05/sql-server-migration-2/)
介绍我们遇到问题和解决方案。
不管是离线全量迁移还是在线无缝迁移，
核心 ETL 工具就是 yugong。

Yugong 是一个成熟工具， 在阿里巴巴去 IOE 行动中起了重要作用，
它与 Otter / Canal 都是阿里中间件团队出品。
它们三者各有分工：
Yugong 设计目标是异构数据库迁移；
Canal 设计用来解决 MySQL binlog 订阅和消费问题；
Otter 则是在 Canal 之上，以准实时标准解决数据库同步问题。
Otter 配备了相对 yugong 更健壮管理工具、分布式协调工具，
从而长期稳定运行。Yugong 设计目标则是一次性迁移工作，偏 Job 类型。
当然 yugong 本身质量不错，长期运行也没问题。
我们有个产线小伙伴使用我们魔改后 yugong，
用来将数据从管理平台同步数据到用户前台，已经稳定跑了半年多了。

<!-- more -->


## yugong 系统结构

这里我不赘述如何使用 yugong，有需求同学直接去
[官方文档](https://github.com/alibaba/yugong) 查看使用文档。

我直接进入关键环节：解剖 yugong 核心模块。
Yugong 数据流是标准 ETL 流程，分别有 Extractor / Translator / Applier
这三个大类来实现 ETL 过程:

![ETL & Java Class](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/201806/etl.png)

我们依次来看看这三大类具体设计。

### Extractor


![Extractor Class](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/201806/extractor.png)

*   `YuGongLifeCycle`：Yugong 组件生命周期声明
*   `AbstractYuGongLifeCycle`：Yugong 组件生命周期一些实现
*   `RecordExtractor`：基础 Extractor Interface
*   `AbstractRecordExtractor`：基础 Extractor 虚拟类，做了一部分实现
*   `AbstractOracleRecordExtractor`：Oracle Extractor 虚拟类，做了一部分 Oracle 相关实现
*   `OracleOnceFullRecordExtractor`：Oracle 基于特定 SQL 一次性 Extractor
*   `OracleFullRecordExtractor`：Oracle 全量 Extractor
*   `OracleRecRecordExtractor`：Oracle 记录 Extractor，用来创建物化视图
*   `OracleMaterializedIncRecordExtractor`：基于（已有）物化视图 Oracle 增量 Extrator
*   `OracleAllRecordExtractor`：Oracle 自动化 Extractor，先 Mark 再 Full，再 Inc

Exctractor 从 Source DB 读取数据写入内存，
Yugong 官方提供 Extractor 抽象出 `AbstractRecordExtractor` 类，
其余类都是围绕 Oracle 实现。
另外 Yugong 设计了 `YuGongLifeCycle` 类实现了组件生命周期管理。

### Translator

![Translator Class](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/201806/translator.png)

*   `DataTranslator`：Translator 基类，为 Row 级别数据处理
*   `TableTranslator`：Translator 基类，为 Table 级别提供处理（官方代码中没有使用）
*   `AbstractDataTranslator`：Data Translator 虚拟类，做了部分实现
*   `EncodeDataTranslator`：转换编码格式 Translator
*   `OracleIncreamentDataTranslator`：为 Oracle 增量数据准备 Translator，会调整一些数据状态
*   `BackTableDataTranslator`：Demo，允许在 Translator 中做回写数据操作
*   `BillOutDataTranslator`：Demo，包含一些阿里业务逻辑 Translator
*   `MidBillOutDetailDataTranslator`：Demo，包含一些阿里业务逻辑 Translator

Translator 读取内存中 RowData 然后变换，
大部分 Translator 做一些无状态操作，比如编码转换。
另外还有一小部分 Translator 做了业务逻辑操作，比如做一些数据回写。


### Applier

![Applier Class](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/201806/applier.png)

*   `RecordApplier`：基础 Applier Interface
*   `AbstractRecordApplier`：基础 Applier 虚拟类，做了一部分实现
*   `CheckRecordRecordApplier`：检查数据一致性 Applier，不做数据写入
*   `FullRecordRecordApplier`：全量数据 Applier，使用 UPSERT 做数据更新
*   `IncreamentRecordApplier`：增量 Applier，使用 Oracle 物化视图为数据源
*   `AllRecordRecordApplier`：自动化 Applier，先使用全量数据 Applier，然后使用增量数据 Applier


Applier 将经过 Translator 处理过的数据写入 Target DB。
Yugong 提供了一致性检查、全量、增量 Applier。
比较特殊是 `AllRecordRecordApplier` 提供了全套自动化操作。


### Others

除了 ETL 三个要素，yugong 还有一些重要类：控制类和工具类。

*   `SqlTemplate`：提供 CRUD / UPSERT 等操作的基类 SQL 模板
*   `OracleSqlTemplate`：基于 SqlTemplate 实现的 Oracle SQL 模板
*   `RecordDiffer`：一致性检查 differ
*   `YugongController`：应用控制器，控制整个应用数据流向
*   `YugongInstance`：控制单个迁移任务实例，一张表对应一个 YugongInstance


## 老战士的问题

说 yugong 有问题会有些标题党，毕竟它是久经考验老战士了。
但对我们来说，开源版本 yugong 还有一些不足：

*   不支持 SQL Server 读取
*   不支持 SQL Server 写入（Rollback 需要写入 SQL Server）
*   不支持 MySQL 读取

除了数据库支持，Yugong 在工程上面倒是也有一些改善空间。
我们最后花费了不少时间，做了工程上改进。

*   抛弃默认打包方式（基于 maven-assembly-plugin 生成类似 LFS 结构 tar.gz 文件），
    改为使用 fat jar 模式打包，仅生成单文件可执行 jar 包
*   抛弃 ini 配置文件，使用 YAML 配置文件格式（已有老配置仍然使用 ini 文件，YAML 主要管理表结构变更）
*   改造 Plugin 模式，将 Java 运行时编译改为反射获取 Java 类
*   拆分 Unit Test / Integration Test，降低重构成本
*   重构 Oracle 继承结构，使其开放 SQL Server / MySQL 接口
*   支持 Canal Redis 格式数据作为 MySQL 在线增量数据源


## 改造之后结构

### Extractor

![Extractor New Class](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/201806/extractor-new.png)

*   `AbstractSqlServerExtractor`：新增抽象 SqlServer Extractor
*   `AbstractMysqlExtractor`：新增抽象 MySQL Extractor
*   `AbstractFullRecordExtractor`：新增抽象 Full 模式 Extractor
*   `SqlServerCdcExtractor`：新增 SQL Server CDC 增量模式 Extractor
*   `MysqlCanalExtractor`：新增 MySQL Canal 格式增量消费 Extractor
*   `MysqlCanalRedisExtractor`：新增 MySQL Canal 格式增量消费 Extractor，使用 Redis 做回溯
*   `MysqlFullExtractor`：新增 MySQL 全量 Extractor
*   `SqlServerFullExtractor`：新增 SQL Server 全量 Extractor

在抽象出三个抽象类之后，整体逻辑更为清晰，如果未来要增加新数据库格式支持，也更为简单。


### Translator


![Translator New Class](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/201806/translator-new.png)


*   `Sha1ShardingTranslator`：根据 Sha1 Sharding Translator
*   `ModShardingTranslator`：根据 Value Mode Sharding Translator
*   `RangeShardingTranslator`：根据范围 Sharding Translator
*   `UserRouterMapShardingTranslator`：特定业务使用， 用户分表 Sharding Translator
*   `UserRouterMapMobileShardingTranslator`：特定业务使用， 用户分表 Sharding Translator
*   `ClassLearningNoteInfoShardingTranslator`：特定业务使用自定义 Translator
*   `ClassLearningIsActiveReverseShardingTranslator`：特定业务使用自定义 Translator
*   `ColumnFixDataTranslator`：调整表结构 Translator
*   `NameStyleDataTranslator`：调整表字段名 Translator，支持按风格对整个表自动转换
*   `CompositeIndexesDataTranslator`：解决复合主键下唯一 PK 确定问题的 Translator


新增了一系列 Translator。


### Applier

![Applier New Class](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/201806/applier-new.png)

*   `SqlServerIncreamentRecordApplier`：新增 SQL Server 增量消费 Applier

Applier 结构调整挺小，主要是增加了 SQL Server 的支持。


## 二次开发心得

如何快速了解一个开源项目？很多同学第一反应就是阅读源码。
看源码固然是有效果，但是性价比太低。
如果项目设计不合理，很快会迷失在代码细节之中。
我的经验是先阅读官方出品的一些 Slide 分享，然后阅读官方核心文档。
Slide 含金量高，在讲述核心中核心。

如果真要去了解细节去阅读源码，那我建议要善用工具，
比如使用 IntelliJ 的 Diagram 功能，抽象出核心类。
还有一些插件比如 SequencePluginReload 方便地生成函数之间调用，实为查看数据流利器。
我在这次开发过程中，也根据生成类图发现了一些问题，
从而在进入 Coding 之前，先对框架继承结构重构。提高了整体开发效率

根据代码风格判断，Yugong 并非是出自一个人之手。这多少会导致代码风格和设计上面不一致。
我自己也常年在业务线里面摸爬滚打，能想象到在快速推进项目中需要糙快猛。
但后人接受开发，多少会有些头疼。
于是我在进入开发之前，引入标准化 CheckStyle，用 Google Style 全局格式化，
使用 Sonar 扫描保证一个代码质量基线。
同时这也是一把双刃剑，格式化项目会导致大量 diff，
这也给我自己埋下了一个苦果，在后期给上游提交 PR 引入无尽问题。

开发过程中我也犯了一些错误。最为头疼是没有在早期考虑到向开源社区贡献，
导致未来向上游合并困难重重，现在还在头疼合并代码中。
另外，由于整体项目时间紧，我贪图实现速度，没有做更详尽单元测试覆盖。
这里没有遵循开源软件的最佳实践。

经过我改造的 Yugong 版本开源地址是：https://github.com/alswl/yugong 。
我也提交了 Pull Request https://github.com/alibaba/yugong/pull/66 ，
正在与官方沟通如何将这部分提交并入上游。

