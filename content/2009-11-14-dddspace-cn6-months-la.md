Title: DDDSpace.cn6个月拉
Author: alswl
Slug: dddspace-cn6-months-la
Date: 2009-11-14 00:00:00
Tags: 日记, WordPress
Category: Life

今天是我博客6周月纪念日。

在这6个月里，dddspace.cn输出了236 文章，输入了465评论，屏蔽了6141条Spam，PR由0->1->2。

Pv和IP比较低迷，大部分来源来自搜索引擎，还有一部分是这段时间认识的新朋友们。

这个博客完整记录了我大学最后一年的生活，并且会将继续陪伴我走下去。（咦？为什么日志存档从2008年开始？哈哈，那是因为我把Baidu
Hi的一部分内容导入了！）

为了庆祝周庆，我重新部署了博客的插件，[CodeColorer的Html编码问题](http://log4d.com/2009/09/the-html-
escape-codecolorer)已经被我彻底搞清楚。我现在已经切换到wp-
syntax了。最大的麻烦："[WordPress编辑器空格在FireFox下面无法缩进](http://log4d.com/2009/09/about-
wordpress-spaces-in-tinymce)"也被我用新的插件"[Dean's FCKEditor With pwwang's Code
Plugin For Wordpress](http://pwwang.com/technology/wp-wp-plugins/deans-
fckeditor-with-pwwangs-code-plugin-for-wordpress)"完美解决。

我现在就位于FCKEditor(CKEditor)下面进行编辑，世界第一的FCKEditor就是比世界第二的TinyMCE阉割版强。

上几张华丽的让我蛋疼的粘代码截图

[![插入代码](http://77g0h6.com1.z0.glb.clouddn.com/2009/11/codein_fck_insert.jpg)](http
://77g0h6.com1.z0.glb.clouddn.com/2009/11/codein_fck_insert.jpg)

[![显示为Code](http://77g0h6.com1.z0.glb.clouddn.com/2009/11/code_in_fck.jpg)](http
://77g0h6.com1.z0.glb.clouddn.com/2009/11/code_in_fck.jpg)

下面的一段Python代码就是我测试缩进用的，代码大意是…呃…哦，是输出一段XNML

    
    # coding=utf-8

#!/usr/bin/env python

# # Copyright 2007 Google Inc.

# # Licensed under the Apache License, Version 2.0 (the "License");

# you may not use this file except in compliance with the License.

# You may obtain a copy of the License at

# # http://www.apache.org/licenses/LICENSE-2.0

# # Unless required by applicable law or agreed to in writing, software

# distributed under the License is distributed on an "AS IS" BASIS,

# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

# See the License for the specific language governing permissions and

# limitations under the License.

#

import wsgiref.handlers

from google.appengine.ext import webapp

class MainHandler(webapp.RequestHandler):

def head(self, *args):

return self.get(*args)

def post(self):

self.response.out.write('''<b>使用者的名称及其大中小三种头像：</b>

<div style="text-align: center;">图片： <xn:profile-pic uid="loggedinuser"
linked="true" size="tiny"> <xn:profile-pic uid="loggedinuser" linked="true"
size="normal"> <xn:profile-pic uid="loggedinuser" linked="true" size="main">

姓名： <xn:name uid="loggedinuser" linked="true" shownetwork="true">
</xn:name></xn:profile-pic></xn:profile-pic></xn:profile-pic></div>''')

def get(self):

self.response.out.write('''<b>使用者的名称及其大中小三种头像：</b>

<div style="text-align: center;">图片： <xn:profile-pic uid="loggedinuser"
linked="true" size="tiny"> <xn:profile-pic uid="loggedinuser" linked="true"
size="normal"> <xn:profile-pic uid="loggedinuser" linked="true" size="main">

姓名： <xn:name uid="loggedinuser" linked="true" shownetwork="true">
</xn:name></xn:profile-pic></xn:profile-pic></xn:profile-pic></div>''')

def main():

application = webapp.WSGIApplication([('/.*', MainHandler)], debug=True)

wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':

main()

