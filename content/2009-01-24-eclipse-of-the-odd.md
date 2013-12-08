Title: Eclipse的奇淫巧计【转】
Author: alswl
Slug: eclipse-of-the-odd
Date: 2009-01-24 00:00:00
Tags: Eclipse
Category: 工欲善其事必先利其器

代码篇：

1.在源代码中快速跳转:

eclipse中的跳转甚至比VS.Net还方便，方法是按住Ctrl键，然后鼠标指向变量名，方法名，类名，就会出现链接，点击就可跳到定义处。

2.实时语法检查:

编辑区右侧如果有红色小方块，直接点击就可跳到有错的行；黄色小方块是警告，可以忽略，但最好检查一下；如果某个函数尚未完成，要提

醒自己注意怎么办？加上注释// TODO，右侧就会有蓝色小方块，提示你此处尚未完成。当一个源码的右侧没有任何提示时，说明这个文件已经

完成了。

3.自动生成getter/setter方法:

只需要申明protected，private类成员变量，然后在Package Explore中找到该类，右键点击，选择"Source""Generate
Getters and

Setters"。

4.更改类名/变量名:

如果涉及到多处修改，不要直接在源码中更改，在Package Explore中找到要改名的类或变量，右键点击，选择"Refactor""Rename"，

eclipse会自动搜索所有相关代码并替换，确保不会遗漏或改错。

5.匹配Try:

如果写的代码需要抛出或者捕捉异常，在JBuilder中，你需要首先引入这个异常类，然后再在写好的代码前后加try，catch或者在方法后面加

throws，在eclipse里完全不必要这样，只需要写好代码，然后按ctrl + 1，这时会出来提示，提示你是throw还是catch这个异常，选择你需要

的，按下enter就可以了。

6.快速书写循环代码：

在写循环或者选择条件的语句时，先写出关键字如if、while，然后按alt + /自己去看有什么好处吧。接下来会出来提示代码，按下tab可以在

框框中跳，按下确定跳出代码提示。

  
热键篇：

ctrl + D：删除行

ctrl + M：当前窗口的最大化或最小化

ctrl + L：跳到指定的行

ctrl + 1：代码纠错提示

alt + /：代码辅助提示

F11：运行上次运行的程序

Ctrl+E 会弹出下拉列表列出打开文件的名称，用户可以利用上下方向键选择要查看的文件或者敲入文件名，这样就会切换到相应的文件。

Alt+Left 和 Alt+Right，利用Alt+左右方向键的方式，可以在打开文件中进行切换，就像用户使用浏览器时一样。

Ctrl+Shift+E，当用户使用Ctrl+Shift+E时，会弹出一个窗口列出打开文件的名称，用户可以利用上下方向键选择要查看的文件。

Ctrl+F6，会弹出一个列表列出打开文件的名称，不要松开Ctrl键，列表会一直打开。用户可以利用上下方向键或者利用Ctrl+Shift+F6选择要

查看的文件。

Ctrl+Shift+R，会打开资源对话框，键入要查看的文件名，回车就会切换到相应的文件。

Alt+F，利用历史纪录也可以达到切换的目的。当使用Alt+F打开文件菜单时，输入历史纪录中的数值就可以了。

Template：Alt + /

修改处：Window->Preference->Workbench->Keys->Command->Edit->Content Assist。

个人习惯：Shift+SPACE(空白)。

简易说明：编辑程序代码时，打sysout +Template启动键，就会自动出现：System.out.println(); 。

设定Template的格式：窗口->喜好设定->Java->编辑器->模板。

程序代码自动排版：Ctrl+Shift+F

修改处：窗口->喜好设定->工作台->按键->程序代码->格式。

个人习惯：Alt+Z。

自动排版设定：窗口->喜好设定->Java->程序代码格式制作程序。

样式页面->将插入tab(而非空格键)以内缩，该选项取消勾选，下面空格数目填4，这样在自动编排时会以空格4作缩排。

  
快速执行程序：Ctrl + F11

个人习惯：ALT+X

修改处：窗口->喜好设定->工作台->按键->执行->启动前一次的启动作业。

简易说明：第一次执行时，它会询问您执行模式，

设置好后，以后只要按这个热键，它就会快速执行。

..我觉得很顺手^___^

  
自动汇入所需要的类别：Ctrl+Shift+O

简易说明：

假设我们没有Import任何类别时，当我们在程序里打入：

BufferedReader buf = new BufferedReader(new InputStreamReader(System.in));

此时Eclipse会警示说没有汇入类别，这时我们只要按下Ctrl+Shift+O，它就会自动帮我们Import类别。

  
查看使用类别的原始码：Ctrl+鼠标左键点击

简易说明：可以看到您所使用类别的原始码。

将选取的文字批注起来：Ctrl+/

简易说明：Debug时很方便。

修改处：窗口->喜好设定->工作台->按键->程序代码->批注

  
将选取的文字取消批注：Ctrl+简易说明：同上。

修改处：窗口->喜好设定->工作台->按键->程序代码->取消批注

  
视图切换：Ctrl+F8

个人习惯：Alt+S。

修改处：窗口->喜好设定->工作台->按键->窗口->下一个视景。

简易说明：可以方便我们快速切换编辑、除错等视景。

3.0里Ctrl+Alt+H可以看到调用当前member的方法,而且可以一层一层上去.

Ctrl+O可以快速切到其他方法.

密技篇：

一套Eclipse可同时切换，英文、繁体、简体显示：

1.首先要先安装完中文化包。

2.在桌面的快捷方式后面加上参数即可，

英文-> -nl "zh_US" ；繁体-> -nl "zh_TW" ；简体-> -nl "zh_CN"。(其它语系以此类推)

像我2.1.2中文化后，我在我桌面的Eclipse快捷方式加入参数-n1 "zh_US"。

"C:Program Fileseclipseeclipse.exe" -n "zh_US"

接口就会变回英文语系噜。

利用Eclipse，在Word编辑文书时可不必将程序代码重新编排：

将Eclipse程序编辑区的程序代码整个复制下来(Ctrl+C)，直接贴(Ctrl+V)到Word或WordPad上，您将会发现在Word里的程序代码格式，
跟

Eclipse所设定的完全一样，包括字型、缩排、关键词颜色。我曾试过JBuilder、GEL、NetBeans...使用复制贴上时，只有缩排格式一样，字型

、颜色等都不会改变。

  
外挂篇：

外挂安装：将外挂包下载回来后，将其解压缩后，您会发现features、plugins这2个数据夹，将里面的东西都复制或移动到Eclipse的features

、plugins数据夹内后，重新启动Eclipse即可。

让Eclipse可以像JBuilderX一样使用拖拉方式建构GUI的外挂：

1.Jigloo SWT/Swing GUI Builder ：

[http://cloudgarden.com/jigloo/index.html](http://cloudgarden.com/jigloo/index
.html)

下载此版本：Jigloo plugin for Eclipse (using Java 1.4 or 1.5)

安装后即可由档案->新建->其它->GUI Form选取要建构的GUI类型。

2.Eclipse Visual Editor Project：

[http://www.eclipse.org/vep/](http://www.eclipse.org/vep/)

点选下方Download Page，再点选Latest Release 0.5.0进入下载。

除了VE-runtime-0.5.0.zip要下载外，以下这2个也要：

EMF build 1.1.1: (build page) (download zip)

GEF Build 2.1.2: (build page) (download zip)

我只测试过Eclipse 2.1.2版本，使用上是OK的！

3.0版本以上的使用者，请下载：

Eclipse build I20040324:

1.0.0 Stream Integration Build I20040325 Thu, 25 Mar 2004 -- 12:09 (-0500)

1.0.0 Stream Nightly Build N20040323a Tue, 23 Mar 2004 -- 13:53 (-0500)

注意：3.0以上版本，仅build I20040324可正常使用。

安装成功后，即可由新建->Java->AWT与Swing里选择所要建构的GUI类型开始进行设计。VE必须配合着对应版本，才能正常使用，否则即使安装

成功，使用上仍会有问题。

  
使用Eclipse来开发JSP程序：

外挂名称：lomboz(下载页面)

[http://forge.objectweb.org/project/showfiles.php?group_id=97](http://forge.ob
jectweb.org/project/showfiles.php?group_id=97)

请选择适合自己版本的lomboz下载，lomboz.212.p1.zip表示2.1.2版，lomboz.3m7.zip表示M7版本....以此类推。lomb
oz安装以及设置教学：

Eclipse开发JSP-教学文件

Java转exe篇：

实现方式：Eclipse搭配JSmooth(免费)。

1.先由Eclipse制作包含Manifest的JAR。

制作教学

2.使用JSmooth将做好的JAR包装成EXE。

JSmooth下载页面：

[http://jsmooth.sourceforge.net/index.php](http://jsmooth.sourceforge.net/inde
x.php)

3.制作完成的exe文件，可在有装置JRE的Windows上执行。

  
Eclipse-Java编辑器最佳设定：

编辑器字型设定：工作台->字型->Java编辑器文字字型。

(建议设定Courier New -regular 10)

编辑器相关设定：窗口->喜好设定->Java->编辑器

外观：显示行号、强调对称显示的方括号、强调显示现行行、显示打印边距，将其勾选，Tab宽度设4，打印编距字段设80。

程序代码协助：采预设即可。

语法：可设定关键词、字符串等等的显示颜色。

附注：采预设即可。

输入：全部字段都勾选。

浮动说明：采预设即可。

导览：采预设即可。

使自动排版排出来的效果，最符合Java设计惯例的设定：

自动排版设定：窗口->喜好设定->Java->程序代码制作格式。

换行：全部不勾选。

分行：行长度上限设：80。

样式：只将强制转型后插入空白勾选。

内缩空格数目：设为4。

