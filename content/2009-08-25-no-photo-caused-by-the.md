Title: 由No photo引起
Author: alswl
Slug: no-photo-caused-by-the
Date: 2009-08-25 00:00:00
Tags: ASP.net
Category: Microsoft .Net
Summary: 

[![](http://www.chinaqiugou.com/images/detail_no_pic.gif)](http://www.chinaqiu
gou.com/images/detail_no_pic.gif)

某个系统，检查用户照片，如果发现用户并没有设定照片就返回一张No Photo的图片。

返回数据库的图片代码比较格式化。

    
    
    int Id = Int32.Parse(Request.Params.Get("Id"));
    string type = Request.Params.Get("type");
    BLL.Student bll = new JznuManager.BLL.Student();
    student = new JznuManager.Model.Student();
    student = bll.GetModel(Id);
    Response.ContentType = "image/jpeg";
    Response.Cache.SetCacheability(HttpCacheability.Public);
    Response.BufferOutput = false;
    //输出图片文件二进制数据
    Response.OutputStream.Write(student.entryPhoto, 0, (int)student.entryPhoto.Length);
    Response.End();

而如果返回的图片为空时候，就需要填充原先的图片Img。

1.我起初设置了Img的默认背景background，当没有图片出来时候，就可以显示出原先背景，但很快发现这个办法的弊病，如果数据库图片过小则会导致背景图片
露出来。

2.我考虑在GetPhoto.aspx这个方法内写入判断，在catch中读取一个本地图片文件，再转化为BitMap，再设置content-
type，用Response.OutputStream输出~~~

3.上面这个方法调试了很久，老是参数错误，最后我突然想起来一个方法。

    
    
    Response.Redirect("./Images/nophot.gif");

这几句话就能解决上述所有问题。

呃，有时候花费了好久，饶了很多弯的问题，其实好好想想反而会很简单。

