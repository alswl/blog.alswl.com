Title: Socket编程之Select【转载】
Author: alswl
Date: 2009-03-24 00:00:00
Tags: 网络编程
Category: C/C++编程
Summary: 

这篇文章讲的是Socket中的select，我觉得还不错就转来了

出处：[http://www.cnblogs.com/xuyuan77/articles/1206418.html](http://www.cnblogs.
com/xuyuan77/articles/1206418.html)

感谢原作者

Select在Socket编程中还是比较重要的，可是对于初学Socket的人来说都不太爱用Select写程序，他们只是习惯写诸如connect、accept
、recv或recvfrom这样的阻塞程序（所谓阻塞方式block，顾名思义，就是进程或是线程执行到这些函数时必须等待某个事件的发生，如果事件没有发生，进程
或线程就被阻塞，函数不能立即返回）。可是使用Select就可以完成非阻塞（所谓非阻塞方式non-block，就是进程或线程执行此函数时不必非要等待事件的发生
，一旦执行肯定返回，以返回值的不同来反映函数的执行情况，如果事件发生则与阻塞方式相同，若事件没有发生则返回一个代码来告知事件未发生，而进程或线程继续执行，所
以效率较高）方式工作的程序，它能够监视我们需要监视的文件描述符的变化情况——读写或是异常。

下面详细介绍一下！

Select的函数格式(我所说的是Unix系统下的伯克利socket编程，和windows下的有区别，一会儿说明)：

int select(int maxfdp,fd_set *readfds,fd_set *writefds,fd_set *errorfds,struct
timeval *timeout);

先说明两个结构体：

第一，struct fd_set可以理解为一个集合，这个集合中存放的是文件描述符(file descriptor)，即文件句柄，这可以是我们所说的普通意义的
文件，当然Unix下任何设备、管道、FIFO等都是文件形式，全部包括在内，所以毫无疑问一个socket就是一个文件，socket句柄就是一个文件描述符。fd
_set集合可以通过一些宏由人为来操作，比如清空集合FD_ZERO(fd_set *)，将一个给定的文件描述符加入集合之中FD_SET(int
,fd_set *)，将一个给定的文件描述符从集合中删除FD_CLR(int
,fd_set*)，检查集合中指定的文件描述符是否可以读写FD_ISSET(int ,fd_set* )。一会儿举例说明。

第二，struct timeval是一个大家常用的结构，用来代表时间值，有两个成员，一个是秒数，另一个是毫秒数。

具体解释select的参数：

int
maxfdp是一个整数值，是指集合中所有文件描述符的范围，即所有文件描述符的最大值加1，不能错！在Windows中这个参数的值无所谓，可以设置不正确。

fd_set *readfds是指向fd_set结构的指针，这个集合中应该包括文件描述符，我们是要监视这些文件描述符的读变化的，即我们关心是否可以从这些文件
中读取数据了，如果这个集合中有一个文件可读，select就会返回一个大于0的值，表示有文件可读，如果没有可读的文件，则根据timeout参数再判断是否超时，
若超出timeout的时间，select返回0，若发生错误返回负值。可以传入NULL值，表示不关心任何文件的读变化。

fd_set *writefds是指向fd_set结构的指针，这个集合中应该包括文件描述符，我们是要监视这些文件描述符的写变化的，即我们关心是否可以向这些文
件中写入数据了，如果这个集合中有一个文件可写，select就会返回一个大于0的值，表示有文件可写，如果没有可写的文件，则根据timeout参数再判断是否超时
，若超出timeout的时间，select返回0，若发生错误返回负值。可以传入NULL值，表示不关心任何文件的写变化。

fd_set *errorfds同上面两个参数的意图，用来监视文件错误异常。

struct timeval* timeout是select的超时时间，这个参数至关重要，它可以使select处于三种状态，第一，若将NULL以形参传入，即
不传入时间结构，就是将select置于阻塞状态，一定等到监视文件描述符集合中某个文件描述符发生变化为止；第二，若将时间值设为0秒0毫秒，就变成一个纯粹的非阻
塞函数，不管文件描述符是否有变化，都立刻返回继续执行，文件无变化返回0，有变化返回一个正值；第三，timeout的值大于0，这就是等待的超时时间，即sele
ct在timeout时间内阻塞，超时时间之内有事件到来就返回了，否则在超时后不管怎样一定返回，返回值同上述。

返回值：

负值：select错误 正值：某些文件可读写或出错 0：等待超时，没有可读写或错误的文件

在有了select后可以写出像样的网络程序来！

举个简单的例子，就是从网络上接受数据写入一个文件中。

例子：

![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif)main()
![](http://www.cnblogs.com/Images/OutliningIndicators/ExpandedBlockStart.gif){
![](http://www.cnblogs.com/Images/OutliningIndicators/InBlock.gif) int sock;
![](http://www.cnblogs.com/Images/OutliningIndicators/InBlock.gif) FILE *fp;
![](http://www.cnblogs.com/Images/OutliningIndicators/InBlock.gif) struct
fd_set fds; ![](http://www.cnblogs.com/Images/OutliningIndicators/ExpandedSubB
lockStart.gif) struct timeval timeout={3,0}; //select等待3秒，3秒轮询，要非阻塞就置0 ![](htt
p://www.cnblogs.com/Images/OutliningIndicators/ExpandedSubBlockStart.gif) char
buffer[256]={0}; //256字节的接收缓冲区
![](http://www.cnblogs.com/Images/OutliningIndicators/InBlock.gif) ![](http://
www.cnblogs.com/Images/OutliningIndicators/ExpandedSubBlockStart.gif) /*
假定已经建立UDP连接，具体过程不写，简单，当然TCP也同理，主机ip和port都已经给定，要写的文件已经打开
![](http://www.cnblogs.com/Images/OutliningIndicators/InBlock.gif)
sock=socket(![](http://www.cnblogs.com/Images/dot.gif));
![](http://www.cnblogs.com/Images/OutliningIndicators/InBlock.gif)
bind(![](http://www.cnblogs.com/Images/dot.gif));
![](http://www.cnblogs.com/Images/OutliningIndicators/ExpandedSubBlockEnd.gif)
fp=fopen(![](http://www.cnblogs.com/Images/dot.gif)); */
![](http://www.cnblogs.com/Images/OutliningIndicators/InBlock.gif)
![](http://www.cnblogs.com/Images/OutliningIndicators/InBlock.gif) while(1) ![
](http://www.cnblogs.com/Images/OutliningIndicators/ExpandedSubBlockStart.gif)
{ ![](http://www.cnblogs.com/Images/OutliningIndicators/InBlock.gif)
FD_ZERO(&fds); //每次循环都要清空集合，否则不能检测描述符变化
![](http://www.cnblogs.com/Images/OutliningIndicators/InBlock.gif)
FD_SET(sock,&fds); //添加描述符
![](http://www.cnblogs.com/Images/OutliningIndicators/InBlock.gif)
FD_SET(fp,&fds); //同上
![](http://www.cnblogs.com/Images/OutliningIndicators/InBlock.gif)
maxfdp=sock>fp?sock+1:fp+1; //描述符最大值加1
![](http://www.cnblogs.com/Images/OutliningIndicators/InBlock.gif)
switch(select(maxfdp,&fds,&fds,NULL,&timeout)) //select使用 ![](http://www.cnblo
gs.com/Images/OutliningIndicators/ExpandedSubBlockStart.gif) {
![](http://www.cnblogs.com/Images/OutliningIndicators/InBlock.gif) case -1:
![](http://www.cnblogs.com/Images/OutliningIndicators/InBlock.gif)
exit(-1);break; //select错误，退出程序
![](http://www.cnblogs.com/Images/OutliningIndicators/InBlock.gif) case 0:
![](http://www.cnblogs.com/Images/OutliningIndicators/InBlock.gif) break;
//再次轮询 ![](http://www.cnblogs.com/Images/OutliningIndicators/InBlock.gif)
default: ![](http://www.cnblogs.com/Images/OutliningIndicators/InBlock.gif)
if(FD_ISSET(sock,&fds)) //测试sock是否可读，即是否网络上有数据 ![](http://www.cnblogs.com/Imag
es/OutliningIndicators/ExpandedSubBlockStart.gif) {
![](http://www.cnblogs.com/Images/OutliningIndicators/InBlock.gif) recvfrom(so
ck,buffer,256,![](http://www.cnblogs.com/Images/dot.gif)..);//接受网络数据
![](http://www.cnblogs.com/Images/OutliningIndicators/InBlock.gif)
if(FD_ISSET(fp,&fds)) //测试文件是否可写
![](http://www.cnblogs.com/Images/OutliningIndicators/InBlock.gif)
fwrite(fp,buffer![](http://www.cnblogs.com/Images/dot.gif));//写入文件
![](http://www.cnblogs.com/Images/OutliningIndicators/InBlock.gif) buffer清空;
![](http://www.cnblogs.com/Images/OutliningIndicators/ExpandedSubBlockEnd.gif)
}// end if break;
![](http://www.cnblogs.com/Images/OutliningIndicators/ExpandedSubBlockEnd.gif)
}// end switch
![](http://www.cnblogs.com/Images/OutliningIndicators/ExpandedSubBlockEnd.gif)
}//end while ![](http://www.cnblogs.com/Images/OutliningIndicators/ExpandedBlo
ckEnd.gif)}//end main
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif)

