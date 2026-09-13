# AGENTS.md

本文件供 AI coding agent（Claude Code 等）在本仓库工作时参考。内容依据 README.md、STYLE.md、`.ai/`、
`.specify/memory/constitution.md`、Makefile 与 CI 配置整理。

## 项目性质

alswl 的个人博客（https://blog.alswl.com ，站名 Log4D），Hugo 静态站点，
主题 hugo-PaperMod（git submodule，位于 `themes/hugo-PaperMod`）。
**这是内容仓库，不是软件项目** —— 主要工作是写文章、配图、发布，代码只是配套设施。

`.specify/memory/constitution.md` 的核心约束：以写作者为锚，工具服务于写稿，
不为「统一感」给写作者增加额外步骤；重要决策与踩坑写进 README/文档而非口头传递。

## 目录结构

- `content/posts/` — 文章，文件名 `YYYY-MM-DD-slug.md`
- `content/{about,board,links,microlog,en}/` — 独立页面
- `static/images/YYYYMM/` — 按发文月份归档的图片
- `layouts/` — 覆盖主题的模板（含 mermaid、render-image 适配）
- `hack/` — 维护脚本（格式化、找无用图、缩图）
- `.ai/` — 文风指导（多版本），`STYLE.md` — 写作风格指南

## 常用命令

```bash
make serve                     # 本地预览（含 draft）
make new name=YYYY-MM-DD-x.md  # 新建文章（走 archetypes/posts.md）
make build-production          # 生产构建
make clean                     # 清掉 public/ 和 .hugo_build.lock

make check                     # 门禁全套：无用图片（全量）+ 本次改动检查
make check-changed             # 只检查本次改动（pre-push 和 CI 跑的就是它）
make format                    # 格式化本次改动的 Markdown
make audit                     # 全量扫描历史存量，只报告不拦截（预期是红的）

make resize-images-in-git-workdir  # 缩放工作区新增/修改的图片到 1000x1000 以内
make sync-images               # 同步 static/images 到对象存储
```

**检查一律只作用于本次改动。** 仓库有大量历史存量（384 篇未格式化文章、
77 张超规格图片、15 处远端图片引用），全量门禁会立刻失败。
`hack/changed-files.sh` 负责算出「本次改动」，lefthook 和 CI 共用它。
存量用 `make audit` 查看，但**不要批量修**。
例外是 `hack/find-unused-images.py`，它靠 `EXCLUDE_DIRS` 排除了历史目录，
现在是全量绿的，保持全量跑。

## 提交与 CI

- lefthook：pre-commit 对暂存的 `.md` 跑 `hack/format.sh`（prettier）并检查非 ASCII 文件名；
  pre-push 跑 `make check-changed`。改完 Markdown 直接提交即可，格式化会自动发生。
- GitHub Actions：`ci.yml` 每次 push 跑「无用图片检查 + 本次改动检查 + 构建」，
  并在 master 上发布到 GitHub Pages。（原先 `build.yml` 和 `gh-pages.yml`
  都监听 push 且都执行构建，master 上会重复构建两次，已合并。）
- `make cdn` 在构建后把 `/images/` 替换为 CDN 前缀 `https://e25ba8-log4d-c.dijingchao.com`，
  只在 CI 里跑，不要在本地对 `public/` 手工执行。

### 工具版本

`.hugo-version` 和 `.prettier-version` 是版本的唯一来源，CI 与本地脚本都读它们。

- **prettier 钉在 `3.9.6`**，规则见 `.prettierrc`（内容就是当时生效的默认值）。
  不钉的话上游发版会重排全部 458 篇文章。
- **Hugo 钉在 `0.148.2`**，`make` 会在本地版本不一致时警告（只警告，不阻断）。

  ⚠️ **升级 Hugo 前先读这里。** 实测 0.148.2 → 0.166.0 会改变线上产物，
  根因是 `config.yaml` 里的 `languageCode: zh` 在 Hugo 0.158.0 起被弃用，
  且现在会真正驱动主题 i18n：

  1. 归档页月份 English → 中文，**锚点 URL 一并改变**
     （`#2009-December` → `#2009-%e5%8d%81%e4%ba%8c%e6%9c%88`），已有深链会失效
  2. 面包屑 `Home` → `主页`，分页 `Next` → `下一页`
  3. Google Analytics `respectDoNotTrack` 默认值 `false` → `true`

  想升级又保持产物不变，需要把 `languageCode` 改成 `en` 并显式设置
  `privacy.googleAnalytics.respectDoNotTrack: false`——但那样 `og:locale` 会从
  `zh` 变成 `en`（无法两全）。当前选择是先不升级。

## 文章约定

Frontmatter：

```yaml
---
title: "中文标题"
slug: "english-slug"
date: YYYY-MM-DDTHH:MM:SS+08:00
categories: ["coding"]
tags: ["tag1", "tag2"]
---
```

- `categories` 单选：coding / life / efficiency / thinking / viewpoint / managment / fun
  （近期文章也出现过中文 category，跟随同期文章即可）
- `slug` 英文小写短横线；文件名日期与 `date` 一致
- 存稿加 `draft: true`；Typora 用户可加 `typora-copy-images-to: ../../static/images/YYYYMM`

图片：

- 新文章统一用绝对路径 `/images/YYYYMM/name.png`
- 历史文章有 `../../static/images/...` 写法，由 `layouts/_default/_markup/render-image.html`
  兼容渲染；**不要批量改写老文章的图片路径**
- 图片提交前缩到 1000x1000 以内（`make resize-images-in-git-workdir`）
- 图片必须被文章引用，否则 CI 的 find-unused-images 会失败
- 图注用 `<small>` 标注来源

其他：

- ` ```mermaid ` 代码块渲染为实时图表，跟随明暗主题
- `<mark>` 高亮核心观点，`<!-- more -->` 标记摘要截断点

## 写作风格

代笔或辅助写作前先读 `STYLE.md`（最完整），`.ai/` 下是几份不同来源的同类指导。
要点：从问题切入而非从技术切入；实用主义基调，声明适用范围与局限；
中英混排，技术术语不强译；每个大章节配小结，文末给扩展阅读；
语气克制但有态度，可以幽默但不浮夸；不写没有实操支撑的纯理论。

## 注意事项

- 编辑既有文章时做外科手术式改动：不顺手「改进」邻近段落、
  不重排格式、不统一历史文章的写法。
- `public/` 是构建产物，已 gitignore，不要提交或手工编辑。
- 微信公众号导出、pandoc 转 GFM、URL 替换等一次性操作的命令见 README.md 的 Tips 段。
