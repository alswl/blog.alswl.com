Title: 正则表达式中的零宽断言
Author: alswl
Slug: regular-expressions-in-the-zero-width-assertion
Date: 2010-01-26 00:00:00
Tags: 正则表达式
Category: 综合技术
Summary: 

这文是上个月开始写的，本来想深入的分析一下零宽断言，可惜工作一直忙，现在又要去转战**DWR**...OMG~~

## 起因

将要上线的系统中有一个字符规则："13位的字符串，其中有8位连续数字"，需要用这则表达式对这个字符串进行判断。而我之前对正则的认识仅仅停留在匹配固定的字符上
，对这个问题一筹莫展。

这时候热心的小邪出现了，我在他的博客 [邪罗刹的菠萝阁](http://www.evlos.org)
留下这个[问题](http://www.evlos.org/2010/01/05/use-regex-to-clear-the-mix-of-tag-
img/#comment-5968)

![](http://upload-log4d.qiniudn.com/2010/01/alswl_ask.jpg)

小邪很热心的撰写了一篇文章给出回答：[ 一个杯具和一个洗具与最近学习手记 :
邪罗刹的菠萝阁](http://www.evlos.org/2010/01/07/a-cuptool-and-a-washtool)。

## 解答

核心字符串如下： '/^(?!(.*?d){9,})(?!(.*?D){6,}).{13}$/';

小邪的文章给了很详细的解答，比我自己解释要好得多～我就索性copy过来，如下：

> > 小邪是这个样子解答的，首先两边的斜杠是 Perl 正则式的要求。

> 然后两边的 ^ 和 $ 用来表示对应的是字符串的开始和结束。

> 接着` .{13}`，. 表示除了换行以外的所有字符，`13` 规定了匹配长度。

>

> > 我们这里前面用了两次零宽断言，第一次，`(?!exp) `这里的 exp 是 `(.*?d){9,}`。

> 表示数字的个数大于等于 9，零宽断言把它反过来就是数字的个数小于 9。

> 第二次 exp 是` (.*?D){6,}` 表示非数字大于等于 6 个以上。

> 即表示非数字的个数大于等于 6，把它反过来就是非数字的个数小于 6。

>

> > 而这里` .* `表示` ?d` 和 `?D `的前面可能有零次或更多次的其他字符。

> 而这里的 `? `表示这段连续的字符会重复零次或一次。

### Python下的实现和测试代码

    
    import re

def fun(p, datas):

for data in datas:

print p.match(data)

if __name__ == '__main__':

p = re.compile(r'^(?!(.*?d){9,})(?!(.*?D){6,}).{13}$');

datas = ['asss13336644ss', 'aas15151515ss', 'aa15151515sss',

'aa15151515ss1', 'aa15151515ss11', 'aa151515151ss',

'aa15151511ssss']

fun(p, datas)

恩，问题解决了，不过，如果想把零宽断言彻底搞清楚，还需要深入学习一下～

## 深入零宽断言

[正则表达式的零宽断言的一个小应用 - 楼兰之风... - 博客园

](http://www.cnblogs.com/xiehuiqi220/archive/2009/02/06/1385481.html)

[正则表达式--零宽断言 - panhf2003的专栏 - CSDN博客

](http://blog.csdn.net/panhf2003/archive/2008/11/19/3337163.aspx)

[正则表达式30分钟入门教程

](http://deerchao.net/tutorials/regex/regex.htm)

[Python正则表达式操作指南 - Ubuntu中文](http://wiki.ubuntu.org.cn/Python%E6%AD%A3%E5%88%9
9%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97#.E5.8F.8D.E6.
96.9C.E6.9D.A0.E7.9A.84.E9.BA.BB.E7.83.A6)

