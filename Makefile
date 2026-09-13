SHELL := /bin/bash
SED=$(shell which gsed || which sed)
HUGO := hugo
PUBLIC_FOLDER := public/
UPDATE_FOLDER := static/images/
# CP is ( in bash, solution from https://stackoverflow.com/a/40751291
CP := (

QSHELL := qshell
BUCKET = blog-alswl-com-202210
CDN_HOST = https://e25ba8-log4d-c.dijingchao.com
DOMAIN = blog.alswl.com
SITEMAP_URL = https://blog.alswl.com/sitemap.xml

.PHONY: build-production
build-production: check-hugo-version
	HUGO_ENV=production $(HUGO)

.PHONY: serve
serve: check-hugo-version
	$(HUGO) serve -D

.PHONY: clean
clean:
	rm -rf $(PUBLIC_FOLDER) .hugo_build.lock

# 本地 hugo 与 .hugo-version 不一致时只警告，不阻断写作
.PHONY: check-hugo-version
check-hugo-version:
	@want=$$(cat .hugo-version); \
	got=$$($(HUGO) version | sed -E 's/.*hugo v([0-9.]+).*/\1/'); \
	if [ "$$want" != "$$got" ]; then \
		echo "警告: 本地 hugo $$got 与 .hugo-version ($$want) 不一致，本地预览可能与线上有差异"; \
	fi

# CI 与 pre-push 的门禁：全量的无用图片检查 + 针对本次改动的增量检查。
# 必须保持绿色。
.PHONY: check
check: check-changed
	python3 hack/find-unused-images.py

# 只检查本次改动引入的文件。
# 仓库有大量历史存量（384 篇未格式化文章、77 张超规格图片、15 处远端图片引用），
# 全量门禁会立刻失败，所以门禁一律是增量的。存量用 make audit 查看。
.PHONY: check-changed
check-changed:
	@files=$$(bash ./hack/changed-files.sh); \
	md=$$(echo "$$files" | grep '\.md$$' || true); \
	img=$$(echo "$$files" | grep -E '^static/images/.*\.(png|jpg|jpeg|gif|webp)$$' || true); \
	rc=0; \
	if [ -n "$$md" ]; then \
		bash ./hack/format.sh --check $$md || rc=1; \
		bash ./hack/find-remote-images.sh $$md || rc=1; \
	else \
		echo "本次没有改动 Markdown"; \
	fi; \
	if [ -n "$$img" ]; then \
		bash ./hack/check-image-size.sh $$img || rc=1; \
	else \
		echo "本次没有改动图片"; \
	fi; \
	exit $$rc

# 格式化本次改动的 Markdown
.PHONY: format
format:
	@md=$$(bash ./hack/changed-files.sh | grep '\.md$$' || true); \
	if [ -n "$$md" ]; then bash ./hack/format.sh $$md; else echo "本次没有改动 Markdown"; fi

# 全量扫描历史存量，仅作报告，不是门禁（预期是红的）
.PHONY: audit
audit:
	-bash ./hack/find-remote-images.sh
	-bash ./hack/check-image-size.sh
	-python3 hack/find-unused-images.py


# no need any more, use cdn upstrem mirror
# cdn -> blog-assets.alswl.com -> raw.githubusercontent.com
.PHONY: sync-images
sync-images:
	echo "Copying files to server..."
	#$(QSHELL) qupload2 --log-level=info --thread-count=10 --rescan-local=true --check-exists --check-size --src-dir=$(shell pwd)/$(UPDATE_FOLDER) --bucket=$(BUCKET)
	aws s3 sync \
		--endpoint-url https://s3-cn-east-2.qiniucs.com \
		--exclude ".*" \
		--exclude "*/.*" \
		./$(UPDATE_FOLDER) s3://blog-alswl-com-202210/

.PHONY: cdn
cdn:
	# public/404.html is works as appendix, just like and 1=1 in sql
	@$(SED) -i 's#src="/images/#src="$(CDN_HOST)/#g' $(shell grep -Rl 'src="/images/' public) public/404.html
	@$(SED) -i 's#href="/images/#href="$(CDN_HOST)/#g' $(shell grep -Rl 'href="/images/' public) public/404.html
	
	@$(SED) -E -i 's#!\[([^]]+)\]\(/images/#!\[\1]\($(CDN_HOST)/#g' $(shell grep -RlE '!\[.+\]\$(CP)\/images\/' public) public/404.html

	# curl --silent "http://www.google.com/ping?sitemap=$(SITEMAP_URL)"
	# curl --silent "http://www.bing.com/webmaster/ping.aspx?siteMap=$(SITEMAP_URL)"
	@echo done

.PHONY: new
name = $(shell date +%Y-%m-%d)-new.md
new:
	$(HUGO) new "posts/$(name)" && open "content/posts/$(name)"

.PHONY: find-remote-images
find-remote-images:
	bash ./hack/find-remote-images.sh


.PHONY: resize-images-in-git-workdir
resize-images-in-git-workdir:
	@echo resize images in git worktree;
	bash ./hack/resize-images-in-git-workdir.sh
