Title: 在Python中调试代码
Author: alswl
Date: 2012-03-20 00:00:00
Tags: ipdb, Paster, pdb, Pylons
Category: Python编程
Summary: 

撰写程序时候，需要在调试上面花费不少时间，好的调试工具可以让这个过程如虎添翼， 靠打 log 调试会是一种很痛苦的过程，我总结一下 Pylons
开发的调试技巧。

吐槽：团队开发时候，每个成员需要学习、总结和分享各自的开发技巧， 这样才能自我提升并提高开发效率。这属于团队文化建设，开发是一种艺术创造过程，
绝对不是简单的复制和粘帖。

## 在 Python 中调试

### pdb

在代码中加入下列语句即可启用交互式调试。

    
    import pdb;pdb.set_trace()

在 pdb 中，可以使用 `h / l / b / n / s / c / j / a / p / ! / q` 这些命令所代表的含义可以通过
`h(elp)` 打印出来。

参考链接：

  * [用PDB库调试Python程序](http://magustest.com/blog/python/use-pdb-debug-python/comment-page-1)

### ipdb

比 pdb 更好用的是 ipdb，需要预先安装 IPython，通过 IPython 可以提供更强的交互功能。

安装 ipdb: `easy_install ipdb` ， 使用方法依然是 `import ipdb;ipdb.set_trace()` 。

ps: 根据我的测试，ipdb 0.61 不能和 ipython 0.91 正常工作， 会报 `ImportError: No module named
core.debugger` 错误，请尝试使用 ipython 0.10 或者更新版本。这个错误在 ipdb 官网有 issue 描述
（[link](https://github.com/gotcha/ipdb/issues/9)）。

### 使用 embed python shell

除了特定代码的调试，有时候我们还需要在开发一个功能之前进行尝试性代码撰写， 这点在 web 开发时候尤其有用。托 Python
动态语言特性的福，我们可以很方便的使用 Interactivate Shell 进行开发。

在项目的根目录建立一个 Python 脚本，比如 `shell.py` ，其中代码如下：

    
    #!/usr/bin/env python
    #coding=utf-8

# desc: 这个shell提供Python上下文环境，方便调试

# author: alswl

# date: 2012-03-20

def main():

# Do something for init here.

try:

from IPython.frontend.terminal.embed import InteractiveShellEmbed

ipshell = InteractiveShellEmbed()

ipshell()

except ImportError:

import code

pyshell = code.InteractiveConsole(locals=locals())

pyshell.interact()

if __name__ == '__main__':

main()

这段代码先尝试使用 IPython 作为交互 shell，如果没有安装就使用原生 Python 作为 交互 Shell。(强烈建议使用 IPython)。

请在 `main()` 方法开始时候做一些初始化动作，比如载入 webapp 的实例并初始化各路config，
这样就能实现即时代码测试功能，提高开发效率，不用一遍遍地跑流程。

参考链接

  * [http://qixinglu.com/archives/embed_python_shell_in_code](http://qixinglu.com/archives/embed_python_shell_in_code) （注意， 这篇文章是2011年的，其中引入 IPython 的 `InteractiveShellEmbed` 的方法已经过期，请参考上面的代码）

### GAE 中的 pdb

有一些特定系统，比如 GAE 和 nosetests，他们会重定向 `std:in` 和 `std:out` ， 造成 pdb
无法正确输入和输出，在使用的使用，需要用以下代码做个 hack。

    
    import sys
    import pdb
    for attr in ('stdin', 'stdout', 'stderr'):
        setattr(sys, attr, getattr(sys, '__%s__' % attr))
    pdb.set_trace()

## Pylons 调试

Paster 的 Shell 交互式调试更显犀利（官方所称杀手级功能）， 可以直接使用 `paster shell dev.ini`
命令启用交互界面，默认会先尝试载入 IPython，不存在就载入原生 Shell。

我当前使用的 Paster 版本为 1.7.5,无法正确识 IPython 0.11及以上版本， 请使用0.9.1或者0.10。

参考链接：

  * [How can I use "paster shell" to develop doctest tests?](http://wiki.pylonshq.com/pages/viewpage.action?pageId=9011323)
  * [stackoverflow 上关于 IPython 版本的问题](http://stackoverflow.com/questions/7389388/pylons-paster-shell-does-not-run-in-ipython)

