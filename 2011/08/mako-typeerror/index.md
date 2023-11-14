

Mako 下面开发时候，遇到这个问题

> TypeError: sequence item : expected string or Unicode, long found

Trace 的情况大概这样（我的错误信息无法再现，这是某位外国友人的错误信息）

> File '/Users/amaslov/Projects/dou-pylons/doupy/doupy/controllers/ root.py',
line 239 in staticpage

>

> return render('/pages/%s.html' % name)

>

> File '/Users/amaslov/Projects/dou-pylons/py/lib/python2.5/site-
packages/Pylons-0.9.7-py2.5.egg/pylons/templating.py', line 274 in render_mako

>

> cache_type=cache_type, cache_expire=cache_expire)

>

> File '/Users/amaslov/Projects/dou-pylons/py/lib/python2.5/site-
packages/Pylons-0.9.7-py2.5.egg/pylons/templating.py', line 249 in
cached_template

>

> return render_func()

>

> File '/Users/amaslov/Projects/dou-pylons/py/lib/python2.5/site-
packages/Pylons-0.9.7-py2.5.egg/pylons/templating.py', line 271 in
render_template

>

> return literal(template.render_unicode(**globs))

>

> File '/Users/amaslov/Projects/dou-pylons/py/lib/python2.5/site-
packages/Mako-0.2.4-py2.5.egg/mako/template.py', line 138 in render_unicode
return runtime._render(self, self.callable_, args, data, as_unicode=True) File
'/Users/amaslov/Projects/dou-pylons/py/lib/python2.5/site-
packages/Mako-0.2.4-py2.5.egg/mako/runtime.py', line 348 in _render

>

> return context._pop_buffer().getvalue()

>

> File '/Users/amaslov/Projects/dou-pylons/py/lib/python2.5/site-
packages/Mako-0.2.4-py2.5.egg/mako/util.py', line 74 in getvalue

>

> return self.delim.join(self.data)

>

> TypeError: sequence item 68: expected string or Unicode, NoneType found

Mako 的邮件列表曾在2009年遇到这个错误，讨论信息在[这里](http://www.mail-archive.com/pylons-
discuss@googlegroups.com/msg11021.html)（需翻墙）

讨论了半天也没什么结果，一直围绕在 default_filter 上面，我改了半天，也没效果。

测试服务器和正式环境都没有问题，最后试了清空`data/session, data/templates` 目录，终于没错误了。

Google 上这个错误信息资料太少，我就记下来，如果哪位同学出现同样错误找到我这里，就方便解决了。


