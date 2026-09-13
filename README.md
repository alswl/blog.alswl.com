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
make serve                     # 本地预览（含 draft）
make new name=YYYY-MM-DD-x.md  # 新建文章
make build-production          # 生产构建
make clean

make check                     # 门禁全套（CI 跑的就是它）
make check-changed             # 只检查本次改动
make format                    # 格式化本次改动的 Markdown
make audit                     # 全量扫描历史存量，只报告不拦截

make resize-images-in-git-workdir  # 缩图到 1000x1000 以内
make sync-images                   # 上传图片到对象存储
```

检查一律只作用于本次改动——仓库有大量历史存量（384 篇未格式化文章、
77 张超规格图片、15 处远端图片引用），不做批量修复。

工具版本钉在 `.hugo-version`（0.148.2）和 `.prettier-version`（3.9.6）。
**升级 Hugo 会改变线上产物，动手前先看 AGENTS.md 的「工具版本」段。**

## Tips

**Mermaid diagrams**: fenced ` ```mermaid ` code blocks render as live diagrams (see `layouts/_default/_markup/render-codeblock-mermaid.html` and `layouts/partials/extend_footer.html`), matching the current light/dark theme.

Asset prefix:

- <del>https://4ocf5n.dijingchao.com/upload_dropbox/</del>
- <del>https://d05fae.dijingchao.com</del>
- https://e25ba8-log4d-c.dijingchao.com

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
---

原文链接: yours
欢迎关注我的微信公众号：窥豹。
3a1ff193cee606bd1e2ea554a16353ee
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
c content/posts/your.md | gsed 's#../../static/images#https://e25ba8-log4d-c.dijingchao.com#g' | pandoc -f markdown_mmd -t gfm+implicit_figures --wrap=none C
```
