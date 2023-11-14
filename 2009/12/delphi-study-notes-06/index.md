

我的博客所在的江西服务器需要服务器搬迁，所以这两天博客无法访问，看到404错误的童鞋们对不起拉…

## 几个概念：Owner/Parent/Sender/Self

Owner/Parent的字面意义都有点拥有者的意思，一个Button的Owner和Parent很有可能都是Form，但实际上这两个概念是没有关系的。

Owner和Parent的区别：Parent对应组件的视觉容器而不是拥有者，比如一个`RadioGroup`是`RadioButton`的Parent；Ow
ner对应组件的拥有者。尽管Parent和Owner很多时候都是同一个对象，但是还是需要严格区分的。

Sender代表的是触发事件的组件，有了Sender参数，能够使用多个组件配合使用。在代码中可以使用`(Sender as
TButton).Caption`这种语句来转换`TObject`类型。

Self呢，相当于C++/Java中的`this`，指向当前对象，代表自身的意思。没有太多可讲的，我觉得如果要获取某个属性，前面加上Self.是个好习惯。

这几个关键字能够加深对面向对象的理解，在VCL编程中，也是必须掌握的。

## VCL编程感观

VCL全程Visual Component Library（可视组件库），称为VCL编程不知道合适不合适，VCL是一个框架，包含相当丰富的控件，多到让我咂舌
，长长的控件面板还要拖拉好几次才能看到全部。Delphi之所以强大，就是因为这个VCL。

比如文件操作，有很多基于传统Pascal的方法，`FileExists()/DirectoryExists()/RenamFile()`这种原始的方法，完全
不是基于面向对象思想的。就我这几天的感觉，应该使用`TFileStream`这样的类，官方描述是"Use TFileStream to access the
information in disk files. TFileStream will open a named file and provide
methods to read from or write to it. "，"用来读取硬盘上文件的信息，打开一个文件并确定一种操作文件读写的权限"，用这个
类来操作文件就类似于Java那种方法，而不是C那样的大量繁琐的函数。这个类的被设计用来读取文件，而不擅长操作文件和文件夹。在这一点上我还是比较喜欢Java中
`File`的操作方法。

我一直把Delphi和C#进行对比，这两者都是出自于同一人。Delphi和C#很多编程思想和结构都非常类似。C#中窗体有`.cs`和`.desiner.cs
`，Delphi中有`.dfm`和`.pas`。我对Delphi的一点点不喜欢是觉得他继承了太多的Pascal的东西，导致有时候不容易对设计进行思维转换。D
elphi最强大的在于VCL，可惜现在Borland都被收购，Delphi成为一门强大而不够活力的语言。

## CnPack包

我之前使用的[DELPHI 7 绿色终结版](http://www.xdowns.com/soft/38/121/2008/Soft_42203.html)
被我换成了原装的之后，发现之前很多功能消失了。检查后发现，原来DELPHI 7 绿色终结版集成了CnPack这一套组件包。

CnPack 是由互联网上一群中国程序员开发的开放源码的自由软件项目，该项目组成立于2002年。当前该项目组的主要的工作成果包括 CnPack
组件包、CnWizards 专家包以及 CVSTracNT 错误跟踪系统等。CnPack 开发团队目前规模有 200 余人，并且还在不断发展壮大中。

下载CnPack，[传送门](http://www.cnpack.org/)

## Delphi的异常处理

这篇文章是这几天本地保存的内容合成的，所以有点乱。下面是我学Delphi基础的最后一块内容，异常处理，代码如下。

    
    program P1;
    {try...catch, try...finally的使用}

{$APPTYPE CONSOLE}

uses

SysUtils;

{创建异常MyErr,并使用Raise抛出}

procedure RaiseTest();

var

MyErr : Exception;

begin

MyErr := Exception.Create('My Error');

Writeln(MyErr.Message);

Raise MyErr;

MyErr.Free;

end;

{使用try...except来捕获错误，使用on...do

来判断错误类型

加入try...finally(这个语法结构真失败，无法

嵌套try...except...finally)}

procedure TryExceptTest();

var

i, j, k : Integer;

begin

Readln(i, j);

try

try

k := i div j;

Writeln(k);

except

on E : EInOutError do

Writeln('Input Error! Message: ', E.Message);

on E : EdivByZero do

Writeln('/ Error! Message: ', E.Message);

end;

finally

Writeln('in finally.');

end;

end;

begin

//RaiseTest();

TryExceptTest();

Readln;

end.

前天在把[Mp3Lrc](http://log4d.com/2009/05/the-executable-file-
mp3lrc)这个小工具写成Delphi的GUI版本，由于昨天课程设计提前答辩，所以没能完成，争取今天晚上弄好。


