

下学期有网络变成，用的是《计算机网络高级软件编程技术》，研究生教材，感觉书写的很泛泛，毕竟是给研究生用的书籍，很多基础的细节都没有写清楚，搞不懂学校怎么弄这
种书，叹一个。

直接导致了我很多东西都得一点一点去网上查找。

很多函数都是用的WinPcap的，所以我又抓紧时间看WinPcap的入门知识。

WinPcap开发包下载：[http://www.winpcap.org/install/default.htm](http://www.winpcap.o
rg/install/default.htm)

里面有开发者包Developer's Pack和普通使用的安装程序，宽带上网助手就是普通的安装包，而开发要使用的则是Developer's Pack。

下来之后，安装到某个目录，然后配置VC，把那个目录的include和lib两个目录放到VC的选项->目录里面。

WinPcap目录下有doc文档，里面的东西相当全面。我运行了两个，都不能直接运行。

第一个简单程序是获取网卡适配器信息，里面一个函数pcap_findalldevs_ex找不到，网上资料说是因为这个函数属于远程网卡获取，它的声明在#incl
ude "remote-ext.h"里面，加上去就可以运行了。

第二个程序错误更多，

```
F:学习网络WiPcap8_08_202Cpp1.cpp(155) : error C2065: 'socklen_t' : undeclared
identifier

F:学习网络WiPcap8_08_202Cpp1.cpp(155) : error C2146: syntax error : missing ';'
before identifier 'sockaddrlen'

F:学习网络WiPcap8_08_202Cpp1.cpp(155) : error C2065: 'sockaddrlen' : undeclared
identifier

F:学习网络WiPcap8_08_202Cpp1.cpp(164) : error C2065: 'getnameinfo' : undeclared
identifier

F:学习网络WiPcap8_08_202Cpp1.cpp(170) : error C2065: 'NI_NUMERICHOST' : undeclared
identifier
```

错误根由是因为WinPcap支持ipv6,而VC的winsock2.h太老了，很多结构都没有被支持，所以产生错误。网上有人说可以用VS新版本调试，我电脑里面
是VS2008，但是仍然产生错误

`_vsnprintf` 属性与生命不匹配，网上没有合适的解决方案，我感觉是WinPcap的某个头文件与stdio.h参数不匹配。

既然VS也无法通过，我实在没能力去修改WinPcap的头文件，所以就用最后一个方案，使用VC6.0的最新的PlatForm
SDK开发包，里面包含了新的头文件，就可以支持WinPcap了。

有人说PSDK只有Windows2003的版本，我在微软里面找到了WinXPSP2的PSDK。

网址如下

[http://www.microsoft.com/msdownload/platformsdk/sdkupdate/XPSP2FULLInstall.htm](http://www.microsoft.com/msdownload/platformsdk/sdkupdate/XPSP2FULLInstall.htm)

里面好几个Cab，网页里面有完整的安装说明。

我正在下，搞好之后如果能用再说。

弄好了，下面是PlatFormSDK安装步骤

(1)安装过程:

CMD运行PSDK-FULL.bat，参数为一个目录，里面会被解压缩安装包，然后Setup，一路Next就可以了。

(2)配置过程

打开Visual C++6.0，在选项里面连接，把PSDK安装后的include和lib加入相应的位置。

特别注意，要把这些目录的顺序调高，我直接放到了最高层去了。

呵呵，编译一下，通过了，好Happy啊。

