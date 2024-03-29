---
title: "正则表达式抓捕替换"
author: "alswl"
slug: "regex-group-catch"
date: "2011-01-19T00:00:00+08:00"
tags: ["editplus", "notepad++", "vim", "visualstudio", "正则表达式", "regex"]
categories: ["coding"]
---

## 问题情境

需要将RDL报表里的GetComment( Parameters!F0001.Value , Parameters!F0002.Value
,"total", Parameters!Language.Value)函数修改为GetCommentForComment(
Parameters!F0001.Value , Parameters!F0002.Value ,"total",
Parameters!Language.Value, "ReportConnection0107")。

## 思路

使用正则表达式里面的分组进行抓获，再用1将中间固定的参数取出，组成新的字符串。

### Vim实现

%s/GetComment(((s*w+!w+.w+s*,){2}s*"w+"s*,s*w+!w+.w+s*))/GetCommentForReport(1
, "ReportConnection0107")/gc

解释：%为全局替换，s为替换。后面则是表达式，和正则表达式差不多，注意是*不需要转义，+ 和 .需要转义，最后的g代表当前行替换，c代表每次替换需要确认。

目标表达式中有1，代表抓获的第一个字符串，多个字符串抓获则依次往下排列。 表示原始字符串。

### NotePad++/EditPlus实现

GetComment(( *[a-zA-Z0-9]+![a-zA-Z0-9]+.[a-zA-Z0-9]+ *,
*[a-zA-Z0-9]+![a-zA-Z0-9]+.[a-zA-Z0-9]+ *, *"[a-zA-Z0-9]+" *,
*[a-zA-Z0-9]+![a-zA-Z0-9]+.[a-zA-Z0-9]+ *))

替换为GetCommentForReport(1, "ReportConnection0107")

解释：不知道为何，我无法使用ws匹配文字和空格，只能使用[a-zA-Z0-9]表示（完整的是[a-zA-Z0-9_]）w，用空格表示s。

### VisualStudio

由于RDL开发必然使用VisualStudio，所以用VS替换更方便。

GetComment({ *[a-zA-Z0-9]+![a-zA-Z0-9]+.[a-zA-Z0-9]+ *,
*[a-zA-Z0-9]+![a-zA-Z0-9]+.[a-zA-Z0-9]+ *, *"[a-zA-Z0-9]+" *,
*[a-zA-Z0-9]+![a-zA-Z0-9]+.[a-zA-Z0-9]+ *})

依旧替换为GetCommentForReport(1, "ReportConnection0107")

解释：VS除了NotePad++/EditPlus的问题外，还有一个严重的问题就是他抓取的不是分组()，而是抓获的花括号{}抓捕的字符串，官方的称呼叫做"带
标记的表达式"，详情可以参考[MSDN正则表达式 (Visual Studio)](http://msdn.microsoft.com/zh-cn/library/2k3te2cs.aspx)。

## PS

所以咯，Vimer，你懂的~

