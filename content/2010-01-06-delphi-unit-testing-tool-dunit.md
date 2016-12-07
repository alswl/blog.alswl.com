Title: Delphi 的单元测试工具DUnit
Author: alswl
Slug: delphi-unit-testing-tool-dunit
Date: 2010-01-06 00:00:00
Tags: Delphi, Delphi, Lib, Testing
Category: Coding

以前写Java时候经常使用一款单元测试工具JUnit，工作之后在用Delphi，自然也要换到Delphi下面的单元测试工具DUnit。

DUnit是XUnit家族中的一员，是Extreme Programming测试实现Xtreme Testing的一种工具。

DUnit的用法和JUnit很类似，如果有相关经验很容易上手。这里是DUnit的官方地址：[http://dunit.sourceforge.net/](h
ttp://dunit.sourceforge.net/) ，下载地址：[http://sourceforge.net/projects/dunit/](h
ttp://sourceforge.net/projects/dunit/)

将DUnit解压至任意目录（我习惯在`D:/Study/DelphiLib/`），打开Delphi 7，将DUnit路径添加到 Tools- >
Environment Options 里面的 Library -> Library Path，这样DUnit就安装完成了。

如果有装过CnPack 的Delphi工具包，就可以很轻松的在 File -> New -> Other -> CnPack ->
DUnit测试实例生成向导 中建立新的测试用例。

下面是我的一个简单的测试用例，测试AppFun中的` GetString() `和 `Add() `方法。

TAppFun.pas

    
    (*
      UTest by Jason
      2010-01-06 21:30
    *)
    unit AppFun;

interface

uses SysUtils;

type TAppFun = class(TObject)

public

class function GetString(sName: string; iAge: Integer): string;

class function Add(iA: Integer; iB: Integer): Integer;

end;

implementation

class function TAppFun.GetString(sName: string; iAge: Integer): string;

begin

result := 'Hello ' + sName + ', your age is ' +

IntToStr(iAge);

end;

class function TAppFun.Add(iA: Integer; iB: Integer): Integer;

begin

Result := iA + iB;

end;

end.

UTest.pas

    
    (*
      UTest by Jason
      2010-01-06 21:30
    *)

unit UTest;

interface

uses

Windows, SysUtils, Classes, TestFramework, TestExtensions;

type

TTest = class(TTestCase)

protected

procedure SetUp; override;

procedure TearDown; override;

published

procedure Test;

procedure TestGetString();

end;

implementation

uses

AppFun, Dialogs;

procedure TTest.Setup;

begin

ShowMessage('In Setup!');

end;

procedure TTest.TearDown;

begin

ShowMessage('In TearDown!');

end;

procedure TTest.Test;

begin

Self.Check(TAppFun.GetString('Jason', 22) = 'Hello Jason, your age is 22',

'Second Test');

end;

procedure TTest.TestGetString();

begin

Check(TAppFun.Add(3, 5) = 8, 'First Test');

end;

initialization

TestFramework.RegisterTest(TTest.Suite);

end.

从上面的代码可以看出，XUnit系列风格都比较类似，很容易操作。

&nbsp_place_holder;[![image](https://ohsolnxaa.qnssl.com/2010/01/dunit.jpg)](https://ohsolnxaa.qnssl.com/2010/01/dunit.jpg)

DUnit还有一些更高阶的操作，比如在控制台输出/在独立线程中运行测试/Exception测试等等，详细操作可以参考下列文档。目前我用到的就是简单的单元测试
。

一点资料：

  1. [DUnit 的官方地址](http://dunit.sourceforge.net/ )
  2. [DUnit 下载地址](http://sourceforge.net/projects/dunit/)
  3. [DUnit 官方文档（英文）](http://dunit.sourceforge.net/README.html)
  4. [DUnit 官方文档（繁体中文）](http://dunit.sourceforge.net/README_CHT.html)
  5. [『Delphi园地』-Delphi单元测试工具Dunit介绍](http://www.delphifans.com/infoview/Article_499.html)
  6. [Delphi单元测试工具Dunit介绍_51Testing软件测试网](http://www.51testing.com/html/32/297.html)

Delphi宝刀不老啊～呵呵～

