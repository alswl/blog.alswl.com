var github=(function(){function a(c){return $("<div/>").text(c).html()}function b(g,f){var e=0,c="",d=$(g)[0];c+='<ul class="list-group" id="github">';for(e=0;e<f.length;e++){c+='<li class="list-group-item"><a href="'+f[e].html_url+'">'+f[e].name+"</a><p><small>"+a(f[e].description||"")+"</small></p></li>"}c+="</ul>";d.innerHTML=c}return{showRepos:function(c){$.ajax({url:"https://api.github.com/users/"+c.user+"/repos?callback=?",dataType:"jsonp",error:function(d){$(c.target+" li.loading").addClass("error").text("Error loading feed")},success:function(f){var e=[];if(!f||!f.data){return}for(var d=0;d<f.data.length;d++){if(c.skip_forks&&f.data[d].fork){continue}e.push(f.data[d])}e.sort(function(h,g){var j=new Date(h.pushed_at).valueOf(),i=new Date(g.pushed_at).valueOf();if(j===i){return 0}return j>i?-1:1});if(c.count){e.splice(c.count)}b(c.target,e)}})}}})();