# Log4D · blog.alswl.com

alswl 的个人博客，使用 Hugo 和 hugo-PaperMod 主题。

- [阅读博客](https://blog.alswl.com/)
- [文档首页](docs/README.md)
- [写作者指南](docs/guide/README.md)：新建文章、配图、链接卡片和转载。
- [站点维护](docs/dev/README.md)：依赖、检查、构建与发布。

## 开始写作

先按[站点维护](docs/dev/README.md#安装与诊断)安装依赖，再在仓库根目录运行：

```bash
make init-theme
make new-post name=YYYY-MM-DD-x.md
make preview-site
```

将示例文件名替换为文章日期和 slug。新文章默认是草稿，本地预览包含草稿。
完整步骤见[写文章与配图](docs/guide/writing.md)。
日常收尾用 `make format-markdown`、`make resize-images` 和 `make check-content`，检查后照常提交。`make help` 查看所有作者命令。

辅助写作前先读 [STYLE.md](STYLE.md)，coding agent 另读 [AGENTS.md](AGENTS.md)。

## 其他发布渠道

- [知乎](https://www.zhihu.com/column/alswl)
- [掘金](https://juejin.cn/user/1380642333663671)
- [SegmentFault](https://segmentfault.com/u/alswl/articles)
