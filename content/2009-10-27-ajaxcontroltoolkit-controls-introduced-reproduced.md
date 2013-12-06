Title: AjaxControlToolKit控件介绍[转载]
Author: alswl
Slug: ajaxcontroltoolkit-controls-introduced-reproduced
Date: 2009-10-27 00:00:00
Tags: AjaxControlToolkit
Category: Microsoft .Net
Summary: 

来源：[ajax toolkit 控件介绍 - 欢迎来到哈哈的天堂 - 博客园](http://www.cnblogs.com/haha8/archive/
2009/09/26/1574412.html)（只是来源，感觉不是这个博客原创，作者应该未知）

文字太多了，所以我没有把代码提取到代码段，只是把标题提出来了，大家不要介意啊…^_^

### 1.Accordion

   功能：实现了QQ、Msn好友分类的折叠效果，就像包含了多个CollapsiblePanels

   细节： (1)不要把Accordion放在Table种同时又把 FadeTransitions 设置为True，这将引起布局混乱

                (2)每一个 AccordionPane control 有一个Header 和Content的 template

                (3)在Content中可以进行任意扩展，你什么都可以放上^_^

                (4)有三种AutoSize modes ：None(推荐) Limit  Fill

                (5)Accordion表现的更像是一个容器

  代码示意：

      <ajaxToolkit:Accordion ID="MyAccordion" runat="server" SelectedIndex="0"
HeaderCssClass="accordionHeader"

            ContentCssClass="accordionContent" FadeTransitions="false"
FramesPerSecond="40"

            TransitionDuration="250" AutoSize="None">

            <Panes>

                <ajaxToolkit:AccordionPane ID="AccordionPane1" runat="server">

                    <Header>

                        <a href="" onclick="return false;"
class="accordionLink">1. Accordion</a></Header>

                    <Content>

                    </Content>

                </ajaxToolkit:AccordionPane>

            </Panes>

        </ajaxToolkit:Accordion>

### 2. AlwaysVisibleControl

    功能：最多的应用是在线小说的目录和不胜其烦的浮动小广告

   细节： (1)避免控件闪烁，把这个控件要在目标位置时使用absolutely position

                (2) HorizontalSide="Center" VerticalSide="Top" 使用这个方法控制浮动在什么位置

代码示意：

    <cc1:AlwaysVisibleControlExtender ID="AlwaysVisibleControlExtender1"
HorizontalSide="Center" VerticalSide="Top"  TargetControlID="Panel1"
runat="server">

### 3.Animation

   功能：28个控件种效果最酷的！顾名思义实现动画效果

   细节： (1)不只是控件：pluggable, extensible framework

                (2)用在什么时候：OnLoad  OnClick  OnMouseOver OnMouseOut OnHoverOver
OnHoverOut

                (3)具体使用有很多可以谈的，有理由单独写一个Animation Xml 编程介绍

  代码示意：

   <ajaxToolkit:AnimationExtender ID="ae"

  runat="server" TargetControlID="ctrl">

    <Animations>

        <OnLoad>  </OnLoad>

        <OnClick>  </OnClick>

        <OnMouseOver>  </OnMouseOver>

        <OnMouseOut>  </OnMouseOut>

        <OnHoverOver>  </OnHoverOver>

        <OnHoverOut>  </OnHoverOut>

    </Animations>

</ajaxToolkit:AnimationExtender>

### 4.CascadingDropDown

   功能：DropDownList联动，调用Web Service

   细节： (1)DropDownList行为扩展

                (2)如果使用Web service 方法签名必须符合下面的形式：

                [WebMethod]

                public CascadingDropDownNameValue[] GetDropDownContents(

                string knownCategoryValues, string category){...}

代码示意：

                 <ajaxToolkit:CascadingDropDown ID="CascadingDropDown1"
runat="server" TargetControlID="DropDownList1" Category="Make"
PromptText="Please select a make"  LoadingText="[Loading makes]"
ServicePath="CarsService.asmx" ServiceMethod="GetDropDownContents"/>

                <ajaxToolkit:CascadingDropDown ID="CascadingDropDown2"
runat="server" TargetControlID="DropDownList2" Category="Model"
PromptText="Please select a model" LoadingText="[Loading models]"
ServiceMethod="GetDropDownContentsPageMethod"
ParentControlID="DropDownList1"/>

                <ajaxToolkit:CascadingDropDown ID="CascadingDropDown3"
runat="server" TargetControlID="DropDownList3" Category="Color"
PromptText="Please select a color" LoadingText="[Loading colors]"
ServicePath="~/CascadingDropDown/CarsService.asmx"
ServiceMethod="GetDropDownContents" ParentControlID="DropDownList2"/>

###    5.CollapsiblePanel

   功能：Xp任务栏折叠效果

   细节： (1)可以扩展任何一个 ASP.NET Panel control

                (2) CollapsiblePanel 默认认为使用了 标准 CSS box model 早期的浏览器要!DOCTYPE
中设置页面为自适应方式提交数据rendered in IE's standards-compliant mode.

代码示意：

   <ajaxToolkit:CollapsiblePanelExtender ID="cpe" runat="Server"

    TargetControlID="Panel1"

    CollapsedSize="0"

    ExpandedSize="300"

    Collapsed="True"

    ExpandControlID="LinkButton1"

    CollapseControlID="LinkButton1"

    AutoCollapse="False"

    AutoExpand="False"

    ScrollContents="True"

    TextLabelID="Label1"

    CollapsedText="Show Details"

    OpenedText="Hide Details"

    ImageControlID="Image1"

    ExpandedImage="~/images/collapse.jpg"

    CollapsedImage="~/images/expand.jpg"

    ExpandDirection="Height"/>

###    6.ConfirmButton

   功能：就是弹出来一个确定对话框

   细节： 本人认为不是最简单实现的方法，我的方法：

   this.Button1.Attributes["onclick"]="javascript:return
confirm('确定要停止下载么？');";

      不知道是不是我没有发现这个控件的其它优势。

### 7.DragPanel

   功能：页面拖动

   细节： (1)TargetControlID 要拖动的控件

                (2)DragHandleID   拖动的标题栏所在的ControlID

代码示意

<ajaxToolkit:DragPanelExtender ID="DPE1" runat="server"

    TargetControlID="Panel3"

    DragHandleID="Panel4" />

### 8.DropDown

   功能：什么都可以以下拉菜单的形式弹出来

   细节： (1)TargetControlID要在什么控件上实现扩展

                (2)DropDownControlID弹出来什么

代码示意：

  <asp:Panel ID="DropPanel" runat="server" CssClass="ContextMenuPanel"
Style="display: none;

            visibility: hidden;">

             <asp:LinkButton runat="server" ID="Option1" Text="Option 1"
CssClass="ContextMenuItem"

                OnClick="OnSelect" />

            <asp:LinkButton runat="server" ID="Option2" Text="Option 2"
CssClass="ContextMenuItem"

                OnClick="OnSelect" />

            <asp:LinkButton runat="server" ID="Option3" Text="Option 3 (Click
Me!)" CssClass="ContextMenuItem"

                OnClick="OnSelect" />

        </asp:Panel>

        <cc1:DropDownExtender runat="server" ID="DDE"
TargetControlID="TextLabel"

            DropDownControlID="DropPanel" />

### 9.DropShadow

   功能：阴影效果，其实可以放给美工实现

   细节： (1)Width 单位：px  默认5px

                (2)Opacity  不透明度0-1.0 默认.5

  代码示意：

    <ajaxToolkit:DropShadowExtender ID="dse" runat="server"

        TargetControlID="Panel1"

        Opacity=".8"

        Rounded="true"

        TrackPosition="true" />

### 10.DynamicPopulate

   功能：能实用Web Service或页面方法来替换控件的内容

   细节： (1)ClearContentsDuringUpdate  替换之前先清除以前的内容（默认True）

                (2)PopulateTriggerControlID 触发器绑定的控件 单击时触发

                (3)ContextKey传递给Web Service的随机字符串

                (4) Web Service方法签名必须符合下面的形式：

                [WebMethod]

                string DynamicPopulateMethod(string contextKey)

                {...}

                Note you can replace "DynamicPopulateMethod" with a naming of
your choice, but the return

                type and parameter name and type must exactly match, including
case.

代码示意：

<ajaxToolkit:DynamicPopulateExtender ID="dp" runat="server"

    TargetControlID="Panel1"

    ClearContentsDuringUpdate="true"

    PopulateTriggerControlID="Label1"

    ServiceMethod="GetHtml"

    UpdatingCssClass="dynamicPopulate_Updating" />

### 11.FilteredTextBox

   功能：文本框数据过滤

   细节： (1)过滤条件Numbers LowercaseLetters UppercaseLetters   Custom

                (2)过滤条件也可以是Custom的组合 FilterType="Custom, Numbers"

                (3)ValidChars="+-=/*()." Custom要定义这样的有效字符串

                (4) 其实这是个鸡肋：你可以输入中文，聊胜于无，忍了

示意代码：

<ajaxToolkit:FilteredTextBoxExtender ID="ftbe" runat="server"

        TargetControlID="TextBox3"

        FilterType="Custom, Numbers"

        ValidChars="+-=/*()." />

### 12.HoverMenu

   功能：鼠标靠近时显示菜单，可以用在在线数据修改的表格上作为功能菜单

   细节： (1)PopupControlID要弹出来什么

                (2)PopupPostion 在哪里弹出来Left (Default), Right, Top, Bottom,
Center.

                (3)OffsetX/OffsetY 弹出项与源控件的距离

                (4) PopDelay 弹出延时显示 单位milliseconds. Default is 100.

代码示意：

<ajaxToolkit:HoverMenuExtender ID="hme2" runat="Server"

    TargetControlID="Panel9"

    HoverCssClass="popupHover"

    PopupControlID="PopupMenu"

    PopupPosition="Left"

    OffsetX="0"

    OffsetY="0"

    PopDelay="50" />

### 13.ModalPopup

   功能：Xp的关机效果，后面全部灰掉，很多邮箱的删除对话框都着种效果

   细节： (1)本质上讲这是一个对话框模版，比ConfirmButton有意义有更强的扩展性！

                (2)从下面的代码中我们发现 点OK的时候可以调用后台方法

                (3)同时可以执行一段脚本

代码示意：

  <asp:Panel ID="Panel2" runat="server" CssClass="modalPopup"
style="display:none">

        <p>

            <asp:Label ID="Label1" runat="server" BackColor="Blue"
ForeColor="White" Style="position: relative"

                Text="信息提示"></asp:Label>&nbsp;</p>

        <p >确定要删除当前下载的任务么？</p>

        <p style="text-align:center;">

        <asp:Button ID="Button1" runat="server" Text="OK" ></asp:Button>

        <asp:Button ID="Button2" runat="server" Text="Cancel"></asp:Button>

        </p>

    </asp:Panel>

    <ajaxToolkit:ModalPopupExtender ID="ModalPopupExtender" runat="server"
TargetControlID="LinkButton1"

    PopupControlID="Panel2" BackgroundCssClass="modalBackground"
DropShadow="true"

    OkControlID="Button1" OnOkScript="onOk()" CancelControlID="CancelButton"
/>

### 14.MutuallyExlcusiveCheckBox

   功能：互斥复选框就像Radio一样

   细节： (1)Key属性用来分组就像RdiolistGroup一样

                (2)argetControlID用来绑定已有的CheckBox

   代码示意：

               <ajaxToolkit:MutuallyExclusiveCheckboxExtender runat="server"

    ID="MustHaveGuestBedroomCheckBoxEx"

    TargetControlID="MustHaveGuestBedroomCheckBox"

    Key="GuestBedroomCheckBoxes" />

### 15.NoBot

   功能：Captcha 图灵测试 反垃圾信息控件

   细节： (1)OnGenerateChallengeAndResponse 这个属性是EventHandler<NoBotEventArgs>
调用服务器端的方法，注意方法签名

                       例如：   protected void CustomChallengeResponse(object
sender, NoBotEventArgs e) {……} 代码示意：

    <ajaxToolkit:NoBot

  ID="NoBot2"

  runat="server"

  OnGenerateChallengeAndResponse="CustomChallengeResponse"

  ResponseMinimumDelaySeconds="2"

  CutoffWindowSeconds="60"

  CutoffMaximumInstances="5" />

### 16.NumericUpDown

   功能：实现Winform里面的Updown

   细节： (1)普通整数增减

                (2)值列表循环显示比如下面的第二个例子RefValues

                (3)调用Web Service的格式：

<ajaxToolkit:NumericUpDownExtender ID="NUD1" runat="server"

    TargetControlID="TextBox1"

    Width="100"

    RefValues="January;February;March;April"

    TargetButtonDownID="Button1"

    TargetButtonUpID="Button2"

    ServiceDownPath="WebService1.asmx"

    ServiceDownMethod="PrevValue"

    ServiceUpPath="WebService1.asmx"

    ServiceUpMethod="NextValue"

    Tag="1" />

代码示意：

           <ajaxToolkit:NumericUpDownExtender ID="NumericUpDownExtender1"
runat="server"

                    TargetControlID="TextBox1" Width="120" RefValues=""

                    ServiceDownMethod="" ServiceUpMethod=""
TargetButtonDownID="" TargetButtonUpID="" />

                <ajaxToolkit:NumericUpDownExtender ID="NumericUpDownExtender2"
runat="server"

                    TargetControlID="TextBox2" Width="120" RefValues="January;
February;March;April;May;June;July;August;September;October;November;December"

                    ServiceDownMethod="" ServiceUpMethod=""
TargetButtonDownID="" TargetButtonUpID="" />

                       <ajaxToolkit:NumericUpDownExtender
ID="NumericUpDownExtender4" runat="server"

                    TargetControlID="TextBox4" Width="80"
TargetButtonDownID="img1"

                    TargetButtonUpID="img2" RefValues="" ServiceDownMethod=""
ServiceUpMethod="" />

### 17.PagingBulletedList

   功能：扩展BulletedList的分页功能

   细节： (1)可以控制每页最多显示多少条，是否排序

                (2)IndexSize表示index headings 的字符数，如果MaxItemPerPage设置了概属性被忽略

                (3)MaxItemPerPage分页每页最大条数

代码示意：

<ajaxToolkit:PagingBulletedListExtender ID="PagingBulletedListExtender1"
BehaviorID="PagingBulletedListBehavior1" runat="server"

                    TargetControlID="BulletedList1"

                    ClientSort="true"

                    IndexSize="1"

                    Separator=" - "

                    SelectIndexCssClass="selectIndex"

                    UnselectIndexCssClass="unselectIndex" />

### 18.PasswordStrength

   功能：验证密码强度

   细节： StrengthIndicatorType两种显示方式：文字提示，进度条提示

代码示意：

<ajaxToolkit:PasswordStrength ID="PasswordStrength1" runat="server"
DisplayPosition="RightSide" TargetControlID="TextBox1"

                    StrengthIndicatorType="Text" PreferredPasswordLength="10"
PrefixText="Strength:"

                    HelpStatusLabelID="TextBox1_HelpLabel"
TextCssClass="TextIndicator_TextBox1"  TextStrengthDescriptions="Very
Poor;Weak;Average;Strong;Excellent"

                    MinimumNumericCharacters="0" MinimumSymbolCharacters="0"
RequiresUpperAndLowerCaseCharacters="false"/>

    <ajaxToolkit:PasswordStrength ID="PasswordStrength2" runat="server"
DisplayPosition="RightSide" TargetControlID="TextBox2"

                    StrengthIndicatorType="BarIndicator"
PreferredPasswordLength="15" HelpStatusLabelID="TextBox2_HelpLabel"

                     BarIndicatorCssClass="BarIndicator_TextBox2"
BarBorderCssClass="BarBorder_TextBox2"

                     MinimumNumericCharacters="1" MinimumSymbolCharacters="1"
RequiresUpperAndLowerCaseCharacters="true" />

    <ajaxToolkit:PasswordStrength ID="PasswordStrength3" runat="server"
DisplayPosition="BelowLeft" TargetControlID="TextBox3"

                    StrengthIndicatorType="Text" PreferredPasswordLength="20"
PrefixText="Meets Policy? " TextCssClass="TextIndicator_TextBox3"

                     MinimumNumericCharacters="2" MinimumSymbolCharacters="2"
RequiresUpperAndLowerCaseCharacters="true"

                     TextStrengthDescriptions="Not at all;Very Low
compliance;Low Compliance;Average Compliance;Good Compliance;Very High
Compliance;Yes"

                     HelpHandleCssClass="TextIndicator_TextBox3_Handle"
HelpHandlePosition="LeftSide" />

### 19.PopupControl

   功能：任何控件上都可以弹出任何内容

   细节： (1)TargetControlID - The ID of the control to attach to

                (2)PopupControlID - The ID of the control to display

                (3)CommitProperty -属性来标识返回的值

                (4) CommitScript -把返回结果值通过脚本处理，用到CommitProperty

  代码示意：

      <ajaxToolkit:PopupControlExtender  ID="PopupControlExtender2"
runat="server" TargetControlID="MessageTextBox"

      PopupControlID="Panel2" CommitProperty="value" CommitScript="e.value +=
' - do not forget!';" Position="Bottom" />

### 20.Rating

   功能：级别控件

   细节： 又是一个鸡肋，没有太大实用价值，看代码吧

   代码示意：

   <ajaxToolkit:Rating ID="ThaiRating" runat="server"

    CurrentRating="2"

    MaxRating="5"

    StarCssClass="ratingStar"

    WaitingStarCssClass="savedRatingStar"

    FilledStarCssClass="filledRatingStar"

    EmptyStarCssClass="emptyRatingStar"

    OnChanged="ThaiRating_Changed" />

### 21.ReorderList

   功能：这个控件的炫酷程度仅次于Animation ，可以动态移动数据

   细节： (1)绑定数据，拖动数据之后数据将被更新到绑定源

                (2)它不是已有控件的扩展是全新的服务器端控件，只是它对Ajax行为是敏感的

                (3)重排的实现有两种方式：CallBack PostBack
前者的发生在页面上是没有PostBack的（也就是没有刷新页面）

                (4) 而数据添加或者编辑的时候就必须要使用PostBack来同步服务器端的数据状态

                (5)PostbackOnReorder就是针对两种策略进行选择

                (6)可以扩展的很多，三言两语难以说尽给出基本框架吧，回头再说

代码示意：

   <ajaxToolkit:ReorderList ID="ReorderList1" runat="server"

    DataSourceID="ObjectDataSource1"

    DragHandleAlignment="Left"

    ItemInsertLocation="Beginning"

    DataKeyField="ItemID"

    SortOrderField="Priority"

    AllowReorder="true">

      <ItemTemplate></ItemTemplate>

      <ReorderTemplate></ReorderTemplate>

      <DragHandleTemplate></DragHandleTemplate>

      <InsertItemTemplate></InsertItemTemplate>

</ajaxToolkit:ReorderList>

### 22.ResizableControl

   功能：就像设计状态一样可以拖动修改大小，可是有什么实际的意义么，放大字体？没有想到

   细节： (1)HandleCssClass - The name of the CSS class to apply to the resize
handle 这个属性必须要有！

  代码示意：

<ajaxToolkit:ResizableControlExtender ID="RCE" runat="server"

    TargetControlID="PanelImage"

    HandleCssClass="handleImage"

    ResizableCssClass="resizingImage"

    MinimumWidth="50"

    MinimumHeight="20"

    MaximumWidth="260"

    MaximumHeight="130"

    OnClientResize="OnClientResizeImage"

    HandleOffsetX="3"

    HandleOffsetY="3" />

### 23.RoundedCorners

   功能：控件圆角 纯粹是控制外观的了，什么时候审美疲劳了还要改，呵呵

   细节： (1)还有一个非常非常坑人的地方：你必须要设置 CssClass="roundedPanel"要不然不起作用

                (2) Radius设置弧度，默认是5

                (3)好象只适用于容器

代码示意：

              <ajaxToolkit:RoundedCornersExtender ID="rce" runat="server"
TargetControlID="Panel1"     Radius="6" />

### 24.Slider

   功能：实现WinForm中的Slider控件效果

   细节： (1)修改文本框的值也可以影响Slider的状态！这个反馈还是有用的！

  代码示意：

              <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>

    <cc1:SliderExtender ID="SliderExtender2" runat="server"

                                BehaviorID="Slider2"

                                TargetControlID="Slider2"

                                BoundControlID="TextBox1"

                                Orientation="Horizontal"

                                EnableHandleAnimation="true"

                                 Minimum="0"

                                Maximum="100"

                                />

### 25.TextBoxWatermark

   功能：文本水印

   细节： 没有什么说的看代码--->

代码示意：

    <asp:TextBox ID="TextBox1" CssClass="unwatermarked" Width="150"
runat="server"></asp:TextBox>

            <cc1:TextBoxWatermarkExtender ID="TextBoxWatermarkExtender1"
runat="server" TargetControlID="TextBox1" WatermarkText="请输入用户名"
WatermarkCssClass="watermarked" />

### 26.UpdatePanelAnimation

   功能：更新动画效果

   细节：代码结构简单但是要说的东西很多，回头再说写专题吧

代码示意：

  <ajaxToolkit:UpdatePanelAnimationExtender ID="ae"

  runat="server" TargetControlID="up">

     <Animations>

        <OnUpdating>  </OnUpdating>

        <OnUpdated>  </OnUpdated>

    </Animations>

</ajaxToolkit:UpdatePanelAnimationExtender>

### 27.ToggleButton

   功能：就是把一个CheckBox的逻辑应用到一个按钮上，于是就有了双态按钮这么个玩意，有点意思啊

   闲言少叙，看代码：

<asp:CheckBox ID="CheckBox1" Checked="true" Text="I like ASP.NET"
runat="server"/>

    <cc1:ToggleButtonExtender ID="ToggleButtonExtender1" runat="server"
TargetControlID="CheckBox1" ImageWidth="19"

     ImageHeight="19" UncheckedImageUrl="Image/down.gif"
CheckedImageUrl="Image/up.gif" CheckedImageAlternateText="Check"

     UncheckedImageAlternateText="UnCheck" />

### 28.ValidatorCallout

   功能：Windows系统中最常见的气泡提示，比如你磁盘空间不足的时候……

   细节： 是对数据验证控件的扩展，比较新鲜

代码示意：

<asp:RequiredFieldValidator runat="server" ID="NReq"
ControlToValidate="NameTextBox" Display="None" ErrorMessage="<b>Required Field
Missing</b><br />A name is required." />

        <asp:RequiredFieldValidator runat="server" ID="PNReq"
ControlToValidate="PhoneNumberTextBox" Display="None"
ErrorMessage="<b>Required Field Missing</b><br />A phone number is
required.<div style='margin-top:5px;padding:5px;border:1px solid #e9e9e9
;background-color:white;'><b>Other Options:</b><br /><a
href='javascript:alert(&quot;not implemented but you get the
idea;)&quot;);'>Extract from Profile</a></div>" />

        <asp:RegularExpressionValidator runat="server" ID="PNRegEx"
ControlToValidate="PhoneNumberTextBox" Display="None" ErrorMessage="<b>Invalid
Field</b><br />Please enter a phone number in the format:<br />(###) ###-####"
ValidationExpression="(((d{3}) ?)|(d{3}-))?d{3}-d{4}" />

        <cc1:ValidatorCalloutExtender runat="Server" ID="NReqE"
TargetControlID="NReq" HighlightCssClass="highlight" />

        <cc1:ValidatorCalloutExtender runat="Server" ID="PNReqE"
TargetControlID="PNReq" HighlightCssClass="highlight" Width="350px" />

        <cc1:ValidatorCalloutExtender runat="Server" ID="PNReqEx"
TargetControlID="PNRegEx" HighlightCssClass="highlight" />

1.Accordion

功能：实现了QQ、Msn好友分类的折叠效果，就像包含了多个CollapsiblePanels

细节： (1)不要把Accordion放在Table种同时又把 FadeTransitions 设置为True，这将引起布局混乱

(2)每一个 AccordionPane control 有一个Header 和Content的 template

(3)在Content中可以进行任意扩展，你什么都可以放上^_^

(4)有三种AutoSize modes ：None(推荐) Limit  Fill

(5)Accordion表现的更像是一个容器

  
代码示意：

<ajaxToolkit:Accordion ID="MyAccordion" runat="server" SelectedIndex="0"
HeaderCssClass="accordionHeader"

ContentCssClass="accordionContent" FadeTransitions="false"
FramesPerSecond="40"

TransitionDuration="250" AutoSize="None">

<Panes>

<ajaxToolkit:AccordionPane ID="AccordionPane1" runat="server">

<Header>

<a href="" onclick="return false;" class="accordionLink">1.
Accordion</a></Header>

<Content>

</Content>

</ajaxToolkit:AccordionPane>

</Panes>

</ajaxToolkit:Accordion>

  
2. AlwaysVisibleControl

功能：最多的应用是在线小说的目录和不胜其烦的浮动小广告

细节： (1)避免控件闪烁，把这个控件要在目标位置时使用absolutely position

(2) HorizontalSide="Center" VerticalSide="Top" 使用这个方法控制浮动在什么位置

代码示意：

<cc1:AlwaysVisibleControlExtender ID="AlwaysVisibleControlExtender1"
HorizontalSide="Center" VerticalSide="Top"  TargetControlID="Panel1"
runat="server">

3.Animation

功能：28个控件种效果最酷的！顾名思义实现动画效果

细节： (1)不只是控件：pluggable, extensible framework

(2)用在什么时候：OnLoad  OnClick  OnMouseOver OnMouseOut OnHoverOver OnHoverOut

(3)具体使用有很多可以谈的，有理由单独写一个Animation Xml 编程介绍

代码示意：

<ajaxToolkit:AnimationExtender ID="ae"

runat="server" TargetControlID="ctrl">

<Animations>

<OnLoad>  </OnLoad>

<OnClick>  </OnClick>

<OnMouseOver>  </OnMouseOver>

<OnMouseOut>  </OnMouseOut>

<OnHoverOver>  </OnHoverOver>

<OnHoverOut>  </OnHoverOut>

</Animations>

</ajaxToolkit:AnimationExtender>

4.CascadingDropDown

功能：DropDownList联动，调用Web Service

细节： (1)DropDownList行为扩展

(2)如果使用Web service 方法签名必须符合下面的形式：

[WebMethod]

public CascadingDropDownNameValue[] GetDropDownContents(

string knownCategoryValues, string category){...}

代码示意：

<ajaxToolkit:CascadingDropDown ID="CascadingDropDown1" runat="server"
TargetControlID="DropDownList1" Category="Make"  PromptText="Please select a
make"  LoadingText="[Loading makes]"  ServicePath="CarsService.asmx"
ServiceMethod="GetDropDownContents"/>

<ajaxToolkit:CascadingDropDown ID="CascadingDropDown2" runat="server"
TargetControlID="DropDownList2" Category="Model" PromptText="Please select a
model" LoadingText="[Loading models]"
ServiceMethod="GetDropDownContentsPageMethod"
ParentControlID="DropDownList1"/>

<ajaxToolkit:CascadingDropDown ID="CascadingDropDown3" runat="server"
TargetControlID="DropDownList3" Category="Color" PromptText="Please select a
color" LoadingText="[Loading colors]"
ServicePath="~/CascadingDropDown/CarsService.asmx"
ServiceMethod="GetDropDownContents" ParentControlID="DropDownList2"/>

  
5.CollapsiblePanel

功能：Xp任务栏折叠效果

细节： (1)可以扩展任何一个 ASP.NET Panel control

(2) CollapsiblePanel 默认认为使用了 标准 CSS box model 早期的浏览器要!DOCTYPE
中设置页面为自适应方式提交数据rendered in IE's standards-compliant mode.

代码示意：

<ajaxToolkit:CollapsiblePanelExtender ID="cpe" runat="Server"

TargetControlID="Panel1"

CollapsedSize="0"

ExpandedSize="300"

Collapsed="True"

ExpandControlID="LinkButton1"

CollapseControlID="LinkButton1"

AutoCollapse="False"

AutoExpand="False"

ScrollContents="True"

TextLabelID="Label1"

CollapsedText="Show Details"

OpenedText="Hide Details"

ImageControlID="Image1"

ExpandedImage="~/images/collapse.jpg"

CollapsedImage="~/images/expand.jpg"

ExpandDirection="Height"/>

6.ConfirmButton

功能：就是弹出来一个确定对话框

细节： 本人认为不是最简单实现的方法，我的方法：

this.Button1.Attributes["onclick"]="javascript:return confirm('确定要停止下载么？');";

不知道是不是我没有发现这个控件的其它优势。

7.DragPanel

功能：页面拖动

细节： (1)TargetControlID 要拖动的控件

(2)DragHandleID   拖动的标题栏所在的ControlID

  
代码示意

<ajaxToolkit:DragPanelExtender ID="DPE1" runat="server"

TargetControlID="Panel3"

DragHandleID="Panel4" />

8.DropDown

功能：什么都可以以下拉菜单的形式弹出来

细节： (1)TargetControlID要在什么控件上实现扩展

(2)DropDownControlID弹出来什么

代码示意：

<asp:Panel ID="DropPanel" runat="server" CssClass="ContextMenuPanel"
Style="display: none;

visibility: hidden;">

<asp:LinkButton runat="server" ID="Option1" Text="Option 1"
CssClass="ContextMenuItem"

OnClick="OnSelect" />

<asp:LinkButton runat="server" ID="Option2" Text="Option 2"
CssClass="ContextMenuItem"

OnClick="OnSelect" />

<asp:LinkButton runat="server" ID="Option3" Text="Option 3 (Click Me!)"
CssClass="ContextMenuItem"

OnClick="OnSelect" />

</asp:Panel>

<cc1:DropDownExtender runat="server" ID="DDE" TargetControlID="TextLabel"

DropDownControlID="DropPanel" />

9.DropShadow

功能：阴影效果，其实可以放给美工实现

细节： (1)Width 单位：px  默认5px

(2)Opacity  不透明度0-1.0 默认.5

代码示意：

<ajaxToolkit:DropShadowExtender ID="dse" runat="server"

TargetControlID="Panel1"

Opacity=".8"

Rounded="true"

TrackPosition="true" />

10.DynamicPopulate

功能：能实用Web Service或页面方法来替换控件的内容

细节： (1)ClearContentsDuringUpdate  替换之前先清除以前的内容（默认True）

(2)PopulateTriggerControlID 触发器绑定的控件 单击时触发

(3)ContextKey传递给Web Service的随机字符串

(4) Web Service方法签名必须符合下面的形式：

[WebMethod]

string DynamicPopulateMethod(string contextKey)

{...}

Note you can replace "DynamicPopulateMethod" with a naming of your choice, but
the return

type and parameter name and type must exactly match, including case.

代码示意：

<ajaxToolkit:DynamicPopulateExtender ID="dp" runat="server"

TargetControlID="Panel1"

ClearContentsDuringUpdate="true"

PopulateTriggerControlID="Label1"

ServiceMethod="GetHtml"

UpdatingCssClass="dynamicPopulate_Updating" />

11.FilteredTextBox

功能：文本框数据过滤

细节： (1)过滤条件Numbers LowercaseLetters UppercaseLetters   Custom

(2)过滤条件也可以是Custom的组合 FilterType="Custom, Numbers"

(3)ValidChars="+-=/*()." Custom要定义这样的有效字符串

(4) 其实这是个鸡肋：你可以输入中文，聊胜于无，忍了

  
示意代码：

<ajaxToolkit:FilteredTextBoxExtender ID="ftbe" runat="server"

TargetControlID="TextBox3"

FilterType="Custom, Numbers"

ValidChars="+-=/*()." />

12.HoverMenu

功能：鼠标靠近时显示菜单，可以用在在线数据修改的表格上作为功能菜单

细节： (1)PopupControlID要弹出来什么

(2)PopupPostion 在哪里弹出来Left (Default), Right, Top, Bottom, Center.

(3)OffsetX/OffsetY 弹出项与源控件的距离

(4) PopDelay 弹出延时显示 单位milliseconds. Default is 100.

代码示意：

<ajaxToolkit:HoverMenuExtender ID="hme2" runat="Server"

TargetControlID="Panel9"

HoverCssClass="popupHover"

PopupControlID="PopupMenu"

PopupPosition="Left"

OffsetX="0"

OffsetY="0"

PopDelay="50" />

13.ModalPopup

功能：Xp的关机效果，后面全部灰掉，很多邮箱的删除对话框都着种效果

细节： (1)本质上讲这是一个对话框模版，比ConfirmButton有意义有更强的扩展性！

(2)从下面的代码中我们发现 点OK的时候可以调用后台方法

(3)同时可以执行一段脚本

代码示意：

<asp:Panel ID="Panel2" runat="server" CssClass="modalPopup"
style="display:none">

<p>

<asp:Label ID="Label1" runat="server" BackColor="Blue" ForeColor="White"
Style="position: relative"

Text="信息提示"></asp:Label>&nbsp;</p>

<p >确定要删除当前下载的任务么？</p>

<p style="text-align:center;">

<asp:Button ID="Button1" runat="server" Text="OK" ></asp:Button>

<asp:Button ID="Button2" runat="server" Text="Cancel"></asp:Button>

</p>

</asp:Panel>

<ajaxToolkit:ModalPopupExtender ID="ModalPopupExtender" runat="server"
TargetControlID="LinkButton1"

PopupControlID="Panel2" BackgroundCssClass="modalBackground" DropShadow="true"

OkControlID="Button1" OnOkScript="onOk()" CancelControlID="CancelButton" />

14.MutuallyExlcusiveCheckBox

功能：互斥复选框就像Radio一样

细节： (1)Key属性用来分组就像RdiolistGroup一样

(2)argetControlID用来绑定已有的CheckBox

代码示意：

<ajaxToolkit:MutuallyExclusiveCheckboxExtender runat="server"

ID="MustHaveGuestBedroomCheckBoxEx"

TargetControlID="MustHaveGuestBedroomCheckBox"

Key="GuestBedroomCheckBoxes" />

15.NoBot

功能：Captcha 图灵测试 反垃圾信息控件

细节： (1)OnGenerateChallengeAndResponse 这个属性是EventHandler<NoBotEventArgs>
调用服务器端的方法，注意方法签名

例如：   protected void CustomChallengeResponse(object sender, NoBotEventArgs e)
{……} 代码示意：

<ajaxToolkit:NoBot

ID="NoBot2"

runat="server"

OnGenerateChallengeAndResponse="CustomChallengeResponse"

ResponseMinimumDelaySeconds="2"

CutoffWindowSeconds="60"

CutoffMaximumInstances="5" />

16.NumericUpDown

功能：实现Winform里面的Updown

细节： (1)普通整数增减

(2)值列表循环显示比如下面的第二个例子RefValues

(3)调用Web Service的格式：

<ajaxToolkit:NumericUpDownExtender ID="NUD1" runat="server"

TargetControlID="TextBox1"

Width="100"

RefValues="January;February;March;April"

TargetButtonDownID="Button1"

TargetButtonUpID="Button2"

ServiceDownPath="WebService1.asmx"

ServiceDownMethod="PrevValue"

ServiceUpPath="WebService1.asmx"

ServiceUpMethod="NextValue"

Tag="1" />

代码示意：

<ajaxToolkit:NumericUpDownExtender ID="NumericUpDownExtender1" runat="server"

TargetControlID="TextBox1" Width="120" RefValues=""

ServiceDownMethod="" ServiceUpMethod="" TargetButtonDownID=""
TargetButtonUpID="" />

<ajaxToolkit:NumericUpDownExtender ID="NumericUpDownExtender2" runat="server"

TargetControlID="TextBox2" Width="120" RefValues="January;February;March;April
;May;June;July;August;September;October;November;December"

ServiceDownMethod="" ServiceUpMethod="" TargetButtonDownID=""
TargetButtonUpID="" />

<ajaxToolkit:NumericUpDownExtender ID="NumericUpDownExtender4" runat="server"

TargetControlID="TextBox4" Width="80" TargetButtonDownID="img1"

TargetButtonUpID="img2" RefValues="" ServiceDownMethod="" ServiceUpMethod=""
/>

  
17.PagingBulletedList

功能：扩展BulletedList的分页功能

细节： (1)可以控制每页最多显示多少条，是否排序

(2)IndexSize表示index headings 的字符数，如果MaxItemPerPage设置了概属性被忽略

(3)MaxItemPerPage分页每页最大条数

代码示意：

<ajaxToolkit:PagingBulletedListExtender ID="PagingBulletedListExtender1"
BehaviorID="PagingBulletedListBehavior1" runat="server"

TargetControlID="BulletedList1"

ClientSort="true"

IndexSize="1"

Separator=" - "

SelectIndexCssClass="selectIndex"

UnselectIndexCssClass="unselectIndex" />

18.PasswordStrength

功能：验证密码强度

细节： StrengthIndicatorType两种显示方式：文字提示，进度条提示

代码示意：

<ajaxToolkit:PasswordStrength ID="PasswordStrength1" runat="server"
DisplayPosition="RightSide" TargetControlID="TextBox1"

StrengthIndicatorType="Text" PreferredPasswordLength="10"
PrefixText="Strength:"

HelpStatusLabelID="TextBox1_HelpLabel" TextCssClass="TextIndicator_TextBox1"
TextStrengthDescriptions="Very Poor;Weak;Average;Strong;Excellent"

MinimumNumericCharacters="0" MinimumSymbolCharacters="0"
RequiresUpperAndLowerCaseCharacters="false"/>

<ajaxToolkit:PasswordStrength ID="PasswordStrength2" runat="server"
DisplayPosition="RightSide" TargetControlID="TextBox2"

StrengthIndicatorType="BarIndicator" PreferredPasswordLength="15"
HelpStatusLabelID="TextBox2_HelpLabel"

BarIndicatorCssClass="BarIndicator_TextBox2"
BarBorderCssClass="BarBorder_TextBox2"

MinimumNumericCharacters="1" MinimumSymbolCharacters="1"
RequiresUpperAndLowerCaseCharacters="true" />

<ajaxToolkit:PasswordStrength ID="PasswordStrength3" runat="server"
DisplayPosition="BelowLeft" TargetControlID="TextBox3"

StrengthIndicatorType="Text" PreferredPasswordLength="20" PrefixText="Meets
Policy? " TextCssClass="TextIndicator_TextBox3"

MinimumNumericCharacters="2" MinimumSymbolCharacters="2"
RequiresUpperAndLowerCaseCharacters="true"

TextStrengthDescriptions="Not at all;Very Low compliance;Low
Compliance;Average Compliance;Good Compliance;Very High Compliance;Yes"

HelpHandleCssClass="TextIndicator_TextBox3_Handle"
HelpHandlePosition="LeftSide" />

19.PopupControl

功能：任何控件上都可以弹出任何内容

细节： (1)TargetControlID - The ID of the control to attach to

(2)PopupControlID - The ID of the control to display

(3)CommitProperty -属性来标识返回的值

(4) CommitScript -把返回结果值通过脚本处理，用到CommitProperty

代码示意：

<ajaxToolkit:PopupControlExtender  ID="PopupControlExtender2" runat="server"
TargetControlID="MessageTextBox"

PopupControlID="Panel2" CommitProperty="value" CommitScript="e.value += ' - do
not forget!';" Position="Bottom" />

20.Rating

功能：级别控件

细节： 又是一个鸡肋，没有太大实用价值，看代码吧

代码示意：

<ajaxToolkit:Rating ID="ThaiRating" runat="server"

CurrentRating="2"

MaxRating="5"

StarCssClass="ratingStar"

WaitingStarCssClass="savedRatingStar"

FilledStarCssClass="filledRatingStar"

EmptyStarCssClass="emptyRatingStar"

OnChanged="ThaiRating_Changed" />

21.ReorderList

功能：这个控件的炫酷程度仅次于Animation ，可以动态移动数据

细节： (1)绑定数据，拖动数据之后数据将被更新到绑定源

(2)它不是已有控件的扩展是全新的服务器端控件，只是它对Ajax行为是敏感的

(3)重排的实现有两种方式：CallBack PostBack 前者的发生在页面上是没有PostBack的（也就是没有刷新页面）

(4) 而数据添加或者编辑的时候就必须要使用PostBack来同步服务器端的数据状态

(5)PostbackOnReorder就是针对两种策略进行选择

(6)可以扩展的很多，三言两语难以说尽给出基本框架吧，回头再说

  
代码示意：

<ajaxToolkit:ReorderList ID="ReorderList1" runat="server"

DataSourceID="ObjectDataSource1"

DragHandleAlignment="Left"

ItemInsertLocation="Beginning"

DataKeyField="ItemID"

SortOrderField="Priority"

AllowReorder="true">

<ItemTemplate></ItemTemplate>

<ReorderTemplate></ReorderTemplate>

<DragHandleTemplate></DragHandleTemplate>

<InsertItemTemplate></InsertItemTemplate>

</ajaxToolkit:ReorderList>

22.ResizableControl

功能：就像设计状态一样可以拖动修改大小，可是有什么实际的意义么，放大字体？没有想到

细节： (1)HandleCssClass - The name of the CSS class to apply to the resize
handle 这个属性必须要有！

代码示意：

<ajaxToolkit:ResizableControlExtender ID="RCE" runat="server"

TargetControlID="PanelImage"

HandleCssClass="handleImage"

ResizableCssClass="resizingImage"

MinimumWidth="50"

MinimumHeight="20"

MaximumWidth="260"

MaximumHeight="130"

OnClientResize="OnClientResizeImage"

HandleOffsetX="3"

HandleOffsetY="3" />

  
23.RoundedCorners

功能：控件圆角 纯粹是控制外观的了，什么时候审美疲劳了还要改，呵呵

细节： (1)还有一个非常非常坑人的地方：你必须要设置 CssClass="roundedPanel"要不然不起作用

(2) Radius设置弧度，默认是5

(3)好象只适用于容器

代码示意：

<ajaxToolkit:RoundedCornersExtender ID="rce" runat="server"
TargetControlID="Panel1"     Radius="6" />

  
24.Slider

功能：实现WinForm中的Slider控件效果

细节： (1)修改文本框的值也可以影响Slider的状态！这个反馈还是有用的！

代码示意：

<asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>

<cc1:SliderExtender ID="SliderExtender2" runat="server"

BehaviorID="Slider2"

TargetControlID="Slider2"

BoundControlID="TextBox1"

Orientation="Horizontal"

EnableHandleAnimation="true"

Minimum="0"

Maximum="100"

/>

25.TextBoxWatermark

功能：文本水印

细节： 没有什么说的看代码--->

代码示意：

<asp:TextBox ID="TextBox1" CssClass="unwatermarked" Width="150"
runat="server"></asp:TextBox>

<cc1:TextBoxWatermarkExtender ID="TextBoxWatermarkExtender1" runat="server"
TargetControlID="TextBox1" WatermarkText="请输入用户名"
WatermarkCssClass="watermarked" />

26.UpdatePanelAnimation

功能：更新动画效果

细节：代码结构简单但是要说的东西很多，回头再说写专题吧

代码示意：

<ajaxToolkit:UpdatePanelAnimationExtender ID="ae"

runat="server" TargetControlID="up">

<Animations>

<OnUpdating>  </OnUpdating>

<OnUpdated>  </OnUpdated>

</Animations>

</ajaxToolkit:UpdatePanelAnimationExtender>

27.ToggleButton

功能：就是把一个CheckBox的逻辑应用到一个按钮上，于是就有了双态按钮这么个玩意，有点意思啊

闲言少叙，看代码：

<asp:CheckBox ID="CheckBox1" Checked="true" Text="I like ASP.NET"
runat="server"/>

<cc1:ToggleButtonExtender ID="ToggleButtonExtender1" runat="server"
TargetControlID="CheckBox1" ImageWidth="19"

ImageHeight="19" UncheckedImageUrl="Image/down.gif"
CheckedImageUrl="Image/up.gif" CheckedImageAlternateText="Check"

UncheckedImageAlternateText="UnCheck" />

28.ValidatorCallout

功能：Windows系统中最常见的气泡提示，比如你磁盘空间不足的时候……

细节： 是对数据验证控件的扩展，比较新鲜

代码示意：

<asp:RequiredFieldValidator runat="server" ID="NReq"
ControlToValidate="NameTextBox" Display="None" ErrorMessage="<b>Required Field
Missing</b><br />A name is required." />

<asp:RequiredFieldValidator runat="server" ID="PNReq"
ControlToValidate="PhoneNumberTextBox" Display="None"
ErrorMessage="<b>Required Field Missing</b><br />A phone number is
required.<div style='margin-top:5px;padding:5px;border:1px solid #e9e9e9
;background-color:white;'><b>Other Options:</b><br /><a
href='javascript:alert(&quot;not implemented but you get the
idea;)&quot;);'>Extract from Profile</a></div>" />

<asp:RegularExpressionValidator runat="server" ID="PNRegEx"
ControlToValidate="PhoneNumberTextBox" Display="None" ErrorMessage="<b>Invalid
Field</b><br />Please enter a phone number in the format:<br />(###) ###-####"
ValidationExpression="(((d{3}) ?)|(d{3}-))?d{3}-d{4}" />

<cc1:ValidatorCalloutExtender runat="Server" ID="NReqE" TargetControlID="NReq"
HighlightCssClass="highlight" />

<cc1:ValidatorCalloutExtender runat="Server" ID="PNReqE"
TargetControlID="PNReq" HighlightCssClass="highlight" Width="350px" />

<cc1:ValidatorCalloutExtender runat="Server" ID="PNReqEx"
TargetControlID="PNRegEx" HighlightCssClass="highlight" />

