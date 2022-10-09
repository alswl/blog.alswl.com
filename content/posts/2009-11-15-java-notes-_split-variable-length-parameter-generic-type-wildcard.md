---
title: "Java笔记 split/不定长度参数/泛型类型通配符"
author: "alswl"
slug: "java-notes-_split-variable-length-parameter-generic-type-wildcard"
date: "2009-11-15T00:00:00+08:00"
tags: ["java", "javase"]
categories: ["coding"]
---

今天看了一下午《[Java学习笔记](http://www.douban.com/subject/2057790/)》，作者林信良，花名良葛格。从书中所获颇
多，正所谓温故而知新，我就把今天的"新"总结一下，加深记忆。良葛格也提倡"在网上写文章是我记录所学的一种方式"。

## split的正则式和其中的正则式

C语言其中有函数strtok，就是按某些char对字符串进行切割。下面给出一个C下面的范例

    
    char str[] = "now # is the time for all # good men to come to the # aid of their country";
    char delims[] = "#";
    char *result = NULL;

result = strtok( str, delims );

while( result != NULL ) {

printf( "result is "%s"n", result );

result = strtok( NULL, delims );

}

在Java中也有类似的StringTokenizer，但是在JDK5中，已经被标记为Legacy
Class(遗产类)，推荐使用String.split(String regex)，可以接受正则表达式。范例如下。

    
    private void init() {
    	Scanner scanner = new Scanner(System.in);

System.out.println("input n and data");

n = scanner.nextInt();

data = new int[n];

String input = scanner.next().trim();

//String[] strData = splitByTokenizer(input);

String[] strData = input.split("[,\s]");

int i = 0;

for (String t : strData) {

data[i] = Integer.parseInt(t);

i++;

}

}

//已过时，Legacy Class(遗产类)

private String[] splitByTokenizer (String input, String regex) {

String [] result = null;

if (input != null && !input.equals("")) {

StringTokenizer commaToker = new StringTokenizer(input, ",");

result = new String[commaToker.countTokens()];

int i = 0;

while (commaToker.hasMoreTokens())

{

result[i] = commaToker.nextToken();

i++;

}

}

return result;

}

## 不定长度参数

听名字这东西就相当有用，也是JDK5开始支持的。（话说现在都JDK6.0了，我们很多童鞋对Java的概念还停留在最开始，其中也包括我，咱们要与时俱进嘛）直接
上代码，就知道怎么用了。

    
    package dddspace.job.exercise1115;

/**

* 使用不定长度参数  
* 参考《Java学习笔记》P153相关内容  
*   
*/  
public class VarArgs {

public static void main(String[] args) {

  
int sum = 0;

sum = VarArgs.sum(1, 2);

System.out.println(sum);

  
sum = VarArgs.sum(1, 3, 5, 7);

System.out.println(sum);

}

//关键在 "int..."

private static int sum(int... nums) {

int sum = 0;

for (int num : nums) {

sum += num;

}

return sum;

}

}

## 泛型类型通配符

如果你还不知道泛型是什么，那么最好补一下基础(via [Baidu Zhidao](http://baike.baidu.com/view/965887.h
tml?wtp=tt))，这个在C++中运用广泛，在JDK5.0加入Java大家族。我这里要解释的是泛型类型的通配符，呃，有点绕口。其实就是让泛型T这个T通
过支持一个接口来支持其实现类。

咱们还是让代码来反应思想吧。

    
    package dddspace.job.exercise1115;

import java.util.ArrayList;

import java.util.LinkedList;

import java.util.List;

/**

* 泛型类型通配符  
* 参考《Java学习笔记》P249相关内容  
*  
*/  
public class WildcardTest<T> {

public static void main(String[] args) {

  
/*想定义泛型为List接口，错误

WildcardTest<List> wildcardTestW= null;

wildcardTestW = new WildcardTest<ArrayList>();

wildcardTestW = new WildcardTest<LinkedList>();

*/  
  
//关键词 "<? extends Class>"匹配正确

WildcardTest<? extends List> wildcardTest= null;

wildcardTest = new WildcardTest<ArrayList>();

wildcardTest = new WildcardTest<LinkedList>();

}

}

## 补遗：关于String/StringBuilder/StringBuffer

简单来说，String是不可变的，每次都是指向不同的内存空间。StringBuilder是可变的，线程不安全。StringBuffer是可变的并且线程安全。
StringBuilder是JDK5.0加入的。（今天5.0开心了，都是推它的）

A.shun有一篇关于String/StringBuilder/StringBuffer的文，可以移步到[这里](http://www.a18zhizao.
cn/y2009/1060_string-stringbuffer-and-stringbuilders-the-
difference.html)看详细介绍。

