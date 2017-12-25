Title: CakePHP的全局变量
Author: alswl
Slug: cakephp-global-variables
Date: 2010-05-17 00:00:00
Tags: PHP, AzaAjaxChat, CakePHP
Category: Coding

毕业设计AzaAjaxChat 中有一个功能，记录当前在线用户，直观的看，用Application对象就可以解决。

忙了一会发现，原来PHP没有Application对象这个概念，于是我想到了全局变量，噩梦便开始了。（Application
和全局变量其实完全不是同一个概念）

我使用的框架是CakePHP，查找资料后，找到了几种CakePHP中使用全局变量的方法。

### 一、使用bootstrap.php文件

在app/config 下面，有一个bootstrap文件，从名字就可以看出，这个是在控制器之前加载的文件，根据官方的描述，有下面几个用法。

>   * 定义方便的函数

>   * 注册全局常量

>   * 定义新增的控制器，视图，控制器路径

通过这个文件可以实现全局变量的声明。

    
    if (!isset ($globalAAC)) {
    	global $globalAAC;
    	$globalAAC = array (
    		'currentMessageId' => -1,
    		'onlineUsers' => array()
    	);
    }

在其他文件中就可以调用这个全局变量了。

### 二、通过Configure 类

Configure类是CakePHP用来进行配置文件的地方，通过write() 和read()方法，也能实现全局变量的读写操作。

    
    Configure::write('Aac.currentMessageId', -1);
    Configure::read('Aac.currentMessageId');
    

其中，还有一个使用Configure的偏门方法，我从 [Need to share global variables throughout your app? » Debuggable Ltd](http://debuggable.com/posts/need-to-share-global-
variables-throughout-your-app:480f4dd5-6f64-4c88-812d-46d5cbdd56cb) 看到的。

    
    $config =& Configure::getInstance();
    $config->myVariable = 'Hello World';

$config =& Configure::getInstance();

debug($config->myVariable);

其实就是通过引用操作Configure 类内部的getInstance() 方法，看源码就能看出来。

### 三、关于类似Application 对象的全局变量

以上两种方法都没错，都可以操作全局变量，但是我却都操作失败了，为此我折腾了整整一天。

我甚至一度把错误归结到CakePHP，后来才发现，原来我冤枉它了。问题的根本是在于，这个全局变量根本不是我所想的那个Application 对象。

什么是Application 对象？Application 对象用于存储和访问来自任何页面的变量，类似于 session
对象。不同之处在于，所有的用户分享一个 Application 对象，而 session 对象和用户的关系是一一对应的。

在翻阅PHP资料之后，我终于在ChinaUNIX找到一些蛛丝马迹 [全局变量，在多个页面的可以使用吗？ - Php - ChinaUnix.net](http://bbs.chinaunix.net/viewthread.php?tid=79537)
。文中一位读者给了很肯定的回答"php中没有基于整个网站的全局变量，一般用数据库什么的替代方案。"。

我再检查一个基于PHP的聊天系统，果然是通过数据库的 online_users来实现在线用户的保存。

吃亏吃在用传统的Java思想做PHP，并且PHP接触时间太短，以后学习的时候必须多用用心了~

