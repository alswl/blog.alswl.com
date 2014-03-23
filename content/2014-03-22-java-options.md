Title: Java 运行参数调整
Author: alswl
Slug: java-options
Date: 2014-03-22 18:31:55
Tags:  JVM
Category: Java
Status: draft

JVM 在线上运行的时候，可以调整一些运行参数，查看参数帮助如下：

运行 `java -h` 可以看到 Java 运行可调整的参数。
运行 `java -X` 可以查看 Java 支持的额外参数。
注意一些参数的默认开启在 JDK6 和 JDK7 之间会有差异，甚至在 JDK7 的不同 update
也会有差异，运行 `java -XX:+PrintFlagsFinal` 查看默认的参数配置。

参考：
[Java HotSpot VM Options](http://www.oracle.com/technetwork/java/javase/tech/vmoptions-jsp-140102.html)
[The most complete list of -XX options for Java JVM ](http://stas-blogspot.blogspot.com/2011/07/most-complete-list-of-xx-options-for.html)
[ Tuning JVM Garbage Collection for Production Deployments ](http://docs.oracle.com/cd/E13209_01/wlcp/wlss30/configwlss/jvmgc.html)
[JVM -XX: 参数介绍](http://www.jvmer.com/jvm-xx-参数介绍/)

以下是一些经验调整：

```
-d64
# 运行在 64 位数据模式下

-server
# 选择 server VM

-Xms1024m
# 初始堆大小，直接固定到 Xmx

-Xmx1024m
# 最大堆大小，根据服务器性能和请求量调整，太大了会导致 GC 时间太长

-XX:+DoEscapeAnalysis:
# 支持逃逸分析（将局部对象实例存储在栈上）
# http://www.iteye.com/topic/473355

-XX:+UseTLAB
# Use thread-local object allocation
# 使用本地线程实例存储，可以减少堆共享锁的竞争

-XX:-RelaxAccessControlCheck
# Relax the access control checks in the verifier
# JDK7 默认不开启

-XX:+AggressiveOpts
# Enable aggressive optimizations - see arguments.cpp
# 启用最新 JVM 调优成果

-XX:+UseBiasedLocking
# Enable biased locking in JVM
# 偏向锁（建议去了解一下轻量级锁和偏向锁）
# 优化单线程程序下面锁资源速度，不适合多线程（所以到底 +/- 我存疑）
# http://www.iteye.com/topic/518066

-XX:+UseFastAccessorMethods
# Use fast method entry code for accessor methods
# 优化 get/set 方法

-XX:ThreadStackSize
# Thread Stack Size (in Kbytes)
# 经验值 4096

-XX:+UseLargePages
# Use large page memory
# 大内存分页

-XX:+UseStringCache
# Enables caching of commonly allocated strings.
# 启用缓存常用的字符串

-XX:+UseCompressedStrings: Use a byte[] for Strings which can be represented as pure ASCII. (Introduced in Java 6 Update 21 Performance Release)
# 降低内存消耗，浪费一点 CPU
# http://stackoverflow.com/questions/8833385/is-support-for-compressed-strings-being-dropped

-XX:+OptimizeStringConcat: Optimize String concatenation operations where possible. (Introduced in Java 6 Update 20)
# 优化字符串连接，对模板渲染操作应该会很有意义

-XX:MaxPermSize
# Maximum size of permanent generation (in bytes)
# 经验值 128m
```
