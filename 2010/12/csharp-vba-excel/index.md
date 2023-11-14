

Excel在日常办公中应用非常广泛，这次我接到一个案子，需要往Excel中写入数据并能够打印出固定格式，前前后后大概花了将近2星期才搞定，现在做一些分享。

## 一、关于操作Excel的几种方式

我们导出Excel，大抵是有两种方法，一种是在服务器端用一些类库或者COM组件直接生成Excel成品，其二是在后台只写入数据，而不写入具体格式，等用户下载完
Excel之后再在客户端上利用vba生成Excel成品。

### 1.1使用"自动化"功能-后台生成成品

微软把后台使用COM组件称之为"自动化"，其实它本身是不建议这种用法，在[257757 号文章（服务器端 Office自动化注意事项）](http://support.microsoft.com/kb/257757)也明文标出"Microsoft
目前建议不要从任何无人参与的、非交互式客户端应用程序或组件（包括 ASP、DCOM 和 NT Service）中进行 Microsoft Office
应用程序的"自动化"，也不为此提供支持，因为 Office 在这种环境中运行时可能会出现不稳定的现象并且/或者会死锁。"

这种方法的优点是给用户更简洁的展现，毕竟原生的Excel成品比半成品来更容易接受，而且可以避免宏安全问题，万一客户端禁止了宏，就只能看到丑陋的模板界面+一坨
数据。

缺点是需要服务端支持，编写成本也比较高（VBA有时候可以直接录制）。服务端支持体现在需要安装一些微软或者第三方的类库。我当时采用的是Office类库，也就是
在安装有Office的机器上面使用Interop.Excel.dll这个中间动态链接库进行操作，需要麻烦的安全设置，效率低不说还会扯出Excel无法关闭的B
ug。

关于效率低我深有体会，我使用这种方法生成5页数据大约2m，客户等的急死，其根本原因是由于COM组件在调用时候，每一个Range这种对象都会产生一个借口请求。

### 1.2、使用ADO.net传输数据+VBA控制模板和数据

这方法的优缺点正好与上文相反，由于只是写入数据，即通过ADO.net的连接方式INSERT一堆数据到Excel文件的隐藏Sheet里面去（别跟我说你不知道E
xcel可以隐藏某个Sheet），所以速度后台速度极快。前台Excel文件虽然需要VBA编程支持，但是在理解Excel模型之后也不是很难的事情。

### 1.3

选择哪种方式，取决于你的需求，如果你在Java平台下面并且输出文件页面格式不复杂，我推荐第一种，如果是.net平台又或者要处理复杂的页面样式，就选用第二种吧
（我前期使用第一种，后来因为效率问题和无法关闭Excel的问题，重写逻辑，选用第二种）。

关于Excel导出方案的选择，微软官方也是不建议使用第一种方案，甚至不提供技术支持。它推荐了一些方案，包括使用报表导出Excel或者ADO.net方式导出（
即第二种），具体文章见[如何使用 Visual C# 2005 或 Visual C# .NET 向 Excel 工作簿传输数据](http://support.microsoft.com/kb/306023/zh-cn)。

## 二、Office Excel文档模型

在写操作Excel代码之前，需要了解一下Excel的文档模型，才能想当然的把代码写出来。

简单说来，我们只要了解Application 、Workbook 、Worksheet
、Range这四种类型，如果需要操作图像的话，还需要多了解一种Chart。

Application就是Excel实例，不仅仅是一个Excel文件，而是整体的Excel程序（Office都是MDI文档体系）。

WorkBook就是实质意义上的某个Excel文件，你可以进行保存操作等等。

Worksheet是某个工作簿类型。

Range是我们打交道最多的，可以理解成一个区域快，也就是常见的"A2:B5"这种表示方式。

了解这几种之后，我们就可以下手操作了。更详细的微软官方文档，可以在[Excel 对象模型概述](http://msdn.microsoft.com/zh-cn/library/wss56bz7(v=vs.80).aspx)找到。

## 三、使用C#操作Excel

我虽然不推荐第一种，但是毕竟是一种解决方案。

需要使用的命名空间为using Excel = Microsoft.Office.Interop.Excel;（使用别名简化一下）

另外需要项目引用Office的类库，如果不是项目形式而是网站形式，则需要手动编译对应Interop.Excel.dll到网站bin目录下面，我使用Excel
2007编译出这个链接库，版本为1.6.0.0，需要的可以点击[Interop.Excel.dll](../../static/images/2010/12/Interop_Excel.zip)下载。

### 3.1 编译Interop.Excel.dll

编译的方法出自于"[使用Office组件读取Excel，引用Microsoft.Office.Interop.Excel出现的问题](http://www.
cnblogs.com/Mainz/archive/2009/11/11/Microsoft_Office_Interop_Excel.html)"&nbs
p_place_holder;

> 进入你的visual studio的sdk下的bin目录，找到TlbImp.exe文件，如果没有，请用光盘安装此文件，详细说明请参照MSDN。&nbsp
_place_holder;

命令行(cmd)进入bin目录，运行TlbImp /out:Interop.Excel.dll
Office安装目录+Excel.exe

此时很可能会报错：TlbImp  error:  Unable
 to  locate  input
 type  library: 
'c:program filesmcrosoft officeofficeEXCEL.EXE'

>

> 此问题很有可能是TlbImp的bug，不支持空格式的路径；（具体原因不明）不要紧，将Excel.exe拷贝入bin目录，直接运行TlbImp
/out:Interop.Excel.dll Excel.exe,提示"Type library imported to
Interop.Excel.dll路径"

>

> 在bin目录下找到Interop.Excel.dll文件。在你的visual studio里将其引用即可。

### 3.2 封装的一个C#操作Excel类库

我把我之前封装的C#操作Excel类库分享一下

注：这个类的Dispose仍然没有解决Excel文件生成之后Excel进程无法正常关闭的问题，目前看来只有杀死进程方法才能起实质性作用。

其实我觉得这个类库除了让我熟悉一下Excel模型之外，并没派上实质的用场~


    /// <summary>
    /// Excel帮助类
    /// Add by alswl 20101130
    /// </summary>
    public class ExcelHelper : IDisposable
    {
        private Excel._Application excelApplication = null;
        public Excel._Workbook workbook = null;
        public Excel._Worksheet worksheet = null;
        private object missing = System.Reflection.Missing.Value;

public ExcelHelper()

{

if (excelApplication == null)

{

excelApplication = new Excel.ApplicationClass();

}

}

/// <summary>

/// ~

/// </summary>

~ExcelHelper()

{

if (excelApplication != null)

excelApplication.Quit();

}

/// <summary>

/// 释放非托管资源

/// </summary>

public void Dispose()

{

try

{

if (excelApplication != null)

{

if (!workbook.Saved)

this.Close(false);

excelApplication.Quit();

System.Runtime.InteropServices.Marshal.ReleaseComObject(worksheet);

System.Runtime.InteropServices.Marshal.ReleaseComObject(workbook);

System.Runtime.InteropServices.Marshal.ReleaseComObject(excelApplication);

GC.Collect(System.GC.GetGeneration(worksheet));

GC.Collect(System.GC.GetGeneration(workbook));

GC.Collect(System.GC.GetGeneration(excelApplication));

if (excelApplication != null)

{

excelApplication = null;

}

GC.WaitForPendingFinalizers();

GC.Collect();

GC.WaitForPendingFinalizers();

GC.Collect();

}

}

catch

{

}

finally

{

GC.Collect();

}

}

/// <summary>

/// 设置当前工作表

/// </summary>

public int CurrentWorksheetIndex

{

set

{

if (value <= 0 || value > workbook.Worksheets.Count)

throw new ArgumentException("索引超出范围");

else

{

object index = value;

worksheet = workbook.Worksheets[index] as Excel._Worksheet;

}

}

}

/// <summary>

/// 打开一个Excel工作薄

/// </summary>

/// <param name="fileName"></param>

public void OpenWorkbook(string fileName)

{

workbook = excelApplication.Workbooks.Open(fileName, missing, missing,
missing, missing, missing,

missing, missing, missing, missing, missing, missing, missing, missing,
missing);

if (workbook.Worksheets.Count > 0)

{

int index = 1;

worksheet = workbook.Worksheets[index] as Excel._Worksheet;

}

}

/// <summary>

/// 添加一个工作表

/// </summary>

/// <param name="SheetName"></param>

/// <returns></returns>

public Excel.Worksheet AddSheet(string sheetName)

{

Excel.Worksheet worksheet =
(Excel.Worksheet)workbook.Worksheets.Add(Type.Missing, Type.Missing,
Type.Missing, Type.Missing);

worksheet.Name = sheetName;

return worksheet;

}

/// <summary>

/// 删除一个Sheet

/// </summary>

/// <param name="sheetName"></param>

public void DeleteSheet(string sheetName)

{

Excel.Worksheet sheet = workbook.Worksheets[sheetName] as Excel.Worksheet;

excelApplication.DisplayAlerts = false;

sheet.Delete();

excelApplication.DisplayAlerts = true;

}

/// <summary>

/// 保存数据

/// </summary>

public void Save()

{

if (workbook != null)

{

workbook.Save();

}

}

/// <summary>

/// 关闭文档

/// </summary>

/// <param name="isSave"></param>

public void Close(bool isSave)

{

object obj_Save = isSave;

workbook.Close(obj_Save, missing, missing);

}

/// <summary>

/// 设置当前工作表中某单元格的值

/// </summary>

/// <param name="range"></param>

/// <param name="value"></param>

public void SetRangeValue(string range, object value)

{

SetRangeValue(worksheet.Name, range, value);

}

/// <summary>

/// 设置工作表中某单元格的值

/// </summary>

/// <param name="sheetName"></param>

/// <param name="range"></param>

/// <param name="value"></param>

public void SetRangeValue(string sheetName, string range, object value)

{

Excel.Worksheet sheet = workbook.Worksheets[sheetName] as Excel.Worksheet;

sheet.get_Range(range, missing).Value2 = value;

}

/// <summary>

/// 删除某个Range，右侧左移

/// </summary>

/// <param name="sheetName"></param>

/// <param name="rangeStr"></param>

public void DeleteRange(string sheetName, string rangeStr)

{

Excel.Worksheet sheet = workbook.Worksheets[sheetName] as Excel.Worksheet;

sheet.get_Range(rangeStr,
missing).Delete(Excel.XlDeleteShiftDirection.xlShiftToLeft);

}

/// <summary>

/// 删除某个Range，右侧左移

/// </summary>

/// <param name="sheetName"></param>

/// <param name="rangeStr"></param>

public void DeleteRange(string rangeStr)

{

DeleteRange(worksheet.Name, rangeStr);

}

/// <summary>

/// 合并单元格

/// </summary>

/// <param name="sheetName"></param>

/// <param name="range1"></param>

/// <param name="range2"></param>

public void Merge(string sheetName, string range1, string range2)

{

Excel.Worksheet sheet = workbook.Worksheets[sheetName] as Excel.Worksheet;

Excel.Range range = worksheet.get_Range(range1, range2);

range.Merge(true);

}

/// <summary>

/// 合并单元格

/// </summary>

/// <param name="range1"></param>

/// <param name="range2"></param>

public void Merge(string range1, string range2)

{

Merge(worksheet.Name, range1, range2);

}

/// <summary>

/// 设置一个单元格的属性

/// </summary>

/// <param name="sheetName"></param>

/// <param name="range"></param>

/// <param name="size">大小</param>

/// <param name="name">字体</param>

/// <param name="color">颜色</param>

/// <param name="HorizontalAlignment">对齐方式</param>

public void SetCellProperty(string sheetName, string rangeStr, double
fontSize, string fontName,

double height, Excel.Constants horizontalStyle)

{

Excel.Worksheet sheet = workbook.Worksheets[sheetName] as Excel.Worksheet;

Excel.Range range = sheet.get_Range(rangeStr, missing);

range.Font.Size = fontSize;

range.Font.Name = fontName;

//range.Font.Color = fontColor;

range.RowHeight = height;

range.HorizontalAlignment = horizontalStyle;

}

/// <summary>

/// 设置一个单元格的属性

/// </summary>

/// <param name="range"></param>

/// <param name="fontSize"></param>

/// <param name="fontName"></param>

/// <param name="fontColor"></param>

/// <param name="horizontalStyle"></param>

public void SetCellProperty(string range, double fontSize, string fontName,

double height, Excel.Constants horizontalStyle)

{

SetCellProperty(worksheet.Name, range, fontSize, fontName,

height, horizontalStyle);

}

/// <summary>

/// 设定Range的边框格式

/// </summary>

/// <param name="rangeStart"></param>

/// <param name="rangeEnd"></param>

/// <param name="topStyle"></param>

/// <param name="rightStyle"></param>

/// <param name="bottomStyle"></param>

/// <param name="leftStyle"></param>

public void SetRangeBorderStyle(string sheetName, string rangeStr,
Excel.XlLineStyle topStyle,

Excel.XlLineStyle rightStyle, Excel.XlLineStyle bottomStyle, Excel.XlLineStyle
leftStyle)

{

Excel.Worksheet sheet = workbook.Worksheets[sheetName] as Excel.Worksheet;

Excel.Range range = sheet.get_Range(rangeStr, missing);

range.Borders[Microsoft.Office.Interop.Excel.XlBordersIndex.xlEdgeTop].LineSty
le = topStyle;

range.Borders[Microsoft.Office.Interop.Excel.XlBordersIndex.xlEdgeRight].LineS
tyle = rightStyle;

range.Borders[Microsoft.Office.Interop.Excel.XlBordersIndex.xlEdgeBottom].Line
Style = bottomStyle;

range.Borders[Microsoft.Office.Interop.Excel.XlBordersIndex.xlEdgeLeft].LineSt
yle = leftStyle;

}

/// <summary>

/// 设定Range的边框格式

/// </summary>

/// <param name="rangeStr"></param>

/// <param name="topStyle"></param>

/// <param name="rightStyle"></param>

/// <param name="bottomStyle"></param>

/// <param name="leftStyle"></param>

public void SetRangeBorderStyle(string rangeStr, Excel.XlLineStyle topStyle,

Excel.XlLineStyle rightStyle, Excel.XlLineStyle bottomStyle, Excel.XlLineStyle
leftStyle)

{

SetRangeBorderStyle(worksheet.Name, rangeStr, topStyle,

rightStyle, bottomStyle, leftStyle);

}

/// <summary>

/// 设定Range数字格式

/// </summary>

/// <param name="sheetName"></param>

/// <param name="rangeStr"></param>

/// <param name="format"></param>

public void SetRangeNumberFormat(string sheetName, string rangeStr, string
format)

{

Excel.Worksheet sheet = workbook.Worksheets[sheetName] as Excel.Worksheet;

Excel.Range range = sheet.get_Range(rangeStr, missing);

range.NumberFormat = format;//0%

}

/// <summary>

/// 设定Range数字格式

/// </summary>

/// <param name="rangeStr"></param>

/// <param name="format"></param>

public void SetRangeNumberFormat(string rangeStr, string format)

{

SetRangeNumberFormat(worksheet.Name, rangeStr, format);

}

/// <summary>

/// 将数据表格添加到Excel指定工作表的指定位置

/// </summary>

/// <param name="dt"></param>

/// <param name="ws"></param>

/// <param name="startX"></param>

/// <param name="startY"></param>

public void AddTable(System.Data.DataTable dt, int startX, int startY)

{

for (int i = 0; i <= dt.Rows.Count - 1; i++)

{

for (int j = 0; j <= dt.Columns.Count - 1; j++)

{

worksheet.Cells[i + startX, j + startY] = dt.Rows[i][j];

}

}

}

/// <summary>

/// 加入分页符

/// </summary>

/// <param name="rangeStr"></param>

/// <param name="lineNumber"></param>

public void AddPageBreak(string rangeStr, int lineNumber)

{

Excel.Range range = worksheet.get_Range("A" + lineNumber.ToString(), missing);

worksheet.HPageBreaks.Add(range);

}

/// <summary>

/// 加入分页符

/// </summary>

/// <param name="lineNumber"></param>

public void AddPageBreak(int lineNumber)

{

AddPageBreak(worksheet.Name, lineNumber);

}

/// <summary>

/// 从当前工作表数据区域复制数据到另一个区域

/// </summary>

/// <param name="sheetFromRange"></param>

/// <param name="sheetToRange"></param>

public void CopyRange2Range(string sheetFromRange, string sheetToRange)

{

CopyRange2Range(worksheet.Name, worksheet.Name, sheetFromRange, sheetToRange);

}

/// <summary>

/// 从一个表的某个数据区域复制数据到另一个表的某个区域

/// </summary>

/// <param name="sheetFromName"></param>

/// <param name="sheetToName"></param>

/// <param name="sheetFromRange"></param>

/// <param name="sheetToRange"></param>

public void CopyRange2Range(string sheetFromName, string sheetToName, string
sheetFromRange, string sheetToRange)

{

Excel.Worksheet sheetFrom = workbook.Worksheets[sheetFromName] as
Excel.Worksheet;

Excel.Worksheet sheetTo = workbook.Worksheets[sheetToName] as Excel.Worksheet;

sheetFrom.get_Range(sheetFromRange,
missing).Copy(sheetTo.get_Range(sheetToRange, missing));

}

/// <summary>

/// 移动Range到另一个Range

/// </summary>

/// <param name="FromRange"></param>

/// <param name="ToRange"></param>

public void MoveRange2Range(string FromRange, string ToRange)

{

MoveRange2Range(worksheet.Name, FromRange, ToRange);

}

/// <summary>

/// 移动Range到另一个Range

/// </summary>

/// <param name="sheetName"></param>

/// <param name="FromRange"></param>

/// <param name="ToRange"></param>

public void MoveRange2Range(string sheetName, string FromRange, string
ToRange)

{

Excel.Worksheet sheet = workbook.Worksheets[sheetName] as Excel.Worksheet;

sheet.get_Range(FromRange, missing).Cut(sheet.get_Range(ToRange, missing));

}

/// <summary>

/// 重设当前工作目录的打印区域

/// </summary>

public void ResetPrintArea()

{

SetPrintArea(worksheet.Name, "");

}

/// <summary>

/// 重设工作目录的打印区域

/// </summary>

public void ResetPrintArea(string sheetName)

{

SetPrintArea(sheetName, "");

}

/// <summary>

/// 设定工作目录的打印区域

/// </summary>

/// <param name="area"></param>

public void SetPrintArea(string area)

{

SetPrintArea(worksheet.Name, area);

}

/// <summary>

/// 设定工作目录的打印区域

/// </summary>

/// <param name="sheetName"></param>

/// <param name="area"></param>

public void SetPrintArea(string sheetName, string area)

{

Excel.Worksheet sheet = workbook.Worksheets[sheetName] as Excel.Worksheet;

sheet.PageSetup.PrintArea = area;

}

/// <summary>

/// 将当前工作表中的表格数据复制到剪切板

/// </summary>

public void Copy()

{

if (worksheet != null)

{

try

{

worksheet.UsedRange.Select();

}

catch { }

worksheet.UsedRange.Copy(missing);

}

}

}

## 四、使用ADO.net+VBA操作Excel

我手头的这个案子在用第一种方法撰写一个星期之后遇到效率瓶颈，无奈改为第二种方法，由于对Excel的文档模型有了较全面的认识，几个主流函数也很清楚，所以写的速
度很快。

这里我还是要佩服一下微软，曾经我对Office很不屑，后来看完《[Word排版艺术](http://book.douban.com/subject/1193
565/)》才开始认识Office，再之后深入PPT和Excel，更是感觉文档模型了不起。。。咳咳咳，扯远了~

### 4.1 使用ADO.net写入数据到Excel文件

废话不说了，上核心代码


    System.Data.OleDb.OleDbConnection objConn = new System.Data.OleDb.OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" +
                        destFileName + ";Extended Properties=Excel 8.0;");
    objConn.Open();

System.Data.OleDb.OleDbCommand objCmd = new System.Data.OleDb.OleDbCommand();

objCmd.Connection = objConn;

foreach (DataRow row in dt.Rows)

{ StringBuilder stringBuilder = new StringBuilder();

stringBuilder.AppendFormat("INSERT INTO [{0}$] (", sheetName);

for (int i = 0; i < dt.Columns.Count; i++)

{

if (i < dt.Columns.Count - 1)

stringBuilder.Append(dt.Columns[i].ColumnName + ",");

else

stringBuilder.Append(dt.Columns[i].ColumnName + ") VALUES (");

}

for (int i = 0; i < dt.Columns.Count; i++)

{

if (i < dt.Columns.Count - 1)

stringBuilder.Append("@" + dt.Columns[i].ColumnName + ",");

else

stringBuilder.Append("@" + dt.Columns[i].ColumnName + ");");

}

objCmd.Parameters.Clear();

for (int i = 0; i < dt.Columns.Count; i++)

{

objCmd.Parameters.Add(dt.Columns[i].ColumnName, row[i]);

}

objCmd.CommandText = stringBuilder.ToString();

objCmd.ExecuteNonQuery();

}

注意点就是INSERT的表明就是Sheet的名字加上中括号和$符号。

### 4.2 使用VBA操作模板和数据

使用VBA操作模板和数据的过程是一个assign的过程，就是把数据和模板杂糅起来，类似于MVC中C控制M输出到V中，我建议针对不同类型的页面制作多个模板，而
不要使用VBA进行各种样式修改操作，减少代码量。我这个案子中使用了8个不同类型模板，毕竟直接使用鼠标拖拽出一个模板比用VBA代码修改处一个模板简单的多。

Excel2007的VBA界面在"开发工具"-"Visual
Basic"中打开，千万不要以为写VBA就是录制宏呀~另外附赠一个小技巧，在VBA编辑界面里面使用Ctrl+J可以自动补全，相当实用。

我把项目分成5个模块：Golbal 、Init 、Insert 、Finalize
、Utils，看名字就知道意思了，其中Utils包含一个中文大写数字转换的函数，供前面使用。

我们需要在Excel自动打开时候进行操作，需要使用函数Workbook_Open，另有Auto_Open，两个有不同之处，可以Google之。

启用代码如下：


    '开启工作簿时候动作
    Private Sub Workbook_Open()
        
        MAIN_SHEET = "报价模板"
        For Each Sheet In Sheets
            If Sheet.Name = MAIN_SHEET Then
                Exit Sub
            End If
        Next
        If Sheets("OPTION").Range("B2").Value = "" Then '如果不存在DH行数，则退出
            Exit Sub
        End If
        
        MsgBox ("初始化数据，请稍等片刻！")
        Call Run
        Call DeleteSheets
        'Call ActiveWorkbook.Save
        MsgBox ("初始化数据完成，请保存Excel文件！")

End Sub

核心代码的话。。。其实没什么核心代码，就是频繁的使用赋值和Copy函数。。。。

## 五、相关资料链接

[C#操作Excel开发报表系列整理](http://www.cnblogs.com/dahuzizyd/archive/2007/04/11/CSharp
_Excel_Report_Chart_All.html)

[检索 COM 类工厂中 CLSID 为 {00024500-0000-0000-C000-000000000046} 的组件时失败，原因是出现以下错误:
80070005](http://www.cnblogs.com/HQT/archive/2006/05/22/406345.html)

PS:8000401a的错误会在服务器上出现，不会在xp上出现，原因是交互式用户也没有Excel操作权限，这时候要给Excel手动制动一个有Excel操作权
限用户，比如administrator。

[Office编程在dot Net环境中总结(Excel篇)](http://archive.cnblogs.com/a/567305/)

好了，这就是我这次Excel学习的分享，谢谢大家耐着性子看完~


