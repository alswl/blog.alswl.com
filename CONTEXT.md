# 工程审计与工具链重构

## 目标与授权

2026-10-19，先审计仓库的工程实现，用户要求将结论记入本文并进入修复。
随后用户明确允许大幅重构，并指出 `hack/` 的脚本入口本身有使用成本。

仓库仍以内容写作为中心。此次收敛环境、检查和发布工具，不改写历史文章，不升级 Hugo。

## 审计发现与处理

| 原问题                                            | 处理结果                                         |
| ------------------------------------------------- | ------------------------------------------------ |
| 格式化脚本会把同文件未暂存草稿一并 `git add`      | 格式化只改工作区；hooks 只读检查 Git 快照        |
| 图片解码或缩图失败被忽略                          | 失败返回错误；缩图先写临时文件，成功才替换原图   |
| 无用图片正则跨属性、跨行，basename 匹配掩盖碰撞   | 统一引用提取，按路径匹配，兼容明确的历史目录映射 |
| 远端图片漏检引用式 Markdown、单引号与多行 HTML    | 同一图片模块识别这些写法，并跳过围栏和行内代码   |
| 文件列表在 Shell 中按空白拆分，未跟踪目录可能漏图 | Git NUL 分隔输出由 Python 解析，直接传 argv      |
| 本机 Hugo 与版本文件不一致，构建仅警告            | 显式安装并选择指定版本，本次使用 0.148.2 构建    |
| 构建后 `grep`/`sed` 改写 `public/`                | CI 构建独立发布目录，转换 CDN 后再交付部署       |
| 多次构建遗留旧哈希资源和旧页面                    | 临时目录完成构建后替换正式产物                   |
| CI 并发发布、图片和文章验收脱节                   | 同分支并发控制；部署后按推送范围验收页面和图片   |
| Atom self 指向 index.xml                          | 修为 atom.xml                                    |
| 历史图片路径用包含匹配与固定偏移截断              | 仅转换明确的 ../../static/ 前缀                  |
| Waline/Mermaid 主版本别名随时间变化               | 固定为原别名查询所得的 2.15.8 / 11.17.2          |

## 最终工具链

- 日常入口为 `make help`；Python 入口为 `python3 -m scripts`。
- 作者动线：`make setup` → 写稿/`make serve` → `make prepare` → `make check` → 手动提交。
- 链接卡片补图：`make enrich post=content/posts/YYYY-MM-DD-slug.md`。
- `hack/` 原有 7 个脚本已移除；卡片抓取实现迁入 `scripts/banners.py`。
- Makefile 只做命令映射，保留 `build-production`、`resize-images-in-git-workdir` 兼容别名。
- Python 工具只用标准库，无 pip 或虚拟环境要求。基础环境为 Python 3.10+、Node/npm、Git、ImageMagick。

用户指出原来的 tools/blog 嵌套不符合常见工程布局，已收敛为单层 `scripts/`：
实现模块和 publishing.json 就近存放，`tests/` 与 `.github/workflows/` 保持独立。
Python 内部入口为 `python3 -m scripts`，日常 Makefile 命令保持一致。

实现职责：`cli.py` 调度、`git.py` 文件范围/快照、`runtime.py` 工具版本与安装、
`images.py` 图片引用与处理、`publishing.py` 发布转换与验收、`banners.py` 可选联网补图。

## 关键约定

1. `.hugo-version`、`.prettier-version` 为唯一版本来源，工具缓存于 `.cache/tools/`。
   `setup` 显式联网安装，Hugo 校验 SHA-256；普通命令不自动下载或降级使用系统其他版本。
2. 范围区分工作区、暂存快照、推送提交和全量历史。pre-commit 不读取未暂存草稿，
   pre-push 检查 stdin 中实际推送的引用，不假定是当前分支。删除分支、gh-pages 不运行内容检查。
3. 格式和图片尺寸只查选定范围，无用图片保持全量与既有目录豁免。
   旧 `upload_dropbox/YYYYMM/` 保留到 `YYYYMM/`、`YYYY/MM/` 的兼容映射，不用任意 basename 兜底。
4. 发布设置在 `scripts/publishing.json`，站点 baseURL 由 Hugo 读取，不重复存储。
   本地构建到 public/；CDN 发布构建只在 CI 执行，产物为 `.cache/publish/`。
5. 图片同步仍为 `make sync-images` 显式操作，不把对象存储凭据放入仓库或自动同步。
   `make verify base=<发布前提交>` 同时检查本次已发布文章和 CDN 图片，记录 UTC 时间并重试。
   验收窗口内未就绪与部署上传失败分别报告，不因一次图片 404 宣布发布失败。
6. 浏览器依赖版本在对应 partial 的 import URL 中固定。2026-10-19 查询原有
   [Waline @v2](https://unpkg.com/@waline/client@v2/package.json) 与
   [Mermaid @11](https://cdn.jsdelivr.net/npm/mermaid@11/package.json) 后选取当时实际解析的版本。

## 验证与状态

- 已实际安装并运行 Hugo 0.148.2、Prettier 3.9.6；`make setup` 可重复运行。
- 35 个工具链回归用例通过，覆盖暂存边界、推送分支、force push、首次推送、空格/重命名、
  图片引用、损坏与多帧图片、缩图失败保护、CDN 输出、构建失败保护与旧产物清理。
- `make check` 全量无用图片检查通过，没有批量处理历史存量。
- 指定版本生产构建成功。只保留原有非 posts 页面缺少 Markdown layout 的提示；
  不再使用本机 Homebrew Hugo 0.167.0，也不再出现由它导致的语言字段升级警告。
- 读取真实生成的 Stage 8 HTML、Markdown、Atom、RSS，纯函数转换后的图片 URL 均使用 CDN，
  XML 仍可解析，Atom self 为 https://blog.alswl.com/atom.xml；未手工编辑 public/。
- 文档与 AGENTS.md 已同步新动线。尚未提交、推送、上传图片或触发线上部署。
- CI 配置已接入新入口；GitHub Actions 和远端部署尚未实际执行，首次提交后需观察运行结果。

详细操作以 [站点维护](docs/dev/README.md) 和 [写文章与配图](docs/guide/writing.md) 为准。

## 发布后图片回源（2026-10-19）

用户明确要求 CI 发布后触发 CDN 回源。已在 master 的 Deploy 与 Verify 之间加入
`make warm-images`，按同一次 push 的基线选择新增/修改的图片，含 Banner 和 SVG。
先重试等待站点图片可访问，再完整 GET CDN 图片，以触发缓存未命中回源。
正文分块读取，拒绝 HTML 错误页和空响应，记录 UTC 时间并重试；无图片改动时不发请求。

已只读查询仓库 Actions Secrets 名称，目前仅有 ACCESS_TOKEN，没有七牛 CDN 密钥。
因此 CI 默认 GET 模式即可工作；成对配置 QINIU_ACCESS_KEY、QINIU_SECRET_KEY 后，
自动先提交七牛官方预热任务，再请求 CDN 图片。不改动现有 Secret，不推断其用途。
官方 API 受理不等于全网任务完成，普通 GET 也不刷新已有旧缓存。错误与上传部署分开报告。
凭据、HTTP、分批请求、站点就绪顺序和跳过行为均有隔离测试，未实际提交官方预热任务。

此前图片流程诊断仍需后续处理：缩图反复编码 JPEG；缺少引用图片存在性检查；
Banner 尚未生成适合 78px 显示的缩略图；文件哈希在下载原始数据时计算，后续缩图改写内容。
这些问题尚未因本次 CI 回源接入而解决。

## 工具链消融（2026-10-19）

按用户要求先补首次安装、Banner 抓取和 CDN 批量转换的测试，再继续消融。
新增 10 个测试，共 45 个；也覆盖暂存后工作区删除、首次推送 hook。
逐项删除、验证、恢复，共 12 项。第一轮五个绿灯中的三个在补测后变红，
说明原测试缺口会掩盖安装与暂存边界退化。最终只删除 image_urls 的重复去重、
hook 中重复的首次推送基线转换；十项保护保留，并补充必要原因注释。

实验与范围见 [工具链消融记录](docs/dev/toolchain-ablation.md)。
测试证明当前契约的行为，不能证明全部新功能的必要性；自维护安装器与可选七牛 API
仍是规模取舍候选，替代安装方案或取消 API 模式不属于本轮只删不改实验。

## 命令与版本策略调整（2026-10-19）

用户指出 setup / prepare / check / build 含义模糊，不需要本地和 CI 精确同版，
要求 CI 更新到最新。此前精确固定版本与暂不升级策略由此更新：

- 删除自建 Hugo 下载校验安装器、工具缓存选择、版本文件及精确版本拦截。
  本地使用 PATH 的 Hugo、仓库 node_modules 或 PATH 的 Prettier；安装交给包管理器。
- init-theme、install-hooks 各自只做一个动作。删除 setup 和 prepare 组合入口。
  format-markdown、resize-images、check-content、build-site、build-publication 明示操作对象。
- CI 用 actions-hugo latest 和 npm prettier@latest，输出实际版本，不复用旧工具缓存。
- 保留新版 Hugo 的中文语言配置，接受既有记录中的本地化和默认值差异；不再为产物完全一致锁旧版。
  旧归档月份锚点变化仍是已知影响。
- 删除仅用于自建安装器的测试，改测无需版本文件、工具缺失提示、本地 Prettier 优先和新版本可用。

这轮是根据用户需求收缩功能契约，不属于上一轮“只删不改”的消融结论。

本轮验证：45 个测试、check-content、doctor、ruff 和本地 Hugo 0.167.0 构建通过。
最新版 Prettier 在线安装受 npm 镜像及官方源超时影响，随后从本机 npm 缓存离线安装
Prettier 3.9.6 到 node_modules，未改变全局 npm 配置；CI 仍安装 latest。
最新版 Hugo 下载未完成，新 GitHub Actions 尚未执行，不宣称线上已验收。

## 发布后暖图简化（2026-10-19）

用户明确指出 warm-images 只需要 curl 访问。已取消可选七牛官方预热、签名和分批 API、
CI 密钥传递、站点预探测及暖图中的重复图片验收逻辑。
现在只选择本次变更的 CDN 图片，逐个 curl GET 丢弃正文，单请求最长 30 秒，HTTP 错误返回失败；
失败后继续请求其余图片，无图片修改则跳过。独立 verify 继续负责带时间戳和重试的发布验收。
普通 GET 不强制刷新旧缓存，也不代表全网预热。此前对应功能的消融保留结论属于旧契约，
本轮按照用户决定缩小功能范围。

验证：38 个测试和 check-content 通过；本机 HTTP 服务实测 curl GET、空格 URL 编码、404 失败及继续请求行为通过，未访问真实 CDN。
