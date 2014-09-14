Title: 小脚本mm->html
Author: alswl
Slug: script-mm2html
Date: 2010-09-27 00:00:00
Tags: Python编程, BooguNote, FreeMind
Category: Coding

我同时在使用两套信息记录工具，知识收集记录工具BooguNote + KMS Wiz，关于这两套系统具体介绍请见[桌面记录神器-
BooguNote](http://log4d.com/2010/04/desktop-recording-tool-boogunote) &
[我所使用的知识管理系统](http://log4d.com/2010/09/my-kms)。

我的使用习惯是在BooguNote中收集日常的琐碎知识点，包括我所想的和工作记录。每个小知识节点的长度大概在200-300字左右。这些被我称为的知识碎片显然
不能直接放入KMS。

BooguNote可以将里面的文字直接复制出来，会在父亲节点上加入+，子节点加入-，这种简单的txt不能满足我的要求。于是我花了点时间写了一个mm文件到ht
ml的转换脚本。

BooguNote的文件格式是boo，可以转换成FreeMind的思维导图格式.mm，我认为用mm作为源数据格式适用范围更大。

    
    #coding=utf-8
    from xml.dom import minidom
    import sys
    import os

class MM2Html:

'转换MM->Html类'

def __init__(self):

self.html = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

<head>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

<style type="text/css">

''' + cssStr + '''

</style>

</head> '''

self.level = 0

self.pos = [0 for x in range(0, 10)]

def procRoot(self, root):

'处理root节点'

for i in root.childNodes:

if i.nodeName == 'node':

self.procNode(i)

self.html += "</body>"

def procNode(self, node):

'处理Node节点'

if node.nodeName == 'node':

self.level += 1

#Tltle处理

if self.isHead(node):

self.pos[self.level - 1] += 1

self.html += self.getHead(node.getAttribute("TEXT"))

for i in node.childNodes:

MM2Html.procNode(self, i)

#文本节点处理

else:

self.html += '<pre style="margin-left:%s;">%s</pre>' %(str(20 * self.level) +
'px',node.getAttribute("TEXT"))

self.pos[self.level: 10] = [0 for x in range(0, 10)]

self.level -= 1

def procNodex(self, node):

deepth = self.position

def isHead(self, node):

'判断是否是标题'

for i in node.parentNode.childNodes:

for j in i.childNodes:

if j.nodeName == 'node':

return True

return False

def getHead(self, text):

'获取标题Html格式化后内容'

titlePrefix = ''

for i in range(0, self.level):

titlePrefix += str(self.pos[i]) + '.'

return "<h%s>%s %s</h%s>" %(self.level, titlePrefix, text, self.level)

def getFiles(type):

'获取当前目录下某类型文件'

files = os.listdir(os.getcwd())

fileList = list()

for file in files:

if os.path.splitext(file)[1].lower() == type:

fileList.append(file)

return fileList

if __name__ == '__main__':

cssFileName = 'style.css'

xmlFileNames = getFiles('.mm')

try:

cssStr = open(cssFileName, 'r').read()

except:

cssStr = ''

for xmlFileName in xmlFileNames:

try:

xmlFile = open(xmlFileName, "r")

xmlDoc = minidom.parse(xmlFile)

except:

print "Unexpected error:", sys.exc_info()[0]

root = xmlDoc.getElementsByTagName('node')[0]

html = open(xmlFileName.split('.')[0] + '.html', 'w')

mm2Html = MM2Html()

mm2Html.procRoot(root)

html.write(mm2Html.html.encode('utf-8'))

html.close()

脚本zip档点击这里下载，里面的CSS格式我用的我博客主题的reset.css，可以自行修改。

传送门：点击这里[下载Boo2Html.zip](http://upload-log4d.qiniudn.com/2010/09/Boo2Html.zip)

oh， SB了，还没说怎么用：把zip档里面的两个文件放到有mm的文件夹里面，双击运行即可（需要Python环境）。

