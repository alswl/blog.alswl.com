Title: Maven下Jetty启动
Author: alswl
Slug: run-jetty-in-maven
Date: 2011-04-04 00:00:00
Tags: Java, Eclipse, Jetty
Category: Coding

部门最近开发的产品使用的开发服务器是Jetty（挂载在GWT中），启动方法是通过Eclipse的External
Tool执行。我对此表示很好奇，特意在自己电脑下面组建了一个Jetty开发环境，发现Maven和Jetty合作起来非常愉快，现在小记之。

## 一、准备Maven配置文件

我使用Maven推荐的标准webapp结构，结构如下，官方文档可以参考[Maven - Introduction to the Standard Directory Layout](http://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)

src/main/java

Application/Library sources

src/main/resources

Application/Library resources

src/main/filters

Resource filter files

src/main/assembly

Assembly descriptors

src/main/config

Configuration files

src/main/webapp

Web application sources

src/test/java

Test sources

src/test/resources

Test resources

src/test/filters

Test resource filter files

src/site

Site

LICENSE.txt

Project's license

NOTICE.txt

Notices and attributions required by libraries that the project depends on

README.txt

Project's readme

使用的pom.xml主要添加了build-
plugins的Jetty插件，另外修改了outputDirectory，从而实现自动编译到`targert/projectName/WEB- INF/classes`目录，实现[Eclipse Hot Code](http://wiki.eclipse.org/FAQ_What_is_hot_code_replace%3F)。

    
    <build>
        <directory>${project.basedir}/target</directory>
        <finalName>${project.artifactId}-${project.version}</finalName>
        <outputDirectory>${project.build.directory}/${project.build.finalName}/WEB-INF/classes</outputDirectory>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-eclipse-plugin</artifactId>
                <version>2.7</version>
                <configuration>
                    <sourceIncludes>
                        <sourceInclude>*</sourceInclude>
                    </sourceIncludes>
                </configuration>
            </plugin>

<plugin>

<groupId>org.apache.maven.plugins</groupId>

<artifactId>maven-plugin-plugin</artifactId>

</plugin>

<plugin>

<groupId>org.apache.maven.plugins</groupId>

<artifactId>maven-compiler-plugin</artifactId>

<configuration>

<source>1.6</source>

<target>1.6</target>

</configuration>

</plugin>

<plugin>

<groupId>org.mortbay.jetty</groupId>

<artifactId>maven-jetty-plugin</artifactId>

</plugin>

</plugins>

</build>

准备几个测试用的Servlet，外加web.xml。运行`mvn
install`即可在target/war下面生成war包，同时在target/projectName/下会生成项目文件。

如果有m2eclipse，那这个动作很容易就可以完成，如果没有，也可以参照我之前的[在Eclipse中使用Maven](http://log4d.com/2011/03/maven-eclipse)。

## 二、撰写Eclipse External Tool

建立可以运行的Jetty实例分为两步，建立Jetty的Java Application和创建jetty.xml配置文件。

1、在Run-Run Configurations中的Java Application中建立一个新的应用，起名为"jetty",使用Main
class为`org.mortbay.xml.XmlConfiguration`，在Arguments - Program arguments中加入`${p
roject_loc}/jetty.xml`，其中`${project_loc}`是动态参数，指向当前项目目录，jetty.xml为我们随后要创建的jett
y配置文件。

[![image](https://ohsolnxaa.qnssl.com/upload_dropbox/201104/run_configurations .png)](https://ohsolnxaa.qnssl.com/upload_dropbox/201104/run_configurations .png)

如果想将这个应用保存成文件，可以修改Common - Sava
as到当前目录，就可以保存为jetty.launch文件了。（没错，就是launch文件，Eclipse的运行配置文件）

[![image](https://ohsolnxaa.qnssl.com/upload_dropbox/201104/eclipse_common.png)](https://ohsolnxaa.qnssl.com/upload_dropbox/201104/eclipse_common.png)

2、准备jetty.xml文件

Jetty是一款轻量形的Web服务器，轻到甚至仅仅靠Maven插件即可运行，不过我们依然需要通过jetty.xml文件进行配置。在项目根目录下建立jetty
.xml（此路径与Java Application中的Arguments相对应，有些朋友可能更习惯放在WEB-INF下面）。

官方说从$JETTY_HOME/webapps/test/WEB-INF/jetty-web.xml可以取到jetty-xml的范例，我这里就提供下载好了。

点击下载[jetty.xml ](https://ohsolnxaa.qnssl.com/upload_dropbox/201104/jetty.xml)，这里面写了hard
code`<Set
name="resourceBase">./target/study_web-1.0-SNAPSHOT</Set>`，请记得替换。

配置好Jetty之后，就可以运行Jetty了，在Run - Run
As中找到名为jetty的运行命令，不出意外的话，Jetty会在4000端口建立一个实例。

当我们在Debug模式运行时，由于我们修改java代码会动态更新到classes目录，所以我们可以在运行时修改代码，不信你可以在Debug时候修改Servl
et中代码试试，这就是所谓Hot code。

Enjoy it!

## 参考文章

[Eclipse中运行Jetty](http://www.daniel-journey.com/archives/214)

[天生一对"Maven2+Jetty" -- Maven2创建并管理WebApp，并使用Maven Jetty Plugin在Eclipse中调试](http://www.blogjava.net/alwayscy/archive/2007/05/19/118584.html)

[目前发现的最好最快的直接在ECLIPSE中JETTY调试方式](http://www.blogjava.net/alwayscy/archive/2007/09/13/144969.html)

