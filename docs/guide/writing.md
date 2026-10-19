# 写文章与配图

本页面向日常写稿的作者。首次按[站点维护](../dev/README.md#安装与诊断)安装依赖，运行 `make init-theme` 初始化主题；
遇到环境问题运行 `make doctor`，命令概览见 `make help`。
工具版本与检查依赖见[站点维护](../dev/README.md)。

## 新建与预览

1. 在仓库根目录创建文章，将示例名称替换为实际日期和 slug：

   ```bash
   make new name=YYYY-MM-DD-x.md
   ```

   命令使用 `archetypes/posts.md` 创建 `content/posts/` 下的文件。
   新文章默认带有 `draft: true`。

2. 编辑文章的 frontmatter 和正文。
3. 启动包含草稿的本地预览：

   ```bash
   make serve
   ```

4. 在 Hugo 输出的本地地址检查文章与图片。

准备发布时移除 `draft: true` 或改为 `false`。发布前检查见[检查、构建与发布](../dev/README.md)。

## 文章约定

文件名使用 `YYYY-MM-DD-slug.md`，文件名日期与 `date` 一致。

```yaml
---
title: "中文标题"
slug: "english-slug"
date: YYYY-MM-DDTHH:MM:SS+08:00
categories: ["coding"]
tags: ["tag1", "tag2"]
---
```

- `slug` 使用英文小写短横线。
- `categories` 单选：coding / life / efficiency / thinking / viewpoint / managment / fun。
  近期文章也出现过中文 category，可跟随同期文章。
- 存稿使用 `draft: true`。
- Typora 可添加 `typora-copy-images-to: ../../static/images/YYYYMM`。

文风与结构以 [STYLE.md](../../STYLE.md) 为主。编辑既有文章时只改目标内容，
不要顺手重排格式或统一历史写法。

## 添加图片

新图片使用 `static/images/YYYYMM/` 存放，月份与发文月份对应。
新文章统一使用 `/images/YYYYMM/name.png` 引用，图注用 `<small>` 标注来源。
图片必须被文章引用，否则无用图片检查会失败。

1. 将图片放入对应月份目录。
2. 在文章中添加图片引用。
3. 在暂存前准备文章和图片：

   ```bash
   make format-markdown
   make resize-images
   ```

   命令格式化本次 Markdown，并通过 ImageMagick 将工作区新增或修改的图片缩到 1000×1000 以内。
   只需缩图可运行 `make resize-images`，旧命令 `make resize-images-in-git-workdir` 仍可使用。
   未跟踪图片也会处理。若意外显示「已处理 0 张图片」，先检查 `git status --short`
   和图片路径，确认原因后再继续，不要直接用手工 `sips` 绕过。

4. 运行 `make check-content` 并在本地预览中检查文章与图片，再暂存文章与图片。

若缩图发生在 `git add` 之后，必须重新暂存图片，避免 index 留下未缩放版本。
历史文章的 `../../static/images/...` 路径由渲染模板兼容，不要批量改写。
[STYLE.md](../../STYLE.md) 中的相对图片路径反映历史写法，新文章按本页约定执行。

## 图表与正文标记

`mermaid` 围栏代码块渲染为实时图表，跟随明暗主题。
实现入口是 [render-codeblock-mermaid.html](../../layouts/_default/_markup/render-codeblock-mermaid.html)
和 [extend_footer.html](../../layouts/partials/extend_footer.html)。

用 `<mark>` 高亮核心观点，用 `<!-- more -->` 标记摘要截断点。
链接卡片用法见[使用 Banner 链接卡片](banner-links.md)。

返回[写作者指南](README.md)。
