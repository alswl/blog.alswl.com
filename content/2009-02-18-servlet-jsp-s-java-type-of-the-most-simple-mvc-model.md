Title: Servlet JSP 的 Java类的最简单MVC模型
Author: alswl
Slug: servlet-jsp-s-java-type-of-the-most-simple-mvc-model
Date: 2009-02-18 00:00:00
Tags: MVC
Category: Java

来自Head First Servlet and JSP

_XML语言_: [web.xml](http://www.fayaa.com/code/view//)

<?xml version="1.0" encoding="UTF-8"?>

<web-app xmlns="http://java.sun.com/xml/ns/j2ee"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

xsi:schemaLocation="http://java.sun.com/xml/ns/javaee
http://java.sun.com/xml/ns/j2ee/web-app_2_4.xsd"

version="2.4"> -->

  
<servlet>

<servlet-name>Ch3 Beer</servlet-name>

<servlet-class>com.example.web.BeerSelect</servlet-class>

</servlet>

  
<servlet-mapping>

<servlet-name>Ch3 Beer</servlet-name>

<url-pattern>/SelectBeer.do</url-pattern>

</servlet-mapping>

  
</web-app>

_HTML语言_: [form.html](http://www.fayaa.com/code/view//)

<html>

<head>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

<title>Beer Selection Page</title>

</head>

  
<body>

<h1 align="center">Beer Selection Page</h1>

<form method="post" action="SelectBeer.do">

select beer characteristics<p>

Color:

<select name="color" size="1">

<option>light

<option>amber

<option>brown

<option>dark

</select>

<br>

<br>

<center>

<input type="submit">

</center>

</form>

</body>

</html>

_Java语言_: [BeerSelect](http://www.fayaa.com/code/view//)

package com.example.web;

  
import com.example.model.*;

import javax.servlet.*;

import javax.servlet.http.*;

import java.io.*;

import java.util.*;

  
public class BeerSelect extends HttpServlet

{

public void doPost(HttpServletRequest request,

HttpServletResponse response)

throws IOException, ServletException

{

// response.setContentType("text/html");

// PrintWriter out = response.getWriter();

// out.println("Beer Selection Advice<br>");

String c = request.getParameter("color");

// out.println("<br>Got beer color " + c);

  
BeerExpert be = new BeerExpert();

List result = be.getBrands(c);

  
// Iterator it = result.iterator();

// while (it.hasNext())

// {

// out.print("<br>try: " + it.next());

// }

  
request.setAttribute("styles", result);

RequestDispatcher view = request.getRequestDispatcher("result.jsp");

view.forward(request, response);

}

}

_Java语言_: [BeerExpert](http://www.fayaa.com/code/view//)

package com.example.model;

  
import java.util.*;

  
public class BeerExpert

{

public List getBrands (String color)

{

List brands = new ArrayList();

if (color.equals("amber"))

{

brands.add("Jack Amber");

brands.add("Red Moose");

}

else

{

brands.add("Jail Pale Ale");

brands.add("Gout Stout");

}

return brands;

}

}

_Java Server Page语言_: [result.jsp](http://www.fayaa.com/code/view//)

<%@ page import="java.util.*"%>

  
<html>

<head>

<title>Beer Recommendations JSP</title>

</head>

  
<body>

<h1 align="center">Beer Recommendations JSP</h1>

<p><%

List sytles = (List)request.getAttribute("styles");

Iterator it = sytles.iterator();

while (it.hasNext())

{

out.print("<br>try: " + it.next());

}

%>

</body>

</html>

