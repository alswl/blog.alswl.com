Title: MemberShip使用心得
Author: alswl
Slug: membership-the-use-of-experience
Date: 2009-11-05 00:00:00
Tags: dotNet, ASP.net, MemberShip
Category: Coding

花了很大一段时间在学习MemberShip，总是要留下一些纪念文章的。
我之前的日志提到过一个简单的用户权限设计：User+Role+UserInRole([http://log4d.com/2009/06/design-of-
user-rights](http://log4d.com/2009/06/design-of-user-
rights))，但是这样还是不够灵活，最好需要能够对每一个功能模块进行权限控制，而且需要符合开闭原则。 MemberShip呢，是微软推出的一套很强大的用
户权限管理系统。就我使用的两大部分，主要包括MemberShip和roleManager这两个模块，分别是对用户和角色进行管理。

## MemberShip对系统进行管理大致分为两个办法

1.可以通过"登录"系列用户控件的任务窗口中的"管理网站"打开"ASP.Net Web 应用程序管理"。 可以控制用户、角色、权限三个主要属性，另外还能选择
"提供程序"（这个provider分为MemberShip和RoleManager两种，如果同名的话，可以选择同一提供程序）
![userControl](https://ohsolnxaa.qnssl.comm/2009/11/userControl.jpg)
![userManager](https://ohsolnxaa.qnssl.comm/2009/11/userManager.jpg)
2.使用Web.config进行配置
其实上面的可视化界面在配置提供程序和访问规则（权限设定）时候，本质上修改的是根目录web.config和各个文件夹下对应的web.config

我的根Web.config

    
    <authentication mode="Forms">
    	<forms name="ThisHouse" defaultUrl="Default.aspx" loginUrl="Signin.aspx" protection="All" timeout="30"/>
    </authentication>
    <membership defaultProvider="SqlProvider">
    	<providers>
    		<add connectionStringName="thisHouseConnectionString" enablePasswordRetrieval="false" enablePasswordReset="true" requiresQuestionAndAnswer="true" applicationName="ThisHouse" requiresUniqueEmail="false" passwordFormat="Clear" maxInvalidPasswordAttempts="255" minRequiredPasswordLength="1" minRequiredNonalphanumericCharacters="1" passwordAttemptWindow="10" passwordStrengthRegularExpression="" name="SqlProvider" type="System.Web.Security.SqlMembershipProvider"/>
    	</providers>
    </membership>
    <roleManager enabled="true" cacheRolesInCookie="true" defaultProvider="SqlProvider">
    		<providers>
    			<add connectionStringName="thisHouseConnectionString" applicationName="ThisHouse" name="SqlProvider" type="System.Web.Security.SqlRoleProvider"/>
    		</providers>
    </roleManager>

我禁止User角色进入Admin文件夹，配置完"访问规则"后，会在Admin文件夹下生成相应web.config

    
    <?xml version="1.0" encoding="utf-8"?>
    <configuration>
        <system.web>
            <authorization>
                <allow roles="User" />
                <allow roles="Admin" />
                <deny users="?" />
            </authorization>
        </system.web>
    </configuration>

这种单纯的安全机制是以文件为单位进行配置的，不能说完美，但是有效且简单，不失为一种不错的权限控制方法。毕竟这样可以脱离在代码中的配置，而只要关注配置文件。缺
点同样明显，如果想在同一个动作aspx文件中进行权限判断，就难以有效的实现，需要修改aspx代码了。

## MemberShip在.NET 3.5中方法的集成

这个标题有点大，实际上在我的课程设计中，用到了判断是否登录、判断用户角色这两个简单的方法。

    
    if (Page.User.Identity.IsAuthenticated)
    {
    	this.Login1.Visible = false;
    	this.LoginStatus1.Visible = true;
    	this.pEditProfile.Visible = true;
    }
    foreach (string role in Roles.GetRolesForUser())
    {
    	if (role == "Admin")
    	{
    		this.pAdmin.Visible = true;
    	}
    }

这段代码第一个if进行了是否登录的判断，然后foreach循环判断用户角色。 大部分方法在"System.Web.Security.Roles"、"Syst
em.Web.Security.Membership"中，可以在MSDN查到相关内容。

## 后话

MemberShip是一个很强大的框架，无论是使用还是学习，都是不错的对象。我这里只是一个星期使用的一点小心得，不是一个HowTo。 .NET既然提供了这么
好的东西，希望大家可以用起来，而不要简单的使用User+代码中判断User的某个权限字段，要把耦合的思想和设计模式的思想在实际中进行一些尝试。（好吧，我设计
模式其实基本不懂```会吹吹罢了）

