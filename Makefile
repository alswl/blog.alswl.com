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

# DEPLOY_LOG := deploy.log


.PHONY: build-production
build-production:
	HUGO_ENV=production $(HUGO)


# no need any more, use cdn upstrem mirror
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
	@echo images is remote:
	bash ./hack/find-remote-images.sh


.PHONY: resize-images-in-git-workdir
resize-images-in-git-workdir:
	@echo resize images in git worktree;
	bash ./hack/resize-images-in-git-workdir.sh
