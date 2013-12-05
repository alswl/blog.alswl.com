Title: Delphi学习笔记02
Author: alswl
Date: 2009-11-28 00:00:00
Tags: Pascal
Category: Delphi编程
Summary: 

今天算是学习Delphi的第二天，昨天熟悉了一下基本概念和开发环境，写了一个简单的Hello world!（传送门-[Hello
world!](http://log4d.com/2009/11/delphi-study-notes-01)）。

说是学Delphi，其实今天我一下午都在学习Pascal语法，这里有一个要点我需要强调"Delphi与其说一门语言，不如说是一个开发环境和开发框架，使用的是
Object Pascal语言"。我今天还停留在Delphi基本语法、变量、数组、指针这些学习上。

说说我对Pascal的第一感觉吧：语法很繁琐，比起C/Java，`if/while/repeate/for`这些语法结构都`begin/end`才支持多语句
（C/Java使用{}，Python使用缩进）。不过正是这个原因，所以代码特别直观，在教学使用和信息学比赛就很适合了。

今天使用的教材是《Pascal基础教程》（传送门-[更多教程](http://log4d.com/2009/11/delphi-study-
notes-01)），还是那句话，相当精简，适合有编程基础的童鞋。

下面是我今天使用的几个例子，我都尽量附带注释了，放在这里以后复习和分享。

**常量、变量、函数、过程、If语句**
    
    program p1;
    {常量、变量、函数、过程、If语句}

{加上$意味着编译指令}

{$APPTYPE CONSOLE}

uses

SysUtils;

const

{标识符，有效长度为63个字符，并且大小写等效}

{常量定义}

pi = 3.14159;

var

{变量定义}

s : Real;

t1_ : String;

_t2 : Integer;

{函数}

function Area(): Real;

var

r : Real;

begin

{输出一串字符串}

Writeln('Pleae enter a number:');

Readln(r);

{标准函数-算术函数-sqr()}

{赋值语句 :=}

Area := pi * sqr(r);

end;

{过程定义-打印较大值}

procedure Larger(x, y : Integer);

begin

{分支语句 if-then-else}

if x > y then

Write(x)

else

Write(y);

Writeln;

end;

begin

Writeln('Call Area function');

{调用函数Area()}

s := Area();

Writeln('s = ', s);

Writeln('back to main');

Writeln('call Larger procedure');

{调用过程Larger()}

Larger(10, 9);

Writeln('back to main');

  
Readln;

end.

**&nbsp_place_holder;学习if/case/while/repeat/for语句**

&nbsp_place_holder;

    
    **program P2;
    {学习if/case/while/repeat/for语句}
    {$APPTYPE CONSOLE}**

uses

SysUtils;

{测试单语句if-then}

procedure IfTest1(x : Real);

var

y : Real;

begin

if x > 0 then

y := 1;

if x = 0 then

y := 0;

if x < 0 then

y := -1;

Writeln(y);

end;

{测试多语句if-then，嵌套begin-...-end语句}

procedure IfTest2(x : Integer);

begin

if x > 0 then

begin

Writeln('test line1');

Writeln('test line2');

end

else

begin

Writeln('test line3');

Writeln('test line4');

end;

end;

{Case语句}

function CaseTest (score : Integer): Char;

var

r : Char;

begin

case score div 10 of

10, 9 : r := 'A';

8 : r := 'B';

7, 6 : r := 'C';

else

r := 'D';

end;

CaseTest := r;

end;

{While...do语句}

procedure WhileTest(n : Integer);

begin

while n > 0 do

begin

{writeln(I：n)-单域宽输出格式}

WriteLn('*' : n);

n := n - 1;

end;

end;

{Repeat语句（自带语句括号功能）}

procedure RepeatTest(n : Integer);

begin

repeat

Writeln('Im in repeater ');

n := n -1;

until n < 0;

end;

{for...do语句}

function ForTest(n : Integer): Integer;

var

i, sum : Integer;

begin

sum := 0;

for i:=1 to 100 do

sum := sum + i;

Writeln(sum);

end;

begin

IfTest1(10);

IfTest1(-5);

IfTest1(0);

IfTest2(3);

IfTest2(-2);

Writeln(CaseTest(95));

Writeln(CaseTest(85));

Writeln(CaseTest(75));

Writeln(CaseTest(65));

Writeln(CaseTest(55));

WhileTest(4);

WhileTest(5);

WhileTest(0);

RepeatTest(5);

ForTest(100);

Readln;

end.

**使用数组**
    
    program P3;
    {使用数组}
    {$APPTYPE CONSOLE}

uses

SysUtils;

const

n = 5;

type

{定义类型-数组类型}

No = array[1..n] of Integer;

S = array[1..n] of Real;

var

i : Integer;

k : Real;

{创建数组类型变量}

num : No;

score : S;

{直接创建一个数组变量}

t : array[0..5] of Integer;

begin

k := 0;

for i := 1 to n do

begin

Readln(score[i]);

k := k + score[i];

end;

k := k / n;

Writeln('平均分为：', k);

Readln;

end.

&nbsp_place_holder;今天基础部分到这儿，明天理一理集合、记录，再练习一些小程序，就可以由Pascal转入Delphi了~

