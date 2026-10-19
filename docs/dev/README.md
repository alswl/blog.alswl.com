# 站点维护

本页面向博客维护者，也供作者在发布前查询检查流程。
命令与实现以 [Makefile](../../Makefile)、[hack/](../../hack/)
和 [CI 配置](../../.github/workflows/ci.yml)为准。

## 本地工具

- Hugo 版本由 [.hugo-version](../../.hugo-version)指定，当前为 `0.148.2`。
  本地版本不一致时，`make` 会警告，但不阻断预览或构建。
- Prettier 版本由 [.prettier-version](../../.prettier-version)指定，当前为 `3.9.6`。
  格式脚本通过 `npx` 调用该版本，需要 Node.js/npm。
- 检查使用 Python 3 和 Bash。缩图需要 ImageMagick 7 的 `magick`。
- 图片对象存储同步使用 AWS CLI，需要已配置的访问凭据。

版本文件是唯一来源。Prettier 配置见 [.prettierrc](../../.prettierrc)，不要因上游发版重排历史文章。

## Hugo 升级约束

仓库已记录的 0.148.2 → 0.166.0 实验会改变线上产物。
`config.yaml` 中的 `languageCode: zh` 在 Hugo 0.158.0 起被弃用，
并会实际驱动主题 i18n：

1. 归档月份从英文变为中文，锚点也随之改变。
   例如 `#2009-December` 变为 `#2009-%e5%8d%81%e4%ba%8c%e6%9c%88`，已有深链会失效。
2. 面包屑 `Home` 变为 `主页`，分页 `Next` 变为 `下一页`。
3. Google Analytics 的 `respectDoNotTrack` 默认值从 `false` 变为 `true`。

若想升级并保持上述行为，需要将 `languageCode` 改为 `en`，并显式设置
`privacy.googleAnalytics.respectDoNotTrack: false`。但这又会使 `og:locale`
从 `zh` 变为 `en`，无法同时保留这些行为。当前选择是先不升级。

## 发布前检查

1. 格式化本次改动的 Markdown：

   ```bash
   make format
   ```

2. 运行门禁：

   ```bash
   make check
   ```

3. 构建生产产物：

   ```bash
   make build-production
   ```

检查完成后，在本地预览中核对文章和图片，再提交改动。
`make clean` 会删除 `public/` 和 `.hugo_build.lock`。

`make check` 包含 `make check-changed` 和全量无用图片检查。
只需快速检查本次改动时，单独运行 `make check-changed`。
日常格式、远端图片和尺寸检查只作用于本次改动。
[changed-files.sh](../../hack/changed-files.sh)计算改动范围，包含工作区未提交文件。
历史文章存在未格式化内容、超规格图片和远端图片引用，不要为通过门禁批量修复。

无用图片检查是例外：`hack/find-unused-images.py` 通过 `EXCLUDE_DIRS` 排除历史目录，
仍需全量执行。`make audit` 用于全量存量报告，预期有历史问题，不作为门禁。

## 提交与 CI

[lefthook](../../lefthook.yaml) 的 pre-commit 对暂存的 Markdown 运行格式化，
并检查非 ASCII 文件名。pre-push 运行 `make check-changed`。
改完 Markdown 可以直接提交，pre-commit 会处理格式。

每次 push 后，GitHub Actions 依次运行无用图片检查、本次改动检查和构建。
`master` 分支构建成功后发布到 GitHub Pages。

## 图片同步与发布验收

图片缩放与暂存顺序见[添加图片](../guide/writing.md#添加图片)。
需要同步对象存储时运行：

```bash
make sync-images
```

命令将 `static/images/` 同步到对象存储。
CI 在构建后运行 `make cdn`，将产物的 `/images/` 前缀改为
`https://e25ba8-log4d-c.dijingchao.com`。只在 CI 里运行该命令，
不要在本地对 `public/` 手工执行。

发布后同时检查文章页和 CDN 图片。首次图片 404 可能只是对象同步或 CDN 传播延迟。
记录观测时点，区分持续失败与正常延迟，不要仅凭一次探测宣布发布失败。
若同步命令报认证或上传错误，如实报告，由负责人判断是否已有其他同步在传播。

## 维护入口

- [Makefile](../../Makefile)：命令定义。
- [hack/](../../hack/)：检查、缩图与元数据抓取脚本。
- [layouts/](../../layouts/)：主题模板覆盖。
- [AGENTS.md](../../AGENTS.md)：agent 执行规则。

主题通过 `themes/hugo-PaperMod` submodule 维护。
`public/` 是被 Git 忽略的构建产物，不要手工编辑或提交。

返回[文档首页](../README.md)。
