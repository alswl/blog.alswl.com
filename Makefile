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

# 只警告不阻断：本地 hugo 由 homebrew 管理，硬拦会挡住写作
.PHONY: check-hugo-version
check-hugo-version:
	@want=$$(cat .hugo-version); \
	got=$$($(HUGO) version | sed -E 's/.*hugo v([0-9.]+).*/\1/'); \
	if [ "$$want" != "$$got" ]; then \
		echo "警告: 本地 hugo $$got 与 .hugo-version ($$want) 不一致，本地预览可能与线上有差异"; \
	fi

# 门禁，必须保持绿色（CI 与 pre-push 跑它）
.PHONY: check
check: check-changed
	python3 hack/find-unused-images.py

# 增量：历史存量会让全量门禁必然失败，存量用 make audit 单独看
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

.PHONY: format
format:
	@md=$$(bash ./hack/changed-files.sh | grep '\.md$$' || true); \
	if [ -n "$$md" ]; then bash ./hack/format.sh $$md; else echo "本次没有改动 Markdown"; fi

# 全量存量报告，预期是红的，所以不作为门禁
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
