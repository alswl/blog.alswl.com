

上个星期以来忙里偷闲一直在写一系列小型的代码生成器，完成一些从需求到结构化代码生成和验证作业。这个小东西是用Python写的，我简单分享一下中间所得。

## 一、配置文件

### 1、YAML格式

数据库连接信息和作业相关信息是存放在数据库中的，配置文件形式可以有很多种选择：XML / ini / txt，我这里选择YAML作为存放。

YAML使用起来相当方便，能够自动解析成对应语言中的变量，比如列表解析为列表，数字文字分别解析成对应的格式变量。

之所以选择YAML，是看中它对语言的亲和性和可读性，GAE的配置文件就是YAML格式。YAML的语法相当简单，用:来分隔key: value，用 -
来分隔列表，注意点是缩进需要用空格，关键符号和内容之间要加上一个空格。我的配置文件如下：

    
    taskId: PQMI06
    taskName: 测试建制作业
    author: alswl
    confirmId: 20101025xxx

headFiles:

- head1.txt  
- head2.txt  
- head3.txt  
bodyFiles:

- body1.txt  
- body2.txt  
- body3.txt

qbe: qbe.txt

qbeGrid: qbegrid.txt

server: 172.16.1.20

user: sa

dbpassword: 518518

databaseSys: ebChainSys30_0

databaseSyn: ebChainSyn30_0

YAML可以用VIM或者notepad++进行编辑，两者都对YAML提供语法高亮支持（博客的SyantaxHighLighter不支持~）。

相关链接：[YAML的官方网站](http://www.yaml.org/)（网站的分隔就是YAML格式，相当有趣）
[YAML简介](http://www.ibm.com/developerworks/cn/xml/x-cn-yamlintro/)（来自IBM）

2、PyYAML

Python有几种YAML的实现，我这里推荐使用PyYAML，比较流行的模块，毕竟我这里只需要简单的读写操作。

PyYAML通过官方宣称的神奇的yaml.load()方法载入YAML文件，可以将列表识别为list和dictionary，通过key可以直接读取对应的值。

我的Demo代码如下：

    
    #coding=utf-8
    '''
    全局配置文件
    alswl
    20101026
    '''
    import os
    import yaml

rootPath = os.path.normpath(os.path.dirname(__file__) + '\..')

configFile = open(rootPath + '''inconfig.yaml''')

configYaml = configFile.read()

configFile.close()

CONFIG = yaml.load(configYaml)

通过上面的方法，我就能获取CONFIG这个变量，然后设置为全局变量使用了。

上面代码中一个小技巧就是使用os.path.dirname(__file__)获取当前的路径的父路径，在通过normpath转换为绝对路径，这样可以使用配置
文件的相对路径，以方便文件的迁移。（使用sys.path[0]也能获取文件运行路径，两者略有小区别）

相关链接：[PyYAML的官网](http://pyyaml.org/) [PyYAML_3.09-2.6下载](http://pyyaml.org/dow
nload/pyyaml/PyYAML-3.09.win32-py2.6.exe)

## 二、数据库连接-pymssql

Python连接MSSQL有多种模块选择，我选用pymssql。pymssql可以在[这里](http://code.google.com/p/pymssq
l/)下载到。我使用的版本是1.9.908。

其他的一些数据库连接模块，可以参考这里：[Py4Database - Woodpecker Wiki for
CPUG](http://wiki.woodpecker.org.cn/moin/Py4Database)以及[DatabaseModules -
Woodpecker Wiki for CPUG](http://wiki.woodpecker.org.cn/moin/DatabaseModules)

很不幸的是，pymssql在IDLE下面会导致IDLE崩溃（经我测试，只要import
_mssql就会崩溃，这个Bug已经在pymssql报告了），所以当操作pymssql时候必须使用PythonWin或者Python
Shell。另外截止目前，pymssql还仅仅支持Python2.6。

下面的Code是简单的操作数据库，定义数据库连接，获取dataset，在for循环读取一遍，完成一个简单的检测动作

    
    conn =_mssql.connect(server=CONFIG['server'], user=CONFIG['user'], password=str(CONFIG['dbpassword']), database=CONFIG['databaseSys'])
    
    def validateEntityInFrmFields(self, webControls, conn, boid):
        if webControls[0].d_ != '':
            boid = boid + '_d' + webControls[0].d_.rjust(2, '0')
        sqlCmd = "SELECT FieldName FROM SYSFrmFields WHERE BOID='%s'" %boid
        conn.execute_query(sqlCmd)
        res = [r for r in conn]
        fs = [i[0] for i in res]
        l = [i.fieldName for i in webControls]
        for i in l[:]:
            if i.strip() == '':
                l.remove(i)
        isSuccess = True
        for i in l:
            if i not in fs:
                isSuccess = False
                print u'SYSFrmFields中不存在栏位%s' %i
        if isSuccess:
            print u'检测成功，恭喜你'
            print u'页面元件需要的Field全部存在于在SYSFrmFieldsn'
        else:
            print u'检测失败'

print u'检测完毕'

简单的pymssql就这么用，import _mssql就可以了，如果需要原生的支持DB-API方式编程，可以使用import mssql。

## 三、脚本运行完之后继续操作

脚本不可避免的需要分包，分模块，然后在里面撰写代码，但有时候我们需要中途使用一些数据完成特定即时的操作。使用IDE的Debug暂停当然可以，但这不是最佳的解
决办法。

下面是我自己摸索出来的方法，也许不是最佳办法，但是可以用，可以在脚本执行完之后继续操作里面定义的变量，以完成更多动作。

用IDE打开Script，然后在里面键入类似代码。

    
    import codegenx;from codegenx import WEBCONTROLS;codegenx.main()
    qbe = WEBCONTROLS['qbe'];

Python中可以通过加入分号来让多条语句放在同一行。经过上面代码的执行，我就可以获取WEBCONTROLS这个codegenx模块中的对象。如果担心cod
egenx中的WEBCONTROLS和Shell中的不一致，可以用id()来看一下内存标示，经我检测发现是一致的。


