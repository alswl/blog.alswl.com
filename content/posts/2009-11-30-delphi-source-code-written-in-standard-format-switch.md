---
title: "Delphi源程序格式书写规范【转】"
author: "alswl"
slug: "delphi-source-code-written-in-standard-format-switch"
date: "2009-11-30T00:00:00+08:00"
tags: ["delphi"]
categories: ["coding"]
---

话说我不喜欢转帖，可是看到实在好的东西又想留下来，真矛盾。为此，我凡是所有转的帖子都在标题上注明转帖，大家如果不感兴趣，可以直接略过。

下面的这篇文章出处：[百度_delphi吧_Delphi 源程序格式书写规范](http://tieba.baidu.com/f?kz=84767888)

文章很长，我看了很长时间，好的代码风格将是一个程序员终身受益。文中的一些关于Tab/空格问题我完全同意，不过在个别地方，比如变量名定义上持中立意见，我觉得每
个人、每个公司的编码风格还是会有出入的。总体来说，这篇文章作为参考是很不错的。

我整理了半小时，将原来的一个p分成3级h2/h3/p，呃，方便阅读吧。

**********原文送上**********

感谢tianhaiyise提供的来自[ht
tp://www.delphiforums.com/](http://www.delphiforums.com/)的译
本

## 1.规范简介

本规范主要规定Delphi源程序在书写过程中所应遵循的规则及注意事项。编写该规范的目的是使公司软件开发人员的源代码书写习惯保持一致。这样做可以使每一个组员都
可以理解其它组员的代码，以便于源代码的二次开发记忆系统的维护。

## 2.一般格式规范

### 2.1缩进

缩进就是在当源程序的级改变时为增加可读性而露出的两个空格。缩进的规则为每一级缩进两个空格。不准许使用Tab。因为Tab会因为用户所作的设 置不同而产生不同的
效果。当遇到begin或进入判断、循环、异常处理、with语句、记录类型声明、类声明等的时侯增加一级，&nbsp_pl
ace_holder;当遇到end或退出判 断、循环、异常处理、with语句、记录类型声明、类声明等的时侯减少一级。例如：

ifTmpInt<>100&nbsp_pl
ace_holder;then

TmpInt:=&nbsp_place_h
older;100;

### 2.2Begin..End

begin语句和end语句在源程序中要独占一行，例如:

forI:=0&nbsp_place_ho
lder;to10dobegin&nbsp
_place_holder;//不正确的用法

end;

forI:=0&nbsp_place_ho
lder;to10do&nbsp_plac
e_holder;&nbsp_place_
holder;//正确的用法

begin

end;

### 2.3空格

在操作符及逻辑判断符号的两端添加空格，例如：I:=I&nbsp_place_ho
lder;+1;，aandb&nbsp_p
lace_holder;等，但添加括号时不需要空格。例如：if(a&nbsp_p
lace_holder;>b)then&n
bsp_place_holder;//错误的用法

If(a>b)&nbsp_place_ho
lder;then//正确的用法

又例如：procedureTest(Param1:integer;&nbsp_p
lace_holder;Param3:string);

## 3.ObjectPascal语法书写格式规范

### 3.1保留字

ObjectPascal语言的保留字或关键词应全部使用小写字母。

### 3.2过程和函数

#### 3.2.1命名及格式

过程和函数的名称应全部使用有意义的单词组成，并且所有单词的第一个字母应该使用大写字母。例如：

procedureformatharddisk;//不正确的命名

procedureFormatHardDisk;//正确的命名

设置变量内容的过程和函数，应使用Set作为前缀，例如：

procedureSetUserName;

读取变量内容的过程和函数，应使用Get作为前缀，例如：

functionGetUserName:string;

#### 3.2.2过程和函数的参数

3.2.2.1命名

统一类型的参数写在同一句中:

procedureFoo(Param1,Param2,&nbsp_place_h
older;Param3:Integer;Param4:&nbsp_place_
holder;string);

3.2.2.2命名

所有参数必须是有意义的；并且当参数名称和其它属性名称重了的时候，加一个前缀'A',例如：

procedureSomeProc(AUserName:string;&nbsp
_place_holder;AUserAge:integer);

3.2.2.3命名冲突

当使用的两个unit中包括一个重名的函数或过程时,那幺当你引用这一函数或过程时，将执行在use&nbsp_place_
holder;子句中后声明的那个unit中的函数或过程。为了避免这种'uses-clause-
dependent'需要在引用函数或过程时，写完整函数或过程的出处。例如：

SysUtils.FindClose(SR);

Windows.FindClose(Handle);

### 3.3变量

#### 3.3.1变量命名及格式

首先所有变量必须起有意义的名字，使其它组员可以很容易读懂变量所代表的意义，变量命名可以采用同义的英文命名，可使用几个英文单词，但每一单词的首字母必须大写。例
如：

var

WriteFormat:：string；

同时对于一些特定类型可采用一定的简写如下：

指针类型

P



纪录类型

Rec



数组类型

Arr



类

Class



循环控制变量通常使用单一的字符如：i,j,或&nbsp_place_holder
;k。另外使用一个有意义的名字例如：UserIndex，也是准许的。

#### 3.3.2局部变量

在过程中使用局部变量遵循所有其它变量的命名规则。

#### 3.3.3全局变量

尽量不使用全局变量，如必须使用全局变量则必须加前缀'g'，同时应在变量名称中体现变量的类型。例如：

gprecUserCount:point;
//名称为UserCount的全局变量,其类型为指向一结构的指针

但是在模块内部可以使用全局变量。所有模块内全局变量必须用'F'为前缀。如果几个模块之间需要进行资料交换，则需要通过声明属性的方法来实现。例如：

type

TFormOverdraftReturn=
class(TForm)

private

{Privatedeclarations}

FuserName:string;

FuserCount:Integer;

ProcedureSetUserName(Value:string);

FunctionGetUserName:string;

public

{Publicdeclarations}

propertyUserName:string&nbsp_place_holde
r;readGetUserNamewrite&nbsp_place_holder
;SetUserName;

propertyUserCount:Integer&nbsp_place_hol
der;readFuserCountwrite&nbsp_place_holde
r;FuserCount;

end;

### 3.4类型

#### 3.4.1大小写协议

保留字的类型名称必须全部小写。Win32API的类型通常全部大写，对于其它类型则
首字母大写，其余字母小写，例如：

var

MyString:string;&nbsp
_place_holder;//reser
vedword

WindowHandle:HWND;&nb
sp_place_holder;//Win32API&nbsp_place_ho
lder;type

I:Integer;&nbsp_place
_holder;//&nbsp_place
_holder;typeidentifierintroduced&nbsp_pl
ace_holder;inSystemunit

#### 3.4.2浮点类型

尽量不使用Real类型，他只是为了和旧的Pascal代码兼容，尽量使用Doubl
e类型。Double类型是对处理器和数据总线做过 最优化的并且是IEEE定义的标
准数据结构。当数值超出Double的范围时，使用Extended。但Extended不被Jave支持。但使用其它
语言编写的DLL时可能会使用Single类型。

#### 3.4.3枚举类型

枚举类型的名字必须有意义并且类型的名字之前要加前缀'T'。枚举类型的内容的名字必须包含枚举类型名称的简写，例如：

TSongType=(stRock,stC
lassical,stCountry,stAlternative,&nbsp_p
lace_holder;stHeavyMetal,stRB);

#### 3.4.4数组类型

数组类型的名字必须有意义并且类型的名字之前要加前缀'T'。如果声明一个指向数组类型的指针必须在该类型的名字之前加前缀'P'，例如：

type

PCycleArray=&nbsp_pla
ce_holder;^TCycleArray;

TCycleArray=&nbsp_pla
ce_holder;array[1..100]ofinteger;

##### 3.4.5记录类型

记录类型的名字必须有意义并且类型的名字之前要加前缀'T'。如果声明一个指向数组类型的指针必须在该类型的名字之前加前缀'P'，例如：

type

PEmployee=&nbsp_place
_holder;^TEmployee;

TEmployee=&nbsp_place
_holder;record

Em
ployeeName:string

Em
ployeeRate:Double;

end;

### 3.5类

##### 3.5.1命名及格式

类的名字必须有意义并且类型的名字之前要加前缀'T'。例如：

type

TCustomer=class(TObje
ct)

类实例的名字通常是去掉'T'的类的名字。例如：

var

Customer:TCustomer;

##### 3.5.2类中的变量

3.5.2.1命名及格式

类的名字必须有意义并且类型的名字之前要加前缀'F'。所有的变量必须是四有的。如果需要从外部访问此变量则需要声明一属性

#### 3.5.3方法

3.5.3.1命名及格式

同函数和过程的命名及格式。

3.5.3.2属性访问方法

所有的属性访问方法必须出现在private或protected&nbsp_pla
ce_holder;中。属性访问方法的命名同函数和过程的命名另外读方法 (readermethod)必须使用前缀'Ge
t'.写方法(writermethod)必须使用前缀'Set'。写方法的参数必须
命名为 'Value'，其类型同所要写的属性相一致。例如：

TSomeClass=class(TObject)

private

FSomeField:Integer;

protected

functionGetSomeField:
Integer;

procedureSetSomeField(&nbsp_place_holder
;Value:Integer);

public

propertySomeField:Int
egerreadGetSomeFieldw
riteSetSomeField;

end;

### 3.6属性

#### 3.6.1命名及格式

同其用操作的，出去前缀'F'的类的变量的名称相一致。

### 3.7文件

#### 3.7.1项目文件

3.7.1.1项目目录结构

程序主目录--Bin（应用程序所在路径）

-Db（本地数据库所在路径）

-Doc（文档所在路径）

-Hlp（帮助文件所在路径）

-Backup（备份路径）

-Tmp（临时文件路径）

3.7.1.2命名

项目文件必须使用一个有意义的名字。例如：Delphi中系统信息的项目文件被命名为
SysInfo.dpr。

#### 3.7.2Form文件

3.7.2.1命名

同Form的名称相一致：例如：Form的名称为FormMain则Form文件的名称就为FormMain.frm。

####
3.7.3DataModule文件

3.7.3.1命名

datamodule文件的命名应该有意义，并且使用'DM'作为前缀。例如：用户d
atamodule被命名为'DMCustomers.dfm'。

#### 3.7.4RemoteDataM
odule文件

3.7.4.1命名

remotedatamodule文件的命名应该有意义，并且使用'RDM'作为前缀
。例如：用户remotedatamodule&nbsp_place_holder
;被命名为'RDMCustomers.dfm'。

#### 3.7.5Unit文件

3.7.5.1普通Unit

3.7.5.1.1Unit文件命名

unit文件的命名应该有意义，并且使用'unit'作为前缀。例如：通用unit被
命名为'UnitGeneral'。

3.7.5.2FormUnits

3.7.5.2.1命名

Formunit文件的名字必须和Form的名称保持一致。例如：主窗体叫FormM
ain.pas则FormUnit文件的名字为：UnitFormMain。

3.7.5.3DataModuleUnit
s

3.7.5.3.1命名

DataModuleunit文件的名字必须
和DataModule的名称保持一致。例如：主DataModule叫DMMain
.pas则DataModuleUnit文件
的名字为：UnitDMMain。

3.7.5.4文件头

在所有文件的头部应写上此文件的用途，作者，日期及输入和输出。例如：

{

修改日期：

作者：

用途：

本模块结构组成：

}

#### 3.7.6Forms和DataModules&nbsp_place_h
older;Forms

3.7.6.1Form类

1.Form类命名标准

Forms类的命名应该有意义，并且使用'TForm'作为前缀。例如：AboutF
orm类的名字为:

TAboutForm=class(TForm)

主窗体的名字为

TMainForm=class(TForm)

2.Form类实例的命名标准

Form的类实例的名字应同期掉'T'的Form类的名字相一致。例如：

TypeName

InstanceName



TaboutForm

AboutForm



TmainForm

MainForm



TCustomerEntryForm

CustomerEntryForm





3.7.6.2DataModulesFor
m

3.7.6.2.1.DataModuleF
orm命名标准

DataModulesForms类的命名应该有意义，并且使用'TDM'作为前缀。
例如：

TDMCustomer=class(TDataModule)

TDMOrders=class(TDataModule)

3.7.6.2.2.DataModule实
例命名标准

DataModuleForm的类实例的名字
应同期掉'T'的DataModuleForm类的名字相一致。例如：

TypeName

InstanceName



TCustomerDataModule

CustomerDataModule



TordersDataModule

OrdersDataModule

### 3.8控件

#### 3.8.1控件实例的命名

控件的实例应使用去掉'T'该控件类的名称作为前缀，例如：

输入用户姓名的Tedit的名字为：EditUserName。

#### 3.8.2控件的简写

控件的名称可使用以下简写，但所用简写于控件名称之间药添加'_'：

3.8.2.1StandardTab

mmTMainMenu

pmTPopupMenu

mmiTMainMenuItem

pmiTPopupMenuItem

lblTLabel

edtTEdit

memTMemo

btnTButton

cbTCheckBox

rbTRadioButton

lbTListBox

cbTComboBox

scbTScrollBar

gbTGroupBox

rgTRadioGroup

pnlTPanel

clTCommandList

3.8.2.2AdditionalTab

bbtnTBitBtn

sbTSpeedButton

meTMaskEdit

sgTStringGrid

dgTDrawGrid

imgTImage

shpTShape

bvlTBevel

sbxTScrollBox

clbTCheckListbox

splTSplitter

stxTStaticText

chtTChart

3.8.2.3Win32Tab

tbcTTabControl

pgcTPageControl

ilTImageList

reTRichEdit

tbrTTrackBar

prbTProgressBar

udTUpDown

hkTHotKey

aniTAnimate

dtpTDateTimePicker

tvTTreeView

lvTListView

hdrTHeaderControl

stbTStatusBar

tlbTToolBar

clbTCoolBar

3.8.2.4SystemTab

tmTTimer

pbTPaintBox

mpTMediaPlayer

olecTOleContainer

ddccTDDEClientConv

ddciTDDEClientItem

ddscTDDEServerConv

ddsiTDDEServerItem

3.8.2.5InternetTab

cskTClientSocket

sskTServerSocket

wbdTWebDispatcher

ppTPageProducer

tpTQueryTableProducer

dstpTDataSetTableProducer

nmdtTNMDayTime

necTNMEcho

nfTNMFinger

nftpTNMFtp

nhttpTNMHttp

nMsgTNMMsg

nmsgTNMMSGServ

nntpTNMNNTP

npopTNMPop3

nuupTNMUUProcessor

smtpTNMSMTP

nstTNMStrm

nstsTNMStrmServ

ntmTNMTime

nudpTNMUdp

pskTPowerSock

ngsTNMGeneralServer

htmlTHtml

urlTNMUrl

smlTSimpleMail

3.8.2.6DataAccessTab

dsTDataSource

tblTTable

qryTQuery

spTStoredProc

dbTDataBase

ssnTSession

bmTBatchMove

usqlTUpdateSQL

3.8.2.7DataControlsTa
b

dbgTDBGrid

dbnTDBNavigator

dbtTDBText

dbeTDBEdit

dbmTDBMemo

dbiTDBImage

dblbTDBListBox

dbcbTDBComboBox

dbchTDBCheckBox

dbrgTDBRadioGroup

dbllTDBLookupListBox

dblcTDBLookupComboBox

dbreTDBRichEdit

dbcgTDBCtrlGrid

dbchTDBChart

3.8.2.8DecisionCubeTa
b

dcbTDecisionCube

dcqTDecisionQuery

dcsTDecisionSource

dcpTDecisionPivot

dcgTDecisionGrid

dcgrTDecisionGraph

3.8.2.9QReportTab

qrTQuickReport

qrsdTQRSubDetail

qrbTQRBand

qrcbTQRChildBand

qrgTQRGroup

qrlTQRLabel

qrtTQRText

qreTQRExpr

qrsTQRSysData

qrmTQRMemo

qrrtTQRRichText

qrdrTQRDBRichText

qrshTQRShape

qriTQRImage

qrdiTQRDBMImage

qrcrTQRCompositeReport

qrpTQRPreview

qrchTQRChart

3.8.2.10DialogsTab

OpenDialogTOpenDialog

SaveDialogTSaveDialog

OpenPictureDialogTOpenPictureDialog

SavePictureDialogTSavePictureDialog

FontDialogTFontDialog

ColorDialogTColorDialog

PrintDialogTPrintDialog

PrinterSetupDialogTPrintSetupDialog

FindDialogTFindDialog

ReplaceDialogTReplaceDialog

3.8.2.11Win31Tab

dbllTDBLookupList

dblcTDBLookupCombo

tsTTabSet

olTOutline

tnbTTabbedNoteBook

nbTNoteBook

hdrTHeader

flbTFileListBox

dlbTDirectoryListBox

dcbTDriveComboBox

fcbTFilterComboBox

3.8.2.12SamplesTab

ggTGauge

cgTColorGrid

spbTSpinButton

speTSpinEdit

dolTDirectoryOutline

calTCalendar

ibeaTIBEventAlerter

3.8.2.13ActiveXTab

cfxTChartFX

vspTVSSpell

f1bTF1Book

vtcTVTChart

grpTGraph

3.8.2.14MidasTab

prvTProvider

cdsTClientDataSet

qcdsTQueryClientDataSet

dcomTDCOMConnection

oleeTOleEnterpriseConnection

sckTSocketConnection

rmsTRemoteServer

midTmidasConnection

## 4．修改规范

本规则所做的规定仅适用于已经纳入配置管理的程序。在这类修改中，要求保留修改前的内容、并标识出修改和新增的内容。并在文件
头加入修改人、修改日期、修改说明等必要的信息。

### 4．1修改历史记录

对源文件进行经过批准的修改时，修改者应在程序文件头加入修改历史项。在以后的每一次修改时，修改者都必须在该项目中填写下列
信息：

修改人

修改时间

修改原因

修改说明即如何修改

### 4．2新增代码行

新增代码行的前后应有注释行说明。

//修改人，修改时间，修改说明

新增代码行

//修改结束

### 4．3删除代码行

删除代码行的前后用注释行说明。

//修改人，修改时间，修改说明

//要删除的代码行（将要删除的语句进行注释）

//修改结束

### 4．4修改代码行

修改代码行以删除代码行后在新增代码行的方式进行。

//修改人，修改时间，修改说明

//修改前的代码行

//修改结束

//修改后的代码行

修改后的代码行

//修改结束

