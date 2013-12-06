Title: 在Eclipse中使用Maven
Author: alswl
Slug: maven-eclipse
Date: 2011-03-18 00:00:00
Tags: Eclipse, Maven
Category: Java编程和Java企业应用
Summary: 

一提到Eclipse中使用Maven，都会想到[m2eclipse](http://m2eclipse.codehaus.org/)这个插件。其实在Ecli
pse下使用Maven不用插件也能完成，我们只需要使用bin/mvn下面的mvn即可。

## 3分钟Maven

Maven官方提供了[Getting Started in 5 Minutes](http://maven.apache.org/guides
/getting-started/maven-in-five-minutes.html)和[Getting Started in 30
Minutes](http://maven.apache.org/guides/getting-
started/index.html)两种教程，我这里再简化一下，记录一下常用命令。

    
    #建立一个空项目，包含一个HelloWorld，可以通过
    #-DarchetypeGroupId=<archetype-groupId> -DarchetypeArtifactId=<archetype-artifactId>
    #命令创建更多类型项目
    mvn archetype:create -DgroupId=com.dddspace.java -DartifactId=helloworld

#编译打包到jar或者war，根据pom中定义

maven package

#jUnit跑跑

mvn test

#神奇的命令，帮助创建Eclipse项目，配置path，默认使用M2_REPO这个变量作为目录

mvn eclipse:eclipse

大约跑完花费3分钟~嗯，有这几个命令，Maven简单操作就OK了，更多的话，去Maven文档溜溜吧。

PS：为了防止Maven编码错误，建议在bin/mvn里面加入一句话`set MAVEN_OPTS=-Dfile.encoding=UTF-8`
这样强制Maven使用UTF-8进行编码。

## 配置Eclipse环境

### 加入M2_REPO

进入Eclipse->preferences->java->build path->classpath
variables，添加M2_REPO这个变量，指向C:/Documents and Settings/userName/.m2/repository，这个
路径是默认的Maven仓库，如果你想搬到其他地方，需要修改mavenconfsetting.xml里面的localRepository。

### 配置String Substitution

通过配置String
Subsitution我们就可以使用Eclipse的lanuch来启动Maven，而不是Eclipse插件启动。首先我们要告诉Eclipse
Maven在哪里。配置Eclipse->preferences->Run/Debug->String Subsitution，加入mvn
=&nbsp_place_holder;D:/dotj_dev/tools/apache-maven-2.2.1/bin/mvn.bat。

### 建立Launch文件

Launch其实是Eclipse的Launcher框架的配置文件，可以定义Application的启动方式。新建一个mvn-war.launch如下：

    
    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <launchConfiguration type="org.eclipse.ui.externaltools.ProgramLaunchConfigurationType">
    <stringAttribute key="bad_container_name" value="helloworldmvn-war.launch"/>
    <stringAttribute key="org.eclipse.ui.externaltools.ATTR_LOCATION" value="${mvn}"/>
    <stringAttribute key="org.eclipse.ui.externaltools.ATTR_TOOL_ARGUMENTS" value="clean compile war:war -U"/>
    <stringAttribute key="org.eclipse.ui.externaltools.ATTR_WORKING_DIRECTORY" value="${workspace_loc:/helloworld}"/>
    </launchConfiguration>
    

Update（2011/03/21）：后来测试发现`bad_container_name`没有也可以正常运行；`${workspace_loc:/hello
world}`修改为`${project_loc}`更为方便。

这个.launch文件内容其实是XML格式的，里面定义了几个属性，用来告诉Eclipse执行什么命令，重要的属性是ATTR_LOCATION和ATTR_TO
OL_ARGUMENTS，我们分别赋值为${mvn}和Maven参数，就可以正确执行了。

类似的，我们可以建立mvn eclipse:eclipse的Launch文件，用来生成Eclipse类型的项目。

PS：使用Substitution的目的其实是为了避免不同开发环境下面Maven位置不相同，保持.launch文件统一。

