# AGENTS.md

本仓库是 alswl 的个人博客 Log4D（https://blog.alswl.com），使用 Hugo 和
`themes/hugo-PaperMod` submodule。**这是内容仓库，主要工作是写文章、配图、发布。**

遵守[项目宪章](.specify/memory/constitution.md)：以写作者为锚，工具服务于写稿，
不为统一流程增加额外步骤。重要决策与踩坑写入仓库文档。

## 按任务阅读

- 写稿或辅助写作：先读 [STYLE.md](STYLE.md) 和[写文章与配图](docs/guide/writing.md)。
  `.ai/` 保留不同来源的文风分析，作为补充参考。
- 添加链接卡片：读[使用 Banner 链接卡片](docs/guide/banner-links.md)。
- 修改模板、脚本、检查或发布流程：读[站点维护](docs/dev/README.md)。
- 升级 Hugo：必须先读[升级约束](docs/dev/README.md#hugo-升级约束)，当前选择不升级。

## 执行约束

- 编辑既有文章只改目标内容，不顺手润色相邻段落、重排格式或统一历史写法。
- 新文章图片使用 `/images/YYYYMM/name.png`，不要批量改写历史相对路径。
- 暂存前运行 `make prepare`（格式化与缩图）；只缩图可用 `make resize`。
  工具不会自动暂存，暂存后格式化或缩图必须重新选择并暂存修改。
  意外显示「已处理 0 张图片」时，先检查 Git 状态与路径，不要手工用 `sips` 绕过。
- 格式、远端图片和尺寸检查只覆盖本次改动，不批量修复历史存量。
  无用图片检查保持全量运行。完整门禁用 `make check`。
- `.hugo-version` 和 `.prettier-version` 是工具版本的唯一来源。
  `make setup` 安装指定版本，`make doctor` 诊断环境，不依赖系统默认 Hugo 版本。
- 不手工编辑或提交 `public/`。CDN 发布构建仅在 CI 执行，产物为 `.cache/publish/`。
- 发布后同时验收文章页与 CDN 图片。记录观测时点，不凭一次图片 404 宣布发布失败。
  同步报认证或上传错误时如实报告，由负责人判断是否已有其他同步在传播。

完整操作步骤与约定从[文档首页](docs/README.md)进入，避免在本文件重复维护。
