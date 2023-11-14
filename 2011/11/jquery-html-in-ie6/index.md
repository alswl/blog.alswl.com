

今天遇到一个jQuery的`.html()`设定错误问题，FF和Chrome下面都能够正常工作，而IE下面却失败。

检查之后，我把问题定性到jQuery.html(html)设定在IE下有问题。当设定html文本中含有空行、空格、Tab时候，会出现异常中断，导致`html
()`设定失败，但是又不会引发js错误。

狗日的IE！

下文是Google来的参考文章：[使用 jQuery .html() 得到的string时,
在IE中出现错误的解决方法](http://sixpoint.me/808/jquery-html-function-ie-error/)

* * *

使用 jQuery 的 .html() 函数( 使用 .text() 也类似 )得到元素内的值使用时，在IE6中出错，FireFox 中正常。

基本代码如下:

    
    <ul class="demo">
        <li>easeInQuad</li>
        <li>easeOutQuad</li>
        <li>easeInOutQuad</li>
    </ul>
    
    
    $('.demo li').each(function(){
        var action = $(this).html();
        $(this).animate({'height': '-=50px' }, 2000, action);
    });
    

debug时将 action 直接用字符串初始化:

    
    //...........
        var action = 'easeInQuad';
    //...........
    

在IE6中正常执行。用 typeof 测 .html() 的值确实是 string。所以猜测是 .htlm() 在 IE6
中使用时会有一些不干净的东西。。。所以使用 $.trim() 函数来把它清洁一下，就可以解决这个问题:

    
    //...........
    var action = $.trim( $(this).html() );
    //...........
    

可是究竟是什么不干净的东西呢？还是因为别的原因？

jQuery 文档中关于 .trim() 函数：

> The $.trim() function removes all newlines, spaces (including non-breaking
spaces), and tabs from the beginning and end of the supplied string. If these
whitespace characters occur in the middle of the string, they are preserved.


