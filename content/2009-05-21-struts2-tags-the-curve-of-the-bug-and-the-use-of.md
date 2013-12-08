Title: Struts2的s:if标签的Bug和曲线使用
Author: alswl
Slug: struts2-tags-the-curve-of-the-bug-and-the-use-of
Date: 2009-05-21 00:00:00
Tags: Struts, 贴吧
Category: Java编程和Java企业应用

贴吧的用户状态显示，登录和未登录应该是不同的div显示，我决定用做标签。

本来应该很简单的事情，却没有我预想中的情形出现，检查后发现失效了，代码如下：

    
    
    <li>${session.userName}欢迎你</li>
    <li><a href="Logout.action">注销</a></li>
    

Struts2的官方文档中标签库介绍写的很清楚，官方示例文档如下

    
    <s:if test="%{false}">
    <div>Will Not Be Executed</div>
    </s:if>
    <s:elseif test="%{true}">
    <div>Will Be Executed</div>
    </s:elseif>
    <s:else>
    <div>Will Not Be Executed</div>
    </s:else>

我现在敢打包票，这个示例无法成功运行。

OGNL有三种取值方式，%,$和#，我之前已经转载过一篇小介绍，按官方文档，这里的$是应该起作用的，但是很可惜，这儿出现了错误。

网友阿木的博客讨论了相关问题：[struts2的if标签](http://blog.sina.com.cn/s/blog_5cecbc550100ck4f.
html)，我没有像他那样详细测试，尝试几次后，代码修改为：

    
    
    <li>${session.userName}欢迎你</li>
    <li><a href="Logout.action">注销</a></li>
    

使用#选择符，而不是其他的，这样就可以正确运行了。

