---
title: "MemberShip在动软生成器下UserId的问题"
author: "alswl"
slug: "membership-moving-soft-issue-of-builder-under-the-userid"
date: "2009-10-23T00:00:00+08:00"
tags: ["dotnet", "codematic", "membership"]
categories: ["coding"]
---

## 背景

这个月的课程设计我抽签是「房屋销售系统」，一个比较简单的类CMS系统。考虑到时间的因素，我放弃了Python in Django，而是选择了我相对熟悉的.N
ET平台。我使用的主要工具是[动软.NET代码生成器](http://www.maticsoft.com/)(一个很强大的.NET代码生成器)+Member
Ship(微软推出的一个Asp.NET的权限系统)。

我之前只是对MemberShip略有耳闻，动软也是用过几次，所以在一个星期内完成这个课程设计还是比较冒险的。呃```呵呵，这也比较符合我的风格，总是要学点东
西的嘛。

## 问题

MemberShip本身是一个很强大的权限管理系统，其中UserId使用的是uniqueidentifier这种值类型，对应到微软提出的一种标示类型GUID
(System.GUID)。这是一种类似「9498ea1f-ce4e-4e6d-b636-1bbbe3db9bde」的非字符串。

动软.NET代码生成器会根据建好的数据库生成相应的代码，可以选择三层模式（BLL+DAL+Model+Web），他会自动生成每层代码。一般来说，生成的项目可
以编译完成，但是如果在其中存在uniqueidentifier这种类型的表，就会产生错误，无法通过编译，错误「找不到类型或命名空间名称「uniqueiden
tifier」（是否缺少 using 指令或程序集引用？）」

## 解决

资料非常少，否则我就不会写日志了，直接转载了。

参考一些零星的帖子+自己尝试，我把解决方法总结如下。

1.修改Model中uniqueidentifier类型，因为C#中根本不存在这种类型，将相应的变量类型定义为Guid。

    
    private Guid _userid;

public Guid userId

{ set{ _userid=value;}

get{return _userid;}

} 2.修改相应的Guid<->string之间的转换，这个根据错误列表一一修改即可。

    
    this.lbluserId.Text=model.userId.ToString();//Guid拥有.ToString()方法
    model.userId = new Guid(userId)//new Guid(string)

3.修改DAL中数据读取/写入部分，其实这一部分还是Guid<->string转换

    
    //model.userId=ds.Tables[0].Rows[0]["userId"].ToString();
    //原始的加上了注释
    model.userId=new Guid(ds.Tables[0].Rows[0]["userId"].ToString());
    //使用new Guid(string)进行转换

经过上面3个部分，代码应该基本没有问题了，其实关键的还是Guid<->string转换，跟着错误列表走一边就基本没有问题了。

## 新的问题

发现用动软生成的Web层中的Add.aspx文件中，如果相对应数据库表有DataTime字段，就会运行时错误「基类包括字段「txtdatetime」，但其类
型(System.Web.UI.WebControls.TextBox)与控件(System.Web.UI.HtmlControls.HtmlInputTe
xt)的类型不兼容。」。

我将<INPUT >中id修改后，能够运行Add.aspx，但是还是无法post提交，我正在尝试解决这个问题。这个问题与MemberShip无关，放在这里只
是希望如果有过客了解Asp.NET，那么就提出一些建议。

## 相关链接

GUID_百度百科：[http://baike.baidu.com/view/185358.htm](http://baike.baidu.com/view/185358.htm)

SQL中的uniqueidentifier类型在c#中用什么类型表示：[http://topic.csdn.net/t/20060918/17/5030341.html](http://topic.csdn.net/t/20060918/17/5030341.html)

关于ASP.NET中C#处理uniqueidentifier数据类型的问题：[http://topic.csdn.net/u/20070517/17/9744a192-a062-4c51-bdf7-273b1480c1d6.html](http://topic.csdn.net/u/20070517/17/9744a192-a062-4c51-bdf7-273b1480c1d6.html)

