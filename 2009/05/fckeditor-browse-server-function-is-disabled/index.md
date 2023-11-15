

FCKeditor应该是功能最强大的网页编辑器了，提供js版本和java版本，而且功能特别丰富。

![image](https://e25ba8-log4d-c.dijingchao.com/images/upload_dropbox/200905/logotop.gif)

[猛击这里打开](http://www.fckeditor.net/)FCKeditor的主页

正是因为功能太丰富，所以往往带来安全原因，用这个可以随意上传图片和文件，还能浏览服务器？！

不行不行，这一定得禁用，否则就是给脚本小子提供工具了嘛。

配置fckconfig.js 118行左右，修改Basic模板，加入图片和表情功能

    
    
    FCKConfig.ToolbarSets["Basic"] = [
    ['Bold','Italic','-','OrderedList','UnorderedList','-','Link','Unlink','-','Image','Smiley']
    ] ;
    

继续修改tckconfig.js 284左右，去除一些浏览功能，修改为false

    
    FCKConfig.LinkBrowser = false ;//关闭增加连接中浏览服务器功能
    FCKConfig.LinkBrowserURL = FCKConfig.BasePath + 'filemanager/browser/default/browser.html?Connector=' + encodeURIComponent( FCKConfig.BasePath + 'filemanager/connectors/' + _FileBrowserLanguage + '/connector.' + _FileBrowserExtension ) ;
    FCKConfig.LinkBrowserWindowWidth    = FCKConfig.ScreenWidth * 0.7 ;        // 70%
    FCKConfig.LinkBrowserWindowHeight    = FCKConfig.ScreenHeight * 0.7 ;    // 70%
    FCKConfig.ImageBrowser = false ;//关闭增加图片中浏览服务器功能
    FCKConfig.ImageBrowserURL = FCKConfig.BasePath + 'filemanager/browser/default/browser.html?Type=Image&amp;Connector=' + encodeURIComponent( FCKConfig.BasePath + 'filemanager/connectors/' + _FileBrowserLanguage + '/connector.' + _FileBrowserExtension ) ;
    FCKConfig.ImageBrowserWindowWidth  = FCKConfig.ScreenWidth * 0.7 ;    // 70% ;
    FCKConfig.ImageBrowserWindowHeight = FCKConfig.ScreenHeight * 0.7 ;    // 70% ;
    FCKConfig.FlashBrowser = false ;
    FCKConfig.FlashBrowserURL = FCKConfig.BasePath + 'filemanager/browser/default/browser.html?Type=Flash&amp;Connector=' + encodeURIComponent( FCKConfig.BasePath + 'filemanager/connectors/' + _FileBrowserLanguage + '/connector.' + _FileBrowserExtension ) ;
    FCKConfig.FlashBrowserWindowWidth  = FCKConfig.ScreenWidth * 0.7 ;    //70% ;
    FCKConfig.FlashBrowserWindowHeight = FCKConfig.ScreenHeight * 0.7 ;    //70% ;
    FCKConfig.LinkUpload = false ;
    FCKConfig.LinkUploadURL = FCKConfig.BasePath + 'filemanager/connectors/' + _QuickUploadLanguage + '/upload.' + _QuickUploadExtension ;
    FCKConfig.LinkUploadAllowedExtensions    = ".(7z|aiff|asf|avi|bmp|csv|doc|fla|flv|gif|gz|gzip|jpeg|jpg|mid|mov|mp3|mp4|mpc|mpeg|mpg|ods|odt|pdf|png|ppt|pxd|qt|ram|rar|rm|rmi|rmvb|rtf|sdc|sitd|swf|sxc|sxw|tar|tgz|tif|tiff|txt|vsd|wav|wma|wmv|xls|xml|zip)$" ;            // empty for all
    FCKConfig.LinkUploadDeniedExtensions    = "" ;    // empty for no one
    FCKConfig.ImageUpload = false ;
    FCKConfig.ImageUploadURL = FCKConfig.BasePath + 'filemanager/connectors/' + _QuickUploadLanguage + '/upload.' + _QuickUploadExtension + '?Type=Image' ;
    FCKConfig.ImageUploadAllowedExtensions    = ".(jpg|gif|jpeg|png|bmp)$" ;        // empty for all
    FCKConfig.ImageUploadDeniedExtensions    = "" ;                            // empty for no one
    FCKConfig.FlashUpload = false ;
    FCKConfig.FlashUploadURL = FCKConfig.BasePath + 'filemanager/connectors/' + _QuickUploadLanguage + '/upload.' + _QuickUploadExtension + '?Type=Flash' ;
    FCKConfig.FlashUploadAllowedExtensions    = ".(swf|flv)$" ;        // empty for all
    FCKConfig.FlashUploadDeniedExtensions    = "" ;                    // empty for no one

OK，世界清净了


