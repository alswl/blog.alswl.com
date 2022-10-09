---
title: "get json failed in IE"
author: "alswl"
slug: "get-json-failed-in-ie"
date: "2011-08-14T00:00:00+08:00"
tags: ["webfront", "ie"]
categories: ["coding"]
---

半夜在开工打补丁，某个 bug 是 Firefox 下面能接受到 Ajax 回调请求，而 IE 不行。

解决方案在[http://stackoverflow.com/questions/425854/jquery-ajax-request-failing-
in-ie](http://stackoverflow.com/questions/425854/jquery-ajax-request-failing-
in-ie)

缘由是由于 IE 不能正常识别`application/json; charset=utf8`

于是修改为`response.headers['Content-Type'] = 'application/json'`

狗日的 IE！

