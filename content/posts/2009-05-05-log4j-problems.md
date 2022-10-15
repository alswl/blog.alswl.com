---
title: "Log4j 遇到的问题"
author: "alswl"
slug: "log4j-problems"
date: "2009-05-05T00:00:00+08:00"
tags: ["工欲善其事必先利其器", "log4j"]
categories: ["efficiency"]
---

今天使用 Log4j 遇到问题是只能打印ERROR级别

最简单的 Log4j.properties 设置

# Set root logger level to DEBUG and its only appender to A1.

log4j.rootLogger=INFO,A1

# A1 is set to be a ConsoleAppender.

log4j.appender.A1=org.apache.log4j.ConsoleAppender

# A1 uses PatternLayout.

log4j.appender.A1.layout=org.apache.log4j.PatternLayout

log4j.appender.logfile.layout.ConversionPattern=%d %p [%c] - %m%n

我老是只能答应ERROR级别，最后发现自己这个工程里面两个设置文件，只有在src文件夹下的才起作用，删除多余的，重新修改src下的就可以起作用了

