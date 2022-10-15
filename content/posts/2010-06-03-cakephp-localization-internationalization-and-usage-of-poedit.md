---
title: "Cakephp的国际化和poEdit的使用"
author: "alswl"
slug: "cakephp-localization-internationalization-and-usage-of-poedit"
date: "2010-06-03T00:00:00+08:00"
tags: ["php", "cakephp", "poedit"]
categories: ["coding"]
---

原文出处：[在Cakephp中使用i18n本地化程序，并使用poedit编辑语言文件 | 程序如此灵动！](http://newsn.net/20090525/472.html)

alswl:
官方的帮助手册都没有这篇文章来的详细，太赞了。这篇文章不仅介绍了CakePHP的使用，更多的介绍了PoEdit的使用，图文并茂，着实详细，感谢原作者苏南。

----- 以下为原文 -----

Cakephp的很强大的i18n功能就是用来实现本地化和国际化的。他通过使用语言配置文件使得程序能够很好的适应变化进行本地化。通过新建locale/chi/
LC_MESSAGES/default.po文件，并指定语言选项为"chi"实现。本文中说的就是如何实现这个本地化过程，当然本文中的poedit并不是必须的
，但是他可以使得工作效率更高。

## 一、关于i18n和L10n

这2个东东其实头一次我看到的时候也是一头雾水，但是经过百度的一通搜索，得出的结论就是，不管是几个n，最终的目的就是实现程序本地化就好了，说白了，就是由很多的
语言配置文件，反正我是这么理解的。大家也可以去看看，[http://baike.baidu.com/view/372835.htm](http://baik e.baidu.com/view/372835.htm) 这里有很详细的说明。

## 二、在Cakephp里面，实现本地化的方法

目前为止，有2种配置方法。

### 2.1 方法一

在config/core.php中使用configure::write来制定语言文件。

Configure::write('Config.language',"chi");

### 2.2 方法二

官方说明：[http://book.cakephp.org/view/162/Localizing-Your- Application](http://book.cakephp.org/view/162/Localizing-Your-Application)

貌似很复杂的说哦。

    
    App::import('Core', 'l10n');
    class TestsController extends AppController{
      $name="Tests";
      function test_function(){
        $this->L10n->new L10n();
        $this->L10n->get("chi");
        .....
      }
    }

### 2.3 做上边设置改动后需要做的：

当然在上面做修改后，还需要修改对应的ctp文件等哦，

所有的直接输出字符串，没有返回值的地方像这样：

`__(``"english"``);`

间接输出字符串，有返回的地方：

`__(``"english"``,``true``);`

还有input要加个label来使他出现中文。

__("english");echo $form->input('name',array('label'=>__('name',true)));

### 2.4 最最重要的一步

就是要编辑这个文件了，locale/chi/LC_MESSAGES/default.po。中间的chi就是语言文件的标志位了。这个文件的格式也很简单，

msgid "Chinese"

msgstr "中国话"

这个的简单重复就行了。

## 三、使用poedit

使用poedit不是必须的，但是可以使工作变得简单的多。官方网站是：[http://www.poedit.net/](http://www.poedit.n et/)

他的主要功用就是使得编辑语言配置文件更加方便和快捷。下面是使用poedit的一些简单的截图和说明。

### 3.1 头一次使用需要选择界面语言

![poedit_01](https://4ocf5n.dijingchao.com/upload_dropbox/201006/poedit-01.png)

![poedit_02](https://4ocf5n.dijingchao.com/upload_dropbox/201006/poedit-02.png)

![poedit_03](https://4ocf5n.dijingchao.com/upload_dropbox/201006/poedit-03.png)

### 3.2 新建一个配置文件，就是我们的目的文件po文件了

![poedit_04](https://4ocf5n.dijingchao.com/upload_dropbox/201006/poedit-04.png)

![poedit_05](https://4ocf5n.dijingchao.com/upload_dropbox/201006/poedit-05.png)

工程信息这里当然要选择好utf8格式了

![poedit_06](https://4ocf5n.dijingchao.com/upload_dropbox/201006/poedit-06.png)

路径这里的基本路径填写cakephp的目录，当然这里居然没有浏览功能，真是崩溃。

注意这里要通过下面的新建按钮新建一个名为"."的路径，这样的话，以后就可以搜索基本路径下面的子目录了。

![poedit_07](https://4ocf5n.dijingchao.com/upload_dropbox/201006/poedit-07.png)

关键字选项卡里面要填上cakephp的标志性本地化函数"__"。

![poedit_08](https://4ocf5n.dijingchao.com/upload_dropbox/201006/poedit-08.png)

当然上面那些选项卡设置好之后，还可以通过菜单类目=》设置调出来，从新设置。

### 3.3 点击那个小地球图标或者类目=》自源更新，开始自动扫描该翻译的文字了

![poedit_09](https://4ocf5n.dijingchao.com/upload_dropbox/201006/poedit-09.png)

![poedit_10](https://4ocf5n.dijingchao.com/upload_dropbox/201006/poedit-10.png)

![poedit_11](https://4ocf5n.dijingchao.com/upload_dropbox/201006/poedit-11.png)

### 3.4 但是这个时候，你可能会发现扫描出来的字段远远少于你需要的东东，原来这个软件不认识ctp文件。这个步骤的设置是让他能识别ctp文件设置。文件=
》首选=》解析器。

**本步骤参考了一个意大利程序员的博客文章，在此向他表示感谢先。**

[http://www.luizz.it/119/cakephp/poedit-e-i-file-
ctp](http://www.luizz.it/119/cakephp/poedit-e-i-file-ctp)

![poedit_12](https://4ocf5n.dijingchao.com/upload_dropbox/201006/poedit-12.png)

![poedit_13](https://4ocf5n.dijingchao.com/upload_dropbox/201006/poedit-13.png)

选中php，选择编辑，然后在第2行内输入ctp文件后缀，如下图，但是注意下图的设置是错误的!虽然上面的提示，是用逗号分隔，但是实践证明，用分号才是正确的选择
。这个很令人崩溃，大概是poedit的一个小bug吧。会出现错误提示。

![poedit_14](https://4ocf5n.dijingchao.com/upload_dropbox/201006/poedit-14.png)

![poedit_14.5](https://4ocf5n.dijingchao.com/upload_dropbox/201006/poedit-145.png)

但是如果用分号分隔的话，仍然会看到如下错误提示。

![poedit_15](https://4ocf5n.dijingchao.com/upload_dropbox/201006/poedit-15.png) 需要在下面的解析器命令下面增加个选项-language=php，注意这里是两个中划线啊。所以这个步骤的要点就是下图所示了。

![poedit_16](https://4ocf5n.dijingchao.com/upload_dropbox/201006/poedit-16.png)

### 3.5 这里通过那个地球图标就可以找出所有需要翻译的字段了，当然这个操作的前提是你已经用__函数把所有的字段都标示好了。如果你按这个图标之前进行了部
分翻译，这个操作如果发现了新字句，这个软件会根据以前的翻译自己翻译字句的，并用棕色突出显示它自动翻译的词语。当然，一般都是不准确的。所以还是需要进行修改保存
操作的说。

![poedit_17](https://4ocf5n.dijingchao.com/upload_dropbox/201006/poedit-17.png)

### 3.6 如果这个时候你查看生成的po文件的时候，比自己手写的文件确实多些设置。

![poedit_18](https://4ocf5n.dijingchao.com/upload_dropbox/201006/poedit-18.png)

