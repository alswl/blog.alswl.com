Title: urllib2.urlopen的中文URL问题
Author: alswl
Slug: urllib2-urlopen-unicode
Date: 2011-06-14 00:00:00
Tags: 
Category: Python编程
Summary: 

在url中使用中文其实是一个坏习惯，会带来一系列的转码问题， 我更喜欢英文译名或者id来标识某个uri。但是现实往往是残酷的，
特别是在我们调用别人服务时候，有时候被逼无奈使用中文URL。

Python中unicode转码一向是让人头疼的问题。数次碰壁之后，我也摸出了一些门道，
研读完[Python字符串的encode与decode](http://ipie.blogbus.com/logs/19379694.html)
之后，就自认为找到了万金油，谁知道这次又碰上这个老冤家。

    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/usr/lib/python2.6/urllib2.py", line 126, in urlopen
        return _opener.open(url, data, timeout)
      File "/usr/lib/python2.6/urllib2.py", line 391, in open
        response = self._open(req, data)
      File "/usr/lib/python2.6/urllib2.py", line 409, in _open
        '_open', req)
      File "/usr/lib/python2.6/urllib2.py", line 369, in _call_chain
        result = func(*args)
      File "/usr/lib/python2.6/urllib2.py", line 1170, in http_open
        return self.do_open(httplib.HTTPConnection, req)
      File "/usr/lib/python2.6/urllib2.py", line 1142, in do_open
        h.request(req.get_method(), req.get_selector(), req.data, headers)
      File "/usr/lib/python2.6/httplib.py", line 914, in request
        self._send_request(method, url, body, headers)
      File "/usr/lib/python2.6/httplib.py", line 951, in _send_request
        self.endheaders()
      File "/usr/lib/python2.6/httplib.py", line 908, in endheaders
        self._send_output()
      File "/usr/lib/python2.6/httplib.py", line 780, in _send_output
        self.send(msg)
      File "/usr/lib/python2.6/httplib.py", line 759, in send
        self.sock.sendall(str)
      File "<string>", line 1, in sendall
    UnicodeEncodeError: 'ascii' codec can't encode characters in position 7-8: ordinal not in range(128)

这次错误引发是在 `urlopen()` 引起的，很有特色，开始使用 `url.encode('utf-8')` 就可以解决了。 今天我做了一些测试。

## 1. ascii + unicode 测试

    
    >>> 'a' + u'b'
    >>> '你' + u'好'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    UnicodeDecodeError: 'ascii' codec can't decode byte 0xe4 in position 0: ordinal not in range(128)
    >>> u'你' + u'好'
    u'u4f60u597d'
    >>> u'a' + '你' + u'好'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    UnicodeDecodeError: 'ascii' codec can't decode byte 0xe4 in position 0: ordinal not in range(128)

上面的测试说明ascii码和unicode码相连操作，结论是有中文记得带上u，就不会有问题。
Python默认解码器是ascii，无法解码unicode中的中文。

## 2. urllib2的测试

    
    >>> import urllib2
    >>> h1 = 'http://baidu.com'
    >>> urllib2.urlopen(h1)
    <addinfourl at 153439532 whose fp = <socket._fileobject object at 0xb74e51ac>>
    >>> h2 = u'http://baidu.com'
    >>> urllib2.urlopen(h2)
    <addinfourl at 153440236 whose fp = <socket._fileobject object at 0x925912c>>
    >>> h3 = 'http://baidu.com?w=测试'
    >>> urllib2.urlopen(h3)
    <addinfourl at 153482348 whose fp = <socket._fileobject object at 0x92593ac>>
    >>> h4 = u'http://baidu.com?w=测试'
    >>> urllib2.urlopen(h4)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/usr/lib/python2.6/urllib2.py", line 126, in urlopen
        return _opener.open(url, data, timeout)
      File "/usr/lib/python2.6/urllib2.py", line 391, in open
        response = self._open(req, data)
      File "/usr/lib/python2.6/urllib2.py", line 409, in _open
        '_open', req)
      File "/usr/lib/python2.6/urllib2.py", line 369, in _call_chain
        result = func(*args)
      File "/usr/lib/python2.6/urllib2.py", line 1170, in http_open
        return self.do_open(httplib.HTTPConnection, req)
      File "/usr/lib/python2.6/urllib2.py", line 1142, in do_open
        h.request(req.get_method(), req.get_selector(), req.data, headers)
      File "/usr/lib/python2.6/httplib.py", line 914, in request
        self._send_request(method, url, body, headers)
      File "/usr/lib/python2.6/httplib.py", line 951, in _send_request
        self.endheaders()
      File "/usr/lib/python2.6/httplib.py", line 908, in endheaders
        self._send_output()
      File "/usr/lib/python2.6/httplib.py", line 780, in _send_output
        self.send(msg)
      File "/usr/lib/python2.6/httplib.py", line 759, in send
        self.sock.sendall(str)
      File "<string>", line 1, in sendall
    UnicodeEncodeError: 'ascii' codec can't encode characters in position 7-8: ordinal not in range(128)

这个测试说明， `urllib2.urlopen()` 可以接受ascii/unicode的英文，也可以接受ascii的中文，
但是一旦是unicode的中文url，就会报转码错误。

so，请尽量英文url，非要用中文，请记得转码。

