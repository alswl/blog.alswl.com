Title: Eclipse中JSP文件的编码设置
Author: alswl
Slug: eclipse-in-the-jsp-file-s-encoding-settings
Date: 2009-02-24 00:00:00
Tags: Eclipse
Category: 工欲善其事必先利其器

在Eclipse中新建JSP页面时候，**contentType="text/html; charset=utf-8"**,
**pageEncoding="utf-8"**, **content="text/html; charset=utf-8"**， 这样连中文字都无法保存
，必须修改成UTF-8才能显示。

在网上找了很久都没有合适的方案，都是给出在General下面的Content Types修改编码，而且下面人留言还说有效，我自己试了去发现根本没有作用。。。

自己琢磨了很久，终于在Web - JSP Files 里面找到了正确的设置，把其中的**Encoding**由ISO改为UTF-8就一切完美解决。

