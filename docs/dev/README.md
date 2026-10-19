# 站点维护

日常入口是 `make help`。作者不需要记住脚本名、依赖安装路径或文件列表参数。
Makefile 只转发命令，具体实现集中在 [scripts/](../../scripts/)。

仓库按 Hugo 内容站点组织：`content/` 写文章，`static/` 放资源，`layouts/` 和 `assets/`
维护页面；`scripts/` 放内部自动化实现，`tests/` 放回归测试，`.github/workflows/` 负责 CI。
作者从 Makefile 调用命令，维护者在 scripts 内按职责修改实现。
工具链精简的验证依据见[消融记录](toolchain-ablation.md)。

## 安装与诊断

需要 Git、Python 3.10+、Hugo、Node.js/npm 和 ImageMagick。
macOS 可使用系统包管理器安装：

```bash
brew install hugo node imagemagick
npm install --no-save --package-lock=false --ignore-scripts --no-audit --no-fund prettier@latest
make init-theme
make doctor
```

Linux 使用包管理器安装 Node.js 和 ImageMagick，Hugo 按[官方安装说明](https://gohugo.io/installation/)
安装。Prettier 安装到仓库的 `node_modules/`，已被 Git 忽略；也支持 PATH 中已有的 Prettier。
Hugo 直接使用 PATH 中的程序。本地不要求与 CI 精确同版，不自动下载或升级工具。
`doctor` 显示实际使用的路径和版本；出现差异时可据此排查。
Prettier 配置见 [.prettierrc](../../.prettierrc)，不要重排历史文章。

Git hooks 可选，安装 lefthook 后运行 `make install-hooks`；图片同步使用 AWS CLI
和已配置的访问凭据。主题初始化、安装 hooks 和依赖安装分别执行，没有组合 setup 命令。

浏览器端依赖也使用精确版本：Waline `2.15.8`、Mermaid `11.17.2`，分别在对应 partial 的
import URL 中声明。它们是 2026-10-19 查询原有 `@v2`、`@11` 别名时实际返回的版本。

## 作者日常流程

```bash
make format-markdown  # 格式化本次修改的 Markdown
make resize-images    # 将本次修改的图片缩到 1000×1000 以内
make check-content    # 检查内容格式、远端图片、尺寸和全量无用图片
make build-site       # 生产构建至 public/
```

检查后照常 `git add`、`git commit`、`git push`。
格式化和缩图都只修改工作区，不自动暂存内容。
若图片已暂存，缩图后需要重新暂存；`make format-markdown` 和 `make resize-images` 可单独运行。
旧命令 `make build-production`、`make resize-images-in-git-workdir` 保留为别名。

`make build-site` 先构建到临时目录，成功后替换 `public/`，防止旧文章和旧哈希资源残留。
失败时保留上次成功产物。`make clean` 清理构建产物。
不要手工编辑或提交 `public/`。

## 检查范围

所有入口使用同一套文件范围计算；文件名通过 Git 的 NUL 分隔输出传递，支持空格和重命名。

| 入口                                          | 检查的内容                                       | 是否修改内容  |
| --------------------------------------------- | ------------------------------------------------ | ------------- |
| `make format-markdown` / `make resize-images` | 未提交修改，包含暂存、未暂存及未跟踪文件         | 格式化 / 缩图 |
| `make check-content`                          | 未提交修改，加全量无用图片检查                   | 否            |
| `make check-changed-content`                  | 未提交修改，跳过全量无用图片检查                 | 否            |
| pre-commit                                    | 暂存快照中的本次文件，不读取未暂存草稿           | 否            |
| pre-push                                      | 实际推送提交与远端提交的差异，加全量无用图片检查 | 否            |
| CI                                            | 推送前后提交的差异，加全量无用图片检查           | 否            |
| `make audit-content`                          | 全量历史内容，预期存在存量问题                   | 否            |

格式、远端图片和尺寸检查只覆盖选定范围。历史未格式化文章、超规格图片和远端引用
不批量修复。无用图片检查保留全量执行及历史目录豁免，按路径识别图片，兼容
`upload_dropbox/YYYYMM/` 对应的两种旧目录布局。

远端图片检查覆盖 Markdown 内联、引用式图片、HTML 图片和封面字段；跳过围栏与行内代码。
尺寸检查验证所有帧，损坏图片会报错。缩图先写临时文件，成功后才替换原图。

提交钩子检查暂存快照，不自动格式化或 `git add`。部分暂存的文章不会混入草稿；
格式失败时运行 `make format-markdown`，检查并重新选择要暂存的修改。
pre-push 通过 [lefthook 的 stdin 支持](https://lefthook.dev/configuration/use_stdin/)
读取实际推送的引用，不假定推送的一定是当前分支。删除分支和 `gh-pages` 不进行内容检查。

首次推送新分支以 `origin/master` 的共同祖先为基线；没有基线的新仓库检查整个提交。
指定的基线不可用时明确报错，不静默跳过检查。
需要显式选择范围时使用统一入口：

```bash
python3 -m scripts check-content --scope staged
python3 -m scripts check-content --scope push --base <commit>
```

## CI 与发布

[CI](../../.github/workflows/ci.yml) 安装最新稳定版 Hugo 和最新 Prettier，输出工具版本，
执行回归测试、本次推送检查和发布构建。同一分支的新任务取消旧任务。
Hugo 使用 [actions-hugo 的 latest 选项](https://github.com/peaceiris/actions-hugo#%EF%B8%8F-use-the-latest-version-of-hugo)，
Prettier 使用 npm 的 latest 标签；不缓存旧工具安装目录。
本地与 CI 共享检查和构建实现，允许版本存在差异。

发布配置集中在 [scripts/publishing.json](../../scripts/publishing.json)：CDN URL、
对象存储 endpoint 和 bucket。站点 URL 由 Hugo 读取 `config.yaml` 的 `baseURL`，不重复配置。
配置中不保存凭据。

CI 专用发布构建命令：

```bash
python3 -m scripts build-publication
```

该命令先运行 Hugo，再在独立临时产物中转换 CDN 地址，完成后生成 `.cache/publish/`。
转换覆盖 HTML、订阅输出、Markdown 导出和链接卡片图片；不会修改本地 `public/`。
`master` 构建成功后发布到 GitHub Pages，其他分支只构建。
旧的独立 `make cdn` 命令已移除；不再用 `grep`/`sed` 修改已生成的本地产物。

## 图片同步与发布验收

图片同步仍是显式操作，需要时运行：

```bash
make sync-images
```

命令将 `static/images/` 同步到配置中的对象存储，不删除远端对象。
CI 不持有或自动配置对象存储上传凭据。

`master` 发布成功后，CI 自动运行 `make warm-images`：先等待站点对应图片可访问，
再对本次新增或修改的 CDN 图片发起完整 GET，读取图片正文，缓存未命中时触发回源。
包含 Banner 图片和 SVG，不扫描全站；没有图片改动则跳过。
请求会记录 UTC 时间并重试，HTTP 200 的 HTML 错误页、空图片和读取失败都视为未成功。
回源步骤失败后仍继续独立验收，CI 报告警告，不将其误报为部署上传失败。

普通 GET 只触发请求所经节点的缓存未命中回源，命中已有缓存时不会强制刷新。
需要七牛官方 CDN 预热时，在 GitHub 仓库 Actions Secrets 中成对添加
`QINIU_ACCESS_KEY`、`QINIU_SECRET_KEY`，密钥须有当前 CDN 域名的预取权限。
CI 会自动使用它们分批提交 [七牛预热任务](https://developer.qiniu.com/fusion/13367/fusion-api-cache-management)，
再请求图片；日志中的 requestId 表示任务已受理，不代表所有节点已预热完成。
凭据不完整或 API 返回错误会明确报错，不输出密钥。未配置这对 Secrets 时，GET 模式仍可运行。
该操作不覆盖同一 URL 的旧缓存；已有 URL 内容变更时需单独刷新缓存，或改用新文件名。

手动针对某次发布执行相同行为：

```bash
make warm-images base=<发布前提交>
```

发布后同时验收本次文章页和 CDN 图片，指定发布前提交作为基线：

```bash
make verify base=<发布前提交>
make verify base=<发布前提交> url=https://blog.alswl.com/2026/10/example/
```

文章 URL 由已安装的 Hugo 的已发布内容清单取得，跳过草稿。
工具记录每次观测的 UTC 时间，默认尝试 4 次，间隔 15 秒；没有文章或图片改动时检查首页。
CI 的回源步骤之后也运行相同验收。窗口结束仍未就绪时给出警告，与部署上传步骤失败分开报告。
首次图片 404 可能是同步或 CDN 传播延迟，不凭一次 404 宣布发布失败。
若显式同步报认证或上传错误，如实报告，由负责人判断是否已有其他同步在传播。

## 工具链维护

实现分为五个职责：

- [cli.py](../../scripts/cli.py)：命令调度与作者提示。
- [git.py](../../scripts/git.py)：范围计算、暂存及推送快照。
- [runtime.py](../../scripts/runtime.py)：已安装工具查找与系统依赖。
- [images.py](../../scripts/images.py)：图片引用、门禁和缩图。
- [publishing.py](../../scripts/publishing.py)：发布产物转换和验收。

链接卡片抓取是 [banners.py](../../scripts/banners.py)，通过 `make enrich post=...` 调用。
Python 工具只使用标准库，不需要 pip、虚拟环境或额外 Python 包管理器。
修改工具链后运行 `make test`、`make check-content` 和 `make build-site`。
回归测试见 [tests/test_blog_tools.py](../../tests/test_blog_tools.py)。

## Hugo 升级行为

仓库已记录的 0.148.2 → 0.166.0 实验会改变线上产物。
`config.yaml` 中的 `languageCode: zh` 在 Hugo 0.158.0 起被弃用，
并会实际驱动主题 i18n：

1. 归档月份从英文变为中文，锚点也随之改变。
   例如 `#2009-December` 变为 `#2009-%e5%8d%81%e4%ba%8c%e6%9c%88`，已有深链会失效。
2. 面包屑 `Home` 变为 `主页`，分页 `Next` 变为 `下一页`。
3. Google Analytics 的 `respectDoNotTrack` 默认值从 `false` 变为 `true`。

若想升级并保持上述行为，需要将 `languageCode` 改为 `en`，并显式设置
`privacy.googleAnalytics.respectDoNotTrack: false`。但这又会使 `og:locale`
从 `zh` 变为 `en`，无法同时保留这些行为。此前选择暂不升级。2026-10-19 用户调整策略为 CI 跟随最新版，本地允许版本差异，
因此不再为保持旧产物而锁定 0.148.2。保留 `languageCode: zh`，接受上述本地化与默认行为变化，
不以改成英文规避升级。历史归档月份深链可能发生变化，旧实验仍作为行为记录保留。

返回[文档首页](../README.md)。
