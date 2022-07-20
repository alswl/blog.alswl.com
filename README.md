# blog.alswl.com

https://blog.alswl.com/
https://www.zhihu.com/column/alswl
https://www.jianshu.com/u/90d9cec0f932

This is my blog.

*   pelicanconf.py for preview
*   publishconf.py for product

## Command

Init:

```
mkvirtualenv -p /usr/local/bin/python3 blog.alswl.com
pip install -r requirements.txt
pelican-themes -U $HOME/dev/myproject/pelican-bootstrap3
```


- `fab new_post:'new post name'`  # new post
- `fab build`  # build for local
- `fab server`  # run in localhost
- `fab publish`  # deploy to remote


```
make name="your post name" new_post

make regenerate
make devserver
open http://127.0.0.1:8000/

make coding
```

## TODO

- Fix indent of pelican must use four space.


## Tips


Asset prefix: `https://4ocf5n.dijingchao.com/upload_dropbox/`

Article footer:

```markdown
--------------------------------------------------------------------------

原文链接: 

3a1ff193cee606bd1e2ea554a16353ee

欢迎关注我的微信公众号：[窥豹](http://mp.weixin.qq.com/mp/getmasssendmsg?__biz=MzIyNTIwMTU3MQ==#wechat_webview_type=1&wechat_redirect)

![窥豹](https://4ocf5n.dijingchao.com/upload_dropbox/201605/qrcode_for_gh_17e2f9c2caa4_258.jpg)

![如果对你有帮助，给作者 ￥2 买张彩票吧。](https://4ocf5n.dijingchao.com/upload_dropbox/meta/wechat-pay-s-crop.png)
```

Markdown to GFM:

```bash
cat content/some-md.md | pandoc -f markdown_mmd -t gfm --wrap=none | pbcopy
```

<del>Wechat mp link process</del>
[微信 Markdown 编辑器 | Doocs 开源社区](https://doocs.gitee.io/md/):


```
MD=content/some-md.md
BODY=$(cat $MD  | sed -E 's/[^!]\[(.+)\]\((.+)\)/(\1)<sup>(via)<\/sup>/g' | sed -E 's/^\[(.+)\]\((.+)\)/(\1)<sup>(via)<\/sup>/g')
FOOTER=$(cat $MD | grep '\[.*\]\(.*\)' -oE | grep -v png | grep -v jpg | sed 's/\[//g;s/\]//g;s/(/: /g;s/)//g' | awk '{print "*   "$0}')

echo $BODY $FOOTER | pbcopy
```
