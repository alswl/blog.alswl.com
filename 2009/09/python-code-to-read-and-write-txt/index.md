

09_09_09在Windows Live Writer下修正

一直有学Python或者Perl的想法，不过没有规划到日程来，最近打算辞职专心考驾照，正好每天都有点时间来学Python。

关于Python和Perl，我并没有什么谁优谁劣的看法，只是感觉Python可能资料会多一点，而且Google App
Enginee支持Python,所以选择了Python。

OK，这几天写的两段小代码，来自《[Python核心编程（第二版）](http://www.china-pub.com/39969&ref=xiangguan)》（原书中写这段有错误，我这儿也算勘误了）

makeTextFile.py

```
'makeTextFile.py -- create text file'

import os ls = os.linesep

#get filename

while True:

fname = raw_input('> a txt file path')

if os.path.exists(fname):

print "Error: '%s' already exists" % fname

else:

break

all = [] print "nEnter lines {'.' by itself to quit).n"

#loop until user terminates input

while True:

entry = raw_input('> ')

if entry == '.':

break;

else:

all.append(entry)

fobj = open(fname, 'w')

fobj.writelines(['%s%s' %(x, ls) for x in all])

fobj.close() print 'Done' raw_input('Press Enter to close') readTextFile.py


    'readTextFile.py -- read and display text file'
    fname = raw_input('Enter filename:')
    print

#attend to open file for reading

try:

fobj = open(fname, 'r')

except IOError, e:

print '*** file open error:', e else:

for eachLine in fobj:

print eachLine,

fobj.close raw_input('Press Enter to close')
```

原书中的输入在while那里出现了错误，压根没有raw_input这行代码，看了china-
pub评论，这本书的确存在一些错误，不过在我看来，瑕不掩瑜拉，还是一本入门的好书。

另外，提醒一下Python初学者：无论是PythonWin还是IDLE (Python
GUI)，初始出现的画面都是command模式，用来交互的，代码是要写到Python
script里面的，相当于新建一个空白txt文档，而不是在">>>"下面。


