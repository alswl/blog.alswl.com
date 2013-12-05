Title: 铁血联盟EdtTxt转换器v0.9
Author: alswl
Date: 2009-11-01 00:00:00
Tags: 
Category: Python编程
Summary: 

上个月时候，[zwwooooo](http://zww.me/)同鞋联系我让帮写一个铁血联盟中需要用到的Edt<->Txt转换器，我前前后后大约三个星期完成
到v0.9，能完成基本的功能（但似乎存在一些未知Bug，-_-#）。由于我之后很长一段时间得找工作，所以不能继续维护这个小工具，现在把他的代码开放，如果有高
人能看到这个小工具，有兴趣的话可以继续维护下去，(zwwooooo，真的很不好意思……)。
一些关于程序说明，zwwooooo原文，更详细可以联系zwwooooo本人：

> edt（后缀） 是游戏对话文件，游戏里有很多种，但都是有规律的，我把一些规律和流程说一下

一、从 edt 提取出对话部分文本，然后转换并输出为 ansi 码文本，用附件的 000.edt 为例说明

1. 把 000.edt 文件用16进制方式打开，对话从"0"处开始，结束标志是2个16进制字节：00 00

2. 000.edt 里面每个/每段对话/说明相隔 640 个字节，即"0"开始为第一段，直到16进制双字节出现"00 00"结束，然后第2段话在第 640
字节处开始，也是以"00 00"表示结束，后面的以此类推。
（因为有几种edt文件，每种edt文件的对话间隔不同，所以这个"间隔"最好设个参数，可以在转换前自定义输入。）

3. 然后把提取出的16进制数全部按UTF-16的双字节（或者转为对应的十进制） -1 处理，如：0~1字节处的双字节值为02 1E（1E为高位，02为地位
----哈哈，这个我好想说多余了），那么进行 -1 处理后得到：01 1E。然后把所有 -1 处理好的数据转换为 ansi 码（注：不转也可以
，直接用UTF-16无bom格式做文本文件----不过这样不太方便编辑），那么文本就出来了

每段话提取并转换后按 000.txt 一样显示，方便修改

4. 对话中的一些特殊字符说明（都是双字节16进制），有些提取转换时需要特殊处理的（不能直接 -1 处理）：
&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;

1）就是刚才说的"00 00"，它是每个对话的结束标志。
&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;

2）"20 00"：UTF-16编码'空格'的编码，这个是保持不变的，不用 -1 处理。
&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;

3）"B3 00" 和 "B4 00"：这两个是游戏专用的特殊控制符，用来控制文本高亮和居中，这个也要 -1 处理，-1 处理后为：B2 00 和 B3
00，但因为ansi码里面没有这个字符，所以要用ansi码里面的2个不常用的字符表示，例如"㈡" "㈢"。

这样就能修改对话了/提取出的英文翻译成中文。

二、把 txt 转换回 edt（直接修改原 edt 文件或者新建一个edt文件，对话部分以外部分用"00 00"填充），当然最好两个方式都行

在v0.9中，我已经可以在程序中对参数进行配置，对系统的blockSize和标识符进行修改。一个已知缺陷是在Edt->Txt的处理行数时候可能出现问题。

程序是[用Python写的](http://log4d.com/2009/10/python-django-mtv-framework-and-php-
mvc-framework)，不要觉得很难，我也是在用Python完成Hello
World之后第三天开始写这个程序，只要有C/Java/C#这些语言一些基础，就可以理解这些程序了。

    
    # coding=utf-8
    import struct
    import os
    import ConfigParser

configParser=ConfigParser.ConfigParser()

CONFIGNAME = 'config.cfg'

blockSize = 640 #size per block 640/480

isDebug = False #isDebug mode True/False

sysEnd = 'x00x00' #end of a sentence, e.g. a space x00x00

startPosition = 00 #start posion

PASS_SYMBOL = 'x20x00' #the list of word not decode

SPECIAL_1 = 'xB3x00' #the word of B300

SPECIAL_2 = 'xB4x00' #the word of B400

sysEndList = {'00': 'x00', '01': 'x01', '02': 'x02', '03': 'x03', '04': 'x04',
'05': 'x05', '06': 'x06', '07': 'x07', '08': 'x08', '09': 'x09', '0a': 'x0a',
'0b': 'x0b', '0c': 'x0c', '0d': 'x0d', '0e': 'x0e', '0f': 'x0f', '10': 'x10',
'11': 'x11', '12': 'x12', '13': 'x13', '14': 'x14', '15': 'x15', '16': 'x16',
'17': 'x17', '18': 'x18', '19': 'x19', '1a': 'x1a', '1b': 'x1b', '1c': 'x1c',
'1d': 'x1d', '1e': 'x1e', '1f': 'x1f', '20': 'x20', '21': 'x21', '22': 'x22',
'23': 'x23', '24': 'x24', '25': 'x25', '26': 'x26', '27': 'x27', '28': 'x28',
'29': 'x29', '2a': 'x2a', '2b': 'x2b', '2c': 'x2c', '2d': 'x2d', '2e': 'x2e',
'2f': 'x2f', '30': 'x30', '31': 'x31', '32': 'x32', '33': 'x33', '34': 'x34',
'35': 'x35', '36': 'x36', '37': 'x37', '38': 'x38', '39': 'x39', '3a': 'x3a',
'3b': 'x3b', '3c': 'x3c', '3d': 'x3d', '3e': 'x3e', '3f': 'x3f', '40': 'x40',
'41': 'x41', '42': 'x42', '43': 'x43', '44': 'x44', '45': 'x45', '46': 'x46',
'47': 'x47', '48': 'x48', '49': 'x49', '4a': 'x4a', '4b': 'x4b', '4c': 'x4c',
'4d': 'x4d', '4e': 'x4e', '4f': 'x4f', '50': 'x50', '51': 'x51', '52': 'x52',
'53': 'x53', '54': 'x54', '55': 'x55', '56': 'x56', '57': 'x57', '58': 'x58',
'59': 'x59', '5a': 'x5a', '5b': 'x5b', '5c': 'x5c', '5d': 'x5d', '5e': 'x5e',
'5f': 'x5f', '60': 'x60', '61': 'x61', '62': 'x62', '63': 'x63', '64': 'x64',
'65': 'x65', '66': 'x66', '67': 'x67', '68': 'x68', '69': 'x69', '6a': 'x6a',
'6b': 'x6b', '6c': 'x6c', '6d': 'x6d', '6e': 'x6e', '6f': 'x6f', '70': 'x70',
'71': 'x71', '72': 'x72', '73': 'x73', '74': 'x74', '75': 'x75', '76': 'x76',
'77': 'x77', '78': 'x78', '79': 'x79', '7a': 'x7a', '7b': 'x7b', '7c': 'x7c',
'7d': 'x7d', '7e': 'x7e', '7f': 'x7f', '80': 'x80', '81': 'x81', '82': 'x82',
'83': 'x83', '84': 'x84', '85': 'x85', '86': 'x86', '87': 'x87', '88': 'x88',
'89': 'x89', '8a': 'x8a', '8b': 'x8b', '8c': 'x8c', '8d': 'x8d', '8e': 'x8e',
'8f': 'x8f', '90': 'x90', '91': 'x91', '92': 'x92', '93': 'x93', '94': 'x94',
'95': 'x95', '96': 'x96', '97': 'x97', '98': 'x98', '99': 'x99', '9a': 'x9a',
'9b': 'x9b', '9c': 'x9c', '9d': 'x9d', '9e': 'x9e', '9f': 'x9f', 'a0': 'xa0',
'a1': 'xa1', 'a2': 'xa2', 'a3': 'xa3', 'a4': 'xa4', 'a5': 'xa5', 'a6': 'xa6',
'a7': 'xa7', 'a8': 'xa8', 'a9': 'xa9', 'aa': 'xaa', 'ab': 'xab', 'ac': 'xac',
'ad': 'xad', 'ae': 'xae', 'af': 'xaf', 'b0': 'xb0', 'b1': 'xb1', 'b2': 'xb2',
'b3': 'xb3', 'b4': 'xb4', 'b5': 'xb5', 'b6': 'xb6', 'b7': 'xb7', 'b8': 'xb8',
'b9': 'xb9', 'ba': 'xba', 'bb': 'xbb', 'bc': 'xbc', 'bd': 'xbd', 'be': 'xbe',
'bf': 'xbf', 'c0': 'xc0', 'c1': 'xc1', 'c2': 'xc2', 'c3': 'xc3', 'c4': 'xc4',
'c5': 'xc5', 'c6': 'xc6', 'c7': 'xc7', 'c8': 'xc8', 'c9': 'xc9', 'ca': 'xca',
'cb': 'xcb', 'cc': 'xcc', 'cd': 'xcd', 'ce': 'xce', 'cf': 'xcf', 'd0': 'xd0',
'd1': 'xd1', 'd2': 'xd2', 'd3': 'xd3', 'd4': 'xd4', 'd5': 'xd5', 'd6': 'xd6',
'd7': 'xd7', 'd8': 'xd8', 'd9': 'xd9', 'da': 'xda', 'db': 'xdb', 'dc': 'xdc',
'dd': 'xdd', 'de': 'xde', 'df': 'xdf', 'e0': 'xe0', 'e1': 'xe1', 'e2': 'xe2',
'e3': 'xe3', 'e4': 'xe4', 'e5': 'xe5', 'e6': 'xe6', 'e7': 'xe7', 'e8': 'xe8',
'e9': 'xe9', 'ea': 'xea', 'eb': 'xeb', 'ec': 'xec', 'ed': 'xed', 'ee': 'xee',
'ef': 'xef', 'f0': 'xf0', 'f1': 'xf1', 'f2': 'xf2', 'f3': 'xf3', 'f4': 'xf4',
'f5': 'xf5', 'f6': 'xf6', 'f7': 'xf7', 'f8': 'xf8', 'f9': 'xf9', 'fa': 'xfa',
'fb': 'xfb', 'fc': 'xfc', 'fd': 'xfd', 'fe': 'xfe', 'ff': 'xff', }

def welcome():

print u'*******************************************************************'

print u'*************************** ***************************'

print u'***************************EdtTxtConvert***************************'

print u'*************************** ***************************'

print u'*******************************************************************'

print u'Any problem can connect me with my web site.'

print u' *powered by alswl* '

print u' *http://dddspace.cn*'

print u' *09-10-01 v0.9* '

def getFiles(type):

'get the files of path'

global dirPath

dirPath = raw_input(u'Input the files path:')

while not os.path.isdir(dirPath):

print u'%s is not a path' %(dirPath)

dirPath = raw_input(u'Input the files path:')

#os.chdir(dirPath)

files = os.listdir(dirPath)

fileList = list()

for file in files:

if os.path.splitext(file)[1].lower() == type:

fileList.append(file)

return fileList

def myInit():

'init the argu'

try:

global blockSize, isDebug, sysEnd, startPosition

configParser.read(CONFIGNAME)

blockSize = configParser.getint('edt_encode_config', 'block_size')

isDebug = configParser.getboolean('edt_encode_config', 'debug')

sysEnd = configParser.get('edt_encode_config', 'sys_end')

startPosition = configParser.getint('edt_encode_config', 'start_position')

viewConfig()

except Exception, e:

print u'configure file %s error！Exiting！' %CONFIGNAME

raw_input(u'Press Enter to exit')

sys.exit()

def viewConfig():

print u'Current configure:'

print u'Block size:%s' %blockSize

print u'Start Position:%s' %startPosition

print u'Debug mode:%s' %isDebug

print u'End Symbol:%s' %toHex(sysEnd)

def setConfig():

global blockSize, isDebug, sysEnd, startPosition

configParser.read(CONFIGNAME)

try:

blockSize = int(raw_input('set block size:'))

startPosition = int(raw_input('set start position:'))

isDebug = bool(raw_input('set is debug mode(empty is False):'))

sysEndInput = raw_input('set symbol of end(eg.0000)')

sysEnd = sysEndList[sysEndInput[:2]] + sysEndList[sysEndInput[2:]]

configParser.set('edt_encode_config', 'block_size', blockSize)

configParser.set('edt_encode_config', 'debug', str(isDebug))

configParser.set('edt_encode_config', 'sys_end', sysEnd)

configParser.set('edt_encode_config', 'start_position', startPosition)

with open(CONFIGNAME, 'wb') as configFile:

configParser.write(configFile)

except Exception, e:

print 'Error set'

raw_input('Press Enter to continue')

def toHex(s):

'format string to hex'

lst = []

for ch in s:

hv = hex(ord(ch)).replace('0x', '')

if len(hv) == 1:

hv = '0'+hv

lst.append(hv)

return reduce(lambda x,y:x+y, lst)

def getBlock(block640):

'get the useful string from block of 640 bytes'

for i in range(0, len(block640), 2):

if block640[i : i+2] == sysEnd:

return block640[:i]

def decode(text):

'-1 operate'

list = ''

for i in range(0, len(text), 2):

try:

rawStr = text[i: i+2]

if rawStr == PASS_SYMBOL :

list += rawStr

elif rawStr == SPECIAL_1:

list += 'x21x32'

elif rawStr == SPECIAL_2:

list += 'x22x32'

else:

a, b = struct.unpack('BB', rawStr)

a -= 1

list += struct.pack('BB', a, b)

except Exception, e:

tt = 0

return list

def encode(text):

'+1 operate'

list = ''

for char in text:

try:

if char == 'x21x32':

list += SPECIAL_1

elif char == 'x22x32':

list += SPECIAL_2

else:

a, b = struct.unpack('BB', char.encode('utf-16')[2:])

a += 1

list += struct.pack('BB', a, b)

except Exception, e:

tt = 0

list += 'x00x00'

return list

def read(file):

'read the block of file(use blockSize)'

return file.read(blockSize)

def edtProcess(edtFile):

'edt->txt process'

fedt = open(dirPath + '\' + edtFile, 'rb')

ftxt = open(dirPath + '\' + edtFile[0:-3] + 'txt', 'w')

global i

i = 0

try:

fedt.seek(startPosition)

while True:

block640 = read(fedt)

if not block640:

break

if i == 640 and isDebug == True:

nonono = 0

block = getBlock(block640)

blockStr = decode(block)

if blockStr != '':

lineNum = u'%d:n' %(i)

lineStr = blockStr.decode('utf-16') + 'nn'

if isDebug:

print lineNum, 'line number:%s' %(hex(i/16))

print lineStr,

ftxt.write(lineNum.encode('gbk'))

ftxt.write(lineStr.encode('gbk'))

i += blockSize

print u'%s -> %s Convert successful' %(fedt.name, ftxt.name)

except Exception, e:

print u'%s -> %s Convert Errorn%s' %(fedt.name, ftxt.name, e)

finally:

fedt.close()

ftxt.close()

def txtProcess(txtFile):

'txt->edt process'

ftxt = open(dirPath + '\' + txtFile, 'r')

fedt = open(dirPath + '\' + txtFile[0:-3] + 'edt', 'wb')

global i

i = 0

try:

fedt.seek(startPosition)

i = 0

blockStr = ''

for eachLine in ftxt:

if eachLine != 'n' and i % 3 != 0:

blockStr += eachLine

if (i+2) % 3 == 0:

if isDebug:

print blockStr.decode('gbk'),

block = encode(blockStr[:-1].decode('gbk'))

fedt.write(block)

fedt.seek(640 - len(block), os.SEEK_CUR)

blockStr = ''

i += 1

print u'%s -> %s Convert successful' %(ftxt.name, fedt.name)

except Exception, e:

print u'%s -> %s Convert Errorn%s' %(ftxt.name, fedt.name, e)

finally:

ftxt.close()

fedt.close()

if __name__ == '__main__':

welcome()

myInit()

while True:

print 'n********Menu********'

print '1.edt->txtn2.txt->edtn3.view confign4.set confign0.exit'

mode = raw_input(u'Please choose:')

if mode == '1':

fileList = getFiles('.edt')

if fileList != None:

print u'fiels ready to convert:%sn' %fileList

raw_input(u'Press Enter to convert')

for edtFile in fileList:

edtProcess(edtFile)

else:

print 'There is no edt files!'

raw_input('Press Enter to continue')

elif mode == '2':

fileList = getFiles('.txt')

if fileList != None:

print u'fiels ready to convert:%sn' %fileList

raw_input(u'Press Enter to convert')

for txtFile in fileList:

txtProcess(txtFile)

else:

print 'There is no txt files!'

raw_input('Press Enter to continue')

elif mode == '3':

print ''

viewConfig()

raw_input('Press Enter to continue')

elif mode == '4':

print ''

setConfig()

raw_input('Press Enter to continue')

elif mode == '0':

break

else:

print 'Error: Input error!!n'

raw_input('Press Enter to continue')

点击这里[下载源代码](http://upload-log4d.qiniudn.com/2009/11/edtTxtConvert_0_9.zip)（edt
TxtConvert.py+config.cfg+reade me.txt，需要Python2.6以上），如果需要exe版本的程序，可以向我索取，也可以[使
用py2exe自行编译](http://log4d.com/2009/09/python-program-will-be-compiled-into-an-
executable-program-exe)。

