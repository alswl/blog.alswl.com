

发现很久没在校内写日志，只有状态的更新，显得内容很单薄，于是想使用校内的日志导入功能导入本博的文章。

在日志页面点击日志导入，接受协议并且输入网址或者QQ号，校内会自动找到相应的RSS链接，接下来出现选择日志导入界面。

导入之后，发现了一个严重的问题，文章是纯文字，并且只有部分，好在最上方有原始文章链接。

Google中相关信息不多，这里有一篇「校内网日志导入功能浅析|
竹枝」<[猛击这里打开](http://blog.anyshpm.com/archives/21)>，里面解释了校内读取的部分。

我仔细检查后，发现的确校内只读取RSS的description部分，而WordPress的Feed中文字，description是纯文字并且剪切过的。

如果要校内显示完整的内容，在无法对校内读取方式进行设定的情况下，只能修改RSS内容，修改description中内容，但是这样给订阅者带来不方便。在我看来，
我没有什么更好的解决办法。

这应该是校内对自己内部文章的一种保护方式吧。。。

