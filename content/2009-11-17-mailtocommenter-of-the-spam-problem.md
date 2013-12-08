Title: MailToCommenter的垃圾邮件问题
Author: alswl
Slug: mailtocommenter-of-the-spam-problem
Date: 2009-11-17 00:00:00
Tags: WordPress
Category: 建站心得

Mail To Commenter发出的邮件会被GMail判定为垃圾邮件，这个问题我曾经发现，不过没有重视起来。鸵鸟理论告诉我说也许只有自己的GMail这样
，别人都是完好的，直到[derek](http://www.derekblog.cn/)同学提出来。

于是乎我开始修改，经过十余次的发送垃圾邮件，我反复查看邮件源码，检查`Mail To
Commenter的`mailtocommenter_send_email`函数，终于修改如下代码。`

`代码部分分别参考`[修改 mail to commenter,让邮件通知更加友好 |&nbsp_place_holder; Simple
happiness](http://xfuxing.com/2009/modify-the-mail-to-commenter-so-that-more-
user-friendly-e-mail-notification.html)和[邪罗刹的菠萝阁 »
如何修改MailToCommenter插件的发件人](http://www.evlos.org/2009/11/03/edit-the-poster-of-
mailtocomments/#comment-1278)，html部分代码是模仿[邪 罗刹](http://www.evlos.org/)的回复修改。

修改`wp-content/plugins/mailtocommenter`下面的`mailtocommenter_functions.php`

    
    
    function mailtocommenter_send_email($to,$subject,$message){
    	$hostname = get_option('home');
    	preg_match("/^(http://)?([^/]+)/i",$hostname, $matches);
    	$blogname = get_option('blogname');
    	$blognameO = $blogname;
    	$blogname .= " <no-reply@";
    	$blogname .= $matches[2];
    	$blogname .= ">";

$charset = get_option('blog_charset');

$headers = "From: $blognameO <no-reply@$matches[2]> n" ;

$headers .= "MIME-Version: 1.0n";

$headers .= "Content-Type: text/html;charset="$charset"n";

$to = strtolower($to);

return @wp_mail($to, $subject, $message, $headers);

}

&nbsp_place_holder;修改Mail To Commenter的邮件代码，我的如下

    
    
    <div style="border: 1px solid rgb(183, 183, 183); margin: 1em 40px; padding: 0pt 15px; background-color: #CCFFFF; color: rgb(17, 17, 17);">
      <p>Hi！<strong>%user%</strong>，你在 <strong>%post_title%</strong> 上的评论有了新回复</p>
    </div>
    <div style="border: 1px solid rgb(183, 183, 183); margin: 1em 40px; padding: 0pt 15px; background-color: #CCFFFF; color: rgb(17, 17, 17);">
      <p>>><strong>你</strong> 说：<br/>
        %your_comment%
      <p>>> <strong>%comment_author%</strong> 回复说： <br/>
        %reply_comment%
      <p>>> 查看原文，请至： <a href="%comment_link%" target="_blank">%comment_link%</a></p>
      <p style="float: right;"> ---- From <a target="_blank" href="%blog_link%/"><strong>%blog_name%</strong></a></p>
    </div>
    

&nbsp_place_holder;收到邮件的效果如下

> Hi！**alswlx**，你在 **紧急声明-关于回复通知是垃圾邮件** 上的评论有了新回复

>

> >>**你** 说：

测试GMail是否通过

>

> >> **alswl** 回复说：

@alswlx

第7次测试成功，修改内容

>

> >> 查看原文，请至： [http://log4d.com/2009/11/emergency-declaration-on-the-reply-
notification-is-spam#comment-6766](http://log4d.com/2009/11/emergency-
declaration-on-the-reply-notification-is-spam#comment-6766)

>

> ---- From [**DDD的一亩三分地**](http://log4d.com/)

