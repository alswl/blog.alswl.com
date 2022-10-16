---
title: "CodeSmith使用心得"
author: "alswl"
slug: "codesmith"
date: "2011-02-26T00:00:00+08:00"
tags: ["工欲善其事必先利其器", "codesmith"]
categories: ["efficiency"]
---

CodeSmith是一款著名的代码生成器，可以帮助开发者完成一些重复性的劳动，并且能够保证更高的代码质量。CodeSmith使用Template（*.cst
）模板进行基础代码片段的定义，支持语言包括C#, Java, VB, PHP, ASP.NET, SQL等等。

![CodeSmith](../../static/images/upload_dropbox/201612/404.png)

## 一个简单的Sample

CodeSmith使用的模板使用方式类似于aspx/jsp页面，也就是基础代码+脚本的方式，大致代码如下（官方的sample2）。

    
    <%@ CodeTemplate Language="C#" TargetLanguage="Text" Description="This template demonstrates using properties in your template." %>
    <%@ Property Name="Person" Type="System.String" Description="This will show up at the bottom of the property grid when the property is selected." %>
    <%-- 
    This template demonstrates using properties in your template.
    --%>
    This is some static content (just like the static HTML in a ASP page).
    <%= "Hello " + this.Person + "!" %>
    This is more static content.
    

这个结构熟悉吧，几行代码分别表示模板属性，参数，脚本（注释），脚本（输出），静态文本。

通过上面这个例子可以直观看到CodeSmith使用方式，无非是在固有的代码片段上面进行一些动态的输出。

例子使用了一个名为Person的属性，其类型是String。在CodeSmith中，所有.net的基础属性都能够使用，除此之外，CodeSmith还封装了一
些特殊的属性类型，方便用户使用，像多行文本，文件选择，XML序列化文件、Key-Value键值对等等。

通过<%@ Assembly Name="SchemaExplorer" %>和<%@ Import Namespace="SchemaExplorer"
%>，我们能够使用自定义的dll和命名空间，托.net平台类库的福，系统的灵活性大大提高了。

## 数据接入

仅仅拥有上面这些特性，CodeSmith还不足以成为一个趁手的工具。真正让自定义功能发挥到极致的是CodeSmith中的SchemaExplorer。

SchemaExplorer的作用是给CodeSmith提供各类基础数据，比如字段的设计、表结构的设计。SchemaExplorer下面有两个比较常用的类，
TableSchema和ViewSchema，能够读取表信息和视图信息。

官方代码片段如下：

    
    <%@ Property Category="1.Database" Name="Tables" Optional="False"
        Type="SchemaExplorer.TableSchemaCollection" 
        Description="Database to create SQLite DDL from." %>
    <% foreach (TableSchema table in Tables) { %>
    -- Table <%= string.Format(EscapeFormat, table.Name) %> data
    <% string columnDefinition = BuildColumns(table); %>
    <% string tableName = BuildTableName(table); %>
    <% DataTable data = table.GetTableData(); %>
    <% foreach (DataRow row in data.Rows) { %>
    INSERT INTO <%= tableName %><%= columnDefinition %> VALUES (<%= BuildInsert(row) %>);
    <% } // for each row%>

<% } // for each table%>

上面代码通过便利Table，生成了一系列INSERT语句。

细心的童鞋可能发现了，描述中提到了"Database to create SQLite DDL from"，没错，通过SchemaExplorer，Code
Smith屏蔽了数据库差异，所以能够使用各大主流数据库，从MySQL到MSSQL，从SQLite到PostreSQL，并且，只要把提供实现了SechemaE
xplorer接口的dll放入CodeSmith/SchemaProviders目录下面，就能够理论上实现各种数据接入（其实。。。官方的SQLite接入都有
问题，反正我死活没成功，最后还是用了原生支持的MSSQL）。

## 我使用的数据接入

CodeSmith提供的SechemaExplorer虽然强大，但是却有一个弊端：它设计用来读取数据库结构，而不是其中的数据。TableSchema类型只提
供字段类型信息，而不提供具体数据内容。

我需要读取的数据并不是表结构，而是里面具体的数据，我需要根据这些数据生成具体代码，所以需求和CodeSmith的设计思路不一致，我早起使用了ViewSche
ma来曲线实现读取数据库内容的功能。（ViewSchema可以读取具体内容）

通过DataRow row in this.V_JOB.GetViewData().Rows，我可以获取视图里面所有数据列。这种方法比较取巧，缺点也显而易见
：每次不同的SQL需要定义一个额外的视图，很快我就放弃了这种办法。

最后我决定使用原生的SQL来获取数据，例子如下

    
    <%@ Assembly Name="Microsoft.ApplicationBlocks.Data" %>
    <%@ Import Namespace="System.Data" %>
    <%@ Import Namespace="System.Data.SqlClient" %>
    <%@ Import Namespace="Microsoft.ApplicationBlocks.Data" %>
    <%
    StringBuilder  sql = new StringBuilder();
    sql.Append("SELECT * n");
    sql.Append("FROM   TASK n");
    sql.Append("       LEFT  JOIN CONTROLER n");
    sql.Append("         ON TASK.guid = CONTROLER.taskGuid n");
    sql.AppendFormat("WHERE  TASK.confirmId = '{0}' n", ConfirmId);
    sql.AppendFormat("       AND TASK.id = '{0}' n", TaskId);
    sql.Append("       AND CONTROLER.bodyNo IS NULL n");
    sql.Append("        OR CONTROLER.bodyNo = 0 ");

SqlConnection connection = new SqlConnection(databaseSchema.ConnectionString);

connection.Open();

DataTable dataTable = SqlHelper.ExecuteDataset(connection, CommandType.Text,
sql.ToString()).Tables[0];

foreach (DataRow row in dataTable.Rows) {

} %>

这个例子就是引用原生的System.Data.SqlClient完成读数据，另外为了简化操作，我使用了微软的SqlHelper进行数据操作封装，即Micro
soft.ApplicationBlocks.Data这个类库。（SqlHelper可以在微软官网下载到）需要引用的类库记得放入CodeSmith/bin目
录下面。

最后，如果Template过于复杂，记得把Template进行分割成小模块，再使用Register关键字引用，以提高复用，DRY。

    
    <%@ Register Name="DscHideField" Template="../Controler/DscHideField.cs.cst" %>

相关链接

[CodeSmith官网](http://www.codesmithtools.com/)

[CodeSmith 介绍 - 代码生成之路 - 博客园](http://www.cnblogs.com/lxf120/archive/2007/04/03
/698707.html)里面有个很详细的Tutorial

[CodeSmith开发系列资料总结 - TerryLee's Tech
Space](http://terrylee.cnblogs.com/archive/2005/12/28/306254.aspx) -
博客园李银河的CodeSmith系列文章，有几个高级议题

