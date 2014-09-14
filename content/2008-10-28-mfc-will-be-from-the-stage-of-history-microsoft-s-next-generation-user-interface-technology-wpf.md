Title: MFC将退出历史舞台，微软的下一代用户界面技术WPF
Author: alswl
Slug: mfc-will-be-from-the-stage-of-history-microsoft-s-next-generation-user-interface-technology-wpf
Date: 2008-10-28 00:00:00
Tags: C, WPF
Category: Coding

转来的，最近对MFC很关注...

WPF简介

  
　　WPF的全称是WindowsPresentationFoundation，是微软新发布的Vista操作系统的三大核心开发库之一，其主要负责的是图形显示，
所以叫Presentation（呈现）。

  
　　作为新的图形引擎，WPF是基于DirectX的，当然增加了很多新的功能。其2D和3D引擎的强大看看Vista的界面就明白了，再加上其对Aero图形引擎的
支持，更加让你刚到神奇。顺便提一下，Aero是专门为3D桌面开发的引擎，可以让桌面实现神奇的3D翻转，这绝对是操作系统有史以来的一次神奇尝试，虽然对硬件配置
的要求也是惊人的，此前已有相关报道称，Vista对显卡十分挑剔就是出于运行Aero的考虑。

  
　　微软公司早在2003年洛杉矶的PDC上就公布了Avalon，他们将其视为下一代用户界面技术，并且得到了开发者和用户的一致赞同。

  
　　在2005年的PDC上，微软公司展示了比2003年更加完整的Avalon版本，并给它取了一个官方新名称：WindowsPresentationFound
ation(WPF)。在此之前，它已经完成了从演示软件到开始阶段alpha版本的API的转变。到了几个月之后的今天，它又成长成为更加先进的beta版本--
你可以使用它来开发你的下一代用户界面程序了。

  
　　那么，WPF是什么，为什么它那么重要呢？

  
　　首先，它清晰而又有效的将用户界面和程序实现分开。它使得设计可视化的用户界面的设计者和编写内部核心代码的开发人员可以并行工作。这是非常重要的：

  
　　•将两者分开，软件开发公司可以使得设计者们集中精力将设计工作做得更好，同时让开发者支持他们。

  
　　•随着软件外包和订购的逐渐风行，WPF使得一些商业的设计者们能够更好的从事界面设计工作，并集成一些简单的功能，而购买的核心代码能够独立的完成内部的一些关
键逻辑而不干扰设计过程。

  
　　•它更好的支持应用软件的国际化。不同的独立的界面可以使用不同的本地化方案，而内部的代码是通用的。

  
　　•它支持软件的"空标签"：可以为不同的用户采用定制的界面而保持核心的逻辑不变。开发者们创建程序逻辑，然后为不同的用户使用不同的界面并贴上他们的商标等。

  
　　WPF使用一种基于XML的语言来定义用户界面从而完成上述的工作。这种语言被称为XAML，XML应用程序标记语言。

  
　　其次，WPF使用一种基于向量而不是基于光栅的绘制引擎，这和曹其的Windows的绘制引擎是截然不同的。光栅绘制引擎通过在屏幕上绘制象素点来绘制表面。象素
只是点；这样的话，如果屏幕分辨率(DPI，每英寸点)增加了，它的效果就会变差。随着现在屏幕都采用超高DPI的分辨率，字体必须使用成百上千个DPI来达到一定的
浏览效果。比如微软Word里缺省的英文字体12号的TimesNewRoman，在现在的普通分辨率情况下效果还可以但是到了超高分辨率的显示器上效果就不行了。管
理这些基于光栅的图像的点将会消耗大量的处理能力，同时也是很浪费的。而采用基于向量的方式来替代象素，在一个可扩展的坐标系里绘制字体和其他线型，使得它们可以独立
于DPI。想想WindowsMetafile（WMF）和位图文件（BMP）之间的差距你就明白了。同时，向量图也使得一些变换如3D，旋转和动画变得更加方便和易
于操作。

  
　　作为新的图形引擎，WPF是基于DirectX的，当然增加了很多新的功能。其2D和3D引擎的强大看看Vista的界面就明白了，再加上其对Aero图形引擎的
支持，更加让你感到神奇。顺便提一下，Aero是专门为3D桌面开发的引擎，可以让桌面实现神奇的3D翻转，这绝对是操作系统有史以来的一次神奇尝试，虽然对硬件配置
的要求也是惊人的，此前已有相关报道称，Vista对显卡十分挑剔就是出于运行Aero的考虑。

  
　&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&
nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nb
sp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp
_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_p
lace_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_pla
ce_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place
_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_h
older;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_hol
der;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holde
r;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&n
bsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
WPF前景分析

  
　　WPF其实不仅仅是图形引擎而已，它将给Windows应用程序的开发带来一次革命，因为新的架构提供了一种全新的开发模式。当然对于普通用户而言，最直观的就是
界面越来越漂亮，看起来越来越舒服了；但对于开发人员而言，界面显示和代码将更好的得到分离，这与从前的桌面应用程序开发有很多不同（界面设置和代码是融合在一起的）
，这是比较具有革命性的改变之一。还有就是桌面应用程序和浏览器应用程序的融合，根据ms的承诺，正在开发中的WPF/E，即WPFEverywhere版本，将为基
于WPF的应用程序提供全面的浏览器支持，这意味着未来开发出的应用程序将可以基于浏览器在不同的操作系统上运行（也就是说桌面应用程序和浏览器应用程序将会融合！！
），当然由于目前还在开发中，我们并不确定会不会有一定的限制，根据WPF/E开发组的定义，WPF/E仍然是WPF的子集，而不是后继版本。总体而言，WPF的前景
应该是一片光明。

目前开发界的对WPF响应程度

  
　　目前已有很多人开始考虑或者已经转向WPF，一场新的学习热潮已经开始。但根据我最近的学习和了解，国内关于WPF的资料很少，除了msdn提供的资料以外，基本
都是来自国外的资料，有些则是国外开发人员blog上的资料，当然都是英文的。因此如果现在能够引进一些WPF的书绝对是很好的时机。而且国外目前的几本WPF书也是
刚刚上市，如果我们可以尽快引进的话，绝对可以帮助国内开发人员在最短时间内赶上国际步伐。

  
　　目前微软针对WPF提供的服务和支持

  
　　随着VistaRTM的发布，微软新一轮的技术推广已经开始。其实在此之前，WPF已经有很大的推广，因为CTP版本已经发布了有一段日子了。当然很多开发人员主
要以技术研究为主，也有少数公司已经开始从事基于WPF的产品研发工作。

  
　　1。目前WPF的正式版本已经发布（随。netframework3。0正式版发布），你可以从msdn上免费下载

  
　　2。相应的技术支持已经开始，但目前仅限于大客户，主要做售前技术支持，对于普通开发人员的技术支持可能要等到明年2月份才会开始（个人知道的情况，请以微软官方
技术支持网站发布的信息为准）

  
　　3。WPF的VS2005插件目前还只有社区预览版（CTP版），也是从msdn上免费下载的，但正式版恐怕还要等一段时间，但使用CTP版本确实已经可以在VS
2005中进行所见即所得的WPF开发。

  
  
　　对比MFC，winform，wpf

  
　　分析：

  
　　MFC生成本机代码，自然是很快。可是，消息循环，减缓了界面显示速度，

  
　　winform封装了win32的api，多次进行P/invoke操作（大部分使用p/invoke操作封装），速度慢。

  
　　wpf是一种新的模型，不再使用win32模型，自己新建模型，使用dx作为新的显示技术，直接访问驱动程序，加快了运行速度，可是，这种模型，需要支持dx9的
显卡，硬件要求高（你还能找到现代机器不支持dx9的吗？）

  
　&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&
nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nb
sp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp
_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_p
lace_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_pla
ce_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place
_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_h
older;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_hol
der;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holde
r;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
&nbsp_place_holder;&nbsp_place_holder; 　MFC，winform，wpf

  
　　开发效率上，MFC<WPF<winform

  
　　尽管MFC开发界面执行效率高但是开发效率低，作为现在的项目开发来说

  
　　时间跟开发效率往往能决定项目的成败，所以除非有特别的需求，否则都回尽量避免用mfc来做开发，MFC只是一个弱封装器

  
　　开发成本，MFC〉wpf〉winform

  
　　用MFC开发成本太高，对开发者能力要求更高，作为客服当然希望开发的费用越少越好，开发者当然希望钱赚得越多越好，这样一比，这也是MFC没落的一个很大的原因

  
　　界面执行效率上，MFC==WPF〉winform

  
　　随着计算机硬件的性能提高，多核cpu的普及，它们的差距会越来越小

  
　　开发灵活性上：wpf〉MFC〉winform

  
　　美观上：Wpf〉winform〉MFC

  
　　这一项中MFC下要开发出一个华丽的ui极其困难，也许你可以说你可以用控件，但是商业开发控件是要收费的！！Wpf很容易就可以做出vista那样的ui特效

  
　　mfc要写出这种效果不知要写到何年何月

  
　　这样一来MFC存在的价值就更低了。效率和美观不如Wpf，开发效率又不如winform，预计不出10年，随着vista取代xp，mfc将会退出历史舞台

  
　　内存使用上：wpf〉winform〉MFC

  
　　随着计算机硬件的性能提高wpf这个缺点会被忽略

  
　　使用范围：wpf〉MFC==winform

  
　　由以上可知：WPF大有取代winform和MFC之势，从未来net的发展来看，MFC以后只会变成一种经典，作为一种技术来供开发者学习，winform和W
PF两者会并存发展，但最终都会被WPF取代，最终实现桌面应用程序和浏览器应用程序的统一。

