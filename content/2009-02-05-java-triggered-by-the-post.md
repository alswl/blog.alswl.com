Title: Java中的POST引发的...
Author: alswl
Slug: java-triggered-by-the-post
Date: 2009-02-05 00:00:00
Tags: Java, 网络编程
Category: Coding

因为一直想写一个刷人气的工具，其中最基本的就是post方法了，然后再收集页面中的元素。今天我就开始着手写Java的POST方法。

在Java.net.*;中用URL构造地址，然后用流写入，似乎应该是很简单的方案，我却一直没成功。我百度Google了很久，参考了很多别人代码，似乎很容易实
现，可是我的一直问题，而我觉得和网上提供的一样。我的代码如下

package netStudy01;

import java.io.*;

import java.net.*;

public class PostBaidu

{

public static void main(String[] args)

{

 try

 {

 URL url = new URL("[
http://localhost/xhpx_web/gradequery.asp](http://localhost/xhpx_web/gradequery
.asp)");

 try

 {


HttpURLConnection conn = (HttpURLConnection) url.openConnection();




HttpURLConnection.setFollowRedirects(false);


conn.setInstanceFollowRedirects(false);


conn.setRequestMethod("POST");


conn.setDoOutput(true);


conn.setDoInput(true);


conn.setRequestProperty("User-Agent",

&n
bsp_place_holder; "Mozilla/5.0 (compatible; MSIE 6.0;
Windows NT)");


conn.setRequestProperty("Content-Type",

&n
bsp_place_holder; "application/x-www-form-urlencoded");




OutputStreamWriter out = new
OutputStreamWriter(conn.getOutputStream(),"ASCII");


String request = "exam_id=123&submit=%CC%E1%BD%BB";


out.write(request);


out.flush();


out.close();




BufferedReader in = new BufferedReader(new
InputStreamReader(conn.getInputStream()));


String line;


StringBuffer content = new StringBuffer();


while ((line = in.readLine()) != null)

 {

&n
bsp_place_holder; content.append(line + "n");

 }


System.out.print(content);

 } catch (IOException
e)

 {


e.printStackTrace();

 }





 } catch (MalformedURLException e)

 {

 e.printStackTrace();

 }



}

}

很不幸，返回的数据一直还是这个提交页面，我尝试了好多方法，甚至用ethereal截取POST信息，用IE的POST信息和JVM的POST信息一一对比并增加信
息，包括"User-Agent","Mozilla/5.0 (compatible; MSIE 6.0; Windows NT)""Content-
Type", "application/x-www-form-urlencoded"都没有什么效果。

如果POST百度，甚至直接都运行时错误，我Java学的太少，完全不知道错误缘由。再加上本来java.net功能就很弱，我想使用Apache.commons
.html-client.*的包来完成，这样也能捕获到网页元素。

Goolge了一会才从Apache的项目列表中找到[http://hc.apache.org/downloads.cgi](http://hc.apache
.org/downloads.cgi)这个组件，呵呵，居然是校内网提供的镜像站点，看来校内的架构也用到了Apache的开源阿。

1.7M下完，配好ClassPath和项目jar，打开java文档，也就是API说明吧，铺天盖地的英文有点怕...呵呵，慢慢看吧，压缩包内还有几个小例子，可
以供参考。

网上详细的资料不多了，得研读好一会，继续学习，Lingoes开着，英语果然很重要阿````

想起以前在.NET平台下面做，轻松容易很多，不用自己辛苦的找组件，MS的实力摆在哪里，全都提供好了。

