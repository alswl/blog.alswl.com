

由于工作中需要使用Dephi，而此之前我对Delphi仅限于听过而已，所以我要在极短的时间内学会一门新的语言。这对我来
说是很有挑战性，也到了证明我以前反复强调"语法不是问题，语言才是跨度"的时候。我需要掌握的是Delphi基本使用和IDE工具使用。我认为，在熟悉C/Java
/.NET的基础上快速掌握一门从未接触过的语言，并非不可完成的任务。

在学习这门未知的语言之前，首先要知道自己学习的是什么东西，框架如何，用来开发哪些类型应用，IDE的情况，下面给出一些简
单解释。

[Pascal](http://zh.wikipedia.org/zh-cn/Pascal)
[Delphi](http://zh.wikipedia.org/zh-cn/Delphi) (via wiki)

**我的主要教程**（电子档）有如下几本：

《[Pascal基本教程](http://www.tanghu.net/gr/zhoukun/pascal/pascal5.htm)》([Google快照](http://203.208.39.132/search?q=cache:EEjmkPEDtpQJ:www.tanghu.net/gr/zhoukun/pascal/pascal5.htm+pascal%E6%95%99%E7%A8%8B&cd=1&hl=zh-
CN&ct=clnk&gl=cn&st_usg=ALhdy2-n00UsziHbgXqjlScPI4vUI2jwTw))

下午在手机还能访问，晚上就无法访问了，只能从Google快照获取内容。教程中文字描述极为简单，通篇只有一页，但是浓缩的精华，对于我这种快速学习很有帮助。

《[PASCAL语言培训教程](http://www.gougou.com/search?search=PASCAL%E8%AF%AD%E8%A8%80%E
5%9F%B9%E8%AE%AD%E6%95%99%E7%A8%8B&id=1)》(via 狗狗)

这个教程是信息学用到的，其中有一些例子和详细的截图（Turbo Pascal下），作为对上面Pascal基本教程的补充还是很不错的。

《[Delphi程序设计基础》-李文池-电子教案](http://www.gougou.com/search?sear
ch=Delphi%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E5%9F%BA%E7%A1%80%E3%80%8B-%E6%9
D%8E%E6%96%87%E6%B1%A0-%E7%94%B5%E5%AD%90%E6%95%99%E6%A1%88&restype=-1&id=1000
0001&ty=0&pattern=0&xmp=0)》(via 狗狗)

这是一套PPT，应该是一本教材的原装课件，内容很丰富，很适合快速学习，Delphi 7。

《[delphi经典编程入门](http://www.gougou.com/search?search=delphi%E7%BB%8F%E5%85%B8%E
7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8&restype=-1&id=10000001&ty=0&pattern=0&xmp=0
)》(via 狗狗)

这是我今天找的十余本Delphi教程中最完整的，内容比较全，缺点是没有截图，版本是Delphi 2.0 -_-!

我并没有去买Dephi的书，我在China-Pub上找了一会，没找到那种大家都非常认可的教材书，罢了，就电子版上阵吧。

**Delphi的学习曲线**

一、Pascal 程序设计基础

 1.1 常量和变量

 1.2 数据类型

 1.3 语句

 1.4 过程和函数

 1.5 程序和单元

 1.6 嵌入式汇编


二、OO（面向对象了）程序设计

 2.1 基本概念

 2.2 类

 2.3 方法

 2.4 继承和多态性

 2.5 对象和VRE

 2.6 属性

 2.7 消息

 2.8 异常处理

 2.9 VRE的实现

所以第一步熟悉Pascal语法，第二步熟悉Dephi框架，第三步有时间再熟悉高阶内容，如网络编程，COM，VRE等

**最后来一个Delphi的Hello World!**
    
    program Project1;

{$APPTYPE CONSOLE}

uses

SysUtils;

var

s : String;

begin

Writeln('Hello world!');

Readln(s);

end.

OK，今天花了2个小时熟悉了Delphi和Pascal，才收获这么多，明天得继续努力了。


