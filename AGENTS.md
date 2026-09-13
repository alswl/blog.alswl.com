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
hugo serve -D                  # 本地预览（含 draft）
make new name=YYYY-MM-DD-x.md  # 新建文章（走 archetypes/posts.md）
make build-production          # 生产构建
make sync-images               # 同步 static/images 到对象存储
make resize-images-in-git-workdir  # 缩放工作区新增图片到 1000x1000 以内
make find-remote-images        # 检出仍指向远端的图片引用
python3 hack/find-unused-images.py # CI 会跑，未被引用的图片会导致构建失败
npx prettier content/posts/*.md --write
```

## 提交与 CI

- lefthook：pre-commit 对暂存的 `.md` 跑 `hack/format.sh`（prettier）；pre-push 做全量检查。
  改完 Markdown 直接提交即可，格式化会自动发生。
- 非 ASCII 文件名会被 pre-commit 拒绝。
- GitHub Actions：`build.yml` 每次 push 跑「未使用图片检查 + 构建」；
  `gh-pages.yml` 在 master 上构建并发布到 GitHub Pages。
- `make cdn` 在构建后把 `/images/` 替换为 CDN 前缀 `https://e25ba8-log4d-c.dijingchao.com`，
  只在 CI 里跑，不要在本地对 `public/` 手工执行。

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
