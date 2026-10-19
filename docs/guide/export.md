# 导出与转载文章

本页供作者将已有文章转换后转载。以下命令在仓库根目录执行，需要 Pandoc。
`pbcopy` 适用于 macOS。将示例路径替换为实际文章路径。

## 转换为 GFM

```bash
cat content/some-md.md | pandoc -f markdown_mmd -t gfm+implicit_figures --wrap=none | pbcopy
```

命令将 GFM 文本放入剪贴板。转载前核对标题、代码块、链接和图片。
本次文档整理未执行该转换命令。

## 微信公众号排版

原 README 使用[微信 Markdown 编辑器](https://doocs.gitee.io/md/)排版。
本仓库不提供公众号发布脚本，具体操作以编辑器为准。

转载可附上原文链接与公众号信息：

```markdown
---

原文链接: yours
欢迎关注我的微信公众号：窥豹。
3a1ff193cee606bd1e2ea554a16353ee
```

## 核对图片地址

博客当前使用的图片 CDN 前缀是 `https://e25ba8-log4d-c.dijingchao.com`。
站外转载需要检查图片 URL 是否可访问，避免保留仓库相对路径。
博客自身的图片同步与 CDN 替换见[站点维护](../dev/README.md#图片同步与发布验收)。

返回[写作者指南](README.md)。
