Title: OGNL中的操作符
Author: alswl
Slug: ognl-operators-in
Date: 2009-05-10 00:00:00
Tags: OGNL, Struts
Category: Java编程和Java企业应用
Summary: 

<s:textfield name="loginName" value="%{#request.loginNames}"/>

使用此表达式，会生成一个文本框，并且，如果request.attribute中有loginNames属性，将会做为些文本框的默认值。

如果只使用#request.loginNames在struts2的标签内部，是不会显示任何值的，注意外面加上的%{}附号，才会被正常的使用。

如果希望如EL语言一样直接输出文件，如在一个<a></a>之间的innerHTML文本为#request.loginNames的值，我们只要使用：<s:pr
operty value="#request.loginNames" />使可以正常使用！

注：

1.${}是EL语言的 %{}这样的形式是ognl表过式语言的，在struts2的标签内部，使用%{}这样的形式，在标签外部可以使用${}EL语言的方式。如
果在struts2的标签内部使用${}这样的方式，会出现以下的错误提示：

According to TLD or attribute directive in tag file, attribute value does not
accept any expressions

2.很多时候，我们使用struts2的一些标签，属性是需要接受集合的，如果集合是保存在request,session，或者是值栈(非根对象的栈顶)，可以使用
#变量名的方式，如果获取的值是在Action中通过特定的方法来获取，就需要使用如 value="userList"这样的方式，只是去掉了前面的#。

