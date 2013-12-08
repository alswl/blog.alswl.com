Title: 禁止WordPress自动替换半角标点符号【转】
Author: alswl
Slug: prohibition-of-wordpress-automatically-to-replace-the-half-angle-punctuation
Date: 2009-07-10 00:00:00
Tags: WordPress
Category: 建站心得

转载自「禁止WordPress自动替换半角标点符号 - 布语博客」<[点击这里打开](http://buyu.name/074.html)>

Wordpress虽好，可毛病也不少，今天发现WordPress会将半角标点符号自动转换成全角的，但并没有替换数据库里的信息，真搞不明白开发团队是怎么想的，
现将解决方法记录如下。

1、 编辑 wp-includes/formatting.php 文件，找到以下代码：

    
    
    // static strings
    $curl = str_replace($static_characters, $static_replacements, $curl);
    // regular expressions
    $curl = preg_replace($dynamic_characters, $dynamic_replacements, $curl);

正是 str_replace() 和 preg_replace() 两个函数在作怪。

2、 将相应语句注释，禁用自动替换功能：

    
    
    // static strings
    //$curl = str_replace($static_characters, $static_replacements, $curl);
    // regular expressions
    //$curl = preg_replace($dynamic_characters, $dynamic_replacements, $curl);

OK，以后Wordpress在也不会自作聪明的将半角标点符号转换成全角标点符号了。

