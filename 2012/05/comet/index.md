


服务器 Push 技术表示服务器可以主动推送消息给客户端浏览器。

## 实现方式 ##

* Comet
  + Ajax 轮询
  + iframe / htmlfile
  + script tag （不中断的连续请求）
  + Flash 通讯
* WebSocket

Comet 本意是彗星，彗星尾巴痕迹很像长连接工作方式，所以 Comet 指代长连接。
在 Ajax 轮询的分类上，存在一些分歧，这里我把轮询认为一种 Comet 方式。

ps：「长连接」在一些场景下，是另外一种意义「HTTP: Keep alive」。不在本文讨论的范围中。

参考链接：

* [Comet：基于 HTTP 长连接的「服务器推」技术](http://www.ibm.com/developerworks/cn/web/wa-lo-comet/)
* [Socket.IO Supported transports](http://socket.io/#browser-support)

<!-- more -->

### 浏览器支持情况 ###

WebSocket 属于 HTML5 规范，需要「先进」浏览器支持，
Flash 通讯需要浏览器安装 Flash 插件，其他方式都可以适应常见浏览器。

参考连接：

* [HTTP持久链接](http://zh.wikipedia.org/wiki/HTTP持久链接)
* [Comet (programming)](http://en.wikipedia.org/wiki/Comet_(programming\))
* [一个误解: 单个服务器程序可承受最大连接数「理论」上是「65535」](http://www.cnblogs.com/tianzhiliang/archive/2011/06/13/2079564.html)
* [How to implement COMET with PHP](http://www.zeitoun.net/articles/comet_and_php/start)

## 各大网站连接情况 ##

可以通过 url 请求来揣测一些东西，比如说，它们没有用 WebSocket，
否则 FireBug 是无法监测的，WebSocket 可以双向通讯。

### 新浪微博 ###

未读信息链接： `http://rm.api.weibo.com/remind/unread_count.json?target=api&_pid=10001&count=2&source=3818214747&callback=STK_133834300664875`

未读信息大约每20秒触发一次，像是 Ajax 轮询。

IM 长连接：
`http://4.46.web1.im.weibo.com/im?jsonp=parent.org.cometd.script._callback5&message=%5B%7B%22channel%22%3A%22%2Fmeta%2Fconnect%22%2C%22connectionType%22%3A%22callback-polling%22%2C%22id%22%3A6%2C%22clientId%22%3A%22b02qp9qw9cgiuxxyn3%22%7D%5D&1338343019008`

可以看出新浪在使用 JSONP 跨域做 IM 长连接，FireBug 中也始终有链接请求，
看上去像 Script Tag 请求方式。

### 知乎 ###

请求链接：
`http://comet.zhihu.com/update?loc=http%3A%2F%2Fwww.zhihu.com%2F&channel=13781e6817833300f0a70f19&callback=zhp13781e6a6f22349b9865b47c8`

依然能在 FireBug 中看到请求地址，说明客户端请求数据还是走 HTTP 方式，
并且会出现 update 动作链接一直出于请求状态，猜测知乎仍然使用 Script Tag 请求。

## 框架支持 ##

### orbited2 ###

[http://labs.gameclosure.com/orbited2/](http://labs.gameclosure.com/orbited2/)

* 跨浏览器
* 容易集成：IRC / XMPP / ActiveMQ / RabbitMQ
* Python

### StreamHub ###

[http://www.stream-hub.com/](http://www.stream-hub.com/)

* 免费版仅支持 10 个在线
* 支持 Java / .net / iPhone

### socket.io ###

[http://socket.io/](http://socket.io/)

* NodeJS
* 推送方式：
  + WebSocket
  + Adobe® Flash® Socket
  + AJAX long polling
  + AJAX multipart streaming
  + Forever Iframe
  + JSONP Polling
* 支持浏览器：
  + Internet Explorer 5.5+
  + Safari 3+
  + Google Chrome 4+
  + Firefox 3+
  + Opera 10.61+
  + iPhone Safari
  + iPad Safari
  + Android WebKit
  + WebOs WebKit

### sockjs-client ###

[https://github.com/sockjs/sockjs-client](https://github.com/sockjs/sockjs-client)

* 支持 Node.js / Erlang / Lua / Python-Tornado
* 跨浏览器

## 实战 Socket.io ##

考虑到上述候选框架的使用场景，这里选择 Socket.IO 作为 Comet 框架。

### 尴尬的 Pylons ##

Pylons 和 Comet 配合有问题，问题处在标准 WSGI 是非异步的。
（看邮件列表里面，似乎新的标准准备支持）。

* [http://stackoverflow.com/a/3090118](http://stackoverflow.com/a/3090118)
* [http://mail.python.org/pipermail/web-sig/2008-July/003545.html](http://mail.python.org/pipermail/web-sig/2008-July/003545.html)
* [Spawning](http://pypi.python.org/pypi/Spawning/)

这样的话，我就直接选择使用 Node.JS 做 Comet 服务器，Nginx 负责转发。

### 简单Demo ###

node.js 代码

```js app.js
/* global __dirname, console */

var app = require('http').createServer(handler),
	io = require('socket.io').listen(app),
	fs = require('fs');

app.listen(8080);

function handler(req, res) {
	fs.readFile(__dirname + '/index.html',
		function (err, data) {
			if (err) {
				res.writeHead(500);
				return res.end('Error loading index.html');
			}

			res.writeHead(200);
			res.end(data);
		});
}

io.sockets.on('connection', function (socket) {
	'use strict';
	socket.emit('news', {hello: 'world, for everyone!'});
	socket.on('my other event', function (data) {
		console.log(data);
	});
	socket.on('private message', function (from, msg) {
		console.log('I received a private message by ', from, ' saying ', msg);
	});
});
```

页面代码

``` html index.html 
<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8">

	<title>Socket.io Demo</title>
	<script src="/socket.io/socket.io.js"></script>
	<script>
		var socket = io.connect('/');

		socket.on('news', function (data) {
			console.log(data);
			socket.emit('my other event', { my: 'data' });
		});
	</script>
</head>
<body>

</body>
</html>
```

连接成功之后，在浏览器控制台里面，可以使用 `socket.emit('my other event', {biu: 'biu'});`
向服务器发送消息。

服务器也可以通过 `socket.emit()` 来向客户端推送消息。

私有信息发送，使用 `socket.emit('private message', 'James', {some: 'message'});` 。

### 跨平台 ###

实测看来，在 IE8 下面， Socket.io 会降级使用 `htmlfile` 来实现 Comet。

而 Firefox 中会有 `websocket / htmlfile / xhr-polling / jsonp-polling` 依次备选，
首选 websocket。


### 安全性 ###

问题：提交数据的身份认证过程，以前在后台由 Web 框架自动完成，而现在流程是
Socket.IO -> RabbitMQ -> Web App，身份验证的复杂度增加了。

思路：Socket.IO 使用 Nginx 代理转发，从而保留同一域名下面的 cookie 信息，
这样能够提交到 Socket.IO 服务器，每次 RabbitMQ Message 都记录 cookie 信息，
后台从 RabbitMQ 读取信息时候，再进行认证。

实际操作：由于 Comet 中的数据流仅负责推送，客户端继续使用原始 POST
方式发送数据到服务器，所以暂时不会产生身份认证问题。

## Node AMPQ 驱动 ##

Socket.IO 提供了一个通用的 Comet 解决方案，下面就需要点润滑剂，将整个数据流跑通。
消息队列 RabbitMQ 正好适合用来做这个。

Rabbit 官网提到了一个套件 [rabbit.js](https://github.com/squaremo/rabbit.js) 。
遗憾的是这个库是混合了 RabbitMQ 和 Node.JS，提供了一个封装好的 Node.JS 库，
而我想要的仅仅是一个 AMPQ 协议驱动。[node-amqp](https://github.com/postwait/node-amqp/blob/master/amqp.js) 则是我们需要的驱动。

### Demo ###

服务器接收者脚本：

``` js app-amqp.js
/* global __dirname, console */

var conn = require('amqp').createConnection({ url: 'amqp://localhost'});

console.log('socket works');
conn.on('ready', function() {
	console.log('conn ready');
	conn.queue('socket.io', {passive: true}, function(queue){
		queue.subscribe(function (json, headers, deliveryInfo) {
			console.log('#json:')
			view(json);
			console.log('#headers:')
			view(headers);
			console.log('#deliveryInfo:')
			view(deliveryInfo);
		});
	});
});

conn.on('error', function() {
	console.error('error');
});

function view(obj) {
	for (var i in obj) {
		if(obj.hasOwnProperty(i)) {
			console.log(i + ': ' + obj[i]);
		}
	}
}
```

用 Python 写的发送者脚本：

``` python producter.py
# coding=utf-8
#! /usr/bin/env python2

import pika
import json
import logging
import time

logger = logging.getLogger()

def main():
    conn = pika.BlockingConnection(
        pika.ConnectionParameters('localhost'))
    chan = conn.channel()
    chan.queue_declare(queue='socket.io')

    count = 10
    while (count > 0):
        message = {'no': count, 'some': 'Message', u'比如': u'中文信息'}
        publish_text(chan, 'socket.io', u'text %d' %count)
        publish_json(chan, 'socket.io', message)
        logger.info('add one message to RabbitMQ')
        #time.sleep(5) # sleep 5 sec
        count -= 1

def publish_text(channel, queue, message):
    channel.basic_publish(exchange='',
                          routing_key=queue,
                          body=json.dumps(message),
                          properties=pika.BasicProperties(
                              content_type='text/plain',
                              content_encoding='utf-8',
                              delivery_mode=1)
                         )

def publish_json(channel, queue, message):
    channel.basic_publish(exchange='',
                          routing_key=queue,
                          body=json.dumps(message),
                          properties=pika.BasicProperties(
                              content_type='application/json',
                              content_encoding='utf-8',
                              delivery_mode=1)
                         )

if __name__ == '__main__':
    main()
```

使用 `node ./app-amqp.js` 运行 Node.JS 服务器，然后运行 `producter.py` 产生
RabbitMQ Message，我使用的数据格式是序列化的 JSON 字串，
还有 `JSON, Thrift, Protocol Buffers, MessagePack` 这些格式可供选择。运行结果如下：

``` text
#json:
data: "text 1"
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-3: ordinal not icontentType: text/plain
#headers:
#deliveryInfo:
contentType: text/plain
contentEncoding: utf-8
deliveryMode: 1
queue: socket.io
deliveryTag: 19
redelivered: false
exchange:
routingKey: socket.io
consumerTag: node-amqp-10880-0.06487216474488378
#json:
比如: 中文信息
some: Message
no: 1
#headers:
#deliveryInfo:
contentType: application/json
contentEncoding: utf-8
deliveryMode: 1
queue: socket.io
deliveryTag: 20
redelivered: false
exchange:
routingKey: socket.io
consumerTag: node-amqp-10880-0.06487216474488378
```

里面有两个 Message，发送数据格式为 `text/plain` 和 `application/json` 。

参考链接：

* [Pika Document](http://pika.github.com/)

## Socket.IO + RabbitMQ ##

最后提供 Socket.IO + RabbitMQ 的完整 Demo，客户端会实时接受到来自消息发送者的消息。

``` js app-amqp.socket.js
/* global __dirname, console */

var app = require('http').createServer(handler),
	io = require('socket.io').listen(app),
	fs = require('fs');

app.listen(8080);

function handler(req, res) {
	fs.readFile(__dirname + '/index.html',
		function (err, data) {
			if (err) {
				res.writeHead(500);
				return res.end('Error loading index.html');
			}

			res.writeHead(200);
			res.end(data);
		});
}

io.sockets.on('connection', function (socket) {
	console.log('io ready');

	var conn = require('amqp').createConnection({ url: 'amqp://localhost'});
	conn.on('ready', function () {
		console.log('conn ready');
		conn.queue('socket.io', {passive: true}, function(queue){
			queue.subscribe(function (json, headers, deliveryInfo) {
				console.log(json);
				console.log(deliveryInfo.contentType);
				if (deliveryInfo.contentType == 'application/json') {
					socket.emit('news', json);
				}
				if (deliveryInfo.contentType == 'text/plain') {
					socket.emit('news', json.data.toString());
				}
			});
		});
	});
});

```

在运行 `producter.py` 后，Python 脚本持续产生 Message 到 RabbitMQ，
`app-amqp-socket.js` 订阅读取 Message 并推送到浏览器端。
浏览器可以在 Console 里面看到日志：

``` text
Object { 比如="中文信息", some="Message", no=1}
```

至此，我们可以完成 WebApp -> RabbitMQ -> Socket.IO -> Browser 的实时推送。

