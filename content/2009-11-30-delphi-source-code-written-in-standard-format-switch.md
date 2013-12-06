Title: Delphi源程序格式书写规范【转】
Author: alswl
Slug: delphi-source-code-written-in-standard-format-switch
Date: 2009-11-30 00:00:00
Tags: 
Category: Delphi编程
Summary: 

话说我不喜欢转帖，可是看到实在好的东西又想留下来，真矛盾。为此，我凡是所有转的帖子都在标题上注明转帖，大家如果不感兴趣，可以直接略过。

下面的这篇文章出处：[百度_delphi吧_Delphi 源程序格式书写规范](http://tieba.baidu.com/f?kz=84767888)

文章很长，我看了很长时间，好的代码风格将是一个程序员终身受益。文中的一些关于Tab/空格问题我完全同意，不过在个别地方，比如变量名定义上持中立意见，我觉得每
个人、每个公司的编码风格还是会有出入的。总体来说，这篇文章作为参考是很不错的。

我整理了半小时，将原来的一个p分成3级h2/h3/p，呃，方便阅读吧。

**********原文送上**********

感谢&nbsp_place_holder;tianhaiyise&nbsp_place_holder;提供的来自&nbsp_place_holder;[ht
tp://www.delphiforums.com/](http://www.delphiforums.com/)&nbsp_place_holder;的译
本

## 1.规范简介

本规范主要规定Delphi源程序在书写过程中所应遵循的规则及注意事项。编写该规范的目的是使公司软件开发人员的源代码书写习惯保持一致。这样做可以使每一个组员都
可以理解其它组员的代码，以便于源代码的二次开发记忆系统的维护。

## 2.一般格式规范

### 2.1缩进

缩进就是在当源程序的级改变时为增加可读性而露出的两个空格。缩进的规则为每一级缩进两个空格。不准许使用Tab。因为Tab会因为用户所作的设 置不同而产生不同的
效果。当遇到begin&nbsp_place_holder;或进入判断、循环、异常处理、with语句、记录类型声明、类声明等的时侯增加一级，&nbsp_pl
ace_holder;当遇到end或退出判 断、循环、异常处理、with语句、记录类型声明、类声明等的时侯减少一级。例如：

if&nbsp_place_holder;TmpInt&nbsp_place_holder;<>&nbsp_place_holder;100&nbsp_pl
ace_holder;then

&nbsp_place_holder;&nbsp_place_holder;TmpInt&nbsp_place_holder;:=&nbsp_place_h
older;100;

### 2.2&nbsp_place_holder;Begin..End

begin语句和end语句在源程序中要独占一行，例如:

for&nbsp_place_holder;I&nbsp_place_holder;:=&nbsp_place_holder;0&nbsp_place_ho
lder;to&nbsp_place_holder;10&nbsp_place_holder;do&nbsp_place_holder;begin&nbsp
_place_holder;//不正确的用法

end;

for&nbsp_place_holder;I&nbsp_place_holder;:=&nbsp_place_holder;0&nbsp_place_ho
lder;to&nbsp_place_holder;10&nbsp_place_holder;do&nbsp_place_holder;&nbsp_plac
e_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_
holder;&nbsp_place_holder;&nbsp_place_holder;//正确的用法

begin

end;

### 2.3空格

在操作符及逻辑判断符号的两端添加空格，例如：I&nbsp_place_holder;:=&nbsp_place_holder;I&nbsp_place_ho
lder;+&nbsp_place_holder;1;，a&nbsp_place_holder;and&nbsp_place_holder;b&nbsp_p
lace_holder;等，但添加括号时不需要空格。例如：if&nbsp_place_holder;(&nbsp_place_holder;a&nbsp_p
lace_holder;>&nbsp_place_holder;b&nbsp_place_holder;)&nbsp_place_holder;then&n
bsp_place_holder;&nbsp_place_holder;//错误的用法

If&nbsp_place_holder;(a&nbsp_place_holder;>&nbsp_place_holder;b)&nbsp_place_ho
lder;then&nbsp_place_holder;//正确的用法

又例如：procedure&nbsp_place_holder;Test(Param1:&nbsp_place_holder;integer;&nbsp_p
lace_holder;Param3:&nbsp_place_holder;string);

## 3.&nbsp_place_holder;Object&nbsp_place_holder;Pascal语法书写格式规范

### 3.1保留字

Object&nbsp_place_holder;Pascal&nbsp_place_holder;语言的保留字或关键词应全部使用小写字母。

### 3.2过程和函数

#### 3.2.1命名及格式

过程和函数的名称应全部使用有意义的单词组成，并且所有单词的第一个字母应该使用大写字母。例如：

procedure&nbsp_place_holder;formatharddisk;//不正确的命名

procedure&nbsp_place_holder;FormatHardDisk;//正确的命名

设置变量内容的过程和函数，应使用Set作为前缀，例如：

procedure&nbsp_place_holder;SetUserName;

读取变量内容的过程和函数，应使用Get作为前缀，例如：

function&nbsp_place_holder;GetUserName:&nbsp_place_holder;string;

#### 3.2.2&nbsp_place_holder;过程和函数的参数

3.2.2.1命名

统一类型的参数写在同一句中:

procedure&nbsp_place_holder;Foo(Param1,&nbsp_place_holder;Param2,&nbsp_place_h
older;Param3:&nbsp_place_holder;Integer;&nbsp_place_holder;Param4:&nbsp_place_
holder;string);

3.2.2.2命名

所有参数必须是有意义的；并且当参数名称和其它属性名称重了的时候，加一个前缀'A',&nbsp_place_holder;例如：

procedure&nbsp_place_holder;SomeProc(AUserName:&nbsp_place_holder;string;&nbsp
_place_holder;AUserAge:&nbsp_place_holder;integer);

3.2.2.3命名冲突

当使用的两个unit中包括一个重名的函数或过程时,&nbsp_place_holder;那幺当你引用这一函数或过程时，将执行在use&nbsp_place_
holder;子句中后声明的那个unit中的函数或过程。为了避免这种'uses-clause-
dependent'需要在引用函数或过程时，写完整函数或过程的出处。例如：

SysUtils.FindClose(SR);

Windows.FindClose(Handle);

### 3.3&nbsp_place_holder;变量

#### 3.3.1&nbsp_place_holder;变量命名及格式

首先所有变量必须起有意义的名字，使其它组员可以很容易读懂变量所代表的意义，变量命名可以采用同义的英文命名，可使用几个英文单词，但每一单词的首字母必须大写。例
如：

var

&nbsp_place_holder;&nbsp_place_holder;WriteFormat:：string；

同时对于一些特定类型可采用一定的简写如下：

指针类型

&nbsp_place_holder;P

&nbsp_place_holder;

纪录类型

&nbsp_place_holder;Rec

&nbsp_place_holder;

数组类型

&nbsp_place_holder;Arr

&nbsp_place_holder;

类

&nbsp_place_holder;Class

&nbsp_place_holder;

循环控制变量通常使用单一的字符如：i,&nbsp_place_holder;j,&nbsp_place_holder;或&nbsp_place_holder
;k。&nbsp_place_holder;另外使用一个有意义的名字例如：UserIndex&nbsp_place_holder;，也是准许的。

#### 3.3.2&nbsp_place_holder;局部变量

在过程中使用局部变量遵循所有其它变量的命名规则。

#### 3.3.3&nbsp_place_holder;全局变量

尽量不使用全局变量，如必须使用全局变量则必须加前缀'g'，同时应在变量名称中体现变量的类型。例如：

&nbsp_place_holder;&nbsp_place_holder;gprecUserCount:&nbsp_place_holder;point;
//名称为UserCount的全局变量,其类型为指向一结构的指针

但是在模块内部可以使用全局变量。所有模块内全局变量必须用'F'为前缀。如果几个模块之间需要进行资料交换，则需要通过声明属性的方法来实现。例如：

type

&nbsp_place_holder;&nbsp_place_holder;TFormOverdraftReturn&nbsp_place_holder;=
&nbsp_place_holder;class(TForm)

&nbsp_place_holder;&nbsp_place_holder;private

{&nbsp_place_holder;Private&nbsp_place_holder;declarations&nbsp_place_holder;}

FuserName:&nbsp_place_holder;string;

FuserCount:&nbsp_place_holder;Integer;

Procedure&nbsp_place_holder;SetUserName(Value:&nbsp_place_holder;string);

Function&nbsp_place_holder;GetUserName:&nbsp_place_holder;string;

&nbsp_place_holder;&nbsp_place_holder;public

{&nbsp_place_holder;Public&nbsp_place_holder;declarations&nbsp_place_holder;}

property&nbsp_place_holder;UserName:&nbsp_place_holder;string&nbsp_place_holde
r;read&nbsp_place_holder;GetUserName&nbsp_place_holder;write&nbsp_place_holder
;SetUserName;

property&nbsp_place_holder;UserCount:&nbsp_place_holder;Integer&nbsp_place_hol
der;read&nbsp_place_holder;FuserCount&nbsp_place_holder;write&nbsp_place_holde
r;FuserCount;

&nbsp_place_holder;&nbsp_place_holder;end;

### 3.4类型

#### 3.4.1&nbsp_place_holder;大小写协议

保留字的类型名称必须全部小写。Win32&nbsp_place_holder;API&nbsp_place_holder;的类型通常全部大写，对于其它类型则
首字母大写，其余字母小写，例如：

var

&nbsp_place_holder;&nbsp_place_holder;MyString:&nbsp_place_holder;string;&nbsp
_place_holder;&nbsp_place_holder;&nbsp_place_holder;//&nbsp_place_holder;reser
ved&nbsp_place_holder;word

&nbsp_place_holder;&nbsp_place_holder;WindowHandle:&nbsp_place_holder;HWND;&nb
sp_place_holder;//&nbsp_place_holder;Win32&nbsp_place_holder;API&nbsp_place_ho
lder;type

&nbsp_place_holder;&nbsp_place_holder;I:&nbsp_place_holder;Integer;&nbsp_place
_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;//&nbsp_place
_holder;type&nbsp_place_holder;identifier&nbsp_place_holder;introduced&nbsp_pl
ace_holder;in&nbsp_place_holder;System&nbsp_place_holder;unit

#### 3.4.2&nbsp_place_holder;浮点类型

尽量不使用&nbsp_place_holder;Real&nbsp_place_holder;类型，他只是为了和旧的Pascal代码兼容，尽量使用Doubl
e&nbsp_place_holder;类型。Double&nbsp_place_holder;类型是对处理器和数据总线做过 最优化的并且是IEEE定义的标
准数据结构。当数值超出Double的范围时，使用Extended&nbsp_place_holder;。但Extended不被Jave支持。但使用其它
语言编写的DLL时可能会使用Single&nbsp_place_holder;类型。

#### 3.4.3&nbsp_place_holder;枚举类型

枚举类型的名字必须有意义并且类型的名字之前要加前缀'T'。枚举类型的内容的名字必须包含枚举类型名称的简写，例如：

TSongType&nbsp_place_holder;=&nbsp_place_holder;(stRock,&nbsp_place_holder;stC
lassical,&nbsp_place_holder;stCountry,&nbsp_place_holder;stAlternative,&nbsp_p
lace_holder;stHeavyMetal,&nbsp_place_holder;stRB);

#### 3.4.4&nbsp_place_holder;数组类型

数组类型的名字必须有意义并且类型的名字之前要加前缀'T'。如果声明一个指向数组类型的指针必须在该类型的名字之前加前缀'P'，例如：

type

&nbsp_place_holder;&nbsp_place_holder;PCycleArray&nbsp_place_holder;=&nbsp_pla
ce_holder;^TCycleArray;

&nbsp_place_holder;&nbsp_place_holder;TCycleArray&nbsp_place_holder;=&nbsp_pla
ce_holder;array[1..100]&nbsp_place_holder;of&nbsp_place_holder;integer;

##### 3.4.5记录类型

记录类型的名字必须有意义并且类型的名字之前要加前缀'T'。如果声明一个指向数组类型的指针必须在该类型的名字之前加前缀'P'，例如：

type

&nbsp_place_holder;&nbsp_place_holder;PEmployee&nbsp_place_holder;=&nbsp_place
_holder;^TEmployee;

&nbsp_place_holder;&nbsp_place_holder;TEmployee&nbsp_place_holder;=&nbsp_place
_holder;record

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;Em
ployeeName:&nbsp_place_holder;string

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;Em
ployeeRate:&nbsp_place_holder;Double;

&nbsp_place_holder;&nbsp_place_holder;end;

### 3.5类

##### 3.5.1&nbsp_place_holder;命名及格式

类的名字必须有意义并且类型的名字之前要加前缀'T'。例如：

type

&nbsp_place_holder;TCustomer&nbsp_place_holder;=&nbsp_place_holder;class(TObje
ct)

类实例的名字通常是去掉'T'的类的名字。例如：

var

&nbsp_place_holder;Customer:&nbsp_place_holder;TCustomer;

##### 3.5.2&nbsp_place_holder;类中的变量

3.5.2.1命名及格式

类的名字必须有意义并且类型的名字之前要加前缀'F'。所有的变量必须是四有的。如果需要从外部访问此变量则需要声明一属性

#### 3.5.3&nbsp_place_holder;方法

3.5.3.1命名及格式

同函数和过程的命名及格式。

3.5.3.2&nbsp_place_holder;属性访问方法

所有的属性访问方法必须出现在private&nbsp_place_holder;或&nbsp_place_holder;protected&nbsp_pla
ce_holder;中。属性访问方法的命名同函数和过程的命名另外读方法 (reader&nbsp_place_holder;method)必须使用前缀'Ge
t'.&nbsp_place_holder;写方法(writer&nbsp_place_holder;method)必须使用前缀'Set'。写方法的参数必须
命名为 'Value'，其类型同所要写的属性相一致。例如：

TSomeClass&nbsp_place_holder;=&nbsp_place_holder;class(TObject)

private

&nbsp_place_holder;FSomeField:&nbsp_place_holder;Integer;

protected

&nbsp_place_holder;function&nbsp_place_holder;GetSomeField:&nbsp_place_holder;
Integer;

&nbsp_place_holder;procedure&nbsp_place_holder;SetSomeField(&nbsp_place_holder
;Value:&nbsp_place_holder;Integer);

public

&nbsp_place_holder;property&nbsp_place_holder;SomeField:&nbsp_place_holder;Int
eger&nbsp_place_holder;read&nbsp_place_holder;GetSomeField&nbsp_place_holder;w
rite&nbsp_place_holder;SetSomeField;

end;

### 3.6属性

#### 3.6.1&nbsp_place_holder;命名及格式

同其用操作的，出去前缀'F'的类的变量的名称相一致&nbsp_place_holder;。

### 3.7文件

#### 3.7.1项目文件

3.7.1.1项目目录结构

程序主目录--Bin（应用程序所在路径）

&nbsp_place_holder;-Db（本地数据库所在路径）

&nbsp_place_holder;-Doc（文档所在路径）

&nbsp_place_holder;-Hlp（帮助文件所在路径）

&nbsp_place_holder;-Backup（备份路径）

&nbsp_place_holder;-Tmp（临时文件路径）

3.7.1.2命名

项目文件必须使用一个有意义的名字。例如：&nbsp_place_holder;Delphi中系统信息的项目文件被命名为&nbsp_place_holder;
SysInfo.dpr。

#### 3.7.2&nbsp_place_holder;Form&nbsp_place_holder;文件

3.7.2.1命名

同Form的名称相一致：例如：Form的名称为FormMain则Form文件的名称就为FormMain.frm。

####
3.7.3&nbsp_place_holder;Data&nbsp_place_holder;Module&nbsp_place_holder;文件

3.7.3.1命名

data&nbsp_place_holder;module文件的命名应该有意义，并且使用'DM'作为前缀。例如：&nbsp_place_holder;用户d
ata&nbsp_place_holder;module&nbsp_place_holder;被命名为'DMCustomers.dfm'。

#### 3.7.4&nbsp_place_holder;Remote&nbsp_place_holder;Data&nbsp_place_holder;M
odule&nbsp_place_holder;文件

3.7.4.1&nbsp_place_holder;命名

remote&nbsp_place_holder;data&nbsp_place_holder;module文件的命名应该有意义，并且使用'RDM'作为前缀
。例如：用户remote&nbsp_place_holder;data&nbsp_place_holder;module&nbsp_place_holder
;被命名为'RDMCustomers.dfm'。

#### 3.7.5&nbsp_place_holder;Unit文件

3.7.5.1普通&nbsp_place_holder;Unit

3.7.5.1.1&nbsp_place_holder;Unit文件命名

unit文件的命名应该有意义，并且使用'unit'作为前缀。例如：&nbsp_place_holder;通用unit&nbsp_place_holder;被
命名为'UnitGeneral'。

3.7.5.2&nbsp_place_holder;Form&nbsp_place_holder;Units

3.7.5.2.1命名

Form&nbsp_place_holder;unit&nbsp_place_holder;文件的名字必须和Form的名称保持一致。例如：主窗体叫FormM
ain.pas&nbsp_place_holder;则Form&nbsp_place_holder;Unit文件的名字为：UnitFormMain。

3.7.5.3&nbsp_place_holder;Data&nbsp_place_holder;Module&nbsp_place_holder;Unit
s

3.7.5.3.1命名

Data&nbsp_place_holder;Module&nbsp_place_holder;unit&nbsp_place_holder;文件的名字必须
和Data&nbsp_place_holder;Module的名称保持一致。例如：主Data&nbsp_place_holder;Module叫DMMain
.pas&nbsp_place_holder;则Data&nbsp_place_holder;Module&nbsp_place_holder;Unit文件
的名字为：UnitDMMain。

3.7.5.4&nbsp_place_holder;文件头

在所有文件的头部应写上此文件的用途，作者，日期及输入和输出。例如：

{

修改日期：

作者：

用途：

本模块结构组成：

}

#### 3.7.6&nbsp_place_holder;Forms和Data&nbsp_place_holder;Modules&nbsp_place_h
older;Forms

3.7.6.1&nbsp_place_holder;Form类

1.&nbsp_place_holder;Form类命名标准

Forms类的命名应该有意义，并且使用'TForm'作为前缀。例如：&nbsp_place_holder;About&nbsp_place_holder;F
orm类的名字为:

TAboutForm&nbsp_place_holder;=&nbsp_place_holder;class(TForm)

主窗体的名字为

TMainForm&nbsp_place_holder;=&nbsp_place_holder;class(TForm)

2.&nbsp_place_holder;Form类实例的命名标准

Form&nbsp_place_holder;的类实例的名字应同期掉'T'的Form类的名字相一致。例如：

Type&nbsp_place_holder;Name

&nbsp_place_holder;Instance&nbsp_place_holder;Name

&nbsp_place_holder;

TaboutForm

&nbsp_place_holder;AboutForm

&nbsp_place_holder;

TmainForm

&nbsp_place_holder;MainForm

&nbsp_place_holder;

TCustomerEntryForm

&nbsp_place_holder;CustomerEntryForm

&nbsp_place_holder;

&nbsp_place_holder;

3.7.6.2&nbsp_place_holder;Data&nbsp_place_holder;Modules&nbsp_place_holder;For
m

3.7.6.2.1.&nbsp_place_holder;Data&nbsp_place_holder;Module&nbsp_place_holder;F
orm&nbsp_place_holder;命名标准

Data&nbsp_place_holder;Modules&nbsp_place_holder;Forms类的命名应该有意义，并且使用'TDM'作为前缀。
例如：

TDMCustomer&nbsp_place_holder;=&nbsp_place_holder;class(TDataModule)

TDMOrders&nbsp_place_holder;=&nbsp_place_holder;class(TDataModule)

3.7.6.2.2.&nbsp_place_holder;Data&nbsp_place_holder;Module&nbsp_place_holder;实
例命名标准

Data&nbsp_place_holder;Module&nbsp_place_holder;Form&nbsp_place_holder;的类实例的名字
应同期掉'T'的Data&nbsp_place_holder;Module&nbsp_place_holder;Form类的名字相一致。例如：

Type&nbsp_place_holder;Name

Instance&nbsp_place_holder;Name

&nbsp_place_holder;

TCustomerDataModule

&nbsp_place_holder;CustomerDataModule

&nbsp_place_holder;

TordersDataModule

&nbsp_place_holder;OrdersDataModule

### 3.8控件

#### 3.8.1&nbsp_place_holder;控件实例的命名

控件的实例应使用去掉'T'该控件类的名称作为前缀，例如：

输入用户姓名的Tedit的名字为：EditUserName。

#### 3.8.2&nbsp_place_holder;控件的简写

控件的名称可使用以下简写，但所用简写于控件名称之间药添加'_'：

3.8.2.1&nbsp_place_holder;Standard&nbsp_place_holder;Tab

mm&nbsp_place_holder;TMainMenu

pm&nbsp_place_holder;TPopupMenu

mmi&nbsp_place_holder;TMainMenuItem

pmi&nbsp_place_holder;TPopupMenuItem

lbl&nbsp_place_holder;TLabel

edt&nbsp_place_holder;TEdit

mem&nbsp_place_holder;TMemo

btn&nbsp_place_holder;TButton

cb&nbsp_place_holder;TCheckBox

rb&nbsp_place_holder;TRadioButton

lb&nbsp_place_holder;TListBox

cb&nbsp_place_holder;TComboBox

scb&nbsp_place_holder;TScrollBar

gb&nbsp_place_holder;TGroupBox

rg&nbsp_place_holder;TRadioGroup

pnl&nbsp_place_holder;TPanel

cl&nbsp_place_holder;TCommandList

3.8.2.2&nbsp_place_holder;Additional&nbsp_place_holder;Tab

bbtn&nbsp_place_holder;TBitBtn

sb&nbsp_place_holder;TSpeedButton

me&nbsp_place_holder;TMaskEdit

sg&nbsp_place_holder;TStringGrid

dg&nbsp_place_holder;TDrawGrid

img&nbsp_place_holder;TImage

shp&nbsp_place_holder;TShape

bvl&nbsp_place_holder;TBevel

sbx&nbsp_place_holder;TScrollBox

clb&nbsp_place_holder;TCheckListbox

spl&nbsp_place_holder;TSplitter

stx&nbsp_place_holder;TStaticText

cht&nbsp_place_holder;TChart

3.8.2.3&nbsp_place_holder;Win32&nbsp_place_holder;Tab

tbc&nbsp_place_holder;TTabControl

pgc&nbsp_place_holder;TPageControl

il&nbsp_place_holder;TImageList

re&nbsp_place_holder;TRichEdit

tbr&nbsp_place_holder;TTrackBar

prb&nbsp_place_holder;TProgressBar

ud&nbsp_place_holder;TUpDown

hk&nbsp_place_holder;THotKey

ani&nbsp_place_holder;TAnimate

dtp&nbsp_place_holder;TDateTimePicker

tv&nbsp_place_holder;TTreeView

lv&nbsp_place_holder;TListView

hdr&nbsp_place_holder;THeaderControl

stb&nbsp_place_holder;TStatusBar

tlb&nbsp_place_holder;TToolBar

clb&nbsp_place_holder;TCoolBar

3.8.2.4&nbsp_place_holder;System&nbsp_place_holder;Tab

tm&nbsp_place_holder;TTimer

pb&nbsp_place_holder;TPaintBox

mp&nbsp_place_holder;TMediaPlayer

olec&nbsp_place_holder;TOleContainer

ddcc&nbsp_place_holder;TDDEClientConv

ddci&nbsp_place_holder;TDDEClientItem

ddsc&nbsp_place_holder;TDDEServerConv

ddsi&nbsp_place_holder;TDDEServerItem

3.8.2.5&nbsp_place_holder;Internet&nbsp_place_holder;Tab

csk&nbsp_place_holder;TClientSocket

ssk&nbsp_place_holder;TServerSocket

wbd&nbsp_place_holder;TWebDispatcher

pp&nbsp_place_holder;TPageProducer

tp&nbsp_place_holder;TQueryTableProducer

dstp&nbsp_place_holder;TDataSetTableProducer

nmdt&nbsp_place_holder;TNMDayTime

nec&nbsp_place_holder;TNMEcho

nf&nbsp_place_holder;TNMFinger

nftp&nbsp_place_holder;TNMFtp

nhttp&nbsp_place_holder;TNMHttp

nMsg&nbsp_place_holder;TNMMsg

nmsg&nbsp_place_holder;TNMMSGServ

nntp&nbsp_place_holder;TNMNNTP

npop&nbsp_place_holder;TNMPop3

nuup&nbsp_place_holder;TNMUUProcessor

smtp&nbsp_place_holder;TNMSMTP

nst&nbsp_place_holder;TNMStrm

nsts&nbsp_place_holder;TNMStrmServ

ntm&nbsp_place_holder;TNMTime

nudp&nbsp_place_holder;TNMUdp

psk&nbsp_place_holder;TPowerSock

ngs&nbsp_place_holder;TNMGeneralServer

html&nbsp_place_holder;THtml

url&nbsp_place_holder;TNMUrl

sml&nbsp_place_holder;TSimpleMail

3.8.2.6&nbsp_place_holder;Data&nbsp_place_holder;Access&nbsp_place_holder;Tab

ds&nbsp_place_holder;TDataSource

tbl&nbsp_place_holder;TTable

qry&nbsp_place_holder;TQuery

sp&nbsp_place_holder;TStoredProc

db&nbsp_place_holder;TDataBase

ssn&nbsp_place_holder;TSession

bm&nbsp_place_holder;TBatchMove

usql&nbsp_place_holder;TUpdateSQL

3.8.2.7&nbsp_place_holder;Data&nbsp_place_holder;Controls&nbsp_place_holder;Ta
b

dbg&nbsp_place_holder;TDBGrid

dbn&nbsp_place_holder;TDBNavigator

dbt&nbsp_place_holder;TDBText

dbe&nbsp_place_holder;TDBEdit

dbm&nbsp_place_holder;TDBMemo

dbi&nbsp_place_holder;TDBImage

dblb&nbsp_place_holder;TDBListBox

dbcb&nbsp_place_holder;TDBComboBox

dbch&nbsp_place_holder;TDBCheckBox

dbrg&nbsp_place_holder;TDBRadioGroup

dbll&nbsp_place_holder;TDBLookupListBox

dblc&nbsp_place_holder;TDBLookupComboBox

dbre&nbsp_place_holder;TDBRichEdit

dbcg&nbsp_place_holder;TDBCtrlGrid

dbch&nbsp_place_holder;TDBChart

3.8.2.8&nbsp_place_holder;Decision&nbsp_place_holder;Cube&nbsp_place_holder;Ta
b

dcb&nbsp_place_holder;TDecisionCube

dcq&nbsp_place_holder;TDecisionQuery

dcs&nbsp_place_holder;TDecisionSource

dcp&nbsp_place_holder;TDecisionPivot

dcg&nbsp_place_holder;TDecisionGrid

dcgr&nbsp_place_holder;TDecisionGraph

3.8.2.9&nbsp_place_holder;QReport&nbsp_place_holder;Tab

qr&nbsp_place_holder;TQuickReport

qrsd&nbsp_place_holder;TQRSubDetail

qrb&nbsp_place_holder;TQRBand

qrcb&nbsp_place_holder;TQRChildBand

qrg&nbsp_place_holder;TQRGroup

qrl&nbsp_place_holder;TQRLabel

qrt&nbsp_place_holder;TQRText

qre&nbsp_place_holder;TQRExpr

qrs&nbsp_place_holder;TQRSysData

qrm&nbsp_place_holder;TQRMemo

qrrt&nbsp_place_holder;TQRRichText

qrdr&nbsp_place_holder;TQRDBRichText

qrsh&nbsp_place_holder;TQRShape

qri&nbsp_place_holder;TQRImage

qrdi&nbsp_place_holder;TQRDBMImage

qrcr&nbsp_place_holder;TQRCompositeReport

qrp&nbsp_place_holder;TQRPreview

qrch&nbsp_place_holder;TQRChart

3.8.2.10&nbsp_place_holder;Dialogs&nbsp_place_holder;Tab

OpenDialog&nbsp_place_holder;TOpenDialog

SaveDialog&nbsp_place_holder;TSaveDialog

OpenPictureDialog&nbsp_place_holder;TOpenPictureDialog

SavePictureDialog&nbsp_place_holder;TSavePictureDialog

FontDialog&nbsp_place_holder;TFontDialog

ColorDialog&nbsp_place_holder;TColorDialog

PrintDialog&nbsp_place_holder;TPrintDialog

PrinterSetupDialog&nbsp_place_holder;TPrintSetupDialog

FindDialog&nbsp_place_holder;TFindDialog

ReplaceDialog&nbsp_place_holder;TReplaceDialog

3.8.2.11&nbsp_place_holder;Win31&nbsp_place_holder;Tab

dbll&nbsp_place_holder;TDBLookupList

dblc&nbsp_place_holder;TDBLookupCombo

ts&nbsp_place_holder;TTabSet

ol&nbsp_place_holder;TOutline

tnb&nbsp_place_holder;TTabbedNoteBook

nb&nbsp_place_holder;TNoteBook

hdr&nbsp_place_holder;THeader

flb&nbsp_place_holder;TFileListBox

dlb&nbsp_place_holder;TDirectoryListBox

dcb&nbsp_place_holder;TDriveComboBox

fcb&nbsp_place_holder;TFilterComboBox

3.8.2.12&nbsp_place_holder;Samples&nbsp_place_holder;Tab

gg&nbsp_place_holder;TGauge

cg&nbsp_place_holder;TColorGrid

spb&nbsp_place_holder;TSpinButton

spe&nbsp_place_holder;TSpinEdit

dol&nbsp_place_holder;TDirectoryOutline

cal&nbsp_place_holder;TCalendar

ibea&nbsp_place_holder;TIBEventAlerter

3.8.2.13&nbsp_place_holder;ActiveX&nbsp_place_holder;Tab

cfx&nbsp_place_holder;TChartFX

vsp&nbsp_place_holder;TVSSpell

f1b&nbsp_place_holder;TF1Book

vtc&nbsp_place_holder;TVTChart

grp&nbsp_place_holder;TGraph

3.8.2.14&nbsp_place_holder;Midas&nbsp_place_holder;Tab

prv&nbsp_place_holder;TProvider

cds&nbsp_place_holder;TClientDataSet

qcds&nbsp_place_holder;TQueryClientDataSet

dcom&nbsp_place_holder;TDCOMConnection

olee&nbsp_place_holder;TOleEnterpriseConnection

sck&nbsp_place_holder;TSocketConnection

rms&nbsp_place_holder;TRemoteServer

mid&nbsp_place_holder;TmidasConnection

## 4．修改规范

&nbsp_place_holder;本规则所做的规定仅适用于已经纳入配置管理的程序。在这类修改中，要求保留修改前的内容、并标识出修改和新增的内容。并在文件
头加入修改人、修改日期、修改说明等必要的信息。

### 4．1修改历史记录

&nbsp_place_holder;对源文件进行经过批准的修改时，修改者应在程序文件头加入修改历史项。在以后的每一次修改时，修改者都必须在该项目中填写下列
信息：

&nbsp_place_holder;修改人

&nbsp_place_holder;修改时间

&nbsp_place_holder;修改原因

&nbsp_place_holder;修改说明即如何修改

### 4．2新增代码行

&nbsp_place_holder;新增代码行的前后应有注释行说明。

&nbsp_place_holder;//&nbsp_place_holder;修改人，修改时间，修改说明

&nbsp_place_holder;新增代码行

&nbsp_place_holder;//&nbsp_place_holder;修改结束

### 4．3删除代码行

&nbsp_place_holder;删除代码行的前后用注释行说明。

&nbsp_place_holder;//修改人，修改时间，修改说明

&nbsp_place_holder;//要删除的代码行（将要删除的语句进行注释）

&nbsp_place_holder;//修改结束

### 4．4修改代码行

&nbsp_place_holder;修改代码行以删除代码行后在新增代码行的方式进行。

&nbsp_place_holder;//修改人，修改时间，修改说明

&nbsp_place_holder;//修改前的代码行

//修改结束

&nbsp_place_holder;//修改后的代码行

&nbsp_place_holder;修改后的代码行

//修改结束

