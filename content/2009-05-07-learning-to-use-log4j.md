Title: 学习使用log4j
Author: alswl
Date: 2009-05-07 00:00:00
Tags: log4j
Category: Java编程和Java企业应用
Summary: 

今天用Log4j时候，感觉只显示message讯息太少了，直觉上这些流行的工具应该会提供更强大的定制功能，就去google了一下

果不其然：相关配置参数如下

# Pattern to output the caller's file name and line number.

# %m 输出代码中指定的消息

# %p 输出优先级，即DEBUG，INFO，WARN，ERROR，FATAL

# %r 输出自应用启动到输出该log信息耗费的毫秒数

# %c 输出所属的类目，通常就是所在类的全名

# %t 输出产生该日志事件的线程名

# %n 输出一个回车换行符，Windows平台为「rn」，Unix平台为「n」

# %d 输出日志时间点的日期或时间，默认格式为ISO8601，也可以在其后指定格式，比如：%d{yyy MMM dd
HH:mm:ss,SSS}，输出类似：2002年10月18日 22：10：28，921

# %l 输出日志事件的发生位置，包括类目名、发生的线程，以及在代码中的行数。

通过配置这些参数可以定制自己想要的记录。

我修改 log4j.properties 文件后却没有得到我预想的效果，经过检查，发现在 appender
的定义名与下面使用的不一致，唉，也不知道当初哪里拷贝来的代码

并且如果想使用定制模式，应该设定log4j.appender.A1.layout=org.apache.log4j.PatternLayout
（其中A1为上面设定的输出位置，我使用的是ConsoleAppender）

下面是我完整的 log4j.properties

# Set root logger level to DEBUG and its only appender to A1.

log4j.rootLogger=INFO,A1

# A1 is set to be a ConsoleAppender.

log4j.appender.A1=org.apache.log4j.ConsoleAppender

# A1 uses PatternLayout.

log4j.appender.A1.layout=org.apache.log4j.PatternLayout

log4j.appender.A1.layout.ConversionPattern=%d{yy-MM-dd hh:mm} %p [%c] - %m%n

输出的样式如下

09-05-07 10:23 INFO message

