var photoTag = {   
    show: function(left,top,width, height, show_resize_square) {
        $('#select-area-box').css({'left':left - 7, 'top':top - 7})
        $('#select-area-box').width(width + 4).height(height + 4).show();
        $('#select-area').width(width).height(height);
        if(show_resize_square) $('#select-area-box span').show();
        else $('#select-area-box span').hide();
    },
    hide: function() {$('#select-area-box').hide();    },
    add:function(tag_name, tag_value, left, top, width, height) {
        var json = {id:Math.floor(Math.random() * 10000)};
        //$.getJSON('add_tag.php', {'name':tag_name,'left':left,'top':top,'width':width,'height':height}, function(json) {
            //reflesh tag list
        //    if(json.message) alert(json.message);
        //    if(json.error == 0) {
                var args = left+','+top+','+width+','+height;
                var li = '<li>&nbsp;';
                li += '<span onmouseover="photoTag.show('+args+');" ';
                li += 'onmouseout="photoTag.hide();">'+tag_name+'</span>';
                li += '(<a href="javascript:;" onclick="photoTag.remove('+json.id+',this.parentNode);" ';
                li += 'onmouseover="photoTag.show('+args+');" onmouseout="photoTag.hide();">删除</a>)';
                li += '<input type="hidden" name="photoField" value="' + tag_name + ':' + tag_value +
                    ',x:' + left + ',y:' + top + ',width:' + width + ',height:' + height + '" />';
                li += '</li>';
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
$(function(){
var is_started = false;
// 选区左上角,和高宽
var info = {'left':0,'top':0,'width':0,'height':0};
var origin = {x:$('#enclose-wrapper').offset().left + (parseInt($('#enclose-wrapper').css('border-left-width'))||0),
              y:$('#enclose-wrapper').offset().top  + (parseInt($('#enclose-wrapper').css('border-top-width'))||0)};
var dnr = new DragResize($('#select-area-box')[0], {
    minWidth:20,
    minHeight:20,
    bound:{left:0,top:0,right:9999,bottom:9999},
    callback:function(i) {
        // 7为左(上)边两个边框的宽度的和, 4为左右(上下)篮色边框宽度的和
        info= {'left':i.left + 7,'top':i.top + 7,'width':i.width - 4,'height':i.height - 4};
        $('#select-area').width(info.width).height(info.height);
        // 将添加标签的表单定位在选区的右边
        $('#form-add-tag').css({'left':i.left + i.width + 10, 'top':i.top});
    }                
});
// 拖动选区
$('#select-area').mousedown(function(e){
    dnr.drag(e);
});
// 调整选区大小
$('#select-area-box span').mousedown(function(e){
    dnr.resize(e, this.className.replace('-resize', ''));
});
// 在图片上点击一下,开始获取选区
$('#photo-wrapper img').mousedown(function(e){
    if(is_started) return;
    is_started = true;
    var left = e.pageX - origin.x - 50 - 7;
    var top  = e.pageY - origin.y - 50 - 7 ;

    info= {'left':left + 7,'top':top + 7,'width':100,'height':100};
    photoTag.show(info.left, info.top, info.width, info.height, true);
    $('#form-add-tag').show().css({'left':left + 100 + 4 + 10, 'top':top});
});
// 鼠标进入图片内时,显示选区
$('#photo-wrapper img').bind('mouseenter',function(e){
    if(!is_started) return;
    photoTag.show(info.left, info.top, info.width, info.height, true);
});
// 确定添加一个标签,或取消
$('#btn-add-tag, #btn-cancel').click(function(e){
    if(this.id == 'btn-cancel') {
        $('#form-add-tag, #select-area-box').hide();
        is_started = false;
        return false;
    }
    if(!$('#tag-name').val()) {
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