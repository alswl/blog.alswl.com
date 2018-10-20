Title: Delphi学习笔记05
Author: alswl
Slug: delphi-study-notes-05
Date: 2009-12-01 00:00:00
Tags: Delphi
Category: Coding

今天是第五天了，我对自己的学习速度很不满意，还是处在半懵懂状态。语法还要经过大脑才能想出来，一点不顺手。

VCL控件使用了几个简单的，**BDE数据库**和**ADO数据库**这一块还没有涉及，**网络编程**也没涉及到。

这几天事情很烦，18号的课程设计赶不上了，我之前又是做的"[**PylexChat**](http://log4d.com/tag/pylexchat)"聊
天系统这么有挑战性的题目。唉，真开始后悔了，老师那里也不好说，郁闷。还得等我组员回来讨论一下，这周就得答辩了。当时老师突然说："那你不是在学Delphi么，
就用Delphi写一个吧"，我狂晕，学一门语言又不是吃菜，总得有个进度吧~

昨天请同学吃饭，我把我生日提前一个月过，请一帮兔崽子吃饭唱歌，闹到11点多才回来，所以昨天的总结今天早晨才更新。

ps:我之前使用的Delphi7版本是绿色精简完美版，在**插入`AboutBox`**和**跟踪源码**（在某个VCL类名如TForm上Ctrl+单击）时
候出现找不到".pas"的错误，我之后重新安装了188MB的安装版，错误消失了，所以推荐大家使用安装版。

以上废话结束，下面正文。

## 1.同构数的Delphi实现

这道题目是在一个PPT上看到的,题目如下："**如果一个数刚好出现在其平方的右边，如5的平方为25，6的平方为36，这样的数我们称为同构数，请编程找出1～9
999的全部同构数**"。题目对我的难点在于类型的转换和`Math`函数的熟悉。

    
    program P1;
    {如果一个数刚好出现在其平方的右边，如5的平方
    为25，6的平方为36，这样的数我们称为同构数，
    请编程找出1～9999的全部同构数}

{$APPTYPE CONSOLE}

uses

SysUtils, Math;

var

{定义这么多变量是为了容易调试}

a, b, c, t : Double;

i : Integer;

begin

for i := 1 to 9999 do

begin

a := i * i;

{Trunc取整}

t := Trunc(Log10(i)) + 1;

{Power x^y}

b := Power(10, t);

c := Trunc(a) mod Trunc(b);

  
if i = c then

Write(i, ' ');

end;

Readln;

end.

注意里面的几个`Math`方法，这些函数的熟悉和累计不是一朝一夕能够完成的，我现在正在总结一个"Dlphi资料小汇总"
，总结好了之后再发布。

## 2.仿Window记事本的编辑器

本来是有一道例题实现Windows计算器，我感觉实现记事本更能接触各种控件，于是花了2个小时摸索这块内容。

代码我就贴一个核心区的，没写注释。如果学过C#，应该很容易看懂，都出自Heljsberg，Application的结构很类似。（等我空下来，好好写一篇文章了
解一下Heljsberg）

实现了打开、保存、字体功能，没有另存为和换行、查找功能。- -#（这是记事本？）

一个小亮点就是如果文章修改了会有(*)标记，呵呵。

上个小图

[![image](http://upload.log4d.com/upload_dropbox/200912/delphi_editor.jpg)](http://upload.log4d.com/upload_dropbox/200912/delphi_editor.jpg)

    
    procedure TForm1.O1Click(Sender: TObject);
    begin
      if odOpenFile.Execute() then
      begin
        FFileName := odOpenFile.FileName;
        mmContent.Lines.LoadFromFile(odOpenFile.FileName);
        Self.Caption := FFileName;
        Self.FIsEdited := False;
      end;

end;

procedure TForm1.S1Click(Sender: TObject);

begin

if FFileName <> '' then

begin

mmContent.Lines.SaveToFile(FFileName);

FFileName := odOpenFile.FileName;

Self.Caption := FFileName;

Self.FIsEdited := False;

end

else

if sdSaveFile.Execute then

begin

FFileName := sdSaveFile.FileName;

mmContent.Lines.SaveToFile(FFileName);

Self.Caption := FFileName;

Self.FIsEdited := False;

end;

end;

procedure TForm1.T1Click(Sender: TObject);

begin

fdFont.Font := mmContent.Font;

if fdFont.Execute then

mmContent.Font := fdFont.Font;

end;

procedure TForm1.X1Click(Sender: TObject);

begin

Form1.Close();

end;

procedure TForm1.A1Click(Sender: TObject);

begin

abAbout.Show();

end;

procedure TForm1.FormCreate(Sender: TObject);

begin

FFileName := '';

FIsEdited := False;

end;

procedure TForm1.mmContentChange(Sender: TObject);

begin

if Self.FIsEdited = false then

Self.Caption := Self.Caption + ' (*)';

Self.FIsEdited := True;

end;

procedure TForm1.FormCloseQuery(Sender: TObject; var CanClose: Boolean);

var

IsExit : Integer;

begin

if FIsEdited = True then

begin

isExit := MessageDlg('正文已修改，是否保存？', mtConfirmation,

[mbYes, mbNo, mbCancel], 0);

case IsExit of

mrYes : Self.S1Click(Sender);

mrCancel : CanClose := False;

end;

end;

end;

end.

我把这个小程序打包，如果对源码有兴趣，可以看一下。

点击这里下载[delphi_editor](http://upload.log4d.com/upload_dropbox/200912/delphi_editor.zip)

学校暖气坏了，我得跑出去洗澡，今天就先到这里吧。

