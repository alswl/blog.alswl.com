---
title: "Python读写剪贴板"
author: "alswl"
slug: "python-clipboard"
date: "2010-10-23T00:00:00+08:00"
tags: ["python", "pywin"]
categories: ["coding"]
---

最近在写一个CodeGenX代码生成器，说是生成器，其实是目前只完成一堆零散的脚本。这些脚本的调用方式一般是从某个txt中读取数据，再写到另外一个txt中。

由于某些数据变动频繁，导致我操作txt次数大增，我怒了，就找了一个脚本自动读写剪贴板。

    
```python
#coding=utf-8
'''
读写剪贴板
'''
import win32clipboard as w
import win32con

def getText():
  w.OpenClipboard()
  d = w.GetClipboardData(win32con.CF_TEXT)
  w.CloseClipboard()
  return d

def setText(aString):
  w.OpenClipboard()
  w.EmptyClipboard()
  w.SetClipboardData(win32con.CF_TEXT, aString)
  w.CloseClipboard()
```

别说有了这个脚本用起来还是蛮方便的，建议丢到Python的lib下面，然后可以方便调用。

如果双击 `.py` 文件调用可能产生无效的情况，测试发现在IDE环境下有效，如果想完成一键转换，就需要一个bat执行一下。

```shell
@echo off
python sql2.py
```

通过执行双击这个脚本，就可以完成读写剪贴板了（记得在系统Path路径加入python所在目录，否则又要报错）。

友情提示，这个脚本需要 `win32clipboard` 这个模块，这个模块装完 `pywin` 就可以加载了。

我使用的环境是Python2.6 + PyWin，
**因为我的Python2.7+pywin32-214.win32-py2.7会出现一个"Still can't get my
hands on win32ui"。** 托上篇文章的福，我安装PyWin时候选择"管理员身份安装"即可。

PS:恨死Python版本控制了，中午弄一个re.sub()，2.6/2.7相差一个flag参数，让我搞鼓了好一会。

