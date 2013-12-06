Title: AzaAjaxChat笔记-实现
Author: alswl
Slug: azaajaxchat-notes-implementation
Date: 2010-08-22 00:00:00
Tags: AzaAjaxChat, Comet, Flex, FMS, JavaScript, RTMP
Category: PHP编程
Summary: 

唔，继续整理笔记，这些是在代码编写中遇到的问题和解决办法的总结，不是Turtial，问题有针对性，内容枯燥，路人可以直接忽略~

### 一、Comet服务器推技术

Comet推技术，一句话概括，就是形成一个不断开的连接，使得服务器能主动向客户端发送信息。这种技术在交互性强的Web产品中应用的非常多，比如GMail。Co
met的实现方式有两种：基于 AJAX 的长轮询（long-polling）方式和基于 Iframe 及 htmlfile
的流（streaming）方式，具体两种实现方式可以参考[Comet：基于 HTTP
长连接的"服务器推"技术](http://www.ibm.com/developerworks/cn/web/wa-lo-comet/)。

我计划把这个技术引入，成为一个亮点，第二种Comet实现方式过于复杂（GMail使用的就是这种），我就尝试第一种。我在测试环境测试了基于 AJAX 的长轮询
（long-polling）方式。这种方式说白了就是在Ajax获取返回数据时候，在状态吗为4（数据传输完成）情况随后进行下次查询。进行循环的查询。

这种Long-polling的轮询方式有点伪Comet。相对于常见的定时查询，不同点是将"查询->返回->再查询"中间的一段断开时间进行重连接。最后因为技术
实现和开发时间，我决定放弃了Comet的实现。

PS：一个系统应该不仅仅是技术的堆积，也应该考虑其他的一些因素，是否有确实需求，开发效率问题。虽然我做了一些前期准备，最终还是没有加入Comet，蛮可惜的。

#### 相关链接：

  * [一步一步打造WebIM（1） - .net - dotnet - JavaEye论坛 ](http://www.javaeye.com/topic/652949)（.net使用IHttpAsyncHandler的实现）
  * [Comet--"服务器推"技术 - 搜狐UED](http://ued.sohu.com/article/118/comment-page-1)（搜狐UED团队的一个小介绍）

### 二、用户状态的处理

开发时候遇到一个逻辑问题，具体描述如下："一个用户登录长时间不活动（比如直接关闭浏览器），系统需要判定此用户为离线。"按照一般设计思路，这个动作应该由后台每
过一段时间自动（比如说5分钟）触发一次，如果用Java或.net实现，会考虑设计一个后台运行的进程进行管理。而现在用的PHP，我查了一下，似乎没有找到相应的
解决办法。

我尝试在系统中设定一个页面每隔几分钟触发一个动作，放置在index.php页面中，但是感觉这个设计有点鸡肋。

这个问题困惑我很久，最后参考了[AJAX Chat](https://blueimp.net/ajax/)的源码，它的思路是在一个新用户上线时候，进行检测所
有用户距离上次其活动的时间来判定每个用户的离线状态。这个也不是最优想法（万一长时间没有用户登录怎么办？），但是比上面那个定时页面要好多了。

如果有PHP达人看到这个，望不惜赐教。

### 三、RTMP

RTPM是一个流媒体传输的协议，我在AzaAjaxChat中用它进行视频聊天画面和音频传输。这块内容可以洋洋洒洒的写一大篇日志，我在这里只是简单罗列一下我用
到的相关内容。

> Real Time Messaging Protocol（实时消息传送协议协议)概述，实时消息传送协议是Adobe
Systems公司为Flash播放器和服务器之间音频、视频和数据传输开发的私有协议。它有三种变种： 1)工作在TCP之上的明文协议，使用端口1935；
2)RTMPT封装在HTTP请求之中，可穿越防火墙； 3)RTMPS类似RTMPT，但使用的是HTTPS连接；

>

> RTMP协议是被Flash用于对象，视频,音频的传输.该协议建立在TCP协议或者轮询 HTTP协议之上。

>

> RTMP协议就像一个用来装数据包的容器，这些数据可以是AMF格式的数据，也可以是FLV中的视/音频数据。一个单一的连接可以通过不同的通道传输多路网络流。
这些通道中的包都是按照固定大小的包传输的。

我使用FMS作为RTPM容器，Adobe FMS（Flash Media Server）是一款能够提供出色的Flash
Video流媒体播放功能的服务器软件。

FMS提供一个强大Script可定制脚本的服务器流媒体引擎，通过这个引擎，允许创建和交付面向互联网任何用户群体的交互媒体应用及服务。FMS还是Adobe公司
跨媒体解决方案中的一部分，针对诸如数据库连接访问、文件系统操作、服务访问等要求，可以同Adobe Flash Player与Adobe AIR一起来实现。

### 四、基于Flex的流媒体传输

#### 4.1 官方Sample-Stratus

AzaAjaxChat中最技术含量的地方在于语音视频聊天。Adobe官网在Flex子类中提供了一个Demo名叫[Stratus](http://labs.a
dobe.com/technologies/stratus/samples/)，正是一个聊天系统。从教程上看，Adobe公司目前开放的Stratus是同时支
持视频和语音P2P的，同时，未来的FMS也可能会支持P2P。

Adobe的某个专家博客还针对Stratus有一篇相当详细的讲解，原文在此[Stratus service for developing end-to-
end applications using RTMFP in Flash Player 10 | Adobe Developer Connection](
http://www.adobe.com/devnet/flashplayer/articles/rtmfp_stratus_app.html)，文中分析了
RTMFP（比RTMP更高阶的流媒体传输协议，支持P2P）和Stratus的相关核心代码。我本想把这篇文章翻译，完成10%之后，意外发现已经有人翻译了，地址
在此[通过Stratus 服务器在Flash Player中使用RTMFP 开发 点对点应用(一) -- Windows Live](http://snow
yrock.spaces.live.com/Blog/cns!B8CBEB7169880B1D!1279.entry?wa=wsignin1.0&sa=18
3740112)，[通过Stratus 服务器在Flash Player中使用RTMFP 开发 点对点应用（二） -- Windows Live](http
://snowyrock.spaces.live.com/blog/cns!B8CBEB7169880B1D!1278.entry?_c=BlogPart)
。

同时可以参考其他例子[FMS3系列(五)：通过FMS实现时时视频聊天（Flash|Flex） - Bēniaǒ成长笔记 -
博客园](http://www.cnblogs.com/beniao/archive/2009/04/28/1444159.html)。

#### 4.2 AzaAjaxChat视频语音核心代码

下面是核心代码。

    
    protected function starChat(event:MouseEvent):void {
    	//同时开始监听
    	doReceive();
    	//初始化一个网络连接 
    	publicNc = new NetConnection();
    	//开始连接 
    	publicNc.connect(rtmpUrl); 
    	//为这个连接添加事件,这个事件有返回连接状态 
    	publicNc.addEventListener(NetStatusEvent.NET_STATUS,onPublishNetStatusHandler); 
    	microphone = Microphone.getMicrophone();
    	camera = Camera.getCamera();
    	if(!camera) {
    		Alert.show('没有开启摄像头或者没有安装摄像头');
    	} else {
    		this.videoPublish.attachCamera(camera);
    	}
    }

private function onPublishNetStatusHandler(event:NetStatusEvent):void {

//根据连接返回的状态信息判断是滞连接成功

if(event.info.code=="NetConnection.Connect.Success"){

appMessage.text += "n发布连接建立成功";

publicNs = new NetStream(publicNc);

publicNs.attachAudio(microphone);

publicNs.attachCamera(camera);

publicNs.client = this;

publicNs.publish(publicName,"live");

}

}

private function doReceive():void {

receiveNc = new NetConnection();

//开始连接

receiveNc.connect(rtmpUrl);

//为这个连接添加事件,这个事件有返回连接状态

receiveNc.addEventListener(NetStatusEvent.NET_STATUS,onReceiveNetStatusHandler
);

}

private function onReceiveNetStatusHandler(event:NetStatusEvent):void {

//根据连接返回的状态信息判断是滞连接成功

if(event.info.code=="NetConnection.Connect.Success"){

appMessage.text += "n接受连接建立成功";

receiveNs = new NetStream(publicNc);

video = new Video();

video.width = 230;

video.height = 173;

video.attachNetStream(receiveNs);

this.videoReceive.addChild(video);

receiveNs.play(receiveName,"live");

} else {

appMessage.text += "n" +　event.info.code;

}

}

#### 4.3 管道NetConnection.connect()

Flex流媒体传输通过通道传输，在NetConnection之上建立连接，由于RTMP和FMS的存在，我们可以很方便的在网络流上写入和读取流媒体信息。Net
Connection.connect()支持FMS流媒体和本地文件，官方解释如下。

> 在 Flash Player 或 AIR AIR 应用程序和 Flash Media Server 应用程序之间创建双向连接,NetConnection
对象如同客户端与服务器之间的管道。

>

> 如果未使用 Flash Media Server，请调用 NetConnection.connect()，以便从本地文件系统或 Web
服务器中播放视频和 MP3 文件。有关支持的编解码器和文件格式的信息，请参阅 [http://www.adobe.com/go/hardware_scali
ng_cn](http://www.adobe.com/go/hardware_scaling_cn)。

#### 4.4&nbsp_place_holder; flash.net.NetConnection 上找不到属性 onBWDone

这个问题参考[在 flash.net.NetConnection 上找不到属性 onBWDone，且没有默认值。解决办法。 - Xiang -
CSDN博客](http://blog.csdn.net/xiang08/archive/2009/07/13/4343551.aspx)，解决如下。

> 在 flash.net.NetConnection 上找不到属性 onBWDone，且没有默认值。

>

> _nc = new NetConnection();

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;_n
c.addEventListener(NetStatusEvent.NET_STATUS,netStatusHandler);

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;_n
c.client = this;

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;_n
c.objectEncoding = ObjectEncoding.AMF0;

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;_n
c.connect("rtmp://localhost/oflaDemo");

>

> 首先添加_nc.client = this.

>

> 然后新建一个方法：public function onBWDone():void{}

>

> 问题解决。

### 五、JavaScript和Flex的交互

页面上的Flex必须响应页面JavaScript的触发事件，Adboe在设计Flex时候，预留了相互调用的端口ExternalInterface，详情可以G
oogle之，类似代码如下。

    
    if (ExternalInterface.available) {
    	ExternalInterface.addCallback("initParams", initParams);
    	ExternalInterface.addCallback("playSound", playSound);
    } else {
    	this.appMessage.text += "nJS无法调用Flash，请检查Flash环境";
    }

但是这种调用方法存在着一个致命的问题：创建一个swf的Object，当对这个swf做隐藏/显示的时候(display:none,display:block)
的时候，swf的所有的注册的javascritp函数都会被干掉(ExternalInterface.addCall方法)。这个是Flex的一个BUG，现在也
还没有解决。

相关讨论可以参见[Javascript无法访问Flex问题~ - rwl6813021 -
JavaEye技术网站](http://rwl6813021.javaeye.com/blog/236344)，文中详细讨论了这个问题，并给出一个解决方案。

有一个折中的方案：即通过LocationConnection(本地通讯,利用两个swf来进行交互)来处理，初始化一个调用的client
swf，负责调用被隐藏的swf中的方法，这样就避开了直接通过javascript调用被隐藏的swf中的方法。

    
    //1：client 发送端:
    private var ucallswfconn:LocalConnection;
    public function init():void {
    	ucallswfconn = new LocalConnection();
    	//注册Javascritp方法，网页调用该flex的方法，通过该方法中转，调用另外一个flex的方法
    	ExternalInterface.addCallback("selectCallControl",flexSelectCallControl);
    }

public function flexSelectCallControl(method:String,param:String):void {

//Alert.show(method+param);

//调用另外一端swf中的方法，参数：1:receiver端监听的服务名称 2:方法名称 3:参数
ucallswfconn.send("ucallexternconn",""+method,""+param);

}

//2：receiver 接收端：

//add by polarbear, 2008.09.04, 本地通讯

this.ucallexternConn = new LocalConnection();

this.ucallexternConn.allowDomain("*");

ucallexternConn.client = this;

try {

this.ucallexternConn.connect("ucallexternconn");

} catch (error:ArgumentError) {

trace("连接失败");

}

注意被调用的函数必须是public的。

我使用这个方法并没有成功，最后我采用的是将视频画面直接放在界面上（很丑，不得已为之）。上文的解决方案只是给出一个思路，感兴趣的话可以自己试试。

### 六、Last

其实还有很多细节地方可以讲讲，我就不一一展开了。整理的文章就是这样，也没什么花样和娱乐，我都懒得加图片了~

祝大家周末愉快，最近我睡眠很不好，每天6点就醒了，中午补个觉去……

