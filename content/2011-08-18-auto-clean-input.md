Title: 简单输入提示框实现
Author: alswl
Slug: auto-clean-input
Date: 2011-08-18 00:00:00
Tags: 
Category: Web前端

早期的输入框提示是这样的（via [baidu](http://tieba.baidu.com/index.html)）

![tieba](http://upload-log4d.qiniudn.com/2011/08/login1.png)

左边一个 label ，右边一个输入框。

比较现代的方式是（via [Discuz!](http://www.discuz.net/)）

![discuz!](http://upload-log4d.qiniudn.com/2011/08/login2.png)

更漂亮的方式是（via [点点](http://www.diandian.com/login)）

![diandian](http://upload-log4d.qiniudn.com/2011/08/login_diandian.png)

登录提示信息是放在输入框里面，可以减少文字干扰，我也想在自己手头的小项目中实现这种效果。

我需要达到几个要求：

  1. 提示信息是可以暂存的，即用户的输入在清空之后，还能够显示原来的提示信息
  2. 只需为 text / textarea 添加一个 class 即可实现效果
  3. 不修改 DOM 节点，避免影响上下文选择器

为了实现效果，我需要将提示信息暂存到某个地方。有3个地方可供选择： js 全局变量、输入框自定义属性、上下文 DOM 节点。

js 全局变量比较难控制元素标识，并不是每个元素都可以精准的用 id 标记；输入框自定义属性会破坏语义；在上下文加入节点会破坏 DOM 树。

权衡之后，我选择了使用 输入框自定义属性实现。

demo 在[这里](http://lab.log4d.com/javascript/autoclean.html)。

封装的方法代码如下

    
    $('.auto_clean').blur(function() {
    	if ($.trim($(this).val()) === '') {
    		$(this).val($(this).attr('message'));
    	}
    }).focus(function() {
    	if ($(this).attr('message') === undefined) {
    		$(this).attr('message', $(this).val());
    	}
    	if ($(this).val() === $(this).attr('message')) {
    		$(this).val('');
    	}
    });
    });

使用方法如下

    
    <input type="text" class="auto_clean" value="搜索用户" /> 
    <br/> 
    <textarea class="auto_clean">请在这里输入</textarea> 

update&nbsp_place_holder;2011/08/25： 感谢 [@行者](http://www.k68.org/) 提醒，使用 html5
的 placeholder 会更干净优美一些，参考见 [Web Forms - Dive Into
HTML5](http://diveintohtml5.org/forms.html)

