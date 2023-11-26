

1.编译时候会出现函数问题

```
'pcap_findalldevs_ex' : undeclared identifier
'PCAP_SRC_IF_STRING' : undeclared identifier
'pcap_open' : undeclared identifier
'PCAP_OPENFLAG_PROMISCUOUS' : undeclared identifier
'=' : cannot convert from 'int' to 'struct pcap *'
```

等一系列函数找不到的问题，导致这些问题的关键在于他们的函数声明并不包含在pcap.h这个

头文件里面，而是包含在remote-ext.h这个函数里面，所以只需要在

#include "pcap.h"后面加上

#include "remote-ext.h"

就可以编译通过了。

网上有网友戏称说是WinPcap开发小组故意做的恶作剧或者是撰写doc说明时候忘记加入了

= =#

2.出现连接错误

```
Cpp3.obj : error LNK2001: unresolved external symbol
[__imp__ntohs@4](mailto:__imp__ntohs@4)

Debug/Cpp3.exe : fatal error LNK1120: 1 unresolved externals
```

一般添加工程只需要添加wpcap.lib这个库文件，而在分析数据包这段代码里，光这个头文件

已经不够了，需要再添加ws2_32.lib这个头文件。其实这个在WinPcap的配置VC里有说明，但

是以前懒，都只用wpcap.lib

3.关于程序运行时候是否需要WinPcap的支持，我无法测试出结果，因为学校上网方式的限制

，所有系统都是有WinPcap运行库文件的，待会儿去网上找找相关资料呢

4.暑假一直看的是英文说明文档，很吃力，最近在搜狗随便一搜，居然发现了有现成翻译好的

中文说明文档，翻译挺不错的，可以去搜索下一下。

终于开始开网络编程课，感叹一下WinPcap的强大，还是停留在用户层的编程，完全没能力看

核心的源代码。。。

