Title: 解决WordPress升级后出现Warning: Cannot modify header information - headers already sent by
Author: alswl
Date: 2010-02-21 00:00:00
Tags: WordPress, 编码
Category: 建站心得
Summary: 

WordPress 2.9.2升级之后出现一个问题，在一些操作，比如删除垃圾留言、发表新的文章时候会提醒一下的错误。

>

Warning: Cannot modify header information - headers already sent by (output
started at /home/alswl/public_html/wp-settings.php:1) in
/home/alswl/public_html/wp-includes/pluggable.php on line 868

我简单查找了一下，这是一个简单的编码问题，1分钟可以搞定了。

1.Ftp下载wp-settings.php这个文件，用记事本打开这个文档。

2.另存为"ANSI"格式的文本。

3.重新上传覆盖原文件。

如果还有其他文件出现问题，继续修改编码有问题的文件。

这样问题就可以解决了，为了以防万一，建议在操作之前记得备份。

参考文章：[解決Wordpress安裝時出現Warning: Cannot modify header information - headers
already sent by - 新後園 - 德語學習部落格 - Poshi的網誌](http://poshi.org/post/401.html)

