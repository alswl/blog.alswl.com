Title: 在Eclipse中使用VSS
Author: alswl
Date: 2010-02-24 00:00:00
Tags: Eclipse, VSS
Category: 工欲善其事必先利其器
Summary: 

原文链接：[Eclipse中安装配置VSS -
51CTO.COM](http://developer.51cto.com/art/200906/127171.htm)

alswl友情提示：**VSS Plugin for Eclipse
**已经更新至1.6.2，链接在[这里](http://sourceforge.net/projects/vssplugin/)

***-BOF-***

## vss安装

### 1. 安装Vss服务器

在服务器上安装vss6.0d，安装好后，在服务器目录C:Program FilesMicrosoft Visual
StudioCommonVSS下有个NETSETUP.EXE文件，共享这个目录，客户机就执行这个NETSETUP.EXE文件进行安装。

### 2. 创建源代码管理数据库

2-1. 在服务端要先创建一个源代码管理数据库，以存储您的开发团队的共享文件的服务器版本。为源代码管理数据库创建共享网络文件夹。在源代码管理服务器中，打开
Windows 资源管理器，新建一个名为 test的文件夹。

2-2. 右击"test"，然后单击"属性"。

2-3. 在"test 属性"对话框中，单击"共享"选项卡，然后单击"共享该文件夹"。现在可以在共享的 test 中创建源代码管理数据库了。

### 3. 创建源代码管理数据库

3-1. 在服务器，单击"开始"按钮，指向"程序"，指向"Microsoft Visual SourceSafe"，然后单击"Visual
SourceSafe 6.0 Admin"。

3-2. 在"Visual SourceSafe Administrator"对话框的"Tools"菜单中，单击"Create Database"。

3-3. 在"Create new VSS Database in"框中，找到上面建立的"test"目录

3-4. Visual Studio .NET
的源代码管理数据库已设置成功。然后添加用户，就是开发团队的人员都给分配一个账号，以后要打开这个数据库要进行身份认证的。

## 在eclipse中配置vss

1. 到网站中下载免费的org.vssplugin_1.4.1-2.0-compability.zip到本机目录；

下载地址：[http://sourceforge.net/projects/vssplugin](http://sourceforge.net/projec
ts/vssplugin)

2. 将org.vssplugin_1.4.1-2.0-compability.zip解压缩；

3. 将解完压缩后得到的org.vssplugin_1.4.1文件夹复制到ECLIPSE_PATHplugins下；（ECLIPSE_PATH是
eclipse的安装路径）

4. 重新启动eclipse；；(如果找不到，就先推出并删除configuration文件中除INI文件的所有文件)

5. Help->About Eclipse Platform->Plug-In Details确认插件加入成功；

6. Window->Customize Perspective…，在对话框中的Window>Show
View和Other中把VSS相关的选项打上钩，OK。

## 在Eclipse中使用VSS（服务器）：

新建程序：

1. 将工具生成好的源文件建好工作路径，将整个工作路径拷贝到服务器的相应位置；

2. 打开Eclipse->File->New->Project…选择服务器上的此本程序的工作路径建立新工程；

3. 右键点选工程->Team->Share Project…；

4. 选择VSS Configuration Wizard，点next；

5. User Name和Password输入你的用户名和密码；

6. 在确保自己的计算机可以在不输入密码的情况下登录到服务器上的情况下，直接输入或点Browse…选择VSS Database目录

（选择VSS文档库的目录：即有srcsafe.ini文件的那个数据库目录）；

7. 打开VSS客户端，在总目录的下面建立一个自己子工程名称相对应的文件夹；

8. Realative mountpoint中选择刚刚在VSS中建好的文件夹后点确定(在VSS中建好的文件夹路径，即项目所要共享到vss的哪个目录下)；

9. 将下面的那个多选框的钩打上，点Finish；

10. 右键选择工程->Team->Add To VSS，输入相应注释后OK；（不可添加全项目）

11. 这样就可以在Team中执行相应的Check-in、Check-out操作了。

![](http://upload-log4d.qiniudn.com/2010/02/vss.jpg)

## 打开一个VSS数据库中已有的工程（客户端）：

1. 打开Eclipse->File->New->Project ；

2. 右键点选工程->Team->Share Project…；

3. 选择VSS Configuration Wizard，点next；

4. User Name和Password输入你的用户名和密码；

5. 在确保自己的计算机可以在不输入密码的情况下登录到服务器上的情况下，直接输入或点Browse…选择VSS Database目录；

6. Realative
mountpoint中选择好相对应的VSS路径后点确定(在VSS中建好的放源代码的文件夹路径，即项目所要共享到vss的哪个目录下)；

7. 将下面的那个多选框的钩打上，点Finish；

8. 右键选择工程->Team->Refresh。

计算机重起后打开工程：

确保本地计算机可以在不输入密码的情况下等录到服务器上；

在服务器上打开Eclipse，右键工程->Open Project；

右键点选工程->Team->Share Project…

