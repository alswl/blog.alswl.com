Title: VS2005无法创建或打开"智能设备"项目的一个问题的解决方法
Author: alswl
Slug: a-solution-of-can-not-create-or-open-the-smart-device-project-in-vs2005
Date: 2010-03-29 00:00:00
Tags: VisualStudio, WinCE
Category: dotNet

### 状况

在VS2005中创建或打开"智能设备"项目时，提示以下错误： "从用户数据存储中检索信息时出错。系统未找到指定的对象。" 和
"由于数据存储中不存在项目引用的设备平台，因此无法打开项目。"

在打开VS2005的"工具"－"设备仿真器管理器"时，提示以下错误： "未能正确加载包"Smart Device Configuration
Package"( GUID = {D245F354-3F45-4516-B1E6-04608DA126CC}
)。请与包供应商联系以获得帮助。由于可能会发生环境损坏，建议重新启动应用程序。要禁止将来加载此包吗? 可以使用"devenv
/resetskippkgs"重新启用包加载。"

### 不成功的解决办法

有说把.csproj文件中的`<PlatformID>4118C335-430C-497f-
BE48-11C3316B135E</PlatformID>`改成`<PlatformID>3C41C503-53EF-4c2a-
8DD4-A8217CAD115E</PlatformID>`，原因说是"3C41C503-53EF-4c2a-
8DD4-A8217CAD115E"来自任意一个能运行的.net
cf2.0项目的.csproj文件，目标平台是ppc2003或wm5.0都可以"，但是很可惜，这个办法在我电脑上没有起作用。

### 成功的解决方法

1. 关闭VS2005。

2. 重命名文件夹`c:Documents and Settings<user>Local SettingsApplication
DataMicrosoftCoreCon1.0`，这将删除所有关于设备配置属性的定制。

3. 重启VS2005，VS2005会自动重建上述配置。

原文链接：[VS2005 无法创建或打开"智能设备"项目的一个问题的解决方法 - bingrrx的专栏 -
CSDN博客](http://blog.csdn.net/bingrrx/archive/2008/07/10/2634481.aspx)

原文的原文链接：<del>http://forums.microsoft.com/MSDN/ShowPost.aspx?PostID=140668&
SiteID=1</del>链接已失效

