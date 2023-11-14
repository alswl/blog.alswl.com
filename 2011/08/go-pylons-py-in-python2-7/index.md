

当使用 Python2.7 +[ go-pylons.py](http://pylonshq.com/download/1.0/go-pylons.py)
创建 Pylons 运行环境的话，会报一下错误。

    
    [alswl@arch-vm xingtong]$ python go-pylons.py myb_env
    New python executable in myb_env/bin/python
    Traceback (most recent call last):
      File "/home/alswl/work/xingtong/myb_env/lib/python2.7/site.py", line 67, in <module>
        import os
      File "/home/alswl/work/xingtong/myb_env/lib/python2.7/os.py", line 398, in <module>
        import UserDict
      File "/home/alswl/work/xingtong/myb_env/lib/python2.7/UserDict.py", line 83, in <module>
        import _abcoll
      File "/home/alswl/work/xingtong/myb_env/lib/python2.7/_abcoll.py", line 11, in <module>
        from abc import ABCMeta, abstractmethod
      File "/home/alswl/work/xingtong/myb_env/lib/python2.7/abc.py", line 8, in <module>
        from _weakrefset import WeakSet
    ImportError: No module named _weakrefset
    ERROR: The executable myb_env/bin/python is not functioning
    ERROR: It thinks sys.prefix is '/home/alswl/work/xingtong' (should be '/home/alswl/work/xingtong/myb_env')
    ERROR: virtualenv is not compatible with this system or executable

STFW 之后，找到了引发错误的根源[virtualenv](https://github.com/pypa/virtualenv)，这个 bug
在[这里](https://github.com/pypa/virtualenv/issues/76)已经修复了。

    
    #!diff
    --- a/virtualenv.py        2010-09-14 21:48:58.078562930 +0200
    +++ b/virtualenv.py        2010-09-14 21:46:20.650769346 +0200
    @@ -51,6 +51,8 @@ REQUIRED_FILES = ['lib-dynload', 'config

if sys.version_info[:2] >= (2, 6):

REQUIRED_MODULES.extend(['warnings', 'linecache', '_abcoll', 'abc'])

+ if sys.version_info[:2] >= (2, 7):

+ REQUIRED_MODULES.extend(['_weakrefset'])

if sys.version_info[:2] <= (2, 3):

REQUIRED_MODULES.extend(['sets', '__future__'])

if is_pypy:

懒人可以点击[go-pylons.py](../../static/images/2011/08/go-pylons.py)下载。


