Title: iNove下的heading样式修改
Author: alswl
Slug: inove-changes-under-the-heading-style
Date: 2009-09-08 00:00:00
Tags: 建站心得, CSS, WordPress
Category: Coding

前段时间主体选择了7color，但是后来发现还是iNove对各种插件的兼容性好，又转回了iNove。

而iNove在我看来并不是完美的，存在些许问题，Heading问题就是我尤其不能忍受的问题。

看看一般的heading，下图是LightWord的

[caption id="attachment_12635" align="alignnone" width="250"
caption="lightWord的heading"][![7color的heading](http://upload.log4d.com/upload_dropbox/200909/7colorHeading.jpg)](http://upload.log4d.com/upload_dropbox/200909/7colorHeading.jpg)[/caption]

再看看iNove的

[caption id="attachment_12636" align="alignnone" width="200"
caption="iNove的Heading"][![iNove的Heading](http://upload.log4d.com/upload_dropbox/200909/iNoveHeading.jpg)](http://upload.log4d.com/upload_dropbox/200909/iNoveHeading.jpg)[/caption]

iNove的文章内容Heading CSS和主题的Heading混合在一起，非常不雅观。我稍作修改，在iNove的style.css最后加上一些样式。

`/* dddspace.cn heading fix STAET */

.post .content h1 {

font-family:Georgia,"Times New Roman","Bitstream Charter",Times,serif;

margin: 0;

padding: 0;

border: none;

color:#555555;

font-size:13px;

font-size-adjust:none;

font-style:normal;

font-variant:normal;

font-weight:normal;

line-height:19px;

font-size:2.15em;

} .post .content h2 {

font-family:Georgia,"Times New Roman","Bitstream Charter",Times,serif;

margin: 0;

padding: 0;

border: none;

color:#555555;

font-size:13px;

font-size-adjust:none;

font-style:normal;

font-variant:normal;

font-weight:normal;

line-height:19px;

font-size:1.85em;

} .post .content h3 {

font-family:Georgia,"Times New Roman","Bitstream Charter",Times,serif;

margin: 0;

padding: 0;

border: none;

color:#555555;

font-size:13px;

font-size-adjust:none;

font-style:normal;

font-variant:normal;

font-weight:normal;

line-height:19px;

font-size:1.6em;

} .post .content h4 {

font-family:Georgia,"Times New Roman","Bitstream Charter",Times,serif;

margin: 0;

padding: 0;

border: none;

color:#555555;

font-size:13px;

font-size-adjust:none;

font-style:normal;

font-variant:normal;

font-weight:normal;

line-height:19px;

font-size:1.4em;

} .post .content h5 {

font-family:Georgia,"Times New Roman","Bitstream Charter",Times,serif;

margin: 0;

padding: 0;

border: none;

color:#555555;

font-size:13px;

font-size-adjust:none;

font-style:normal;

font-variant:normal;

font-weight:normal;

line-height:19px;

font-size:1.2em;

} .post .content h6 {

font-family:Georgia,"Times New Roman","Bitstream Charter",Times,serif;

margin: 0;

padding: 0;

border: none;

color:#555555;

font-size:13px;

font-size-adjust:none;

font-style:normal;

font-variant:normal;

font-weight:normal;

line-height:19px;

font-size:1em;

} /* dddspace.cn heading fix END */`

好了，这下子样式就修复了，基本覆盖了边框，位置，文字大小宽度这些元素了。

现在的样式：

# <h1>Heading1</h1>

## <h2>Heading1</h2>

### <h3>Heading1</h3>

#### <h4>Heading1</h4>

##### <h5>Heading1</h5>

###### <h6>Heading1</h6>

