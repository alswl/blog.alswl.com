Title: python中目录与文件操作
Author: alswl
Date: 2009-09-16 00:00:00
Tags: 
Category: Python编程
Summary: 

本文来源：[python:目录与文件操作_浸在苏打水里的玩偶](http://hi.baidu.com/javalang/blog/item/6ce3293
f866596ee55e72334.html)

os和os.path模块

os.listdir(dirname)：列出dirname下的目录和文件

os.getcwd()：获得当前工作目录

os.curdir:返回但前目录（'.')

os.chdir(dirname):改变工作目录到dirname

os.path.isdir(name):判断name是不是一个目录，name不是目录就返回false

os.path.isfile(name):判断name是不是一个文件，不存在name也返回false

os.path.exists(name):判断是否存在文件或目录name

os.path.getsize(name):获得文件大小，如果name是目录返回0L

os.path.abspath(name):获得绝对路径

os.path.normpath(path):规范path字符串形式

os.path.split(name):分割文件名与目录（事实上，如果你完全使用目录，它也会将最后一个目录作为文件名而分离，同时它不会判断文件或目录是否存在
）

os.path.splitext():分离文件名与扩展名

os.path.join(path,name):连接目录与文件名或目录

os.path.basename(path):返回文件名

os.path.dirname(path):返回文件路径

    
    >>> import os
    >>> os.getcwd()
    'C:\Python25'

>>> os.chdir(r'C:temp')

>>> os.getcwd()

'C:\temp'

>>> os.listdir('.')

['temp.txt', 'test.py', 'testdir', 'tt']

>>> os.listdir(os.curdir)

['temp.txt', 'test.py', 'testdir', 'tt']

>>> os.path.getsize('test.py')

38L

>>> os.path.isdir('tt')

True

>>> os.path.getsize('tt')

0L

>>> os.path.abspath('tt')

'c:\temp\tt'

>>> os.path.abspath('test.py')

'c:\temp\test.py'

>>> os.path.abspath('.')

'c:\temp'

>>> os.path.split(r'.tt')

('.', 'tt')

>>> os.path.split(r'c:temptest.py')

('c:\temp', 'test.py')

>>> os.path.split(r'c:temptest.dpy')

('c:\temp', 'test.dpy'

>>> os.path.splitext(r'c:temptest.py')

('c:\temp\test', '.py')

>>> os.path.splitext(r'c:temptst.py')

('c:\temp\tst', '.py')

>>> os.path.basename(r'c:temptst.py')

'tst.py'

>>> os.path.dirname(r'c:temptst.py')

'c:\temp'

