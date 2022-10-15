---
title: "Ajax 好玩的拖拽（顺便测试chrome下文字编辑的代码高亮）"
author: "alswl"
slug: "ajax-drag-and-drop-fun-the-way-chrome-test-the-code-under-the-highlighted-text-editor-search"
date: "2009-02-26T00:00:00+08:00"
tags: ["webfront", "ajax"]
categories: ["coding"]
---

_HTML语言_: [ajax 拖拽](http://www.fayaa.com/code/view//)

<HTML>

<HEAD>

<TITLE> New Document </TITLE>

<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />

<style type="text/css">

body

{

margin:10px;

}

  
  
#dragHelper

{

position:absolute;/*重要*/

border:2px dashed #000000;

background-color:#FFFFFF;

filter: alpha(opacity=30);

}

  
  
.normal

{

position:absolute;/*重要*/

width:300px;

#height:10px;

border:1px solid #666666;

background-color:#FFFFFF;

}

  
  
.over

{

position:absolute;/*重要*/

width:300px;

#height:10px;

border:1px solid #666666;

background-color:#f3f3f3;

filter: alpha(opacity=50);

}

  
  
.dragArea {

CURSOR: move;

}

  
  
</style>

</HEAD>

  
  
<BODY oncontextmenu="window.event.returnValue=false">

<input type="text" id="evt" name="eventValue" size="40" />

<div id="dragHelper" style="display:none"></div>

<div class="normal" overClass="over" dragClass="normal">

<table width="100%">

<tbody>

<tr bgcolor="#CCCCCC" bar="yes"><td><a href="#">Cobao</a></td><td
dragArea="yes" class="dragArea">........</td><td><a href="#" color:
rgb(170,85,0)>"openClose(this)">-</a> x</td></tr>

<tr><td colspan="3">地址:http://www.svnhost.cn</td></tr>

<tr><td colspan="3">关键字:<a href="http://www.svnhost.cn">SVN托管</a></td></tr>

<tr><td colspan="3">说明:</td></tr>

</tbody>

</table>

</div>

<div class="normal" overClass="over" dragClass="normal">

<table width="100%">

<tbody>

<tr bgcolor="#CCCCCC" bar="yes"><td>新浪</td><td dragArea="yes"
class="dragArea">........</td><td><a href="#" color:
rgb(170,85,0)>"openClose(this)">-</a> x</td></tr>

<tr><td colspan="3">地址:http://www.sina.com.cn</td></tr>

<tr><td colspan="3">关键字:<a href="http://www.svnhost.cn">SVN托管</a></td></tr>

<tr><td colspan="3">说明:</td></tr>

</tbody>

</table>

</div>

<div class="normal" overClass="over" dragClass="normal">

<table width="100%">

<tbody>

<tr bgcolor="#CCCCCC" bar="yes"><td>网易</td><td dragArea="yes"
class="dragArea">........</td><td><a href="#" color:
rgb(170,85,0)>"openClose(this)">-</a> x</td></tr>

<tr><td colspan="3">地址:http://www.163.com</td></tr>

<tr><td colspan="3">关键字:<a href="http://www.svnhost.cn">SVN托管</a></td></tr>

<tr><td colspan="3">说明:</td></tr>

</tbody>

</table>

</div>

  
  
  
</BODY>

<SCRIPT LANGUAGE="JavaScript">

<!--

var dragObjs = []; //可以拖拽的元素数组

var dragObjTops = [];

  
  
var dragHelper = document.getElementById("dragHelper"); //拖拽时位置框

var dragObj = null; //拖拽对象元素

var dragObjPos = 0;

  
  
var dragObjOffset = {left:0,top:0}; //拖拽对象原始位置

var mouseInDragObjOffset = {x:0,y:0}; //鼠标在拖拽对象中的相对位置

  
  
var initHeight = 40;

  
  
Number.prototype.NaN0=function(){return isNaN(this)?0:this;}

  
  
function getPosition(e){ //获取元素相对文档的绝对位置

var left = 0;

var top = 0;

while (e.offsetParent){

left += e.offsetLeft;

top += e.offsetTop;

e = e.offsetParent;

}

  
  
left += e.offsetLeft;

top += e.offsetTop;

  
  
return {x:left, y:top};

  
  
}

  
  
function mouseCoords(ev){ //获取鼠标相对文档的绝对位置

if(ev.pageX || ev.pageY){

return {x:ev.pageX, y:ev.pageY};

}

return {

x:ev.clientX + document.body.scrollLeft - document.body.clientLeft,

y:ev.clientY + document.body.scrollTop - document.body.clientTop

};

}

  
  
function getMouseOffset(target, ev){ // 获取鼠标相对元素的相对位置

ev = ev || window.event;

  
  
var elementPos = getPosition(target);

var mousePos = mouseCoords(ev);

return {x:mousePos.x - elementPos.x, y:mousePos.y - elementPos.y};

}

  
  
function mouseDown(ev){

ev = ev || window.event;

target = ev.srcElement || ev.target;

  
  
if(dragObj){

return;

}

  
  
  
var dragArea = false;

if(target.getAttribute("dragArea")){

dragArea = true;

}

  
  
while(!target.getAttribute("isDragObj")){

if(target.tagName=="HTML")

break;

target = target.parentNode;

}

  
  
if(dragArea && target.getAttribute("isDragObj")){

dragObj = target;

//重写的目的是让当前对象在最上层

document.body.removeChild(dragObj);

document.body.appendChild(dragObj);

  
  
//记录下拖拽对象原始位置

dragObjOffset.left = dragObj.style.left;

dragObjOffset.top = dragObj.style.top;

  
  
dragObj.className = dragObj.getAttribute("overClass");

//鼠标在拖拽对象中的相对位置

mouseInDragObjOffset = getMouseOffset(dragObj, ev);

  
  
dragHelper.style.left = dragObj.style.left;

dragHelper.style.top = dragObj.style.top;

dragHelper.style.width = dragObj.offsetWidth;

dragHelper.style.height = dragObj.offsetHeight;

dragHelper.style.display = "";

  
  
//alert(dragObj.offsetWidth+":"+dragObj.clientWidth);

}

}

  
  
function mouseUp(ev){

ev = ev || window.event;

target = ev.srcElement || ev.target;

  
  
if(dragObj){

dragObj.style.left = dragHelper.style.left;

dragObj.style.top = dragHelper.style.top;

  
  
dragHelper.style.display = "none";

dragObj.className = dragObj.getAttribute("dragClass");

dragObj = null;

}

  
  
}

  
  
function mouseMove(ev){

ev = ev || window.event;

  
  
if(dragObj) {

var mousePos = mouseCoords(ev);

  
/*dragHelper.style.left = dragObjOffset.left;

dragHelper.style.top = dragObjOffset.top;

dragHelper.style.width = dragObj.offsetWidth;

dragHelper.style.height = dragObj.offsetHeight;

dragHelper.style.display = "";*/

  
  
var windowWidth = document.body.offsetWidth; //窗口宽度

var windowHeight = document.body.offsetHeight; //窗口高度

  
  
//拖拽对象应该所在当前位置

var dragObjLeft = mousePos.x - mouseInDragObjOffset.x;

var dragObjTop = mousePos.y - mouseInDragObjOffset.y;

  
  
//增加判断，不然拖拽对象拖出浏览器窗口

if(dragObjLeft >= 0 && dragObjLeft <= windowWidth - dragObj.offsetWidth - 20)

dragObj.style.left = dragObjLeft;

  
  
if(dragObjTop >=0)

dragObj.style.top = dragObjTop;

  
  
repaint();

}

}

  
  
//克隆对象

function cloneObject(srcObj, destObj){

destObj = srcObj.cloneNode(true);

}

  
  
function makeDraggable(element){

element.setAttribute("isDragObj", "y");

}

  
  
function repaint(){

for(i=0; i<dragObjs.length; i++){

if(dragObjs[i] == dragObj){

dragObjPos = i;

dragObjs[i] = dragHelper;

break;

}

}

  
  
if(dragObjPos>0 &&
parseInt(dragObj.style.top)<parseInt(dragObjs[dragObjPos-1].style.top)){

dragObjs[dragObjPos] = dragObjs[dragObjPos-1];

dragObjs[dragObjPos-1] = dragHelper;

dragObjPos = dragObjPos - 1;

}

  
  
if(dragObjPos<dragObjs.length-1 &&
parseInt(dragObj.style.top)>parseInt(dragObjs[dragObjPos+1].style.top)){

dragObjs[dragObjPos] = dragObjs[dragObjPos+1];

dragObjs[dragObjPos+1] = dragHelper;

dragObjPos = dragObjPos + 1;

}

paintDragObjs();

dragObjs[dragObjPos] = dragObj;

  
  
}

  
  
function paintDragObjs(){

var h = 40;

for(i=0; i<dragObjs.length; i++){

dragObjs[i].style.left = 20;

dragObjs[i].style.top = h;

h += dragObjs[i].offsetHeight + 10;

}

}

  
  
function openClose(obj){

obj.innerHTML = obj.innerHTML=="-"?"+":"-";

while(obj.tagName != "TBODY"){

obj = obj.parentNode;

}

  
  
for(i=0; i<obj.childNodes.length; i++){

if(obj.childNodes[i].nodeName == "#text"

|| obj.childNodes[i].getAttribute("bar")){ continue; }

obj.childNodes[i].style.display=obj.childNodes[i].style.display==""?"none":"";

}

  
  
paintDragObjs();

}

  
  
document.onmousedown = mouseDown;

document.onmouseup = mouseUp;

document.onmousemove = mouseMove;

  
  
window.onload = function(){

var objs = document.getElementsByTagName("Div");

for(i=0; i<objs.length; i++){

var item = objs.item(i);

//if(i==1)item.style.height=150;

if(item.getAttribute("overClass")){

makeDraggable(item);

dragObjs.push(item);

item.style.left = 20;

item.style.top = initHeight;

dragObjTops.push(initHeight);

initHeight += item.offsetHeight + 10;

}

}

  
  
// dragHelper = document.createElement('DIV');

// dragHelper.style.cssText = 'position:absolute;display:none;';

// document.body.appendChild(dragHelper);

}

//-->

</SCRIPT>

</HTML>

用http://www.fayaa.com/网站提供的在线编辑器做的，找了类似的工具很久，甚至去了FCKEditer网站，不过效果都不怎么理想，这个网站提供
的非常不错，强烈推荐收藏

