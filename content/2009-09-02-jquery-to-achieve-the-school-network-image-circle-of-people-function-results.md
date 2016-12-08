Title: jQuery图片圈人功能在ASP.NET下的改进
Author: alswl
Slug: jquery-to-achieve-the-school-network-image-circle-of-people-function-results
Date: 2009-09-02 00:00:00
Tags: dotNet, JavaScript, jQuery, 人人
Category: Coding

项目中需要一个类似于校内圈人效果的js控件，找了一下基本没有直接能用的，只有一些未完成，我只能自己动手了。 基本框架参照这篇文章《[JS实现校内网"图片圈人
"功能效果](http://www.cnblogs.com/czy1121/archive/2009/03/03/1402105.html)》（强烈推荐这篇
文章，这段代码写的很帅气） 我把代码摘录如下，不过还是建议大家去看原文的一些分析。

## 原始Code:

运行环境： 1.jQuery支持 2.DragResize类（czy1121作者写的一个js类，更多信息可以参照《[Javascript Resize和Dr
ag类,基于jQuery](http://www.cnblogs.com/czy1121/archive/2009/02/26/1398971.html)》
）

### 样式：

    
    
    #enclose-wrapper {
    	position: relative;
    	z-index: 0;
    	border: 4px solid #DDD;
    	background-color: #FFF;
    }
    #form-add-tag {
    	margin-left: 8px;
    	position: absolute;
    	padding: 5px 3px;
    	border: 1px solid #005EAC;
    	float: left;
    	display: inline;
    	background-color: #FFF;
    }
    #select-area-box {
    	position: absolute;
    	border: 5px solid #D8DFEA;
    	float: left;
    }
    #select-area {
    	position: relative;
    	padding: 0;
    	border: 2px solid #005EAC;
    	z-index: 15;
    	cursor: move;
    	background: url(spacer.gif) no-repeat -1px -1px;
    }
    #select-area-box span {
    	position: absolute;
    	border: 1px solid #005EAC;
    	width: 8px;
    	height: 8px;
    	background-color: #FFF;
    	font-size: 0;
    	z-index: 18;
    }
    #select-area-box span.north-west-resize {
    	cursor: nw-resize;
    	left: 0;
    	top: 0;
    	margin-left: -1px;
    	margin-top: -1px;
    }
    #select-area-box span.north-east-resize {
    	cursor: ne-resize;
    	right: 0;
    	top: 0;
    	margin-right: -1px;
    	margin-top: -1px;
    }
    #select-area-box span.south-west-resize {
    	cursor: sw-resize;
    	left: 0;
    	bottom: 0;
    	margin-left: -1px;
    	margin-bottom: -1px;
    }
    #select-area-box span.south-east-resize {
    	cursor: se-resize;
    	right: 0;
    	bottom: 0;
    	margin-right: -1px;
    	margin-bottom: -1px;
    }
    #enclose-wrapper ul#tag-list {
    	list-style: none;
    	margin: 0;
    	padding: 0;
    	font-size: 13px;
    	float: left;
    }
    #enclose-wrapper ul#tag-list li {
    	list-style: none;
    	float: left;
    }
    #enclose-wrapper ul#tag-list li a {
    	color: #F60;
    }
    

### js实现代码：

    
    
    var photoTag = {
        show: function(left, top, width, height, show_resize_square) {
            $('#select-area-box').css({
                'left': left - 7,
                'top': top - 7
            })
            $('#select-area-box').width(width + 4).height(height + 4).show();
            $('#select-area').width(width).height(height);
            if (show_resize_square) $('#select-area-box span').show();
            else $('#select-area-box span').hide();
        },
        hide: function() {
            $('#select-area-box').hide();
        },
        add: function(tag_name, tag_value, left, top, width, height) {
            var json = {
                id: Math.floor(Math.random() * 10000)
            };
            var args = left + ',' + top + ',' + width + ',' + height;
            var li = '
    
      * ';         li += '';         li += '([删除](javascript:;))';         li += '';         li += '
    ';
            $('#tag-list').append(li);
        },
        remove: function(id, li) {
            li.parentNode.removeChild(li);
        }
    };
    $(function() {
        var is_started = false;
        // 选区左上角,和高宽
        var info = {
            'left': 0,
            'top': 0,
            'width': 0,
            'height': 0
        };
        var origin = {
            x: $('#enclose-wrapper').offset().left + (parseInt($('#enclose-wrapper').css('border-left-width')) || 0),
            y: $('#enclose-wrapper').offset().top + (parseInt($('#enclose-wrapper').css('border-top-width')) || 0)
        };
        var dnr = new DragResize($('#select-area-box')[0], {
            minWidth: 20,
            minHeight: 20,
            bound: {
                left: 0,
                top: 0,
                right: 9999,
                bottom: 9999
            },
            callback: function(i) {
                // 7为左(上)边两个边框的宽度的和, 4为左右(上下)篮色边框宽度的和
                info = {
                    'left': i.left + 7,
                    'top': i.top + 7,
                    'width': i.width - 4,
                    'height': i.height - 4
                };
                $('#select-area').width(info.width).height(info.height);
                // 将添加标签的表单定位在选区的右边
                $('#form-add-tag').css({
                    'left': i.left + i.width + 10,
                    'top': i.top
                });
            }
        });
        // 拖动选区
        $('#select-area').mousedown(function(e) {
            dnr.drag(e);
        });
        // 调整选区大小
        $('#select-area-box span').mousedown(function(e) {
            dnr.resize(e, this.className.replace('-resize', ''));
        });
        // 在图片上点击一下,开始获取选区
        $('#photo-wrapper img').mousedown(function(e) {
            if (is_started) return;
            is_started = true;
            var left = e.pageX - origin.x - 50 - 7;
            var top = e.pageY - origin.y - 50 - 7;
            info = {
                'left': left + 7,
                'top': top + 7,
                'width': 100,
                'height': 100
            };
            photoTag.show(info.left, info.top, info.width, info.height, true);
            $('#form-add-tag').show().css({
                'left': left + 100 + 4 + 10,
                'top': top
            });
        });
        // 鼠标进入图片内时,显示选区
        $('#photo-wrapper img').bind('mouseenter',
        function(e) {
            if (!is_started) return;
            photoTag.show(info.left, info.top, info.width, info.height, true);
        });
        // 确定添加一个标签,或取消
        $('#btn-add-tag, #btn-cancel').click(function(e) {
            if (this.id == 'btn-cancel') {
                $('#form-add-tag, #select-area-box').hide();
                is_started = false;
                return false;
            }
            if (!$('#tag-name').val()) {
                alert('标签名不能为空！');
                return false;
            }
            // 添加标签
            photoTag.add($('#tag-name').val(), $('#tag-value').val(), info.left, info.top, info.width, info.height);
            // 隐藏选区和表单
            $('#form-add-tag, #select-area-box').hide();
            is_started = false;
        });
        photoTag.hide();
    });

### Html代码

    
    
    <div id="enclose-wrapper">
      <div id="photo-wrapper" style="margin:15px auto;text-align:center;"> <img id="photo" src="heroes_s3_peter.jpg" /> </div>
      <div>
        <ul id="tag-list">
          <li>相片中：</li>
          <li> <span onmouseover="photoTag.show(0,0,85,66);" onmouseout="photoTag.hide();">aaa</span> (<a href="javascript:;" onclick="photoTag.remove('342',this.parentNode);" onmouseover="photoTag.show(0,0,85,66);" onmouseout="photoTag.hide();">删除</a>) </li>
        </ul>
      </div>
      <div id="select-area-box">
        <div id="select-area"></div>
        <span></span><span></span> <span></span><span></span> </div>
      <div id="form-add-tag" style="display:none;"> 输入标签：

<input id="tag-name" name="tag-name" type="text" />

<button id="btn-add-tag" type="button">确认</button>

<button id="btn-cancel" type="button">取消</button>

</div>

</div>

## 改进

在Asp.NET下这段代码存在几个问题（毕竟这段代码应该只能算是Demo）：1.无法和服务器进行数据交互。2.无法在ASP.NET环境下获取相关id。3.只
能提交到服务器一个"标签"，不足以完成需求。

### 修改后js:

    
    
    var photoTag = {
        show: function(left, top, width, height, show_resize_square) {
            $('#select-area-box').css({
                'left': left - 7,
                'top': top - 7
            })
            $('#select-area-box').width(width + 4).height(height + 4).show();
            $('#select-area').width(width).height(height);
            if (show_resize_square) $('#select-area-box span').show();
            else $('#select-area-box span').hide();
        },
        hide: function() {
            $('#select-area-box').hide();
        },
        add: function(tag_name, tag_value, left, top, width, height) {
            var json = {
                id: Math.floor(Math.random() * 10000)
            };
            //$.getJSON('add_tag.php', {'name':tag_name,'left':left,'top':top,'width':width,'height':height}, function(json) {
            //reflesh tag list
            //    if(json.message) alert(json.message);
            //    if(json.error == 0) {
            var args = left + ',' + top + ',' + width + ',' + height;
            var li = '
    
      * ';         li += '';         li += '([删除](javascript:;))';         li += '';         li += '
    ';
            $('#tag-list').append(li);
            //    }
            //});
        },
        remove: function(id, li) {
            //$.getJSON('remove_tag.php', {'tag_id':id}, function(json) {
            //reflesh tag list
            //    if(json.message) alert(json.message);
            //    if(json.error == 0)
            li.parentNode.removeChild(li);
            //});
        }
    };
    $(function() {
        var is_started = false;
        // 选区左上角,和高宽
        var info = {
            'left': 0,
            'top': 0,
            'width': 0,
            'height': 0
        };
        var origin = {
            x: $('#enclose-wrapper').offset().left + (parseInt($('#enclose-wrapper').css('border-left-width')) || 0),
            y: $('#enclose-wrapper').offset().top + (parseInt($('#enclose-wrapper').css('border-top-width')) || 0)
        };
        var dnr = new DragResize($('#select-area-box')[0], {
            minWidth: 20,
            minHeight: 20,
            bound: {
                left: 0,
                top: 0,
                right: 9999,
                bottom: 9999
            },
            callback: function(i) {
                // 7为左(上)边两个边框的宽度的和, 4为左右(上下)篮色边框宽度的和
                info = {
                    'left': i.left + 7,
                    'top': i.top + 7,
                    'width': i.width - 4,
                    'height': i.height - 4
                };
                $('#select-area').width(info.width).height(info.height);
                // 将添加标签的表单定位在选区的右边
                $('#form-add-tag').css({
                    'left': i.left + i.width + 10,
                    'top': i.top
                });
            }
        });
        // 拖动选区
        $('#select-area').mousedown(function(e) {
            dnr.drag(e);
        });
        // 调整选区大小
        $('#select-area-box span').mousedown(function(e) {
            dnr.resize(e, this.className.replace('-resize', ''));
        });
        // 在图片上点击一下,开始获取选区
        $('#photo-wrapper img').mousedown(function(e) {
            if (is_started) return;
            is_started = true;
            var left = e.pageX - origin.x - 50 - 7;
            var top = e.pageY - origin.y - 50 - 7;
            info = {
                'left': left + 7,
                'top': top + 7,
                'width': 100,
                'height': 100
            };
            photoTag.show(info.left, info.top, info.width, info.height, true);
            $('#form-add-tag').show().css({
                'left': left + 100 + 4 + 10,
                'top': top
            });
        });
        // 鼠标进入图片内时,显示选区
        $('#photo-wrapper img').bind('mouseenter',
        function(e) {
            if (!is_started) return;
            photoTag.show(info.left, info.top, info.width, info.height, true);
        });
        // 确定添加一个标签,或取消
        $('#btn-add-tag, #btn-cancel').click(function(e) {
            if (this.id == 'btn-cancel') {
                $('#form-add-tag, #select-area-box').hide();
                is_started = false;
                return false;
            }
            if (!$('#tag-name').val()) {
                alert('标签名不能为空！');
                return false;
            }
            // 添加标签
            photoTag.add($('#tag-name').val(), $('#tag-value').val(), info.left, info.top, info.width, info.height);
            // 隐藏选区和表单
            $('#form-add-tag, #select-area-box').hide();
            is_started = false;
        });
        photoTag.hide();
    });

### Html代码：

    
    
    <div id="enclose-wrapper">
      <div id="photo-wrapper">
        <asp:Image ID="ImgPhoto" Visible="false" runat="server" />
      </div>
      <div>
        <ul id="tag-list">
        </ul>
      </div>
      <div id="select-area-box">
        <div id="select-area"> </div>
        <span></span><span></span><span></span><span></span> </div>
      <div id="form-add-tag" style="display: none;"> 名称：
        <input id="tag-name" name="tag-name" type="text" />
        

数值：

<input id="tag-value" name="tag-value" type="text" />

<button id="btn-add-tag" type="button"> 确认</button>

<button id="btn-cancel" type="button"> 取消</button>

</div>

</div>

这边的主要修改在于把框子的右边的内容增加为名称和数值，方便数据的识别。

### 后台ASP.NET文件读取

    
    
    string[] fields = Request.Params.GetValues("photoField");

这里呢，由于上传的元素`name`相同，都是`photoField`，所以通过`Params.GetValues()`就可以取出`string`数组，这样就
能获取所有数据了。数据格式是"`ddl:小楠,x:98.88333129882812,y:146,width:100,height:100`"这种形式，依靠
","分割。

### 相关下载

[DragResize.js](https://ohsolnxaa.qnssl.com/2009/09/DragResize.js)
[template.js](https://ohsolnxaa.qnssl.com/2009/09/template.js)
[css.css](https://ohsolnxaa.qnssl.com/2009/09/css.css)

