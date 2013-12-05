Title: Delphi学习笔记03
Author: alswl
Date: 2009-11-29 00:00:00
Tags: 
Category: Delphi编程
Summary: 

学习Delphi第三天，早晨起来之后跑去图书馆找了一本书《[Delphi开发经验技巧宝典](http://www.china-
pub.com/36610)》，翻开这本书发现更适合作为手册查阅，而不是学习教材。最后借了一本《[Delphi面向对象程序设计](http://www
.china-pub.com/734474)》的教材，属于"21世纪高等学校应用型教材"系列。

今天主要完成了Pascal到Delphi的过度，学习使用**集合set**、**记录record**、**指针Pointer**和**简单的可视化编程**。

在百度[Delphi吧](http://tieba.baidu.com/f?kw=delphi)逛时候发现[索引越界](http://passport.ba
idu.com/?business&un=%CB%F7%D2%FD%D4%BD%BD%E7#0)居然是Delphi吧主，里面有一篇文章关于[Delphi的编
码风格](http://tieba.baidu.com/f?kz=84767888)，我一会转过来。

Ps:啊，你不知道索引越界？！那百度贴吧伴侣总应该听过吧，偷偷告诉你，这个软件就是索引越界用Delphi开发的。

好了，下面是正文，我今天使用的代码，咱们让代码来反应思想吧（其实我是懒得总结每个用法~）。

    
    program P2;
    {集合、记录、指针学习}
    {$APPTYPE CONSOLE}

uses

SysUtils;

{集合set}

procedure SetTest();

type

{定义子集类型,子集类型元素不能超过256}

TSomeInts = 1..250;

TIntSet = set of TSomeInts;

var

set1, set2 : TIntSet;

i : integer;

begin

set1 := [1, 3, 5, 7, 9];

set2 := [2, 4, 6, 8, 10];

{似乎Pascal不能输出Set内元素，书上解释是

因为Set是无序的，只能使用下列方式来判断。

使用Low()/Hign()函数获得有序数据类型的边

界。}

for i:= Low(TSomeInts) to High(TSomeInts) do

begin

{Set有一套操作方法，就是并、交、叉、等于

、不等于、属于，下面就是用到属于in}

if i in set1 then Write(i);

end;

Writeln;

end;

{记录record}

procedure RecordTest ();

type

{这是定义一个记录，类似于结构体}

TStudent = record

StNumber : integer;

StName : string;

stScore : Real;

end;

var

{其实我对这里的数据初始化不太懂，也许

是因为受C++/Java影响，我始终觉得应该

有一个构造过程，不知道这一个构造过程

是在var实现还是在给成员变量初次赋值实

现。}

student1 : TStudent;

begin

student1.StNumber := 1000;

student1.StName := '张三';

student1.stScore := 85.5;

Writeln(student1.StName);

end;

{指针}

procedure PointerTest ();

var

{定义指针}

p1, p2 : ^integer;

x : integer;

begin

x := 100;

{使用@取变量地址}

p1 := @x;

Writeln('x = ', x);

{注意^的使用}

Writeln('p1^ = ', p1^);

{使用New()对指针分配内存空间

ps；Object Pascal有一种Pointer类型，使用GetMem()

来分配未知大小内存情况，Pointer表示无类型指针。}

New(p2);

p2^ := 20;

Writeln('p2 = ', p2^);

{使用Dispose()释放内存空间}

Dispose(p2);

end;

begin

SetTest();

RecordTest();

PointerTest ();

Readln;

end.

&nbsp_place_holder;下面是一个学生分数登记系统，用了`TEdit/TRadioGroup/TListBox`等简单控件。整个项目一共三个文
件"`P3.dpr`"、"`UScore.dfm`"、"`UScore.pas`"，分别是项目文件、窗体文件、模块文件。下面是对应的代码（我发现Delphi
7想在代码状态编辑.dpr/.dfm这种文件特别麻烦）。

    
    program P3;
    {项目文件，也是入口程序，相当于C#的application.cs}
    uses
      Forms,
      UScore in 'UScore.pas' {FrmScore};

{$R *.res}

begin

{Hejlsberg不愧是Delphi/C#之父，如此神似}

Application.Initialize;

Application.CreateForm(TFrmScore, FrmScore);

Application.Run;

end.

下面是窗体文件UScore.dfm，注释始终无法加入。

    
    object FrmScore: TFrmScore
      Left = 612
      Top = 163
      Width = 315
      Height = 389
      Caption = 'Student Score'
      Color = clBtnFace
      Font.Charset = DEFAULT_CHARSET
      Font.Color = clWindowText
      Font.Height = -11
      Font.Name = 'MS Sans Serif'
      Font.Style = []
      OldCreateOrder = False
      PixelsPerInch = 96
      TextHeight = 13
      object edtNo: TEdit
        Left = 32
        Top = 32
        Width = 121
        Height = 21
        TabOrder = 0
      end
      object edtName: TEdit
        Left = 32
        Top = 72
        Width = 121
        Height = 21
        TabOrder = 1
      end
      object rgSex: TRadioGroup
        Left = 176
        Top = 32
        Width = 105
        Height = 65
        Caption = #24615#21035
        ItemIndex = 0
        Items.Strings = (
          #30007
          #22899)
        TabOrder = 2
      end
      object gbScore: TGroupBox
        Left = 32
        Top = 112
        Width = 249
        Height = 81
        Caption = 'gbScore'
        TabOrder = 3
        object edtChinese: TEdit
          Left = 16
          Top = 16
          Width = 121
          Height = 21
          TabOrder = 0
        end
        object edtMath: TEdit
          Left = 16
          Top = 48
          Width = 121
          Height = 21
          TabOrder = 1
        end
      end
      object lbDisplay: TListBox
        Left = 32
        Top = 248
        Width = 249
        Height = 105
        ItemHeight = 13
        TabOrder = 4
      end
      object btnAdd: TButton
        Left = 56
        Top = 208
        Width = 75
        Height = 25
        Caption = 'btnAdd'
        TabOrder = 5
        OnClick = btnAddClick
      end
      object btnDisplay: TButton
        Left = 168
        Top = 208
        Width = 75
        Height = 25
        Caption = 'btnDisplay'
        TabOrder = 6
        OnClick = btnDisplayClick
      end
    end
    
    
    unit UScore;
    {UScore.pas，一个模块文件}

interface

uses

Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,

Dialogs, StdCtrls, ExtCtrls;

type

TFrmScore = class(TForm)

edtNo: TEdit;

edtName: TEdit;

rgSex: TRadioGroup;

gbScore: TGroupBox;

edtChinese: TEdit;

edtMath: TEdit;

lbDisplay: TListBox;

btnAdd: TButton;

btnDisplay: TButton;

procedure btnAddClick(Sender: TObject);

procedure btnDisplayClick(Sender: TObject);

private

{ Private declarations }

public

{ Public declarations }

end;

{定义一个Student类型记录}

Student = record

stuNo : string[8];

name : String[8];

sex : String[2];

chinese, math : integer;

end;

var

frmScore: TFrmScore;

{定义Student类型动态数组}

stus : array of Student;

{我没找到这个count初始化为0，应该是自动初始化为0了}

count : integer;

{不知道书上原始代码定义这个file干嘛，莫非想写入文件？}

f : file of Student;

implementation

{$R *.dfm}

procedure TFrmScore.btnAddClick(Sender: TObject);

begin

count := count + 1;

SetLength(stus, count);

{这里使用了with开域语句，省去重复输入stus}

with stus[count - 1] do

begin

stuNo := edtNo.Text;

name := edtName.Text;

if rgSex.ItemIndex = 0 then

sex := '男'

else

sex := '女';

chinese := StrToInt(edtChinese.Text);

math := StrToInt(edtMath.Text);

end;

ShowMessage('第' + IntToStr(count) +'条记录添加完毕。');

{直接调用DisplayClick，使用Sender作为触发源}

btnDisplayClick(Sender);

end;

procedure TFrmScore.btnDisplayClick(Sender: TObject);

var

i : integer;

s : string;

begin

{ListBox增加Item}

lbDisplay.Items.Clear();

for i := Low(stus) to High(stus) do

begin

s := stus[i].stuNo + ', ' + stus[i].name + ', ' +

stus[i].sex + IntToStr(stus[i].chinese) + ', ' +

IntToStr(stus[i].math);

lbDisplay.Items.Add(s);

end;

end;

end.

这个分数记录系统的作用仅仅是为了熟悉Delphi可视化开发，没有任何可实用价值，Google过来的同学估计要哭了，哈哈~

明天开始要准备Object Pascal的内容，再加强控件的认识和使用。

