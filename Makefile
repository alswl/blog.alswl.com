PYTHON ?= python3
BLOG := $(PYTHON) -B -m scripts
.DEFAULT_GOAL := help

export BLOG_POST_NAME = $(name)
export BLOG_POST = $(post)
export BLOG_VERIFY_URL = $(url)
ifneq ($(base),)
export CHANGED_FILES_BASE = $(base)
endif

.PHONY: help init-theme install-git-hooks check-tools new-post preview-site fetch-banner-metadata format-markdown resize-images check-content build-site upload-images warm-cdn-images verify-publication build-cdn-site test-toolchain clean-build build-production resize-images-in-git-workdir

help: ## 显示命令、处理范围和副作用
	@awk 'BEGIN {FS = ":.*## "} /^##@/ {printf "\n%s\n", substr($$0, 5)} /^[a-zA-Z0-9_-]+:.*## / {printf "  make %-24s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

##@ 环境
init-theme: ## 下载或更新主题 submodule 到仓库记录的提交
	git submodule sync -- themes/hugo-PaperMod
	git submodule update --init -- themes/hugo-PaperMod

install-git-hooks: ## 安装提交与推送检查钩子，需要已安装 lefthook
	lefthook install

check-tools: ## 只读：显示 Hugo、Prettier 等依赖的实际版本和路径
	@$(BLOG) doctor

##@ 写文章
new-post: ## 新建草稿：name=YYYY-MM-DD-slug.md，写入 content/posts/
	@$(BLOG) new

preview-site: ## 启动本地预览服务器，包含草稿
	@$(BLOG) serve

fetch-banner-metadata: ## 联网抓取卡片图片与描述，修改文章：post=content/posts/…
	@$(BLOG) enrich

##@ 提交前（本次修改包含已暂存、未暂存和未跟踪文件）
format-markdown: ## 修改本次 Markdown 的格式，不自动暂存
	@$(BLOG) format-markdown

resize-images: ## 修改本次配图，缩到 1000×1000 以内，不自动暂存
	@$(BLOG) resize-images

check-content: ## 只读：检查本次格式、远端图片、尺寸，以及全量无用图片
	@$(BLOG) check-content

build-site: ## 用生产配置生成 public/，成功后替换旧产物
	@$(BLOG) build-site

##@ 发布图片与验收
upload-images: ## 上传 static/images/ 到对象存储，不删除远端文件，需要凭据
	@$(BLOG) sync-images

warm-cdn-images: ## curl GET 本次发布的 CDN 图片：base=<发布前提交>
	@$(BLOG) warm-images

verify-publication: ## 只读：重试验收文章页与 CDN 图片：base=<发布前提交> [url=…]
	@$(BLOG) verify

##@ 维护与 CI
build-cdn-site: ## 仅 CI：构建 .cache/publish/ 并替换图片 CDN 地址，不执行部署
	@$(BLOG) build-publication

test-toolchain: ## 运行 scripts/ 的回归测试
	@$(BLOG) test

clean-build: ## 删除 public/、.cache/publish/ 和 Hugo 构建锁
	@$(BLOG) clean

# Preserve commands used before this refactor; keep them out of daily help.
build-production: build-site
resize-images-in-git-workdir: resize-images
