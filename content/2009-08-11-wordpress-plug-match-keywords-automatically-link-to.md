Title: wordpress关键字自动链接匹配插件[转]
Author: alswl
Slug: wordpress-plug-match-keywords-automatically-link-to
Date: 2009-08-11 00:00:00
Tags: 建站心得, WordPress
Category: Coding

原文链接：《[wordpress关键字自动链接匹配插件 | 长沙SEO特色高端咨询顾问服务](http://www.changshaseo.com/seo-
tools/882.html)》[](http://www.changshaseo.com/seo-tools/882.html)

相关链接：《[wordpress插件 中文关键词自动连接 |
Muboard](http://muboard.com/591)》（这位博主曾为该插件0.3x版本做过中文优化）

中文版下载地址：[猛击这里下载](href="http://www.changshaseo.com/blog-mechanics-keyword-link-
plugin-v01.zip)

**wordpress关键字自动匹配链接插件** 这个工具非常好使，我找了很久了，以后发文章就省事多了，不用一个一个去加链接了，呵呵，So Cool！

下面引用原文：

Wordpress Keyword Link Plugin

This is a little Wordpress 2.3+ plugin that helps you to automatically link
defined keywords to certain articles on your own blog, or elsewhere on the
internet.

A plugin that allows you to define keyword/link pairs. The keywords are
automatically linked in each of your posts. This is usefull for improving the
internal cross referencing pages inside your site or to automatically link to
external partners (SEO).

Example:  「A visit to the UK is not complete without a visit to Stonehenge.」

Would become:  「A visit to the UK is not complete without a visit  to <A
href=」link」>Stonehenge</a>.」

You can decided for each link if you would like to:

  * Add a 「No Follow」
  * Match only on the first mention
  * Open a new window on clicking the link
  * Match any case (ignore case) in the keyword
It is possible to CSS style links:

  * If the link is an affiliate you would like to disclose
  * Any other link tagged by the plugin
To help maintain longer keyword lists it is also possible to import and export
lists of keywords to a comma seperated values (CSV) file, handy if you would
like to edit the list of keywords in a spreadsheet.  ** **

    
    **Features **

  * Optional: Only link the first instance of a keyword [default is all]
  * Optional: Open a new window for a link
  * Optional: Mark a link as 「nofollow」
  * Optional: Ignore case when matching [Rome,ROME,ROMe]
**Screenshot**

![image](http://www.dijksterhuis.org/wp-content/uploads/2008/09/keywordlink2.gif)

**Installation **

  1. Just [download the ZIP file](http://downloads.wordpress.org/plugin/blog-mechanics-keyword-link-plugin-v01.zip), and unpack it in the /wp-content/plugins directory.
  2. 中文版，点击这里下载  [DOWN](http://www.changshaseo.com/blog-mechanics-keyword-link-plugin-v01.zip) ，中文wrodpress 一定要,而且只能用这个，**改造兼容中文字符.**
  3. Activate the plugin
  4. Enter your keyword-link pairs in the option panel for the plug-in.
v0.6

  * It is now possible to use apostrophes in keywords (the boy’s hat)
  * You can import and export the keyword list to and from a comma seperated filed
v0.5

  * Fixed a 「space」 issue
  * Added basic help to the configuration page
  * Added support for affiliate links
v0.4.5

  * Added: A little bit of javascript to allow for editing of existing keywords as some of you  now have over 150 entries it will also jump to the editor at the bottom of the screen.
v0.4.2

  * Fixed: Compatibly problem with Ozh Click counter plugin
v0.4

  * Fixed the linking of matching url’s problem
  * It is now possible to open a new window for a link (target=_blank)
  * It is now possible to ignore case when matching a keyword
v0.3.1

It is now possible to specify per link if you would like to :

  * Link only the first mention of the keyword in the article (or all, which is the default)
  * Tag a link as 「nofollow」 , useful for external links.
The replacement routine is also smarter about linking keywords. For example:
「magic」 will match 「magic」 , but no longer to 「magically」.

**version 0.2**

If you would like to modify the style of the link. For example to make the
link bold add the following to your style.css file:

.bm_keywordlink { font-weight: bold; }

