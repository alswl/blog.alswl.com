Title: java.net.*操作session/GET/POST方法
Author: alswl
Slug: java-net-operation-session-get-post-method
Date: 2009-06-09 00:00:00
Tags: Java, JavaSE, Lib, 网络编程
Category: Coding

终于又考完一门试，开始做课程设计了，结果课程设计给工作室一个尾气3个月的项目，而这次的先用我写的贴吧放上去，我变得暂时空闲了，开始着手写校内开心农场小工具-
全能拖拉机。 首先要解决的就是校内登录的问题，那就是Get/Post方法了，还有用户状态保存，就是session的操作。Java不同于C#，那位可以集成系统
的浏览器或者之间创建一个Browser。

开始写了自己的第一个版本。

    
    import java.io.BufferedReader;
    import java.io.IOException;
    import java.io.InputStreamReader;
    import java.net.MalformedURLException;
    import java.net.ProtocolException;
    import java.net.URL;
    import java.net.HttpURLConnection;

public class FarmerHelper {

/**

* @param args  
* @throws ProtocolException  
*/  
public static void main(String[] args) throws ProtocolException {

String loginUrlStr = "http://login.xiaonei.com/Login.do";

String homeUrlStr = "http://home.xiaonei.com/Home.do";

URL loginUrl = null;

URL homeUrl = null;

HttpURLConnection loginConn = null;

HttpURLConnection homeConn = null;

try {

loginUrl = new URL(loginUrlStr);

homeUrl = new URL(homeUrlStr);

try {

loginConn = (HttpURLConnection) loginUrl.openConnection();

homeConn = (HttpURLConnection) homeUrl.openConnection();

} catch (IOException e) {

print("Conn't open the url connection!");

e.printStackTrace();

}

} catch (MalformedURLException e) {

print("Illegal URL!");

e.printStackTrace();

return;

}

loginConn.setRequestMethod("POST");

loginConn.setRequestProperty("User-Agent",

"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.0.10)"

+ " Gecko/2009042316 Firefox/3.0.10");

loginConn.setRequestProperty("Keep-Alive", "300");

loginConn.setRequestProperty("Connection", "keep-alive");

loginConn.setRequestProperty("email", "alswlwangzi@163.com");

loginConn.setRequestProperty("password", "xh77Gffb_i");

loginConn.setRequestProperty("submit", "登录");

loginConn.setRequestProperty("Keep-Alive", "300");

try {

loginConn.connect();

String headerName = null;

String cookie = "";

/*

* for (int i=0; (headerName =  
* loginConn.getHeaderFieldKey(i))!=null; i++) { if  
* (headerName.equals("Set-Cookie")) { cookie =  
* loginConn.getHeaderField(i); print(cookie); } }  
*/  
cookie = loginConn.getHeaderField("Set-Cookie");

print(cookie);

homeConn.setRequestProperty("Cookie", cookie);

homeConn.setRequestMethod("GET");

homeConn.connect();

BufferedReader in = new BufferedReader(new InputStreamReader(

homeConn.getInputStream()));

String lineStr = null;

while ((lineStr = in.readLine()) != null) {

// print(lineStr);

print(new String(lineStr.getBytes("GBK"), "UTF-8"));

}

} catch (IOException e) {

print("conn't connect to the server!");

e.printStackTrace();

}

}

private static void print(Object o) {

System.out.println(o);

}

}

想法总是好的，现实总是残酷的，调试很久，用WireShark抓包，都是有Length
Required错误，这个比较头疼，我感觉是我session传递的问题（其实不是，后来发现是Post的格式问题），于是网上找来一个Session操作类。

[猛击这里下载cookiemanager](https://ohsolnxaa.qnssl.com/upload_dropbox/200906/cookiemanager.java) 同时你可以参考这个类作者的文章
[猛击这里打开HOW-TO: Handling cookies using the java.net.* API](http://www.hccp.org/java-net-cookie-how-to.html)，谢谢这位外国朋友的帮助。 可惜尽管有这个外国朋友帮助，我写了第二个版本，仍然遇到了相同问题，Length
Required... 崩溃了，开始查找网络编程书，同时参考WireShark的抓包，我惊讶的发现，我把数据域写到了Headers里面去了。
这个致命性的错误导致服务器不能找到正确的数据，并且没有提供数据域的大小Content-Length，所以导致服务器报错。
最后再借花献佛，送上一个完整操作Http GET/POST的类[猛击这里下载httprequestproxy](https://ohsolnxaa.qnssl.com/upload_dropbox/200906/httprequestproxy.java)依然感谢原作者，

[猛击这里打开原文链接](http://benlsoft.javaeye.com/blog/97059)友情提示一下，这个类是07年写的，里面有一些注释说明在1.4和1.5下几个参数不一样，我没有亲测，建议使用1.5
的设置 嗯，有这两个类，明天工作应该会轻松一些，继续fighting!

