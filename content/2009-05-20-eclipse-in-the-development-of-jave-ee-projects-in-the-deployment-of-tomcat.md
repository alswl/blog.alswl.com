Title: Eclipse中开发的Jave EE项目在Tomcat的部署
Author: alswl
Slug: eclipse-in-the-development-of-jave-ee-projects-in-the-deployment-of-tomcat
Date: 2009-05-20 00:00:00
Tags: Tomcat, 编码
Category: Java编程和Java企业应用
Summary: 

贴吧最基本的功能写完了，正好可以应付数据库设计课的实验。于是我准备把贴吧的项目从Eclipse的开发环境中移植出来，在Tomcat中进行部署。

也许是习惯了Eclipse提供的便利，这个小小的移植，居然难倒了我，直接把Eclipse里的PostBar考出，根本不能运行，直接报404错误。Google
上也没有提供详细的步骤，也许大家都觉得这个问题很简单吧，呵呵。

我琢磨了一会，终于整理出了头绪。

1.修改Apache-conf-server.xml这个文件，修改其中一段<Host>...</Host>如下所示

    
    
    <host appbase="webapps" name="localhost"
        unpackWARs="true" autoDeploy="true"
        xmlValidation="false" xmlNamespaceAware="false">
    	<context debug="0" docbase="F:T3" path="/postbar">
    		  reloadable="true" crossContext="true">
    	</context>
    </host>

这一段的作用是在原先webapps的目录下添加虚拟目录/postbar，并且指定实际目录是"F:T3"

2.打开目录listtings功能，这样能帮助调试，正式发布可以关闭。 在Apache-conf-web.xml中找到

    
    
    <init-param>
    	<param-name>listings</param-name>
    	<param-value>false</param-value>
    </init-param>

把其中的false改为true就可以了。

3.打包Java EE项目。其实与其我们花时间考虑classes的位置，tld文件位置等繁琐的问题，可以直接使用Eclipse的输出功能，具体是项目右键-
Export 然后选择WAR file，就可以输出一个打包的项目文件。

4.在Tomcat的index.jsp里有stauts，输入管理密码后，可以进入一个状态页面，这里提供上传WAR文件并配置，可以这么做，但是其实可以直接用W
inRAR解压缩WAR文件，然后复制到之前设置的目录中。

这样，就可以再Tomcat使用项目，而不用考虑太多的部署问题了。 当然，我更建议初学者好好研究一下Java EE项目的部署要求，而不是简单的会用。
我也该认真看看孙鑫大大的Java EE前面的基础章节了...

本以为这样就可以使用项目，结果半路杀出一个程咬金，表单提交的中文都是乱码。

又遇到乱码问题了，呵呵，幸好不是初哥，我用Log4j调试一下，查看Tomcat/logs/，检查下面相应的txt文件，发现Action读取时候就出现了乱码，
数据库也是乱码，说明乱码产生原因在服务器端获取数据时候，我Google一下，发现Connector可以设置编码集，具体设置是Tomcat/conf/serv
er.xml

    
    
    <Connector port="8080" protocol="HTTP/1.1" connectionTimeout="20000"/>

将其修改为

    
    
    <Connector port="8080" protocol="HTTP/1.1"  connectionTimeout="20000" redirectPort="8443" URIEncoding="utf-8" />

重新测试表单数据发送，一切没有问题了。 细节决定一切啊.

