Title: Dlphi资料小汇总
Author: alswl
Slug: dlphi-a-small-summary-of-knowledge
Date: 2009-12-05 00:00:00
Tags: 
Category: Delphi编程

学Delphi大概一周时间，我经历从当初的初生牛犊不怕虎，到现在感慨Delphi的强大和复杂。说实话，我以前觉得Delphi是一门过气的语言，现在我重新修正
自己的观点，没有弱势的语言，只有菜鸟的程序员。

Delphi的整个架构让我叹为观止，我这么短的学习周期，只能学到一点基础的皮毛。由于完全自学，我花费很多精力在资料的收集上（很痛苦没有找到一本合适的书），现
在我把我这段时间的资料收集整理，分享我的所得（这篇文章经历1个星期，发布时候遇到服务器卡住，丢失了一次，幸好我灵机一动，用FireFox脱机找回了缓存页面，
还是得信春哥啊）。

资料繁杂，很多都是来自信息采集站点，我无法一一署名，在这里对这些资料的原作者表示谢意。

  1. Delphi7的文件类型
  2. Delphi的关键字
  3. 类型之间转换函数
  4. 组件的常用属性
  5. 组件的常用事件
  6. 常用类型和函数的uses单元
  7. Delphi常用的ADO组件
  8. ADO组件常用属性
  9. ADO数据集类组件的共同方法

## Delphi7的文件类型

文件扩展名 文件类型说明 产生时间

BMP、ICO、CUR

位图、图标及光标图像文件

程序设计时

BGP

项目组文件，由多目标项目管理器产生

程序设计时

BPL

BORLAND PACKAGE LIBRARY（组件库文件）

编译连接后

CBA

压缩格式文件，做WEB发布时使用

设计时

CFG

项目配置文件。项目配置文件保存着项目的配置信息

设计时

DCP

DELPHI COMPONENT PACKAGE（Delphi组件包）

编译时

DCU

DELPHI COMPILED UNIT，编译原始文件后的中间产物

编译时

DFM

DELPHI FORM FILE（窗体文件）

程序设计时

~DFM

DFM的备份文件

程序设计时

DLL

DYNAMIC LINK LIBRARY（动态链接库文件）

编译连接时

DOF

DELPHI OPTION FILE，设计多语言项目时使用的语言翻译配置文件，多语言项目中每个窗体的每一种语言都有一个DNF文件

程序设计时

DPK

DELPHI PACKAGE，软件包项目的源代码文件

程序设计时

DPR

项目文件

程序设计时

~DPR

DPR的备份文件

程序设计时

DSK

DESKTOP FILE，保存现在DELPHI视窗的位置、正在编辑的文件以及其它桌面的设定文件

程序设计时

LIC

OCX文件相关的授权文件

编译连接时

OCX

OLE控件文件，是一特殊的DLL文件可包含ACTIVEX控件或窗体

编译连接时

PAS

DELPHI源代码文件

程序设计时

~PAS

PAS的备份文件

程序设计时

RES、RC

项目的资源文件,包含项目的图标、光标及字体等信息

程序设计时

EXE

可执行文件

编译连接时

TLB

类型库文件

程序设计时

## Delphi的关键字

and

array

As

asm

begin

Case

Class

Const

constructor

destructor

Dispinterface

Div

Do

downto

Else

End

except

exports

File

Finalization

Finally

for

function

Goto

If

Implementation

In

inherited

initialization

inline

Interface

is

label

library

Mod

Nil

not

object

Of

or

out

packed

procedure

program

property

raise

record

repeat

resourcestring

set

Shl

shr

string

then

threadvar

To

try

type

unit

until

uses

var

while

With

xor

## 类型之间转换函数

函数 功能

Chr

将一个有序数据转换为一个ANSI字符

Ord

将一个有序类型值转换为它的序号

Round

转换一个实型值为四舍五入后的整型值

Trunc

转换一个实型值为小数截断后的整型值

Int

返回浮点数的整数部分

IntToStr

将数值转换为字符串

IntToHex

将数值转换为十六进制数字符串

StrToInt

将字符串转换为一个整型数，如字符串不是一个合法的整型将引发异常

StrToIntDef

将字符串转换为一个整数，如字符串不合法返回一个缺省值

Val

将字符串转换为一个数字（传统Turbo Pascal例程用于向后兼容）

Str

将数字转换为格式化字符串（传统Turbo Pascal例程用于向后兼容）

StrPas

将零终止字符串转换为Pascal类型字符串，在32位Delphi中这种类型转换是自动进行的

StrPCopy

拷贝一个Pascal类型字符串到一个零终止字符串, 在32位Delphi中这种类型转换是自动进行的

StrPLCopy

拷贝Pascal类型字符串的一部分到一个零终止字符串

FloatToDecimal

将一个浮点数转换为包含指数、数字及符号的十进制浮点记录类型

FloatToStr

将浮点值转换为缺省格式的字符串

FloatToStrF

将浮点值转换为特定格式的字符串

FloatToText

使用特定格式，将一个浮点值拷贝到一个字符串缓冲区

FloatToTextFmt

同上面例程，使用特定格式，将一个浮点值拷贝到一个字符串缓冲区

StrToFloat

将一个Pascal字符串转换为浮点数

TextToFloat

将一个零终止字符串转换为浮点数

## 组件的常用属性

属性 说明

Height

高度

Width

宽度

Left

组件在容器内的水平坐标，相对于容器左边。

Top

组件在容器内的垂直坐标，相对于容器上边。

Align

组件上的对齐方式（居上、居下、居左、居右、居中）

Visible

设置组件是否可见，默认值为可见（值为true）

Caption

显示类组件的标题

Color

组件的背景颜色

Font

设置组件显示文本的字体

Ctl3D

是否以3D方式显示组件，默认值为true

ShowHint

是否显示组件的提示信息，默认值为true，与Hint连用

Hint

当鼠标指针移到组件上时，组件显示的提示信息

Enabled

是否允许用户操作组件，true表示允许，false表示不允许

Name

用于标识组件的名称，在程序中通过Name可以调用该组件

TabOrder

Tab次序

## 组件的常用事件

事件 说明

OnClick

触发条件

OnDblClick

当鼠标双击时触发本事件

OnMouseDown

当鼠标左键按下时触发本事件

OnMouseMove

当鼠标移动时触发本事件

OnKeyDown

当按下任意键（包括组合键）时触发本事件

OnKeyPress

当按下任意键（单字符键）时触发本事件

OnKeyUp

当松开已按下键时触发本事件

OnEnter

当获得焦点时触发本事件

OnExit

当失去焦点时触发本事件

OnStartDrag

当开始拖动时触发本事件

OnDragDrop

当组件拖动操作结束时触发本事件

## 常用类型和函数的uses单元

Type Unit

_Stream

ADODB_TLB

akTop, akLeft, akRight, akBottom

Controls

Application (the variable not a type)

Forms

Beep

SysUtils or Windows (different functions)

CGID_EXPLORER

ShlObj

CN_BASE

Controls

CoInitialize

ActiveX

CopyFile

Windows

CoUnInitialize

ActiveX

CreateComObject

ComObj

CreateOleObject

ComObj

Date

SysUtils

DeleteFile

SysUtils or Windows (different versions)

DispatchInvokeError

ComObj

DWORD

Windows

EDatabaseError

DB

EncodeDateTime

DateUtils

EnumWindows

Windows

EOleError

ComObj

EOleException

ComObj

EOleSysError

ComObj

Exception

SysUtils

ExtractFileName

SysUtils

FileExists

SysUtils

FileOpen

SysUtils

FILETIME

Windows

FindFirst

SysUtils

FindFirstFile

Windows

FindWindow

Windows

FlushFileBuffers

Windows

fmOpenRead

SysUtils

fmShareDenyWrite

SysUtils

Format

SysUtils

FormatDateTime

SysUtils

FreeAndNil

SysUtils

fsBold

Graphics

ftWideString

DB

ftString

DB

GetCurrentProcessId

Windows

GetEnvironmentVariable

SysUtils or Windows (different versions)

GetFileAttributes

Windows

GetFileVersionInfoSize

Windows

GetWindowLong

Windows

GetStdHandle

Windows

HDC

Windows

HFont

Windows

HINTERNET

WinInet

HKEY_CURRENT_USER

Windows

IHTMLDocument2

MSHTML or MSHTML_TLB

IHTMLElement

MSHTML or MSHTML_TLB

IHTMLEventObj

MSHTML or MSHTML_TLB

IID_IWebBrowser2

SHDocVw or SHDocVw_TLB

IMessage

CDO_TLB

InternetClosehandle

WinInet

InternetOpenUrl

WinInet

InternetReadFile

WinInet

IntToHex

SysUtils

IntToStr

SysUtils

IOleCommandTarget

ActiveX

IOleContainer

ActiveX

IPersistStreamInit

ActiveX

IsSameDay

DateUtils

IStream

ActiveX

IWebBrowser2

SHDocVw or SHDocVw_TLB

LockWindowUpdate

Windows

Log10

Math

LowerCase

SysUtils

LPSTR

Windows

MAX_PATH

Windows

MessageBox

Windows

MessageDlg

Dialogs

MB_YESNO, MB_OK etc

Windows

MinutesBetween

DateUtils

Now

SysUtils

OleInitialize

ActiveX

OleUninitialize

ActiveX

PItemIDList

ShlObj

POleCmd

ActiveX

POleCmdText

ActiveX

PostMessage

Windows

PosX

StrUtils

QueryHighPerformanceCounter

Windows

QueryPerformanceCounter

Windows

ReverseString

StrUtils

RoundTo

Math

SendMessage

Windows

SetForegroundWindow

Windows

ShellExecute

ShellAPI

ShellExecuteEx

ShellAPI

SHGetFileInfo

ShellAPI

SHFILEINFO

ShellAPI

ShowMessage

Dialogs

Sleep

SysUtils

StrAlloc

SysUtils

StrPas

SysUtils

StrToDate

SysUtils

StrToInt

SysUtils

StrToIntDef

SysUtils

TAdoConnection

ADODB

TAdoQuery

ADODB

TAlign

Controls

TAlignment

Classes

TAnchors

Controls

TBitmap

Graphics

TBlobStream

DBTables

TCanvas

Graphics

TClientSocket

ScktComp

TComboBox

StdCtrls

TComponent

Classes

TControl

Controls or QControls

TCriticalSection

SyncObjs

TField

DB

TFieldType

DB

TFileName

SysUtils

TFileStream

Classes

TForm

Forms

TFrame

Forms

TGroupBox

StdCtrls

TIID

ActiveX

TIniFile

IniFiles

TJPEGImage

Jpeg

TLabel

StdCtrls

TList

Classes

TMemo

StdCtrls

TMemoryStream

Classes

TMouseButton

Controls

TNofityEvent

Classes

TObjectList

Contnrs

TOSVersionInfo

Windows

TPanel

ExtCtrls

TPoint

Types

TProcessEntry32

TlHelp32

TProgressBar

ComCtrls or QComCtrls

TRadioButton

StdCtrls

TRadioGroup

ExtCtrls

TRect

Types

TRegistry

Registry

Trim

SysUtils

TRoundToRange

Math

TSearchRec

SysUtils

TSize

Windows

TSocketAddrIn

Winsock

TStaticText

StdCtrls

TStream

Classes

TStringList

Classes

TStrings

Classes

TStringStream

Classes

TSystemTime

Windows

TTable

DBTables

TTabSheet

ComCtrls

TThread

Classes

TTreeNode

ComCtrls

TWebBrowser

SHDocVw or SHDocVw_TLB

TWinSocketStream

ScktComp

TWMCommand

Messages

Unassigned

Variants

VarArrayCreate

Variants

VarArrayOf

Variants

VirtualProtect

Windows

WM_USER

Messages

YearOf

DateUtils

## Delphi常用的ADO组件

ADO组件 作用

TADOConnection

该组件用于建立数据库的连接。

TADODataSet

这是ADO提取及操作数据库数据的主要数据集，该组件可以从一个或多个基表中提取数据。

TADOTable

主要用于操作和提取单个基表的数据。

TADOQuery

该组件是通过SQL语句实现对数据库数据的提取及操作。

TADOStoredProc

该数据集是专门用于运行数据库中的存储过程的。

TADOCommand

该组件用于运行一些SQL命令。

RDSConnection

一个进程或一台计算机传递到另一个进程或计算机的数据集合，用于远程数据访问。

## ADO组件常用属性

属 性 说明

Active

Active属性指定数据集是否处于打开状态。设置Active属性为True,则数据集被打开；设置Active属性为False，则数据集被关闭。

State

State属性表明了当前数据集的状态

CacheSize

指定数据集的缓冲区大小。

CommandTimeout

CommandTimeout属性是一个整型数，指定执行一个命令的最大允许时间，默认值是30秒。

Connection

指定所使用的数据源连接组件的名称，即TADOConnection 组件的名称。

ConnectionString

即连接字符串，用于指定数据库的连接信息。

CursorLocation

指定数据库记录指针是采用客户端模式还是服务器端模式。

CursorType

指定在数据集中使用的记录指针类型。

AutoCalcFields

设为 True 则允许应用程序触发OnCalcFields事件。

BOF

为True时，表示当前指针指向第一条记录,否则为False。

EOF

为True时，表示当前指针指向最后一条记录,否则为False。

Bookmark

在数据集中设定标记，用于在一个数据集中获得或者设置当前记录。

Filter

设置过滤条件。

Filtered

相当于过滤的开关，当Filtered属性的值为True时，数据集从数据库中获取符合条件的记录；当Filtered属性的值为False时不执行过滤。

FilterOptions

确定过滤方式。

FieldCount

返回该数据集的字段数。

FieldDefList

返回数据集字段定义列表。

FieldDefs

表明数据集中字段的定义信息。如字段的数据类型、数据长度、名称等。

FieldList

数据集中字段组件的连续列表。

Fields

数据集中字段的集合，用于访问数据集中的字段。

FieldValues

可访问当前记录所有字段值列表。

Found

表示FindFirst、FindNext、FindLast或者FindPrior是否成功。

IndexName

指定当前使用的索引。

LockType

指定了数据集打开数据库时，对数据表中的记录的锁定类型。

MaxRecords

指定记录集中一次允许从数据库中返回的最大记录数。 默认值为0，表示不限制返回行数。

Modified

表示数据集是否被更改了。布尔型。

Name

数据集组件名称

RecNo

数据集的记录号。

RecordCount

与数据集相关的记录总数。

RecordSize

表示数据集中记录缓冲区的大小。

## ADO数据集类组件的共同方法

方法 说明

ActiveBuffer

返回一个PChar，包含激活记录的数据

Append

添加一个新的记录到数据集中

AppendRecord

添加一个新的记录到数据集中。以数组参数传递来的值填充字段

BookmarkValid

该方法传递一个Bookmark参数，如果此Bookmark在数据集中有效则返回True

Cancel

取消对数据集的修改，并设置数据集的状态为dsBrowse

CancelBatch

在批更新模式下，撤销一批正等待处理的更新

CancelUpdates

撤消一个准备执行的更新操作。用于一般更新模式，在Post执行之前调用

Clone

克隆另外一个数据集到当前调用组件

CheckBrowseMode

当前记录更改时，自动提交或取消数据更改。

ClearFields

清除激活记录的所有字段值

Close

关闭数据集

CompareBookmarks

比较两个书签，如果这两个书签引用同样的记录则返回0，如果第一个书签指定所引用的记录在数据集中的位置比第二个书签在数据集中的位置靠前则返回一个小于0的值，否则
返回一个大于0的值

ControlsDisabled

Boolean特性，表示相应的控件是否失效

方法

说明

Create

构造函数

CreateBlobStream

从一个Field参数创建一个BlobStream

CursorPosChanged

使内部光标定位无效

Delete

删除当前的记录

DeleteRecords

删除记录集中的一行或多行记录。

Destroy

析构函数

DisableControls

在更新过程中使相应的控件无效

Edit

将记录的状态设置为dsEdit；记录在编辑模式下

EnableControls

使相应的控件有效

FieldByName

返回动态的TField，通过字段名搜索

FindField

如果找到指定的字段名则返回一个TField；否则返回nil

FindFirst

返回一个Boolean值，表示查找的成功或者失败；将光标定位在数据集中的第一个记录上

FindLast

返回一个Boolean值，表示查找的成功或者失败；将光标定位在数据集中的最后一个记录上

FindNext

返回一个Boolean值，表示查找的成功或者失败；将光标定位在数据集中当前记录的下一个记录上

方法

说明

FindPrior

返回一个Boolean值，表示查找的成功或者失败；将光标定位在数据集中当前记录的前一个记录上

First

将光标定位在第一条记录上

FreeBookmark

该方法传递一个用GetBookmark方法返回的书签，释放这个书签

GetBlobFieldData

返回BLOB字段值，根据FieldNo将值返回到一个字节数组：TBlobFieldData

GetBookmark

返回代表当前记录的书签

GetCurrentRecord

返回一个Boolean值，表示Buffer参数是否被当前记录缓冲区的值所填充

GetDetailDataSets

用每一个嵌套的数据集填充TList参数

GetDetailLinkFields

用字段组件（此组件构成了一个主细节关系）填充两个TList参数

GetFieldData

如果成功的话以字段数据填充一个缓冲区

GetFieldList

将所有由FieldNames参数指定的字段组件拷贝到TList参数中

GetFieldNames

返回数据集中所有字段名的一个列表，保存在TStrings参数中

GetIndexNames

获取当前数据集的索引名称的列表。

GotoBookmark

将光标定位到由Bookmark参数指定的记录中

Insert

将数据集设置为插入模式（State = dsInsert）

InsertRecord

插入一个记录，字段值由传递过来的变体数的常量数组填充

方法

说明

IsEmpty

一个Boolean值，表示数据集是否为空

IsLinkedTo

如果数据集已经连接到参数TDataSource，则返回True

IsSequenced

如果数据库表格由数据集表示则返回True，表示记录号码是否代表记录的顺序

Last

将光标定位到数据集中的最后一个记录

LoadFromFile

从一个文件中读以数据到ADO数据集中。

Locate

定位一条记录并把这条记录作为当前记录。如果找到记录则返回True

Lookup

由找到的记录中返回指定字段的值

MoveBy

将光标定位到由当前记录加上偏移量所代表的记录上

Next

将光标定位到下一个记录

Open

打开数据集

Post

将记录中的修改发送到数据库

Prior

将光标定位到前一个记录

Refresh

重新从数据库读取数据

Requery

刷新记录集，可以保持数据集的数据和数据库一致

Resync

从数据库中重新获取前一个、当前的和下一个记录

