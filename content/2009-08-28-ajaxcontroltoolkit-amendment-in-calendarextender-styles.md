Title: AjaxControlToolkit中CalendarExtender样式修正
Author: alswl
Slug: ajaxcontroltoolkit-amendment-in-calendarextender-styles
Date: 2009-08-28 00:00:00
Tags: dotNet, AjaxControlToolkit, CSS
Category: Coding

在[The Official Microsoft ASP.NET Site](http://www.asp.net)上有一个很强大的控件[AJAX Control Toolkit](http://ajaxcontroltoolkit.codeplex.com/Release/ProjectRelease
s.aspx?ReleaseId=27326)，其功能非常完整，几乎涵盖了表现层方面各种应用，使用也很方便，有中文详细支持，能给程序员很大帮助。

我现在使用的其中一款控件叫做CalendarExtender，其实是一个DatePicker（日期选择器），这个控件可以直接在Input控件上添加「扩展程序
」，就完成了所有工作。

[![偏移](https://4ocf5n.dijingchao.com/upload_dropbox/200909/0e9aa6590cdc.jpg)](https://4ocf5n.dijingchao.com/upload_dropbox/200909/0e9aa6590cdc.jpg)

让我意外的是，这个控件在我的页面上工作时候样式似乎有些不正常。

页面漂移了！我仔细检查了FireBug，发现下面的样式中的padding影响了其td。(页面可不是我设计的```)

[![Firebug](https://4ocf5n.dijingchao.com/upload_dropbox/200909/Firebug.jpg)](https://4ocf5n.dijingchao.com/upload_dropbox/200909/Firebug.jpg)

如果修改CSS，就带来了大量的页面需要修改class/id，所以我只能修正CalendarExtender。（话说人家jQuery在这儿丝毫不受影响，全部元
素都覆盖了样式，AJAX Control Toolkit在样式上还是不如jQuery）

我在CalendarExtender外面包了一层div，再覆盖CalendarExtender的td属性。

Html代码：

    
    <div>
    <asp:TextBox ID="TbBirthday" runat="server"></asp:TextBox>
    <cc1:CalendarExtender ID="TbBirthday_CldEx" runat="server" Enabled="True" TargetControlID="TbBirthday" FirstDayOfWeek="Monday" Format="yyyy-MM-dd" PopupPosition="BottomRight">
    </cc1:CalendarExtender></div>

CSS代码：

    
    /*bugs for CalendarExtends*/
    .content .table .calendar td {/*.calender td 前的类是我网页中的上层元素*/
    margin: 0px;
    padding: 0px;
    }

这样一来，就可以解决这个问题了。

[![修正](https://4ocf5n.dijingchao.com/upload_dropbox/200909/e249092a13bc.jpg)](https://4ocf5n.dijingchao.com/upload_dropbox/200909/e249092a13bc.jpg)

最后，附送一个汉化控件的技巧：其实下载后，已经有语言包在下载包里面，之所以没有启用中文，是因为没有打开ScriptManager的全球化控制，把Script
Manager的EnableScriptGlobalization改为true即可。

Asp.NET代码：

    
    <asp:ScriptManager ID="ScriptManager1" runat="server" EnableScriptGlobalization="True">
    </asp:ScriptManager>

