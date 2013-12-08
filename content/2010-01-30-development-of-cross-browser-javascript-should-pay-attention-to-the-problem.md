Title: 开发跨浏览器JavaScript时要注意的问题
Author: alswl
Slug: development-of-cross-browser-javascript-should-pay-attention-to-the-problem
Date: 2010-01-30 00:00:00
Tags: JavaScript
Category: Web前端

最近在做系统的B/S部分，用DWR做Ajax处理，期间遇到一些浏览器兼容的问题，`table.insertRow()`和`row.insertCell()`
在IE下没有问题，但在FireFox下无效。同事说不用考虑FireFox的兼容，客户使用的环境就是IE。我偏执的认为就算不在所有浏览器下通过，至少在我的Fi
reFox下需要正常运行。

晚上花了一点时间稍微研究了一下跨浏览器开发JavaScript时要注意的问题，的确好多学问。我对JavaScript的认识还太浅，得花时间做一些功课了。

顺便推荐一本JavaScript书《**JavaScript语言精粹** 》，是大名鼎鼎的"O'Reilly"系列，我只看了试读的第一章节，斗胆推荐

在[随网之舞](http://dancewithnet.com)的[《JavaScript语言精粹》 @
随网之舞](http://dancewithnet.com/2009/04/02/javascript-the-good-parts/)有更详细的介绍。

![](http://t.douban.com/lpic/s3651235.jpg)

传送门：

[购买](http://www.china-pub.com/195292)《JavaScript语言精粹 》via China-Pub

[评论](http://www.douban.com/subject/3590768/) 《JavaScript语言精粹》via 豆瓣

**样章阅读**：[第一章. 精华](http://images.china-pub.com/ebook195001-200000/195292/ch01.pdf) [第十章. 优美的特性](http://images.china-pub.com/ebook195001-200000/195292/ch10.pdf)

以下文章没有URL出处，作者 liqun，来源：<strike>www.comecode.com</strike>（连接已失效）

××××××××××想回家的分割线××××××××××

## 1、向表中追加行

定义table时使用tbody元素，以保证包括IE在内的所有浏览器可用

例：定义如下一个空表

<table id="myTable">

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&n
bsp_place_holder; <tbody id="myTableBody"></tbody>

</table>

向这个表中增加行的正确做法是，把行增加到表体，而不是增加到表。

Var cell =
document.createElement("td").appendChild(document.createTextNode("foo"));

Var row = document.createElement("tr").appendChild(cell);

Document.getElementById("myTableBody").appendChild(row);

*IE中需要先创建行，再创建列，再创建内容

## 2、设置元素的样式

Var spanElement = document.getElementById("mySpan");

//下面写法保证出IE外，所有浏览器可用

spanElement.setAttribute("style","font-weight:bold;color:red;");

//下面的写法保证IE可用

spanElement.style.cssText="font-weight:bold;color:red;";

## 3、设置元素的class属性

Var element = document.getElementById("myElement");

//下面的写法保证除IE外，所有浏览器可用

Element.setAttribute("class","styleClass");

//下面写法保证IE可用

Element.setAttribute("className","styleClass");

## 4、创建输入元素

Var button = document.createElement("input");

//单行文本框、复选框、单选框、单选钮、按钮需要此属性区别

Button.setAttribute("type","button");

Document.getElementById("formElement").appendChild(button);

## 5、向输入元素增加事件处理程序

Var formElement=document.getElementById("formElement");

//所有浏览器可用

formElement.onclick=function(){doFoo();};

//除IE外，所有浏览器可用

formElement.setAttribute("onclick","doFoo();");

## 6、创建单选钮

If(document.uniqueID){

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&n
bsp_place_holder; //Internet Explorer

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&n
bsp_place_holder; Var radioButton=document.createElement("<input type='radio'
name='radioButton' value='checked'>");

}else{

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&n
bsp_place_holder; //Standards Compliant

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&n
bsp_place_holder; Var radioButton=document.createElement("input");

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&n
bsp_place_holder; radioButton.setAttribute("type","radio");

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&n
bsp_place_holder; radioButton.setAttribute("name","radioButton");

&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&n
bsp_place_holder; radioButton.setAttribute("value","checked");

}

## 7、insertRow,insertCell,deleteRow

在IE中，table.insertRow()如果没有指定参数，则在表格后面添加行，默认参数位-1；如果在Firefox中，则一定要加参数，如：insertR
ow(-1)。

