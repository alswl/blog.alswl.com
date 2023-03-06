# blog.alswl.com

- https://blog.alswl.com/
- https://www.zhihu.com/column/alswl
- https://juejin.cn/user/1380642333663671
- https://segmentfault.com/u/alswl/articles
- <del>https://www.jianshu.com/u/90d9cec0f932</del>
- ata
- intranet yuque

This is my blog.


## Command

```
# upload images
make sync-images

hugo serve -D
hugo
hugo new posts/new.md
```


## Tips


Asset prefix: 

- <del>https://4ocf5n.dijingchao.com/upload_dropbox/</del>
- https://d05fae.dijingchao.com


**Wechat mp link process**:


- <del>sed</del>

  ```
  MD=content/some-md.md
  BODY=$(cat $MD  | sed -E 's/[^!]\[(.+)\]\((.+)\)/(\1)<sup>(via)<\/sup>/g' | sed -E 's/^\[(.+)\]\((.+)\)/(\1)<sup>(via)<\/sup>/g')
  FOOTER=$(cat $MD | grep '\[.*\]\(.*\)' -oE | grep -v png | grep -v jpg | sed 's/\[//g;s/\]//g;s/(/: /g;s/)//g' | awk '{print "*   "$0}')
  
  echo $BODY $FOOTER | pbcopy
  ```

- [微信 Markdown 编辑器 | Doocs 开源社区](https://doocs.gitee.io/md/):


**Article footer**:

```markdown
--------------------------------------------------------------------------

原文链接: yours

3a1ff193cee606bd1e2ea554a16353ee

欢迎关注我的微信公众号：[窥豹](http://mp.weixin.qq.com/mp/getmasssendmsg?__biz=MzIyNTIwMTU3MQ==#wechat_webview_type=1&wechat_redirect)

![窥豹](https://4ocf5n.dijingchao.com/upload_dropbox/201605/qrcode_for_gh_17e2f9c2caa4_258.jpg)
```

**Markdown to GFM**:

```bash
cat content/some-md.md | pandoc -f markdown_mmd -t gfm+implicit_figures --wrap=none | pbcopy
```

**Image size nomalize**:

```
cd dir
for i in $(ls); do convert $i -resize 1000x1000\> $i; donen
```

**Replace URL**

```
c content/posts/your.md | gsed 's#../../static/images#https://d05fae.dijingchao.com#g' | pandoc -f markdown_mmd -t gfm+implicit_figures --wrap=none C
```
