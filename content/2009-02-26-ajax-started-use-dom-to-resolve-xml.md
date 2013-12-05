Title: Ajax起步：使用DOM解析XML
Author: alswl
Date: 2009-02-26 00:00:00
Tags: AJAX
Category: Web前端
Summary: 

只要代码没问题，基本上就没有问题，唯一值得注意的是虽然是html文档，但是如果想使用dom解析xml，还是必须使用服务器的，否则XMLHttpRequest
返回的status就是0了。

_XML语言_: [studentdata.xml](http://www.fayaa.com/code/view//)

<?xml version="1.0" encoding="UTF-8"?>

<classmates>

<student>

<sid>0371</sid>

<sname>张三</sname>

<sage>17</sage></student><student>

<sid>0372</sid>

<sname>李四</sname>

<sage>18</sage></student><student>

<sid>0373</sid>

<sname>王五</sname>

<sage>18</sage></student></classmates>

_HTML语言_: [domxml.html](http://www.fayaa.com/code/view//)

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">

<html>

<head>

<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<title>使用DOM解析XML</title>

<script type="text/javascript" src="domxml.js"></script>

</head>

<body>

<form>

<input type="button" value="解析XML" color: rgb(170,85,0)>"sendRequest();"/>

</form>

</body>

</html>

_JavaScript语言_: [domxml.js](http://www.fayaa.com/code/view//)

var XMLHttpReq;

var url = "studentdata.xml";

function createXMLHttpRequest() {

if (window.XMLHttpRequest)

XMLHttpReq = new XMLHttpRequest();

else if (window.ActiveXObject) {

try {

XMLHttpReq = new ActiveXObject("Msxml2.XMLHTTP");

}

catch (e) {

try {

XMLHttpReq = new ActiveXObject("Microsoft.XMLHTTP");

}

catch (e) {

alert("create faile");

}

}

}

}

function sendRequest() {

createXMLHttpRequest();

XMLHttpReq.onreadystatechange = processResponse;

XMLHttpReq.open("GET", url, true);

XMLHttpReq.send(null);

}

function processResponse() {

if (XMLHttpReq.readyState == 4) {

if (XMLHttpReq.status == 200) {

readXml();

}

else {

window.alert(XMLHttpReq.statusText);

window.alert("请求页面有异常");

}

}

}

function readXml() {

// alert("start read");

var table = document.createElement("table");

table.setAttribute("border", "1");

table.setAttribute("width", "600");

document.body.appendChild(table);

var caption = "学生信息" + url;

table.createCaption().appendChild(document.createTextNode(caption));

var header = table.createTHead();

var headerrow = header.insertRow(0);

headerrow.insertCell(0).appendChild(document.createTextNode("学号"));

headerrow.insertCell(1).appendChild(document.createTextNode("姓名"));

headerrow.insertCell(2).appendChild(document.createTextNode("年龄"));

var students = XMLHttpReq.responseXML.getElementsByTagName("student");

  
for (var i =0; i < students.length; i++) {

var stud = students[i];

var sid = stud.getElementsByTagName("sid")[0].firstChild.data;

var sname = stud.getElementsByTagName("sname")[0].firstChild.data;

var sage = stud.getElementsByTagName("sage")[0].firstChild.data;

var row = table.insertRow(i + 1);

row.insertCell(0).appendChild(document.createTextNode(sid));

row.insertCell(1).appendChild(document.createTextNode(sname));

row.insertCell(2).appendChild(document.createTextNode(sage));

}

}

