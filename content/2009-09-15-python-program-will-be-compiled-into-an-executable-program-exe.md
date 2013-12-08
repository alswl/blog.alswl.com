Title: 将Python程序编译为exe可执行程序
Author: alswl
Slug: python-program-will-be-compiled-into-an-executable-program-exe
Date: 2009-09-15 00:00:00
Tags: Lib
Category: Python编程

Python很强大，这个py2exe程序能够把.py文件编译为.exe可执行文件，真是如虎添翼啊。

我注意到这个细节：这篇文章发表于 2005-6-5 23:34作者wolfg太犀利了。

原文出处：[py2exe初接触（一） - Python -
ChinaUnix.net](http://bbs3.chinaunix.net/thread-556861-1-1.html)

## py2exe是什么？

py2exe是一种python发布工具，可以把python脚本转换成windows下的可执行程序，不需要安装python便可运行。

py2exe现在可以用来创建使用了wxPython, Tkinter, Pmw, PyGTK, pygame, win32com client and
server 等模块的程序。

详细介绍可以看它的官方网站 http://starship.python.net/crew/theller/py2exe/

### 1. 下载安装py2exe

py2exe目前的版本是0.5.4，根据你安装的python的版本选择下载的文件

[py2exe-0.5.4.win32-py2.3.exe](http://prdownloads.sourceforge.net/py2exe/py2ex
e-0.5.4.win32-py2.3.exe?download) (现在是0.6.9-alswl)

或

[py2exe-0.5.4.win32-py2.4.exe](http://prdownloads.sourceforge.net/py2exe/py2ex
e-0.5.4.win32-py2.4.exe?download)

安装后的文件应该在你的python安装目录下的Libsite-packagespy2exe

### 2.  使用py2exe

我们先准备一个简单的python程序hello.py

    
    # hello.py
    def main():
        print "Hello, World!"
    if __name__ == '__main__':
         main()

然后为使用py2exe写一个脚本setup.py

    
    # setup.py
    from distutils.core import setup
    import py2exe
    setup(console=["hello.py"])

运行setup.py，记得要传一个参数给它

    
    python setup.py py2exe

应该看到一些输出信息

    
    running py2exe
    creating E:ProjectsWorkSpacePythonbuild
    creating E:ProjectsWorkSpacePythonbuildbdist.win32
    creating E:ProjectsWorkSpacePythonbuildbdist.win32winexe
    creating E:ProjectsWorkSpacePythonbuildbdist.win32winexecollect
    creating E:ProjectsWorkSpacePythonbuildbdist.win32winexetemp
    creating E:ProjectsWorkSpacePythondist
    *** searching for required modules ***
    *** parsing results ***
    creating python loader for extension '_sre'
    *** finding dlls needed ***
    *** create binaries ***
    *** byte compile python files ***
    byte-compiling C:Python23libcopy_reg.py to copy_reg.pyc
    byte-compiling C:Python23libsre_compile.py to sre_compile.pyc
    byte-compiling E:ProjectsWorkSpacePythonbuildbdist.win32winexetemp_sre.py to _sre.pyc
    byte-compiling C:Python23libmacpath.py to macpath.pyc
    byte-compiling C:Python23libpopen2.py to popen2.pyc
    byte-compiling C:Python23libatexit.py to atexit.pyc
    byte-compiling C:Python23libos2emxpath.py to os2emxpath.pyc
    byte-compiling C:Python23libsre_constants.py to sre_constants.pyc
    byte-compiling C:Python23libre.py to re.pyc
    byte-compiling C:Python23libntpath.py to ntpath.pyc
    byte-compiling C:Python23libstat.py to stat.pyc
    byte-compiling C:Python23libstring.py to string.pyc
    byte-compiling C:Python23libwarnings.py to warnings.pyc
    byte-compiling C:Python23libUserDict.py to UserDict.pyc
    byte-compiling C:Python23librepr.py to repr.pyc
    byte-compiling C:Python23libcopy.py to copy.pyc
    byte-compiling C:Python23libtypes.py to types.pyc
    byte-compiling C:Python23libposixpath.py to posixpath.pyc
    byte-compiling C:Python23libsre.py to sre.pyc
    byte-compiling C:Python23liblinecache.py to linecache.pyc
    byte-compiling C:Python23libsre_parse.py to sre_parse.pyc
    byte-compiling C:Python23libos.py to os.pyc
    *** copy extensions ***
    copying C:Python23DLLs_sre.pyd ->; E:ProjectsWorkSpacePythondist
    *** copy dlls ***

py2exe会在当前目录下生成两个目录 build和dist

build里是一些py2exe运行时产生的中间文件，dist里有最终的可执行文件

library.zip

  
w9xpopen.exe

  
python23.dll

  
hello.exe

现在可以运行hello.exe了

    
    E:ProjectsWorkSpacePythondist>;hello
    Hello, World!

不过记得如果要发布到别的机器上时，library.zip、
w9xpopen.exe、python23.dll这几个文件是必须要和hello.exe在一起的。

好了，这次先到这里，下次我们做一个wxPython的例子

最后，大家试试运行

    
    python setup.py py2exe --help

看看py2exe都有哪些参数

