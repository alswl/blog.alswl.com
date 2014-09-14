Title: 获取每日Bing图片
Author: alswl
Slug: get-daily-bing-picture
Date: 2010-07-19 00:00:00
Tags: Python, Bing
Category: Coding

在使用公司一个Redirect开发工具页面时候，想个性化一下，就想添加一个背景，最好每天能自动变化，我第一个想到的就是Bing。

放狗搜索，发现一篇文章 [抓取每天必应bing背景图片 - huangct的专栏 - CSDN博客](http://blog.csdn.net/huangc
t/archive/2009/10/27/4734844.aspx)，文中提供了抓取程式的Python代码，我摘录如下。

    
    import urllib
    import time
    def main():
        url = 'http://www.bing.com'
        f = urllib.urlopen(url)
        html = f.read()
        f.close()
        a = html[html.index('/fd/hpk2'):]
        data = a[:a.index('',id:')]
        url = data.replace('\', '')
        url = 'http://www.bing.com'+url
        name=time.strftime("%Y%m%d", time.localtime())
        name=name+".jpg"
        urllib.urlretrieve(url,name)

if __name__ == "__main__":

main()

关键的步骤是MS修改了jpg的url方式，用g_img={url:'/fd/hpk2/BambooBoat_ZH-
CN1057817945.jpg'这样的字符串躲避机器人的抓取。简单的替换即可完成。

我用C#重写了代码实现，如下所示。

    
    using System;
    using System.Collections.Generic;
    using System.Text;
    using System.Net;
    using System.IO;

namespace com.dddspace.GetBingImg

{ #region 获取Bing图片

class GetBingImg

{

static void Main(string[] args)

{

try

{

string html = GetHtml("http://www.bing.com");

html = html.Substring(html.IndexOf(@"/fd/hpk2/"));

html = html.Substring(0, html.IndexOf(".jpg") + 4);

html = html.Replace("\", "");

string url = "http://www.bing.com" + html;

Console.WriteLine(url);

}

catch (Exception e)

{

Console.WriteLine(e.ToString());

}

}

public static string GetBingImg()

{

string html = GetHtml("http://www.bing.com");

html = html.Substring(html.IndexOf(@"/fd/hpk2/"));

html = html.Substring(0, html.IndexOf(".jpg") + 4);

html = html.Replace("\", "");

return "http://www.bing.com" + html;

}

/// <summary>

/// 获得页面的html代码

/// </summary>

/// <param name="url">页面地址</param>

protected static string GetHtml(string url)

{

string html = "";

HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);

request.Accept = "*/*";

HttpWebResponse response = null;

Stream stream = null;

StreamReader reader = null;

try

{

response = (HttpWebResponse)request.GetResponse();

stream = response.GetResponseStream();

reader = new StreamReader(stream, Encoding.UTF8);

html = reader.ReadToEnd().Replace("rn", ""); //我知道这里会改变html代码，但和这里没关系

}/*

catch (Exception excpt)

{

Console.WriteLine(excpt);

Console.Write("n【注意】出现异常，输入任意字符和回车继续：");

Console.ReadLine();

}*/

finally

{

if (reader != null)

{

reader.Close();

reader.Dispose();

}

if (stream != null)

{

stream.Close();

stream.Dispose();

}

if (response != null)

{

response.Close();

}

}

return html;

}

}

#endregion

}

没多大的技术含量，就是用来把玩把玩。

在.aspx中加一个Panel，然后使用`this.Panel1.BackImageUrl =
BingImg.GetBingImg();`设置一下背景图片就万事OK了。现在，一个死板的小工具就稍微变得丰富多彩一些，是不是会让你工作的情绪略微提高呢~

附上今天的Bing图片

[![](http://cn.bing.com/fd/hpk2/Finca_ZH-
CN2784763289.jpg)](http://cn.bing.com/fd/hpk2/Finca_ZH-CN2784763289.jpg)

