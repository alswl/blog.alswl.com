Title: PDA"未能建立与网络的连接"的解决办法
Author: alswl
Slug: solution-of-pda-failed-to-establish-a-network-connection
Date: 2010-03-31 00:00:00
Tags: PDA, VisualStudio, WinCE
Category: Microsoft .Net, 移动编程和手机应用开发
Summary: 

遇到这个问题大凡是因为模拟器或者真机无法连接网络，所以需要先测试网络是否畅通，在真机或者模拟器的IE中打开需要的WebService地址，看看是否能够正常获
取。

确定是网络原因后，可以采用多种方式连接网络，比如使用虚拟网卡来实现，又或者使用ActiveSync来实现。

### 使用本地网卡

在模拟器的文件-配置中的网卡中，选择本地网卡，可能会需要提示安装Virtual PC
2007，我不愿意装这么一个大家伙，也就没有尝试这种方法，需要的朋友可以在[Download details: Virtual PC 2007](http:
//www.microsoft.com/downloads/details.aspx?FamilyID=04d26402-3199-48a3-afa2-2d
c0b40a73b6&DisplayLang=en)来下载Virtual PC 2007进而连接互联网。

### 使用ActiveSync

ActiveSync是一个连接Win系列手持到电脑的同步软件，通过它可以使真机或者模拟机连接网络，步骤如下。

1、打开ActiveSync ，点击文件-连接设置，在"允许连接到以下其中一个端口"下选择"DMA"。

2、打开 VS2005，点击菜单工具-设备仿真管理器，选择一个windows mobile 5.0 PocketPC
模拟器。在右键菜单中点击"连接"。等模拟器启动后，再点击"插入底座"，此时，通过ActiveSync来连接到模拟器，并进行数据同步。

3、测试一下能不能连上网络，比如说Baidu（现在G.cn已经不能作为能否上网的标志了）或者WebService地址。

### 参考连接

[PDA智能程序访问WebService，报告"未能建立与网络的连接"?

](http://www.chinaret.com/user/topic_view.aspx?u=jianfangkk&id=0b10f862-db59-4
a52-9ceb-9ef1023acd9a)

[请问PDA智能程序访问WebService，报告"未能建立与网络的连接"?

](http://topic.csdn.net/u/20080610/18/da506852-57da-
4df0-beb4-6952eece2f4e.html)

