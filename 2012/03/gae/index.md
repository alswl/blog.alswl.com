

GAE 和我蛮有缘分，我初学 Python 的其中一个原因就是当时 GAE 刚推出， 当时想法是免费的应用要用起来，要不然就浪费了。随后也假模假样的看文档，
就是没有什么产出。

去年写了一个小应用 [dbevent2gc](https://github.com/alswl/dbevent2gc) ， 期间发现 GAE
和普通程序开发的诸多不同，又遭遇 GAE 配额大幅缩水， 写出来的应用运转的不太稳定。在南京图书馆的架上看见这本《GAE 编程指南读书笔记》，
立即借回家仔细阅读。

  * GAE 的简介  

    * 运行时环境 Python / Java
    * 数据存储 Datastore（实体 / 查询 / 索引 / 事务）
    * 服务（Memcache / GAccount / 任务队列 / 计划任务）
    * 工具（SDK / appcfg / dev_appserver / 控制台）
  * 入门（安装 / GAccount / webapp / app.yaml / /_ah/admin / 注册部署 / login:required）
  * 处理流程：请求 - 前端 - 引用服务器 / 静态文件服务器 - 服务  

    * 配额限制：请求限制 / CPU 限制 / 服务限制 / 部署限制 （最新配额：http://code.google.com/intl/zh-CN/appengine/docs/quotas.html）
  * 数据存储  

    * GAE 的数据存储方式和传统的 RDBMS 差异比较大，更类似于对象数据库。
    * 类别 kind / 键 / 键名 key name
    * 可以通过键来获取和操作对象  

      * `e = db.get(db.Key('Entity', 'alphabeta'))` / `e = Entity.get(k)`
      * `e = db.get(k)`
      * `e.delete()` / `db.delete(e1, e2)` / `db.delete(k)`
    * Expando 基类可以任意扩展属性，Model 基类则不可。
    * GAE 中基本类型与 Python / Java 中基本类型的差异
    * 多值属性
  * 数据查询  

    * 查询和类别 `db.query()` `query.filter()` `query.order()`
    * 查询和键：查询结果要么返回实体，要么返回键（ `key_only=True` ）
    * 可以用 GQL 写查询语句，不能写 CUD
    * 获取结果： `fetch()`
  * 索引  

    * 每条查询都需要维护一条索引，在 `index.yaml` 中可以配置
    * 排序之后的索引查询很快，查询效率和返回结果集有关
    * 实体的每个属性会自动维护两条索引：升序和降序
    * 查询时候选取对应的索引进行查询，条件语句可能和排序语句相冲突
    * 不等于 / IN 操作符将引发一系列变换出的查询
    * 多值字段的索引：每个值会成为索引中一行 / 实体会因此分散 / 取第一次成功扫描到的行
    * 多值会引入爆炸索引问题
  * 事务  

    * 通过实体组来控制事务，实体组会在同一块存储区
    * GAE 使用乐观锁
    * 使用 `AModel(parent=p)` 构造祖先，然后通过 `run_in_transation()` 回调事务处理函数
    * BigTable 中使用日志+时间戳来跟踪实体的修改，保证数据并发和一致性
    * 事务更新和索引更新：可能返回的索引结果和实体不一致
  * Python 数据建模  

    * 声明 / 类型 / 验证（ `validate()` ）
    * 不编入索引的属性 `indexed=False`
    * 时间类型的自动值
    * 模型变化带来的维护问题：修改属性类型 / 添加一个必要属性是不向后兼容的。
    * 关系建模  

      * db.ReferenceProperty
      * collection_name
    * 多对多关系的处理  

      * 键列表方法：使用多值属性
      * 链接模型方法：相当于中间表概念
    * 模型的继承：通过 `db.PolyModel` 实现多态查询
  * Memcache  

    * CRUD
  * 获取 URL 资源  

    * `urlfetch()`
  * RPC 异步请求调用，闭包调用
  * 邮件和 XMPP  

    * 额，亲用到时候看 Google 官方文档吧～
  * 大批量数据操作和远程访问  

    * `/remote_api`
    * Bulk Loader 大量数据操作
    * 远程 shell `remote_api_shell.py app-id`
  * 任务队列和计划任务  

    * 队列： `queue.yaml` / 令牌桶
    * 计划任务： `cron.yaml`
    * 都是通过设定主动触发某个 url
  * Django  

    * 看 Django 文档吧，亲～
  * 部署  

    * 上传 `appcfg.py update ./clock`
    * 通过 url 使用特定版本： `version-id.latest.app-id.appspot.com`
    * 版本只维护代码，数据库还是同一份
    * 下载日志 `appcfg.py request_logs clock logs.txt`


