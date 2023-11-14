

年前换了一次服务器，之后发现[Lifestream](http://log4d.com/stream)的Errors飙升到1000+错误，检查一下，发现是获
取不了豆瓣的rss链接。正好这台主机支持SSH，连入之后CURL了一下豆瓣服务器，发现Time out。

紧接着发现中国内的所有域名都无法使用CURL获取，联系小张之后，得知该主机曾经被入侵过，于是屏蔽了中国大陆的ip段（囧~入侵和中国ip有毛关系）

遂想用GAE做个代理服务器，反正获取RSS也只要Get一下，代码没几句。把这项任务放入Toodledo之后，就一直没去弄，今天发现GAE
Laucher升级了，就部署到自己GAE上了。

地址格式如[http://jasontiproxy.appspot.com/proxy?url=www.douban. com/feed/people/alswl/interests](http://jasontiproxy.appspot.com/proxy?url=www.douban.com/feed/people/alswl/interests)，url参数名后面跟着具体的url。

代码其实就是用urllib2获取一下html，核心如下。

    
    #!/usr/bin/env python

from google.appengine.ext import webapp

from google.appengine.ext.webapp import util

import urllib2

class MainHandler(webapp.RequestHandler):

def get(self):

url = self.request.get('url')

if url.find('http://') < 0:

url = 'http://' + url

conn = urllib2.urlopen(url)

html = conn.read()

encoding = conn.headers['content-type'].split('charset=')[-1]

html = html.decode(encoding).encode('utf-8')

self.response.out.write(html)

def main():

application = webapp.WSGIApplication([('/proxy', MainHandler)],

debug=True)

util.run_wsgi_app(application)

if __name__ == '__main__':

main()

申请一个空间，部署上去就行了，这个小应用可以临时获取一下网页内容，不支持Post和替换url，所以称之为"最简陋的GAE代理"。


