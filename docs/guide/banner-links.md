# 使用 Banner 链接卡片

给独立成行的 Markdown 链接加 `!banner` title，即可显示为卡片。
图片和描述可留空，渲染时不会联网。图片为空或本地文件不存在时，显示灰色地球占位图。
右侧依次显示标题、描述和网站名，缺少描述时省略。链接文字作为标题。文字为空或仅为 URL 时显示目标 URL。
网站名显示目标域名，站内链接显示站点名。

本地预览使用仓库图片，CI 发布产物会将图片地址转换为 CDN URL。
发布后，本次新增或修改的 Banner 图片与普通配图一起自动请求回源并验收，
详见[图片同步与发布验收](../dev/README.md#图片同步与发布验收)。

```markdown
[项目主页](https://example.com "!banner")
[项目主页](https://example.com "!banner (/images/202610/project.jpg) 这里是描述")
```

## 补充图片和描述

补图命令只处理独立成行的 `!banner` 标记，并跳过代码块。
以下命令在仓库根目录执行，文章路径按需替换。

1. 抓取卡片的图片和描述：

   ```bash
   make fetch-banner-metadata post=content/posts/2026-10-18-ai-native-stage-8.md
   ```

2. 缩放抓取到的图片：

   ```bash
   make format-markdown
   make resize-images
   ```

3. 在本地预览中核对卡片。
4. 检查改动后暂存文章与图片。

缩图和暂存顺序见[写文章与配图](writing.md#添加图片)。

## 重试与缓存

只重新尝试缺图卡片（包括已缓存但页面没有提供图片的情况）：

```bash
python3 -m scripts enrich --retry-missing content/posts/2026-10-18-ai-native-stage-8.md
```

脚本优先读取 Open Graph，其次读取 Twitter Card 和普通 description。图片保存到文章月份目录。
没有分享图时尝试正文首图或 oEmbed 缩略图。YouTube 可通过 oEmbed 补充缩略图。
抓取失败时保留原链接。图片失败时仍保存已取得的描述。
成功的页面信息和图片路径缓存在 `.cache/banner-metadata/`（不提交）。再次运行同一命令时，
只重试失败的请求。图片失败会复用页面信息，仅重新下载图片，本地图片被删除后也会重新下载。
页面本身没有图片或描述时保留空元数据，结果也会缓存。已有本地图片且没有缓存的标记默认保留。
需要强制更新全部结果时，加 `--refresh`：

```bash
python3 -m scripts enrich --refresh content/posts/2026-10-18-ai-native-stage-8.md
```

返回[写作者指南](README.md)。
