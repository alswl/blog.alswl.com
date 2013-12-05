Title: Working with Python subprocess[译文]
Author: alswl
Date: 2012-10-16 00:42
Tags: subprocess, bash, shell, 译文
Category: Python编程
Summary: 


8月底到魔都开始新工作，头一个月当然各种忙，都没时间来更新博客。

这篇文章是在写 [Btrace][btrace] 脚本时候查资料看到的，
看着不错就顺手翻译，没想到差点烂在草稿箱出不来啊出不来。
熬了一个月才磨出来，媳妇都快成婆了有木有。

原文链接：[Working with Python subprocess - Shells, Processes, Streams, Pipes, Redirects and More][source]

----

注意

> 关于「执行命令时候发生了什么」这个问题，可以在
> [http://en.wikipedia.org/wiki/Redirection\_(computing)][computing]
> 找到更多最新信息。这篇文章遵循 [GFDL][] 协议。

在我的上一篇日志中，我写到如何
[build a command line interface with sub-commands in Python][last-post]。
这次我来尝试如何通过 Python 的 `subprocess` 模块来和命令行指令进行交互。

我想达到的目标是：

* 查看当你键入命令时究竟发生了什么
* 如何确认一个命令是否存在并找出到底在哪
* 通过 Python 或 shell 执行命令
* 向一个运行中的进程读取 STDOUT 或写入 STDIN
* 检查进程的退出返回状态
* 理解 Bash 在命令中断中扮演的角色，并如何将它们发送给程序

<!-- more -->

## 执行程序时发生了什么

当你双击桌面上的终端程序图标时，就会打开一个载入 `shell` 的程序。
你键入的命令不会直接在内核执行，而是先和 shell 进行交互。

```
    Command      (eg. `ls -l')
       ↓
Terminal Program (eg. `gnome-terminal')
       ↓
     Shell       (eg Bash)
       ↓
     Kernel      (eg. Linux 2.6.24)
```

更多关于 shell 的信息：

* [http://en.wikipedia.org/wiki/Unix\_shell][unix-shell]

更多关于进程如何运行的信息：

* [http://pangea.stanford.edu/computerinfo/unix/shell/processes/processes.html][processes]

当你通过 Python 执行程序时候，你可以选择直接从内核执行或者通过 shell。
如果你选择直接执行，你就没办法和 bash 同样方式执行命令。

我们先看看怎么使用 shell 和那些好玩的特性功能，
然后再通过 `subprocess` 来实现同样的功能，

### 数据流

在 UNIX 和 Linux 下，有三个被称作 *流* 的 I/O 通道，它们通过文本终端
（比如用 gnome-terminal 运行 Bash）和其他应用程序（比如通过 Python 的
`subprocess` ）这类环境来连接程序。
这几个 I/O 通道分别称为 *标准输入*， *标准输出*，和 *标准错误输出* ,
它们的 *文件描述符* 分别为 0，1，2。

<table>
  <thead>
    <tr>
      <th> 句柄 </th> <th> 名称 </th> <th> 描述 </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td> 0 </td> <td> stdin </td> <td> 标准输入 </td>
    </tr>
    <tr>
      <td> 1 </td> <td> stdout </td> <td> 标准输出 </td>
    </tr>
    <tr>
      <td> 2 </td> <td> stderr </td> <td> 标准错误输出 </td>
    </tr>
  </tbody>
</table>

这里你能看到标准输入叫做 `stdin`，标准输出称作 `stdout`，标准错误输出叫做
`stderr` 。

流是这样工作的：从终端输出获取输入并通过标准输入发送到程序，
程序返回的正常输出从标准输出输出，错误则返回到环境上下文的标准错误输出。
维基百科有幅图将描述这个过程：

[![Stdstreams-notitle.svg][Stdstreams-notitle.svg]][Wiki:Stdstreams-notitle.svg]

如果你想将流从一个程序重定向到另一个地方，请看下文分解。

## 使用 Shell

### 重定向标准输入和输出到文件

你可以在 Bash 中使用 `>` 操作符将一个程序的标准输出重定向到一个文件
（在其他 Shell 也许略有语法差异）。这里有个范例：

``` bash
program1 > file1
```

`program1` 执行后的输出结果从标准输出流写入 `file1`，并将 `file1`
其中现有的内容所替换。如果你只是想追加内容，你可以使用 `>>` 操作符：

``` bash
program1 >> file1
```

`<` 操作符可以被用来从文件中读取数据并传输到程序的标准输入流：

```bash
program1 < file1
```

同样的，`program1` 会被执行，但是此时 `file1` 取代了键盘，
成为了标准输入的数据源。

你可以组合 shell 操作符以完成更复杂的操作。
下面这个范例中，`program1` 从 `file1` 获取数据并发送到标准输入。标准输出则从
`program1` 输出到 `file2`。

``` bash
program1 < file1 > file2
```

也许有时候你需要从一个程序获取输出并将其作为另一个程序的输入。
你可以通过一个临时文件来实现这个操作：

``` bash
program1 > tempfile1
program2 < tempfile1
rm tempfile1
```

这种方法有点累赘，因此 shell 提供了方便的机制，称为 *管道*

### 管道

管道允许一个程序的标准输出直接输入到另一个程序的标准输入流中，
而无须创建临时文件：

``` bash
program1 | program2
```

操作符 `|` 被称作 *管道* 符号，因此这种操作就被称为 *管道*。

这里有一幅来自维基百科的图片来描述管道：

[![Pipeline.svg][Pipeline.svg]][Wiki:Pipeline.svg]

这里有个使用 `find .`（遍历当前目录下的文件和目录）的例子，将输出定向到 `grep`
程序来查找特定文件：

``` bash
find . | grep "The file I'm after.txt"
```

第一个程序产生的数据是一行一行地导向第二个程序的，所以在第一个程序运行结束之前，
第二个程序就可以开始使用它们。

### 从文件重定向标准输入和输出

在重定向标准输出的同时，你也可以重定向其他流，
比如重定向标准错误输出到标准输出。我们已经讨论过在 Bash 中，
可以在文件描述符之前使用 `>`，`<` 和 `>>` 操作符来重定向数据流
（还记得之前讨论的数字 0，1，2 么）。如果把标准输出代表的数字 1 省略掉看，
会发现我们一直在使用标准输出。

下面这条命令执行 `program1` 并将所有标准 *错误* 数据输出到 `file1`。

``` bash
program1 2> file1
```

执行 `program1`，错误信息就被重定向到 `file` 了。

这里有个范例程序让你来测试，将它保存成 `redirect1.py`：

``` python
import sys
while 1:
    try:
        input = sys.stdin.readline()
        if input:
            sys.stdout.write('Echo to stdout: %s'%input)
            sys.stderr.write('Echo to stderr: %s'%input)
    except KeyboardError:
         sys.exit()
```

这个程序始终将接受到的输入数据并同时输出到 stdout 和 stderr 。

在 csh 衍生出来的 shell 中，语法则是在重定向符号之后加上 `&` 符号，
可以达到同样的效果。（译者注：即 `|&`）

另一个常用的特性是将一个输出流重定向到定一个。
最常见的用法是将标准错误输出重定向到标准输出，
这样就可以把错误信息和正确信息合并在一起，比如：

``` bash
find / -name .profile > results 2>&1
```

命令将会找出所有名叫 `.profile` 的文件。
如果没有重定向，它将输出命中信息到 stdout，错误信息到 stderr
（比如有些目录无权限访问）。如果标准输出定向到文件，错误信息则会显示在命令行上。
为了在结果文件中可以同时看到命中信息和错误信息，我们需要使用 `2>&1`
将标准错误输出（2）输出到标准输出（1）。（这次即使在 Bash 中也需要 `&` 符。）

虽然语法上可以将 `2>&1` 放到 `>` 前面，但这样不能正常工作。
事实上，当解析器读取 `2>&1` 时候，它还不知道标准输出将重定向到哪里，
所以标准错误输出就不会被合并。

如果使用管道合并输出流，那么合并符号 `2>&1` 需要在管道符号 `|` 之前。比如：

``` bash
find / -name .profile 2>&1 | less
```

Bash 中的合并输出简写形式是：

``` bash
command > file 2>&1
```

为：

``` bash
command &>file
```

或者：

``` bash
command >&file
```

但是最好别用简写形式，否则你会弄糊涂。我提倡宁愿麻烦但是要清晰。

`&>` 操作符同时重定向标准输出和标准错误输出。
它的作用和在 Bourne Shell 中的 `command > file 2>&1` 一样。

### 管道链

重定向可以和管道连接起来组成复杂的命令，比如：

``` bash
ls | grep '\.sh' | sort > shlist
```

列出当前目录下所有文件，然后过滤剩下仅包含 .sh 的内容，根据文字编码排序，
然后将最终结果输出到 shlist。这种类型的命令经常在 shell 脚本和批处理文件中使用。

### 多重输出重定向

标准命令 `tee` 可以重定向一个命令到多个地方。

``` bash
ls -lrt | tee xyz
```

这将文件列表同时输出到标准输出和文件 `xyz` 中。

### Here 文档

大部分 Shell，包括 Bash 都支持 *Here 文档*，它允许你使用 `<<` 
操作符和一些文本作为分隔符将文本块嵌入到命令之中。

在下面的范例中，文本块被传送给 `tr` 命令，同时使用 `END_TEXT` 作为 Here
文档分隔符来指明文本的开始和结束。

``` bash
$ tr a-z A-Z <<END_TEXT
> one two three
> uno dos tres
> END_TEXT
ONE TWO THREE
UNO DOS TRES
```

经过 `tr` 处理后，输出的结果是 `ONE TWO THREE` 和 `UNO DOS TRES`。

一种常用用法是用 Here 文档向文件添加文本。
默认情况下，文本中的变量是会被替换成真实值的。

``` bash
$ cat << EOF
> Working dir $PWD
> EOF
Working dir /home/user
```

通过在 Here 文档标签引上单引号或者双引号，就可以避免这种转义：

``` bash
$ cat << "EOF"
> Working dir $PWD
> EOF
Working dir $PWD
```

## 介绍 `subprocess`

刚才我们讨论过了一些命令行提供的功能，现在让我们体验一下 `subprocess` 模块。
你可以在命令行中运行下面这条简单的命令：

``` bash
$ echo "Hello world!"
Hello world!
```

让我们试着在 Python 中运行它。

以前我们需要使用一堆各异的标准库来实现进程管理。
从 Python 2.4 开始，所有功能都被精心地整理到 `subprocess` 这个模块，
其中的 `Popen` 类可以提供所有我们需要的。

注意

> 如果你对新的 `Popen` 如何替换旧模块，[subprocess-doc][subprocess-documentation]
> 有一个章节解释过去是如何作用以及当前是如何作用。

`Popen` 可以接受一下参数，详情可以在 [using-the-subprocess-module][http://docs.python.org/library/subprocess.html#using-the-subprocess-module]：


``` bash
subprocess.Popen(args, bufsize=0, executable=None, stdin=None,
    stdout=None, stderr=None, preexec_fn=None, close_fds=False,
    shell=False, cwd=None, env=None, universal_newlines=False,
    startupinfo=None, creationflags=0
)
```

## 使用 Shell

让我们以 Hello World! 这个例子开始。和之前类似，通过
Python shell 执行下列命令：

``` bash
>>> import subprocess
>>> subprocess.Popen('echo "Hello world!"', shell=True)
Hello world!
<subprocess.Popen object at 0x...>
```

如你所见，标准输出和同样打印出 `Hello world!` ，
区别在于命令行显示了一个我们创建的 `subprocess.Popen` 实例。

如果你将代码保存为 `process_test.py` ，然后在命令行执行，你会得到一样的结果：

``` bash
$ python process_test.py
Hello world!
```

看上去运行 OK。

你可能在琢磨我们到底使用了哪个 shell。Unix 的默认 shell 是 `/bin/sh` ，
而 Windows 下面则取决于 `COMSPEC` 这个环境变量。
如果你设置 `shell=True` ，则可以通过 `executable` 参数来自定义 shell。

``` bash
>>> subprocess.Popen('echo "Hello world!"', shell=True, executable="/bin/bash")
Hello world!
<subprocess.Popen object at 0x...>
```

和我们之前看到的一样，但是如果你使用特定的 shell ，
你也许会发现不同的地方。

让我们探索一下通过 Python 使用 shell 的其他特性：

变量解析：

``` bash
>>> subprocess.Popen('echo $PWD', shell=True)
/home/james/Desktop
<subprocess.Popen object at 0x...>
```

管道和重定向：

``` bash
subprocess.Popen('echo "Hello world!" | tr a-z A-Z 2> errors.txt', shell=True)
<subprocess.Popen object at 0x...>
>>> HELLO WORLD!
```

`errors.txt` 应该是空的，因为没有任何错误产生。
有趣的是在我电脑上，`Popen` 实例在 `HELLO WORLD!` 被打印到标准输出
*之前* 出现。
恩，管道和重定向都可以正常工作。

Here 文档：

``` bash
>>> subprocess.Popen("""
... cat << EOF > new.txt
... Hello World!
... EOF
... """, shell=True)
<subprocess.Popen object at 0xb7dbbe2c>
```

`new.txt` 文件正常生成，并且包含内容 `Hello World!` 。

如我们预料，在 shell 中正常运行的命令同样可以在 Python shell 中运行。

## 字符串和参数列表

现在可以轻松地在 Python 中执行命令行了，你也许会需要传递变量过去。
假设我们要用 `echo` 重写刚才那个函数：

``` python
def print_string(string):
	print string
```

你也许想当然这样写：

``` python
def print_string(string):
	subprocess.Popen('echo "%s"'%string, shell=True)
```

这种写法，当字符串是 `Hello World!` 时候没问题：

``` bash
>>> print_string('Hello world!')
Hello world!
```

但这样就有问题：

``` bash
>>> print_string('nasty " example')
/bin/sh: Syntax error: Unterminated quoted string
```

这个命令会被执行成 `echo "nasty" example"` ，唔，这里的转义有问题。

一种解决方式是在代码里面做好转义，但这样会很麻烦，
你需要处理所有可能出现的转义字符和空格等等。

Python 可以帮你处理好，条件是你不能直接操作 shell，
如何操作看下文。

## Shell 之外

现在让我们试试不操作 shell 来实现同样的效果：

``` bash
def print_string(string):
	subprocess.Popen(['echo', string], shell=False)

>>> print_string('Hello world!')
Hello world!
>>> print_string('nasty " example')
nasty " example
```

现在你可以看到它正常地处理了转义。

注意

> 实际上你也可以在 `shell=False` 那里直接使用一个单独的字符串作为参数，
> 但是它必须是命令程序本身，这种做法和在一个列表中定义一个 `args`
> 没什么区别。而如果当 `shell=False` 时候直接执行字符串命令，则会报错：

``` python
>>> subprocess.Popen('echo "Hello world!"', shell=False)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python2.5/subprocess.py", line 594, in __init__
	errread, errwrite)
  File "/usr/lib/python2.5/subprocess.py", line 1147, in _execute_child
	raise child_exception
OSError: [Errno 2] No such file or directory
```

如果我们还是坚持使用一个字符串，Python 会认为这个 *完整的字符串*
是一个可执行的程序名，而实际上没有一个叫做 `echo "Hello world!"`
的程序，所以报错了。正确的做法要用 list 分开传送参数。

### 检查 PATH 中的程序

这里有个方法可以找出程序真正的位置：

``` python
import os
def whereis(program):
	for path in os.environ.get('PATH', '').split(':'):
		if os.path.exists(os.path.join(path, program)) and \
		   not os.path.isdir(os.path.join(path, program)):
			return os.path.join(path, program)
	return None
```

让我们用它来找出 `echo` 程序在哪里：

``` python
>>> location = whereis('echo')
>>> if location is not None:
...     print location
/bin/echo
```

这个方法同样可以检查用户的 `PATH` 里面是否有 Python 需要的程序。

当然你也可以使用命令行中的程序 `whereis` 来找出程序的路径。

``` bash
$ whereis echo
echo: /bin/echo /usr/share/man/man1/echo.1.gz
```

注意

> 无论我们使用 `shell` 为 `True` 或者 `False` ，
> 我们都没有指定执行程序的全路径。
> 如果这个程序在上下文环境的 `PATH` 变量中，我们才可以执行。
> 当然如果你愿意，指定全路径也没问题。

你也可以坚持指定 `executable` 为想要执行的程序，
然后 `args` 就不设定程序。虽然没看到明确的文档，不过我电脑上面可以这么执行：

``` python
>>> subprocess.Popen(['1', '2', '3'], shell=False, executable='echo')
2 3
<subprocess.Popen object at 0xb776f56c>
```

不直接使用 shell 会导致不能直观地使用重定向、管道、here 文档、shell
参数或其他那些可以在命令行使用的技巧。接下来我们会看看怎么使用这些功能。

## 从标准输出和错误重定向

当你使用 `Popen` 执行程序时候，输出内容通常被发送到 stdout，
这也是为什么你能看到这些内容。

当你想尝试从某个程序读取标准输出信息时候，则需要在调用 `Popen` 之前设定
`stdout` 参数。要设定的值是 `subprocess.PIPE`：

`subprocess.PIPE`
> 可以为 `Popen` 指定标准输入、标准输出和标准错误输出的参数，
> 需要注意的是标准输出流需要打开可写。

这里有个范例：

``` python
>>> process = subprocess.Popen(['echo', 'Hello World!'], shell=False, stdout=subprocess.PIPE)
```

To read the output from the pipe you use the `communicate()` method:

为了从管道获取输出，你可以使用 `communicate()` 方法：

``` python
>>> print process.communicate()
('Hello World!\n', None)
```

`communicate()` 的返回值是一个 tuple，第一个值是标准输出的数据，
第二个输出是标准错误输出的内容。

这里有段脚本能让我们测试标准输出和标准错误输出的表现行为，
将它存为 `test1.py`：

``` python
import sys
sys.stdout.write('Message to stdout\n')
sys.stderr.write('Message to stderr\n')
```

执行它：

``` python
>>> process = subprocess.Popen(['python', 'test1.py'], shell=False, stdout=subprocess.PIPE)
Message to stderr
>>> print process.communicate()
('Message to stdout\n', None)
```

注意标准错误输出在被生成后就打印了，而标准输出则被管道传输了。
这是因为我们只设定了标准输出的管道，让我们同时也设定标准错误输出。

``` python
>>> process = subprocess.Popen(['python', 'test1.py'], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
>>> print process.communicate()
('Message to stdout\n', 'Message to stderr\n')
```

这次标准输出和标准错误输出都被 Python 获取到了。

现在所有的消息能被打印出来了，如果我们再次调用 `communicate()`，
则会得到一个错误信息：

``` python
>>> print process.communicate()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python2.5/subprocess.py", line 668, in communicate
	return self._communicate(input)
  File "/usr/lib/python2.5/subprocess.py", line 1207, in _communicate
	rlist, wlist, xlist = select.select(read_set, write_set, [])
ValueError: I/O operation on closed file
```

`communicate()` 方法读取标准输出和标准错误输出时候，遇到结束符（EOF）
就会结束。

### 重定向 stderr 到 stdout

如果你想将错误信息重定向到标准输出，只需要给 `stderr` 
参数指定一个特殊值： `stderr=subprocess.STDOUT` 即可。

## 写入标准输入

写数据入一个进程和之前所述比较类似。为了要写入数据，需要先打开一个管道到标准输入。
通过设定 `Popen` 参数 `stdin=subproces.PIPE` 可以实现。

为了测试，让我们另外写一个仅输出 `Received:` 和输入数据的程序。
它在退出之前会输出消息。调用这个 `test2.py`：

``` python
import sys
input = sys.stdin.read()
sys.stdout.write('Received: %s'%input)
```

为了发送消息到标准输入，把你想发送的信息作为 `communicate()` 的参数 `input` 。让我们跑起来：

``` python
>>> process = subprocess.Popen(['python', 'test2.py'], shell=False, stdin=subprocess.PIPE)
>>> print process.communicate('How are you?')
Received: How are you?(None, None)
```

注意 `test2.py` 发送的信息被打印到标准输出，随后的是 `(None, None)` ，
这是因为标准输出和标准错误输出没有设定输出管道。

你可以和之前那样指定 `stdout=subprocess.PIPE`
和 `stderr=subprocess.PIPE` 来设定输出管道。

### 类文件属性

`Popen` 拥有 `stdout` 和 `stderr` 属性，从而可以当作文件一样写出数据，同时 `stdin` 属性可以像文件一样读取数据。
你可以使用他们来替换 `communicate()`。下面我们将看如何用它们。

### 读写同一个进程

这里有个例子，将它保存为 `test3.py`：

``` python
import sys

while True:
	input = sys.stdin.readline()
	sys.stdout.write('Received: %s'%input)
	sys.stdout.flush()
```

这个程序也是简单的响应接受到的数据，让我们把它跑起来：

``` python
>>> import time
>>> process = subprocess.Popen(['python', 'test3.py'], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
>>> for i in range(5):
...     process.stdin.write('%d\n' % i)
...     output = process.stdout.readline()
...     print output
...     time.sleep(1)
...
Received: 0

Received: 1

Received: 2

Received: 3

Received: 4

>>>
```

每隔一秒钟会输出一行。

现在你应该掌握了所有需要通过 Python 来跟 Shell 交互需要的知识。

## 获取返回值， `poll()` 和 `wait()`

当一个程序退出时候，他会返回一个正整数来表明它的退出状态。
0 代表「成功地结束」，非零则表示「非正常结束」。
大部分系统要求返回值在 0-127 之间，其他都是未定义的结果。
一些系统会有事先定义好的错误对应关系，但一般不被拿出来用。
Unix 程序通常使用 2 作为命令语法错误，1 作为其他错误。

你可以通过 `Popen` 的 `.returncode` 属性获取程序返回值。这儿有个例子：

``` python
>>> process = subprocess.Popen(['echo', 'Hello world!'], shell=False)
>>> process.poll()
>>> print process.returncode
None
>>> process.poll()
0
>>> print process.returncode
0
```

这个 `returncode` 并不是一开始就设定好的，最初是默认值 `None`，
它会一直是 `None` 知道你调用 `subprocess` 的方法比如 `poll()` 和 `wait()`。
这些方法会设定 `returncode`。因此，如果你想知道返回值，那就调用 `poll()`
和 `wait()`。

`poll()` 和 `wait()` 方法区别很小：

 `Popen.poll()`
:	检查子进程是否结束。并设置和返回 `.returncode` 属性。
 `Popen.wait()`
:	等待子进程结束。并设置和返回 `.returncode` 属性。

## 便捷的方法

`subprocess` 模块还提供了很多方便的方法来使得执行 shell 命令更方便。
我没有全部试试。（译者：意思是让读者自己挖掘？）

## 理解 `sys.argv`

如果你想写一个 Python 脚本来接受命令行参数，
那么命令行的参数会被传送并成参数 `sys.argv`。
这里有个小范例，将它保存成 `command.py` 。

``` python
#!/usr/bin/env python

if __name__ == '__main__':
    import sys
    print "Executable: %s"%sys.argv[0]
    for arg in sys.argv[1:]:
        print "Arg: %s"%arg
```

`if __name__ == '__main__'` 这行确保代码在被执行是才运行，
而不是被引入时候运行。给这个文件执行权限：

``` bash
$ chmod 755 command.py
```

这里是一些运行时的范例：

``` bash
$ python command.py
Executable: command.py
$ python command.py arg1
Executable: command.py
Arg: arg1
$ python command.py arg1 arg2
Executable: command.py
Arg: arg1
Arg: arg2
```

注意无论 Python 脚本怎么执行， `sys.argv[0]` 始终是脚本的名称。
`sys.argv[1]` 和之后的参数是命令行接受的参数。
你可以通过使用参数 `-m` 来强制 Python 脚本作为模块导入使用。

``` bash
$ python -m command
Executable: /home/james/Desktop/command.py
$ python -m command arg1
Executable: /home/james/Desktop/command.py
Arg: arg1
$ python -m command arg1 arg2
Executable: /home/james/Desktop/command.py
Arg: arg1
Arg: arg2
```

如你所见，Python 将 `-m` 作为命令的一部分，因此 `sys.srgv[0] 包含了脚本的全路径。
现在我们来直接执行它：

``` bash
$ ./command.py
Executable: ./command.py
$ ./command.py arg1
Executable: ./command.py
Arg: arg1
$ ./command.py arg1 arg2
Executable: ./command.py
Arg: arg1
Arg: arg2
```

看吧，`sys.argv[0]` 包含 Python 脚本的名称， `sys.argv[1]`
以及他的兄弟们还是老样子，包含各类参数。

### 展开 Shell

有时候，我们会在 shell 中使用通配符来设定一组参数，比如，
我们在 Bash 中运行：

``` bash
$ ./command.py *.txt
```

你可能觉得输出应该是：

``` bash
Executable: ./command.py
Arg: *.txt
```

这不是你想要的结果。输出结果应该依赖当前文件夹中 `.txt` 文件的数目。执行效果如下：

``` bash
Executable: ./command.py
Arg: errors.txt
Arg: new.txt
Arg: output.txt
```

Bash 会将 `\*.txt` 自动展开成所有符合 `.txt` 的参数。所以接受到的参数会超过你预期。

你可以通过将参数用引号抱起来来关闭 Shell 解释特性，
但是只要你用过，就会意识到在大多数情况下面这是非常有用的功能。

``` bash
$ ./command.py "*.txt"
Executable: ./command.py
Arg: *.txt
```

更多关于 Bash 解释信息，可以看 [http://www.gnu.org/software/bash/manual/bashref.html#Filename-Expansion][bash-expansions]

## 拓展阅读

可以参考：

* [http://www.doughellmann.com/PyMOTW/subprocess/](http://www.doughellmann.com/PyMOTW/subprocess/) (and its O'Reilly copy here)
* [http://docs.python.org/library/subprocess.html](http://docs.python.org/library/subprocess.html)
* [http://webpython.codepoint.net/cgi_shell_command](http://webpython.codepoint.net/cgi_shell_command)
* [http://www.artima.com/weblogs/viewpost.jsp?thread=4829](http://www.artima.com/weblogs/viewpost.jsp?thread=4829) (About writing main() functions)

未来相关的文章：

* 进程间信号通信
* 后台执行程序

[btrace]: http://kenai.com/projects/btrace/pages/Home
[source]: http://jimmyg.org/blog/2009/working-with-python-subprocess.html
[computing]: http://en.wikipedia.org/wiki/Redirection_(computing)
[GFDL]: http://www.gnu.org/copyleft/fdl.html
[last-post]: http://jimmyg.org/blog/2009/python-command-line-interface-%28cli%29-with-sub-commands.html
[unix-shell]: http://en.wikipedia.org/wiki/Unix_shell
[processes]: http://pangea.stanford.edu/computerinfo/unix/shell/processes/processes.html
[Stdstreams-notitle.svg]: http://upload-log4d.qiniudn.com/2012/09/Stdstreams-notitle.svg.png
[Wiki:Stdstreams-notitle.svg]: http://en.wikipedia.org/wiki/File:Stdstreams-notitle.svg
[Pipeline.svg]: http://upload-log4d.qiniudn.com/2012/09/Pipeline.svg.png
[Wiki:Pipeline.svg]: http://en.wikipedia.org/wiki/File:Pipeline.svg
[subprocess-doc]: http://docs.python.org/library/subprocess.html#replacing-older-functions-with-the-subprocess-module
[using-the-subprocess-module]: http://docs.python.org/library/subprocess.html#using-the-subprocess-module
[bash-expansions]: http://www.gnu.org/software/bash/manual/bashref.html#Filename-Expansion