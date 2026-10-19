# AGENTS.md

本仓库是 alswl 的个人博客 Log4D（https://blog.alswl.com），使用 Hugo 和
`themes/hugo-PaperMod` submodule。**这是内容仓库，主要工作是写文章、配图、发布。**

遵守[项目宪章](.specify/memory/constitution.md)：以写作者为锚，工具服务于写稿，
不为统一流程增加额外步骤。重要决策与踩坑写入仓库文档。

## 按任务阅读

- 写稿或辅助写作：先读 [STYLE.md](STYLE.md) 和[写文章与配图](docs/guide/writing.md)。
  `.ai/` 保留不同来源的文风分析，作为补充参考。
- 添加链接卡片：读[使用 Banner 链接卡片](docs/guide/banner-links.md)。
- 导出或转载文章：读[导出与转载](docs/guide/export.md)。
- 修改模板、脚本、检查或发布流程：读[站点维护](docs/dev/README.md)。
- 修改 Hugo 配置：先读[升级行为记录](docs/dev/README.md#hugo-升级行为)。CI 使用最新版，本地允许版本差异。

## 仓库定位

- `content/posts/`：文章；`archetypes/posts.md`：新文章模板。
- `static/images/YYYYMM/`：文章配图，对应站点路径 `/images/YYYYMM/`。
- `layouts/`、`assets/`：本站模板覆盖与样式；`config.yaml`：Hugo 配置。
- `themes/hugo-PaperMod/`：主题 submodule，初始化用 `make init-theme`。
- `scripts/`、`tests/`、`.github/workflows/`：工具实现、回归测试和 CI。
- `docs/guide/` 面向写作者，`docs/dev/` 面向维护者。操作步骤在对应文档维护。

## 写作与配图

- 编辑既有文章只改目标内容，不顺手润色相邻段落、重排格式或统一历史写法。
- 新文章用 `make new-post name=YYYY-MM-DD-slug.md` 创建，文件名日期与 frontmatter
  的 `date` 一致，`slug` 使用英文小写短横线。保留 `draft: true`，准备发布时再移除或改为 `false`。
- 用 `make preview-site` 预览草稿，核对文章排版与图片。
- 新文章图片使用 `/images/YYYYMM/name.png`，不要批量改写历史相对路径。

## 检查与维护

命令从 `make help` 查询，默认在仓库根目录运行。

- 暂存前按需运行 `make format-markdown` 和 `make resize-images`（格式化与缩图）。
  工具不会自动暂存，暂存后格式化或缩图必须重新选择并暂存修改。
  意外显示「已处理 0 张图片」时，先检查 Git 状态与路径，不要手工用 `sips` 绕过。
- 格式、远端图片和尺寸检查只覆盖本次改动，不批量修复历史存量。
  无用图片检查保持全量运行。完整门禁用 `make check-content`。
- 本地使用已安装的 Hugo 和 Prettier，CI 安装最新版，允许版本差异。
  `make check-tools` 显示实际工具版本；不维护自建安装器或精确版本拦截。
- 修改工具链后运行 `make test-toolchain`、`make check-content` 和 `make build-site`。
  模板或配置修改后运行 `make build-site`，并检查受影响页面。
- Python 工具只使用标准库；作者命令统一由 Makefile 提供，内部实现放在 `scripts/`。

## 发布与验收

- 不手工编辑或提交 `public/`。CDN 发布构建仅在 CI 执行，产物为 `.cache/publish/`。
- 推送 `master` 会触发 CI 部署，其他分支只构建。图片需通过 `make upload-images`
  显式同步，CI 不负责上传原图。发布配置不保存凭据。
- 发布后同时验收文章页与 CDN 图片。记录观测时点，不凭一次图片 404 宣布发布失败。
  同步报认证或上传错误时如实报告，由负责人判断是否已有其他同步在传播。

完整操作步骤与约定从[文档首页](docs/README.md)进入，避免在本文件重复维护。
