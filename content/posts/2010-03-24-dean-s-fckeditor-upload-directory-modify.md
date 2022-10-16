---
title: "Dean's FCKEditor上传目录修改"
author: "alswl"
slug: "dean-s-fckeditor-upload-directory-modify"
date: "2010-03-24T00:00:00+08:00"
tags: ["建站心得", "ckeditor", "wordpress"]
categories: ["coding"]
---

一直喜欢WorePress默认的上传文件方法，通过`WP-content/uploads/年/月`分组。

网站改版时候果断的把[Dean's FCKEditor With pwwang's Code Plugin For Wordpress](http://wordpress.org/extend/plugins/deans-fckeditor-with-pwwangs-
code-plugin-for-wordpress/)换成了[Dean's FCKEditor For Wordpress](http://wordpress.org/extend/plugins/deans-fckeditor-for-wordpress- plugin/)，Dean's FCKEditor With pwwang's Code Plugin For
Wordpress是带一个代码编辑器的CKEditor插件，和WP-Syntax配合很好用，而Dean's FCKEditor For
Wordpress是常规的CKEditor。

PS:为神马要用两款插件呢，其实都是为了代码高亮，现在我发现Dean's FCKEditor For
Wordpress+[SyntaxHL](http://github.com/RichGuk/syntaxhl)才是王道啊～

这两款插件都会把文件上传到`/wp-
content/uploads/image`(file/flash子文件夹)。这点让我很不喜欢，我还是喜欢默认的WordPress上传路径。

修改`wp-contentpluginsfckeditor-for-wordpress-
pluginfilemanagerconnectorsphpconfig.php`如下。其实就是声明一个变量，然后替换掉文件路径。

    
    $Config['Enabled'] = $deans_fckeditor->can_upload();
    $dateMonth = date('Y/m/');
    $Config['UserFilesPath'] = $deans_fckeditor->user_files_url . $dateMonth;
    $Config['UserFilesAbsolutePath'] = $deans_fckeditor->user_files_absolute_path . $dateMonth;
    
    
    $Config['AllowedExtensions']['File']	= array('7z', 'aiff', 'asf', 'avi', 'bmp', 'csv', 'doc', 'fla', 'flv', 'gif', 'gz', 'gzip', 'jpeg', 'jpg', 'mid', 'mov', 'mp3', 'mp4', 'mpc', 'mpeg', 'mpg', 'ods', 'odt', 'pdf', 'png', 'ppt', 'pxd', 'qt', 'ram', 'rar', 'rm', 'rmi', 'rmvb', 'rtf', 'sdc', 'sitd', 'swf', 'sxc', 'sxw', 'tar', 'tgz', 'tif', 'tiff', 'txt', 'vsd', 'wav', 'wma', 'wmv', 'xls', 'xml', 'zip') ;
    $Config['DeniedExtensions']['File']		= array() ;
    $Config['FileTypesPath']['File']		= $Config['UserFilesPath']  ;
    $Config['FileTypesAbsolutePath']['File']= ($Config['UserFilesAbsolutePath'] == '') ? '' : $Config['UserFilesAbsolutePath'] ;
    $Config['QuickUploadPath']['File']		= $Config['UserFilesPath'] ;
    $Config['QuickUploadAbsolutePath']['File']= $Config['UserFilesAbsolutePath'] ;

呃，懒孩子们我就直接提供下载了。

config.php文件下载：[fckeditor-for-wordpress-plugin_config.zip](/images/upload_dropbox/201003/fckeditor-for-wordpress-plugin_config.zip)

看不懂的就算了～

