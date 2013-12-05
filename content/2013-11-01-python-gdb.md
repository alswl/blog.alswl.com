Title: 在 Python 中使用 GDB 来调试[译文]
Author: alswl
Date: 2013-11-01 01:11
Tags: GDB, 译文
Category: Python编程
Summary: 


大约一年前，我接触了 Java 中的 [Btrace](http://kenai.com/projects/btrace)
能够不停机查看线上 JVM 运行情况的特性让我艳羡不已。
另外还有强悍的 jStack 和 jConsole 来进行运行期侦测，JVM 的工业级强度果然不是盖的。

当时公司技术方面也遇到了一些瓶颈，一部分原因是 CPython 本身的 IO 模型问题，
另一方面也和早期代码写的极不工整脱不了关系。万般无奈之下，我们用
Jython 推翻重做了主要业务，效果立竿见影，但同时也把真实问题给规避掉了。

在这之后我们在 JVM 的领导下，走上了康庄大道。但我心中始终还有一个梗，
就是想对性能遇到瓶颈的 Python Process 进行线上侦测。
这篇文章就是开始的第一步。

PS:这篇文章理论上是可行的，但是在我机器（Ubuntu 12.04 / 系统自带 Python）
无法正常执行，会爆出 `unable to read python frame information`
的问题。解决方法我会在下篇文章中写出。这里只是单纯翻译一下原文。

原文可以移步 [https://wiki.python.org/moin/DebuggingWithGdb](https://wiki.python.org/moin/DebuggingWithGdb)。

<!--more-->

----

有一些类型的 bugs 很难使用 Python 直接进行 debug，比如

* 段错误（无法被捕捉的 Python 异常）
* 卡住的进程（这种情况下面没法使用 `pdb` 来进行跟踪）
* 控制之外的后台处理 daemon 进程

这些情况下，你可以使用尝试使用 `gdb`。

## 准备 ##

需要在系统安装 `gdb` 和 Python debug 扩展。
Python debug 扩展包含了一些 debug 命令，并且添加了一些 Python 特定的命令到 `gdb`。
在主流的 Linux 发行版中，你可以轻松的安装他们：

Fedora:

```
sudo yum install gdb python-debuginfo
```

Ubunt:

```
sudo apt-get install gdb python2.7-dbg
```

在一些老系统上面，也一样可以使用 `gdb`，具体看文章末尾。

## 使用 `GDB` ##

有两种可行的方法：

1. 一开始就使用 `gdb` 来启动应用
1. 连接到一个已经运行的 Python 进程

在 `gdb` 下面启动 Python 同样有两种方式：

交互式：

```
$ gdb python
...
(gdb) run <programname>.py <arguments>
```

自动：

```
$ gdb -ex r --args python <programname>.py <arguments>
```

这样的话，它会一直运行直到退出、段错误、或者人为的停止（使用 `Ctrl+C`）。

如果进程已经开始运行，你可以通过 PID 来接入它：

```
$ gdb python <pid of running process>
```

## 调试进程 ##

如果你的程序段错误了， `gdb` 会自动暂停程序，这样你可以切换到 `gdb`
命令行来检查状态。你也可以人为地使用 `Ctrl+C` 来暂停程序运行。

查看 [EasierPythonDebugging](https://fedoraproject.org/wiki/Features/EasierPythonDebugging)
获得 `gdb` 里面的 Python 命令列表。

## 查看 C 调用栈 ##

如果你在 debug 段错误，你最想做的可能就是查看 C 调用栈。

在 `gdb` 的命令行里面，只要运行一下命令：

```
(gdb) bt
#0  0x0000002a95b3b705 in raise () from /lib/libc.so.6
#1  0x0000002a95b3ce8e in abort () from /lib/libc.so.6
#2  0x00000000004c164f in posix_abort (self=0x0, noargs=0x0)
    at ../Modules/posixmodule.c:7158
#3  0x0000000000489fac in call_function (pp_stack=0x7fbffff110, oparg=0)
    at ../Python/ceval.c:3531
#4  0x0000000000485fc2 in PyEval_EvalFrame (f=0x66ccd8)
    at ../Python/ceval.c:2163
...
```

运气好的话，你可以直接看到问题出现在什么地方。如果它提供的信息不能直接帮你解决问题，
你可以尝试继续追踪调用栈。
调式的结果取决于 debug 信息的有效程度。

## 查看 Python 调用栈 ##

如果你安装了 Python 扩展，你可以使用

```
(gdb) py-bt
```

可以获取熟悉的 Python 源代码。


## 对挂住的进程开刀 ##

如果一个进程看上去挂住了，他可能在等待什么东西（比如锁、IO 等等）。
也有可能在拼命的跑循环。连接上这个进程，然后检查调用栈也许可以帮上忙。

如果进程在疯狂循环，你可以先让它运行一会，使用 `cont` 命令，
然后使用 `Ctrl+C` 来暂停，并且打印出调用栈。

如果一些线程卡住了，下面的命令可能会帮上忙：

```
(gdb) info threads
  Id   Target Id         Frame
  37   Thread 0xa29feb40 (LWP 17914) "NotificationThr" 0xb7fdd424 in __kernel_vsyscall ()
  36   Thread 0xa03fcb40 (LWP 17913) "python2.7" 0xb7fdd424 in __kernel_vsyscall ()
  35   Thread 0xa0bfdb40 (LWP 17911) "QProcessManager" 0xb7fdd424 in __kernel_vsyscall ()
  34   Thread 0xa13feb40 (LWP 17910) "python2.7" 0xb7fdd424 in __kernel_vsyscall ()
  33   Thread 0xa1bffb40 (LWP 17909) "python2.7" 0xb7fdd424 in __kernel_vsyscall ()
  31   Thread 0xa31ffb40 (LWP 17907) "QFileInfoGather" 0xb7fdd424 in __kernel_vsyscall ()
  30   Thread 0xa3fdfb40 (LWP 17906) "QInotifyFileSys" 0xb7fdd424 in __kernel_vsyscall ()
  29   Thread 0xa481cb40 (LWP 17905) "QFileInfoGather" 0xb7fdd424 in __kernel_vsyscall ()
  7    Thread 0xa508db40 (LWP 17883) "QThread" 0xb7fdd424 in __kernel_vsyscall ()
  6    Thread 0xa5cebb40 (LWP 17882) "python2.7" 0xb7fdd424 in __kernel_vsyscall ()
  5    Thread 0xa660cb40 (LWP 17881) "python2.7" 0xb7fdd424 in __kernel_vsyscall ()
  3    Thread 0xabdffb40 (LWP 17876) "gdbus" 0xb7fdd424 in __kernel_vsyscall ()
  2    Thread 0xac7b7b40 (LWP 17875) "dconf worker" 0xb7fdd424 in __kernel_vsyscall ()
* 1    Thread 0xb7d876c0 (LWP 17863) "python2.7" 0xb7fdd424 in __kernel_vsyscall ()
```

当前运行的线程被标记为 `*`，要查看 Python 代码运行到哪里，使用 `py-list` 查看：

```
(gdb) py-list
2025        # Open external files with our Mac app
2026        if sys.platform == "darwin" and 'Spyder.app' in __file__:
2027            main.connect(app, SIGNAL('open_external_file(QString)'),
2028                         lambda fname: main.open_external_file(fname))
2029
>2030        app.exec_()
2031        return main
2032
2033
2034    def __remove_temp_session():
2035        if osp.isfile(TEMP_SESSION_PATH):
```

查看所有进程的 Python 代码位置，可以使用：

```
(gdb) thread apply all py-list
...
 200
 201        def accept(self):
>202            sock, addr = self._sock.accept()
 203            return _socketobject(_sock=sock), addr
 204        accept.__doc__ = _realsocket.accept.__doc__
 205
 206        def dup(self):
 207            """dup() -> socket object

Thread 35 (Thread 0xa0bfdb40 (LWP 17911)):
Unable to locate python frame

Thread 34 (Thread 0xa13feb40 (LWP 17910)):
 197            for method in _delegate_methods:
 198                setattr(self, method, dummy)
 199        close.__doc__ = _realsocket.close.__doc__
 200
 201        def accept(self):
>202            sock, addr = self._sock.accept()
 203            return _socketobject(_sock=sock), addr
...
```

## 引用 ##

* [http://fedoraproject.org/wiki/Features/EasierPythonDebugging](http://fedoraproject.org/wiki/Features/EasierPythonDebugging)
* [https://code.google.com/p/spyderlib/wiki/HowToDebugDeadlock](https://code.google.com/p/spyderlib/wiki/HowToDebugDeadlock)

## 老系统上的 GDB ##

有时候你需要在老系统上面安装 `gdb`，这时候你可能需要下列信息：

### GDB Macros ###

一些随着 Python 发布的 GDB 脚本可以用来调试 Python 进程。
你可以把 Python 源码里面的 `Misc/gdbinit`  拷贝到 `~/.gdbinit`，
或者从 [Subversion](http://svn.python.org/view/python/branches/release27-maint/Misc/gdbinit?view=log)
来拷贝他们。请注意你的 Python，确保使用正确的代码版本，否则有些功能可能无法工作。

请注意有些新的 GDB 命令只有在 debug 需要的库存在才能正常工作。

这个脚本在 Ubuntu 上面的 gcc 4.5.2 工作时，会爆出错误
`No symbol "co" in current context.`，是因为 `call_function` 在
[PyEval_EvalFrameEx](https://wiki.python.org/moin/EvalFrameEx) 和
[PyEval_EvalCodeEx](https://wiki.python.org/moin/EvalCodeEx) 之间。
重新使用 `make "CFLAGS=-g -fno-inline -fno-strict-aliasing"`
编译 Python 可以解决这个问题。

### 使用 Python Stack Traces GDB 脚本 ##

在 gdb 命令行里，可以这样查看 Python stack trace:

```
(gdb) pystack
```

同样的，可以获取一列 stack frame 的 Python 变量：

```
(gdb) pystackv
```

更多 gdbinit 里面没定义的有用的脚本可以在这里找到：

[http://web.archive.org/web/20070915134837/http://www.mashebali.com/?Python_GDB_macros:The_Macros](http://web.archive.org/web/20070915134837/http://www.mashebali.com/?Python_GDB_macros:The_Macros)