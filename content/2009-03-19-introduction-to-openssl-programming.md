Title: OpenSSL 编程入门【转载-这篇很精】
Author: alswl
Slug: introduction-to-openssl-programming
Date: 2009-03-19 00:00:00
Tags: OpenSSL, SSL
Category: C
Summary: 

**OpenSSL ****编程入门**

  
作者:Eric Rescorla on Sat, 2001-09-01 01:0

如果你急切的想构建一个简单的Web客户端和服务器对,这时你就需要使用SSL了..

SSL是一种保护基于TCP协议的网络应用最快而且最简单的的方法,如果你正在用C语言做开发,那么对于你来说,最好的选择可能就是使用OpenSSL了.
OpenSSL是在Eric Young的SSLeay包的基础上对TSL/SSL的一个免费的执行(类似于BSD方式的License).然而, 不幸运的事情是,
伴随OpenSSL一起发布的文档和示例代码并不是很完全, 使用它的人需要更多的东西.在OpenSSL被使用之处,
man手册都相当优秀,可是这些手册失去了大的背景 因为它们只是参考资料而不是教程.

OpenSSL的API多而复杂, 因此我们在此并不会作出一个完整的讲述. 相反,我的目的只是教会你如何去高效的使用man手册.在本文中,
我们将会通过构建一个简单的Web客户端和服务器来演示OpenSSL的基本特点. 而在后续的第二篇中我们将会介绍OpenSSL的一些高级特性,
比如会话恢复和客户端认证等.

在话题开始之前, 我会认为你已经熟悉SSL和HTTP了, 或者最起码在概念层上应该有一些了解. 如果你对此一无所知,
推荐一个比较好的方法,那就是参考RFC(参见附录).

由于篇幅原因, 本文只包涵了源代码的一些摘录, 完整的代码可以从作者的站点[http://www.rtfm.com/openssl-
examples/](http://www.rtfm.com/openssl-examples/)上下载.

**程序**  
我们的客户端是一个简单的HTTPS(见 RFC 281![](/DOCUME~1/%E7%8B%84%E6%95%AC%E8%B6%85/LOCALS~1/
Temp/msohtml1/01/clip_image001.gif)客户端,它在初始化了一个到达服务器的SSL连接之后便通过这个连接将HTTP请求传送给H
TTP服务器. 然后等待服务器端的响应,并将响应信息打印在屏幕上.这是对通常那些"获取并且打印信息"的程序功能更简化的一个例子.

服务器端程序是一个简单的HTTPS 服务器, 它等待从客户端发出的TCP连接, 每当接收到一个连接时,它会磋商这个连接(的合法性).
一旦这个连接被确定下来, 它会读取客户端的HTTP请求, 并将HTTP请求的响应信息传输给客户端. 当响应传输完毕时它会关闭这个连接.

我们的第一个任务就是建立一个上下文对象(一个SSL_CTX), 这个上下文对象会在每次需要建立新的SSL连接的时候被用来创建一个新的连接对象.
而这些连接对象则用于SSL的握手,读和写.

(使用上下文对象)这种方法有两个优点: 首先, 上下文对象允许一次初始化多个结构体, 这样就提提高了性能. 在大多数应用中,
每一个SSL连接都使用相同的加密算法(keying material)和CA(certificate authority)列表等. 而采用上面这种方法,
我们就不需要在每次连接的时都去加载这些信息(加密算法和证书), 而只需要在程序启动时将它们加载进上下文对象中. 然后,当我们需要创建一个新的连接时,
只需要将新的连接简单的指向这个上下文对象就可以了. 使用一个简单的上下文对象的第二个好处就是它允许多个SSL连接之间共享数据,
比如用于SSL会话恢复的SSL缓冲(cache). 上下文初始化由主要的四个任务组成, 通过列表1所示的initialize_ctx()函数来完成.

**列表**** 1 initialize_ctx()**  
在应用OpenSSL之前, 整个库需要进行初始化, 这个过程通过SSL_library_init()函数来完成,它主要加载OpenSSL将会用到的算法,
如果我们想要很好的报告差错信息, 同样需要通过SSL_load_error_strings()来加载错误字符串, 否则,
就不能够将OpenSSL的错误映射为字符串.

我们同样需要创建一个对象来作为错误打印的上下文.
OpenSSL为输入和输出抽象了一个叫做BIO对象的概念.这样可以使得程序员针对不同种类的IO通道(socket, 中断,内存缓冲等)使用相同的函数,而唯一
的差别就是在函数中使用的是不同种类的BIO对象.在本例中,我们通过将一个BIO对象与标准错误stderr绑定来打印错误信息.

如果你正在写一个能够执行客户端认证的服务器或者客户端程序, 你就需要加载自己的公钥或者私钥以及相关的证书.证书存储空隙中,
并且通过SSL_CTX_use_certificate_chain_file()函数与CA证书一起被加载形成证书链表.
SSL_CTX_use_PrivateKey_file()函数用来加载私钥.出于安全原因, 私钥通常通过密码来加密, 如果使用密码加密的话,
密码回调函数(通过SSL_CTX_set_default_passwd_cb()来设置)将会在获取密码时被调用的.

如果你需要认证已经连接到你的客户端, OpenSSL需要知道你信任哪些CA,
SSL_CTX_load_verify_locations()调用用来加载CA.

为了保证安全, OpenSSL需要一个好的强性随机数源, 通常,为随机数生成器(RNG)提供种子原料是应用本身的责任,
然而,如果/dev/urandom可用的话,OPenSSL会自动的使用/var/urandom来为RNG播种,
由于/dev/urandom在Linux是标准化的, 我们不需要为它做任何事情, 这个就很方便了, 因为收集随机数很诡异,而且很容易引起系统抖动上升.
注意,如果你在一台不是Linux的系统上,你可能会在某些时刻得到错误数据, 因为随机数产生器没有被播种, OpenSSL的rand(3)
man手册为你提供了更多可以参考的信息.

**客户端**  
当SSL完成了对SSL上下文对象的初始化后，它已经为连接到服务器做好准备。OpenSSL要求我们自己建立一条从客户端到服务器的TCP连接，然后使用这个TCP
套接字创建一个SSL套接字.为了方便期间，我们把TCP连接的创建划分到函数tcp_connect()(这里没有给出实现，但是在下载的代码中可以看的到)中去实
现。

当TCP连接创建好以后，我们创建一个SSL对象来处理这个连接。这个对象需要与套接字绑定,注意，我们并不是直接把SSL对象绑定到套接字上，而是创建一个使用这个
套接字的BIO对象, 然后将SSL对象绑定到这个BIO上。

这个抽象层允许你通过各种通道来使用OpenSSL而不是套接字，前提是你已经有了

一个合适的BIO对象。例如，有一个OpenSSL测试程序纯粹通过内存缓冲区来连接SSL客户端和服务器。一个比较实用的做法就是支持一些套接字根本无法访问协议来
进行连接。例如，你可以通过一个连续行(serial line)来运行SSL。

SSL连接的第一步就是执行SSL握手，握手鉴别服务器(也可以选择鉴别客户端客户端)并且建立保护剩余传输所需要的加密算法。SSL_connect()
调用用来执行SSL握手.由于我们使用

的是阻塞式的套接字，所以SSL_connect()函数在SSL握手没有完成或者没有检测到一个差错之前是不会返回的。成功时，这个函数返回1，返回0或者负数表示
出错。

调用如下：

**[[Copy to clipboard]](http://linux.chinaunix.net/bbs/thread-852198-1-1.html######)**** ****[[ - ]](http://linux.chinaunix.net/bbs/thread-852198-1-1.html######)**

**CODE:**

/* Connect the TCP socket*/

sock=tcp_connect(host,port);

/* Connect the SSL socket */

ssl=SSL_new(ctx);

sbio=BIO_new_socket(sock,BIO_NOCLOSE);

SSL_set_bio(ssl,sbio,sbio);

if(SSL_connect(ssl)<=0)

&nbsp_place_holder;&nbsp_place_holder; berr_exit("SSL connect error");

if(require_server_auth)

&nbsp_place_holder;&nbsp_place_holder; check_cert(ssl,host);

  
当我们初始化到达服务器的SSL连接时，我们需要先校验服务器的证书链。OpenSSL为我们做一些这样的校验，但是不幸的是，其他的校验工作总是与具体的应用相关(
所以不能通过OpenSSL来完成)，因此，我们需要自己去做这些工作。我们的例子代码做的主要测试就是检验服务器的身份。这个通过列表2的函数check_cert
()来实现。

**列表****2 check_cert****函数**  
当检测到服务器的证书链有效的时候，你需要验证你正在查看的证书与你期望的服务器所拥有的身份是否相匹配。在大多数情况下，这意味着服务器的DNS名字出现在证书中，
或者在Subject Name 的Common Name域，或者位于证书的扩展部分(certificate
extension).尽管每种协议在识别服务器身份的时候有少许的差别，但是RFC
2818包括了通过SSL/TSL识别HTTP服务器身份的规则。如果你没有什么很明了的意图去做其他事情，按照RFC 2818 的规则去做是一个很好的做法.

由于大多数证书还一直将域名放在Common Name字段而不是扩展部分。所以我们只进行了

Common 字段的校验，我们通过SSL_get_peer_certificate() 函数来提取服务器的证书，然后将证书的Common
Name字段与我们连接的客户机名称进行比对，如果不匹配的话，肯定出错了，我们退出程序。

在0.9.5版本之前，OpenSLL容易遭到一种证书扩展攻击，为了方便理解，我们考虑下面的情况，一个服务器鉴别由Bob签名的证书，如图1示，Bob并不是你的
一个CA，但是它的证书却是由你信任的一个CA签名的。

如果你接受这个证书，你可能会有很大的麻烦，但是CA签名了Bob的证书这个事实却意味着它通过了对Bob的身份确认，但却不是说Bob可以被信任.如果你知道你想要
与Bob做生意，那很好，但是如果你想要与Alice（你从从来没听说过，但是Bob为她担保）和Bob一起做生意，那这些信息就没有用了。

通常，保护你免于此类攻击的唯一方法就是限制证书链的长度，目的就是使你明确你所观看的证书就是CA签名的。V3版的X.509证书包含了一种方法，它使得CA能够在
一些证书上做标签说明这些证书是其他CA的。这种方法允许一个CA有一个简单的根CA，然后根CA可以认证其他的辅助CA。

当前的OpenSSL(v0.9.5和以后的)都会校验这些扩展，因此不论你是否校验证书链的长度，这些扩展攻击都会被自动防御掉。比0.9.5更早的OpenSSL
一点都不作这些扩展部分校验，所以如果要使用这个版本之前的OpenSSL的话，你必须自己限制链的长度。0.9.5版的OpenSSL在校验上有一些问题，所以如果
你正在使用它你也许应该进行一些更新。initialize_ctx() 函数中，代码#ifdefed提供了对老版本链长度的校验，我们使用SSL_CTX_set
_verify_depth()函数强迫OpenSSL去校验链的长度。总之，强烈建议你升级到0.9.6，主要是因为比较长的链（但是也有可能是故意构造的）越来越
流行了，绝对最新和最好的版本就是OpenSSL 0.9.66了

我们使用列表3的代码来写HTTP请求，出于演示的目的，我们使用了或多或少的在REQUEST_TEMPLATE变量中可以找到的硬线路(HardWired)HT
TP请求。由于连接的机器可能会改变，我们不需要填充Host这个头信息。这个通过snprintf来实现。然后我们通过SSL_write()函数来发送数据到服务
器端，SSL_write()的API或多或少与Write()函数类似，区别就是在write中我们传递文件描述符，而在前者中传递SSL对象。

**列表****3 ****写****HTTP****请求。**  
有经验的TCP程序员都知道，我们在函数的返回值不等于我们想要写入的字节数时抛出一个错误,而不是循环的调用些函数. 在阻塞模式下，SSL_write()函数已
经足够，因为在所有的数据都被写完或者发生差错之前，这个调用是不会返回的。然而write()函数却可能只会写入一部分数据，我们可以通过设置SSL_MODE_E
NABLE_PARTIAL_WRITE标志位来允许部分写(本文没有应用)，在这种情况下，你需要循环的调用写函数。

在老版本的HTTP1.0中，服务器传输它的HTTP响应然后关闭连接。在后来的版本中，引入的持续连接，支持同一连接上多个连续的事务。为了方便和简洁，在本文并不
使用这种持续的连接。我们忽略(允许设置持续连接的)头部信息，使服务器通过关闭连接来通知响应的结束。在操作上，意味着我们只需要持续读，直到文件结束，这样也相应
的简化了事务。

OpenSSL使用SSL_read() 函数来读取数据，正如列表4中所示，跟使用read()一样，我们只需要简单的选择一个合适大小的缓冲，然后将它传递给SS
L_read()函数。注意到缓冲区的大小在此处并没有多么的重要，SSL_read() 和read()一样，返回可用的数据，哪怕它比请求的数据量小.
另外，如果没有数据可以读取，读函数将会阻塞。

**列表****4 ****读取响应**  
BUFSIZZ的大小, 基本上可以说与性能是持平的, 这种性能持平与我们简单的从普通的套接字读取是不同的.
在那种情况下,对read的每一次调用都需要上下文切换到内核态去,由于上下文在内核态和用户态之间切换是非常昂贵的,
程序员在读取数据的时候都尽量使用较大的缓冲从而减少读取的次数(从而减少了上下文切换的次数). 然而当我们在使用SSL的时候, 对read()的调用次数,
也就是上下文在内核态和用户态切换的次数, 在很大程度上取决于数据写入的记录数而不是SSL_read()的调用次数.

例如,如果客户端写入了1000Byte的记录, 然后我们调用SSL_read()每次读取1Byte,
那么对SSL_read()的第一次调用会使得所有的记录被读入,
然后剩下的调用就只是将记录从SSL缓冲中读出来.因此,在使用SSL而不是普通的套接字读取数据时,缓冲区的大小选择并不是特别的重要.
如果数据被写成一系列小的记录, 你可能想通过对Read的一次单独的调用来读取所有的记录. 这时候,
OpenSSL为你提供了一个标志位,那就是SSL_CTRL_SET_READ_AHEAD, 通过设置这个标志位就可以打开这种读的开关.

注意本文中使用switch语句来处理SSL_get_error()函数返回值这种用法，使用普通的套接字的一个方便之处就是任何的负的返回值(最典型的是－1)都
代表失败，然后你可以检测errno去查看真正发生了什么事情。但是errno在这里并不起什么作用，因为它只代表了一个系统错误，而我们想要做的是对SSL错误进行
处理。同样编程时需要对errno进行细心的处理,以便实现线程安全。

在OpenSSL中提供了SSL_get_error()调用而不是errno, 这个调用使得我们可以检测返回值以确定是否有错误发生，如果有错误发生，是什么错误
。如果返回值是一个正数，说明我们读取到了一定的数据，这时候将它简单的打印到屏幕上. 一个真正的客户端会解析HTTP响应然后或者显示数据或者将数据保存到磁盘。
但是对OpenSSL而言,这些并没有多大意义，所以我们在此处不会涉及对响应信息的具体处理。

如果返回值是0，并不表示没有数据可以读取，因为在没有数据可以读取的情况下，正如上面已经讨论过的一样,
我们的函数肯定会被阻塞住的。所以,此处返回的0表明这个套接字已经被关闭了，当然也就没有任何数据可以读取了，所以我们退出循环。

如果返回值是一个负值，这时肯定发生了某种错误。我们只关心两种类型的错误：普通错误和提前关闭的错误，我们使用SSL_get_error()函数来决定得到的是那
种类型的错误，差错处理在客户端的程序中非常的简单。所以对于大多数错误，我们仅仅使用berr_exit()函数来打印一行错误信息然后退出，然后,提前关闭这种错
误需要进行特殊的处理.

TCP使用FIN片断来表明发送者已经发送完所有的数据. SSL v2 允许任何一端通过发送TCP FIN字段来结束SSL连接.
但是,这种原则却会遭受一种截断攻击，攻击者可以自己伪造一个TCP FIN来终止连接，使得发送的数据比实际要发送的少.
除非受害者有某种方法知道他将要接收多长的数据，否则她/他很容易会认为接收到的那一部分长度的数据已经是所有的了。

为了解决此种安全隐患，SSL v3引入了close_notify()警报机制，close_notify是一个SSL消息(因此是安全的)但却不是SSL数据流的
一部分，因此应用程序并不能看到它。在close_notify消息被发送出去之后，任何数据将不能再传输了。

因此当SSL_read()返回0表示套接字已经被结束时，这其实意味这close_notify消息已经收到，如果客户端在收到close_notify消息之前收
到一个FIN，SSL_read()将会返回一个错误，这种情况叫做提前关闭。

一个比较简单的客户端可能在遇到任何一个提前关闭的情况时都会报告一个错误然后退出.

这个处理是SSL V3采取的默认处理方式，但是，不幸的是，对于客户端来说,发送提前关闭消息是一个很常见的差错。所以，如果你不是为了一直汇报错误的话，你最好忽
略这些提前关闭消息。我们的代码进行了特别的处理，它报告错误却不随着错误而退出程序。

  
如果在读取响应的时候没有发生任何错误，这时我们就需要发送自己的close_notify 消息给服务器端，这个是通过SSL_shutdown() 函数来实现的
,在讨论服务器端的时候我们会仔细的研究这个函数的。但是大体的思想却很简单：返回1表示完全关闭，0表示不完全关闭，－1表示出错。由于我们已经收到了服务器端发送
的close_notify消息，所以唯一可能出现的问题就是我们在发送我们自己的close_notify消息时出了差错，要不然的话，SSL_shutdown(
)函数将会成功的（返回值为1）

最后，我们需要销毁申请的变量对象，因为这个程序最终要退出的，释放这个操作并不是严格意义上必须的进行的，但是在更一般的程序中它却是必要的。

**服务器**  
我们的Web服务器除了比客户端更复杂点外, 可以说是客户端的一个镜像，首先，为了服务器能处理多个客户端，要要调用fork()来创建子进程，然后我们用Open
SSL使用的BIO对象的API来一次一行的读取客户端的请求，同样用BIO来实现对客户端的缓冲写，最后，服务器端的关闭过程有些复杂。

通常在一台Linux系统上，服务器处理多个客户端连接最简单的方法就是为每个客户端fork()出一个子进程，我们在这里是在accept()返回之后通过fork
()来创建子进程。每一个子进程独立运行并且在对客户端进行服务以后自行退出。尽管这种方法在比较繁忙的Web服务器上可能相当慢，但是在此处却是可以接受的，列表5
是主服务器的accept循环

**列表****5 ****服务器接收连接循环**  
在fork()和创建SSL对象之后，服务器调用SSL_accept()函数，从而引起OpenSSL执行了服务器端的SSL握手，跟使用SSL_connect(
)一样，由于我么使用的是阻塞式的套接字，所以SSL_accept()函数将会一直阻塞直到握手完成为止。因此，SSL_accept()返回的唯一情况就是握手完
成或者检测到错误。SSL_accept()返回1表示成功，返回0或者负数表示失败。OpenSSL的BIO对象在某种程度上有栈的特性，因此我们可以把SSL对象
封装在BIO(SSL_BIO对象)中，然后把那个BIO封装在一个缓冲的BIO对象中，如下所示：

**[[Copy to clipboard]](http://linux.chinaunix.net/bbs/thread-852198-1-1.html######)**** ****[[ - ]](http://linux.chinaunix.net/bbs/thread-852198-1-1.html######)**

**CODE:**

&nbsp_place_holder;&nbsp_place_holder; &nbsp_place_holder;&nbsp_place_holder;
&nbsp_place_holder;&nbsp_place_holder; &nbsp_place_holder;&nbsp_place_holder;
&nbsp_place_holder;&nbsp_place_holder; &nbsp_place_holder;&nbsp_place_holder;
&nbsp_place_holder;&nbsp_place_holder; &nbsp_place_holder;&nbsp_place_holder;
&nbsp_place_holder;&nbsp_place_holder; &nbsp_place_holder;&nbsp_place_holder;
io=BIO_new(BIO_f_buffer());

&nbsp_place_holder;&nbsp_place_holder;
&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
ssl_bio=BIO_new(BIO_f_ssl());

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
BIO_set_ssl(ssl_bio,ssl,BIO_CLOSE);

&nbsp_place_holder;&nbsp_place_holder;
&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;
BIO_push(io,ssl_bio);

  
这种方法允许我们使用BIO_* 函数族来操作新类型的IO对象,从而实现对SSL连接的缓冲读和写。在此处，你也许会问，为什么这个用法更好？（或者这有什么好的）
。主要的原因是，这种方法编程起来很舒服，它使得程序员能够去处理一种更自然的单元(行或者字符等)而不是SSL记录。

**请求**  
HTTP请求由请求信息行后面跟着一堆头信息行再加上一个可选体组成。头信息行是通过空行来结束的（例如，一对CRLF，有时候崩溃的客户端会发送一对LF），最舒服
的读取请求信息行和头信息行的方式就是一次读取一行，直到读取到空行为止。我们可以使用列表6中的OpenSSL_BIO_gets()调用来实现这个操作。

**列表****6 ****读取请求**  
OpenSSL_BIO_gets()调用表现的类似于标准输入输出调用fgets(),它使用任意大小的缓冲区和长度从SSL连接中读取一行数据到缓冲中去，读取的
结果通常以空字符结束(但也包括结束符LF)。因此，我们每次简单的读取一行，直到读到某一行包括一个简单的LF或者CRLF。

由于我们使用固定大小的缓冲，所以有可能，也许不太可能，我们会读取到很长的一行，在这种

情况下，这一行将被分解成两行，在极端不可能的情况下，分隔正好在CRLF之前发生，这样的话，从前一行读取到的第二行就只包括一个CRLF了，这时候我们就会迷惑，
认为头序列提前结束了。一个真正的Web服务器会检测这种情况的，但是在这里却不值得去做。注意，不管到达的行数是多少，都不会有缓冲区溢出的情况发生。所有可能发生
的就是我们会错误的解析头信息。

注意到我们并不需要用HTTP请求做任何事情，所以只是读取然后将它丢弃。真正的实现将会读取请求信息行和头信息行，计算是否有一个消息体存在然后读取这个消息体。

下一步就是写HTTP响应并且关闭连接：

**[[Copy to clipboard]](http://linux.chinaunix.net/bbs/thread-852198-1-1.html######)**** ****[[ - ]](http://linux.chinaunix.net/bbs/thread-852198-1-1.html######)**

**CODE:**

if((r=BIO_puts

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; (io,"HTTP/1.0 200
OK\r\n"))<0)

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; err_exit("Write
error");

if((r=BIO_puts

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; (io,"Server:
EKRServer\r\n\r\n"))<0)

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; err_exit("Write
error");

if((r=BIO_puts

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; (io,"Server test
page\r\n"))<0)

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; err_exit("Write
error");

if((r=BIO_flush(io))<0)

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder; err_exit("Error
flushing BIO");

  
注意我们在程序中使用BIO_puts()而不是SSL_write()。这样我们就可以一次写一行响应消息，而把所有的行当作一条SSL记录发送出去，这种做法是很
重要的，因为准备（计算完整性，校验，加密等）一个SSL传输记录的花销是非常大的。因此，使一条传输的记录尽可能的大是一个很好的主意。

我们有必要留意一下所使用的缓冲写方法. 首先，在关闭之前你需要冲掉缓冲区，SSL对象并不知道你已经在它上面布置了一层BIO，所以，如果你破坏了SSL连接，将
会使得剩余截断的数据留在缓冲区中。BIO_flush() 函数是用来处理这个的。同样，默认情况下,OpenSSL为BIO对象使用了1024Byte大小的缓冲
区，由于SSL记录大小可以长达16K，所以使用1024Byte大的缓冲可能会引起过多的碎片(从而使效率下降)，你可以使用BIO_ctrl()
函数来增加缓冲区的大小。

一旦完成了响应的传送，我们需要发送close_notify消息，前面已经讲到了，是通过SSL_shutdown来实现的，不幸的是，当服务器首先关闭的时候，情
况变得游戏蹊跷。我们对SSL_shutdown() 的第一次调用会发送close_notify消息，但是在另一端却不会取寻找它。所以它会很快的以0作为结果返
回，表明关闭过程没有完成。然后,就需要应用程序自身再一次调用SSL_shutdown()函数了。

这里也可以存在两种观点，我们能够肯定已经看到了自己关注的HTTP请求的整个部分，然后对其他都不感兴趣，因此，我们可以并不在乎客户端是否发送了close_no
tify消息，相反，如果严格的遵守协议并且要求其它人也这么作的话，我们也就就需要收到一个close_notify消息。

如果坚持第一种观点的话，一切将会变得很简单，我们简单的调用SSL_shutdown()
函数发送我们的close_notify消息，然后不管客户端是否发送一个close_notify
消息，就立刻退出。如果坚持第二种观点的话(本文的例子服务器就是这么做的)，事情就变得比较复杂了，因为客户端通常都不会表现的多么正常。

我们面临的第一个问题就是客户端通常都不会发送close_notifys消息。事实上，有些客户端在它们收到HTTP响应时便会立即关闭连接(有些IE是这么做的)
，当我们在发送close_notify时，另一端可能正在发送一个TCP RST字段，在这种情况下，程序将会捕获SIGPIPE信号，在本文,
我们将会在函数initialize_ctx()中安装一个虚设的SIGPIPE信号处理器来避免这种情况的发生。

我们面临的另外一个问题就是客户端可能不会立即发送一个close_notify消息来作为对服务器端close_notify消息的回应，一些版本的Netscap
e 要求你首先发送一个TCP FIN标志。因此我们在第二次调用SSL_shutdown()之前调用了shutdown(s,1)函数，当我们使用1作为第一个参
数时，shutdown()函数发送了

一个FIN标志，但是却使得套接字处于打开并且读的状态。服务器端关闭的代码如列表7所示.

**列表****7 ****访问****SSL_shutdown()**  
**其它相关的东西**  
在本文，我们只是提及了使用OpenSSL时的一些表面的观点，下面是更多的一些观点：

一种更复杂的检测证书中服务器名字的方法就是使用X.509当中的subjectAltName扩展部分。为了做这个检测，我们需要从证书中提取出这个部分来，然后根
据hostname检测这个部分，同样，能够在证书中根据wild-carded 名字来检测主机名也是非常有意思的事情。

注意这些程序处理差错都是根据错误简单的退出程序，一个真正的应用将会识别出错误类型然后发信号告诉给用户或者一些审计日志，而不是直接退出。

下篇文章中，我们将会讨论一些OpenSSL的高级特性，包括会话恢复，多路传输,非阻塞IO以及客户端认证等。

