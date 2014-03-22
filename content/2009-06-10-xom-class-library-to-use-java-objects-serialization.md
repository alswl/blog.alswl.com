Title: 使用XOM类库对Java对象进行序列化
Author: alswl
Slug: xom-class-library-to-use-java-objects-serialization
Date: 2009-06-10 00:00:00
Tags: JavaSE, Lib
Category: Java

校内工具需要保存用户名和帐号，我就想把帐号信息作为一个XiaoneiUser类，然后对其进行对象持久化。
Google下的方法有好几种方法进行持久化，JDOM， DOM4J,
SAX等。我看了之后，感觉都比较麻烦，我个人比较喜欢使用jdk自带的工具，但是查阅jdk api之后，感觉使用javax.xml.*下工具开发更加困难。
我仅仅是需要对一个简单的对象进行持久化来保存数据，并不需要太多太复杂的功能。最后我决定使用《Thinking in Java》推荐的开源类库：XOM
[猛击这里打开www.xom.nu](http://www.xom.nu) 友情提示一下，网站可以打开，但是下载的连接貌似被墙了，至少我教育网连不上去。推荐
一个在线代理服务器古狗在线代理（[猛击这里打开](http://www.ggproxy.com/)），通过它就可以下载类库了。
使用类库非常简单，我这里提供个小例子。XiaoneiUser类

    
    package cn.dddspace.xiaonei.bean;

import java.io.OutputStream;

import nu.xom.*;

public class XiaoneiUser {

/**

* 用户Email  
*/  
private String userEmail;

/**

* 用户Password  
*/  
private String userPassword;

public String getUserEmail() {

return userEmail;

}

public void setUserEmail(String userEmail) {

this.userEmail = userEmail;

}

public String getUserPassword() {

return userPassword;

}

public void setUserPassword(String userPassword) {

this.userPassword = userPassword;

}

/**

* 将类转换为XML  
*   
* @return  
*/  
public Element getXML() {

Element userE = new Element("xiaoneiUser");

Element userEmailE = new Element("userEmail");

userEmailE.appendChild(userEmail);

Element userPasswordE = new Element("userPassword");

userPasswordE.appendChild(userPassword);

userE.appendChild(userEmailE);

userE.appendChild(userPasswordE);

return userE;

}

/**

* 复制构造函数  
*   
* @param xiaoneiUser  
*/  
public XiaoneiUser(Element xiaoneiUser) {

userEmail = xiaoneiUser.getFirstChildElement("userEmail").getValue();

userPassword = xiaoneiUser.getFirstChildElement("userPassword")

.getValue();

}

/**

* 构造函数  
*   
* @param userEmail  
* @param userPassword  
*/  
public XiaoneiUser(String userEmail, String userPassword) {

this.userEmail = userEmail;

this.userPassword = userPassword;

}

/**

* Format输出函数  
*   
* @param os  
* @param doc  
* @throws Exception  
*/  
public void format(OutputStream os, Document doc) throws Exception {

Serializer serializer = new Serializer(os, "UTF-8");

serializer.setIndent(4);

serializer.setMaxLength(60);

serializer.write(doc);

serializer.flush();

}

}

Test类入口函数

    
    /**
     * @title Test.java
     * @author ddd
     * @time 2009-6-10 16:35:36
     * @site http://log4d.com
     */
    package cn.dddspace.xiaonei.test;

import java.io.BufferedOutputStream;

import java.io.File;

import java.io.FileNotFoundException;

import java.io.FileOutputStream;

import cn.dddspace.xiaonei.bean.XiaoneiUser;

import nu.xom.*;

public class Test {

/**

* @param args  
* @throws Exception   
* @throws FileNotFoundException   
*/  
public static void main(String[] args) throws FileNotFoundException, Exception
{

XiaoneiUser user = new XiaoneiUser("a@a.com", "123");

  
//序列化user为xml文档

Document doc = new Document(user.getXML());

//输出到屏幕

user.format(System.out, doc);

//输出到XML文件user.xml

user.format(new BufferedOutputStream(new FileOutputStream(

"user.xml")), doc);

  
//反序列化XML文件为XiaoneiUser对象

Document doc2 = new Builder().build("user.xml");

Element element = doc2.getRootElement();

XiaoneiUser user2 = new XiaoneiUser(element);

//输出对象信息，验证对象

System.out.println(user2.getUserEmail());

System.out.println(user2.getUserPassword());

}

}

代码非常简单，如果要进行简单的对象序列化，我觉得这个400kb的类库非常实用

