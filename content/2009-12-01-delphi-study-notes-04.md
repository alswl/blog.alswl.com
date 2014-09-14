Title: Delphi学习笔记04
Author: alswl
Slug: delphi-study-notes-04
Date: 2009-12-01 00:00:00
Tags: Delphi, 
Category: Coding

今天主要学习了Object Pascal的**面向对象**部分：类的定义、继承、多态这些基本操作。

1.Delphi的关键词好麻烦，居然result都没法用，返回值的错误我查找了很久才明白为什么编译器说result重定义。

2.语法结构严谨，比如类定义必须在`interface`之后，过程/函数的实现必须要分开，而无法写成C++/Java那种inner类定义，写起来难免缚手缚脚
。

3.大小写的语法规范很麻烦，像`Integer/String`这些关键词，我真不知道该不该首字母大写。还有变量的定义，按照"Delphi编码规范"是应该大写
，可是这样就需要频繁的使用Shift，还是喜欢Java的那种首字符小写的驼峰式，能够清楚地把函数/过程/变量区分开。

4.`fuction/procedure`除了返回值又没什么大区别，现在想来真爱死void了。

下面上今天学习的代码，是类的**定义**、**继承**、**多态**这些。

## 1.类的使用

    
    unit USharp;

{接口定义}

interface

type

{定义类TSharp}

TSharp = class(TObject)

private

FWeight : Double;

procedure SetWeight(Weight : Double);

public

{定义属性Weight}

property Weight : Double read FWeight write SetWeight;

procedure Display();

procedure Draw() ;virtual;

end;

{实现}

implementation

procedure TSharp.SetWeight(Weight : Double);

begin

FWeight := Weight;

end;

procedure TSharp.Display();

begin

{Self.ClassName获取当前类名}

Writeln('Im ', Self.ClassName, ' , my weight is ', FWeight);

end;

{空方法，我不明白虚方法为什么还需要在基类实现…}

procedure TSharp.Draw();

begin

end;

end.

## 2.类的继承和多态

    
    unit UCircle;
    {Circle类模块}
    interface

uses

USharp;

  
type

TCircle = class(TSharp)

private

FR : Double;

procedure SetR (R : Double);

public

property R : Double read FR write SetR;

{重载父类Display方法}

procedure Display();

{重写父类Draw虚方法，关键词override}

procedure Draw(); override;

end;

implementation

procedure TCircle.SetR(R : Double);

begin

FR := R;

end;

procedure TCircle.Display();

begin

Writeln('Im ', Self.ClassName, ' , I am in TCircle.');

end;

procedure TCircle.Draw();

begin

Writeln('Draw a Circle.');

end;

end.

    
    unit USquare;

interface

uses

USharp;

type

{定义类TSharp}

TSquare = class(TSharp)

private

FX : Double;

FY : Double;

procedure SetX(X : Double);

procedure SetY(Y : Double);

public

{定义属性Weight}

property X : Double read FX write SetX;

property Y : Double read FY write SetY;

procedure Display();

{重写父类Draw虚方法，关键词override}

procedure Draw(); override;

end;

{实现}

implementation

procedure TSquare.SetX(X : Double);

begin

FX := X;

end;

procedure TSquare.SetY(Y : Double);

begin

FY := Y;

end;

procedure TSquare.Display();

begin

{Self.ClassName获取当前类名}

Writeln('Im ', Self.ClassName, ' , my x is ', X, ', y is ', Y);

end;

procedure TSquare.Draw();

begin

Writeln('Draw a Square.');

end;

end.

    
    program P2;
    {使用类继承和多.pas文件}

{$APPTYPE CONSOLE}

uses

SysUtils,

USharp in 'USharp.pas',

UCircle in 'UCircle.pas',

USquare in 'USquare.pas';

var

Sharp : TSharp;

Circle : TCircle;

Square : TSquare;

{用来进行多态的TSharp}

SharpVirtual : TSharp;

{用来进行类型转换的TSquare}

SquareForAs : TSquare;

begin

Sharp := TSharp.Create();

Sharp.Weight := 1.3;

Sharp.Display();

Circle := TCircle.Create();

Circle.Weight := 2.2;

Circle.R := 1.2;

Circle.Display();

Square := TSquare.Create();

Square.Weight := 4.5;

Square.X := 2;

Square.Y := 3;

Square.Display();

{将变量分别指向TCicle和TSquare，运行Draw实现多态}

SharpVirtual := TCircle.Create();

SharpVirtual.Draw();

SharpVirtual := TSquare.Create();

SharpVirtual.Draw();

{is操作符}

Writeln(Circle is TCircle);

Writeln(SharpVirtual is TCircle);

Writeln(SharpVirtual is TSquare);

{as类转换操作符}

SquareForAs := SharpVirtual as TSquare;

SquareForAs.Draw;

Readln;

end.

&nbsp_place_holder;本来准备入手**VCL**，结果事情太多，下午党员会议，晚上我又提前1个月过生日请朋友吃饭唱歌，耽误了```

