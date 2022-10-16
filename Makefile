SHELL := /bin/bash
HUGO := hugo
QSHELL := qshell
PUBLIC_FOLDER := public/
UPDATE_FOLDER := static/images/
BUCKET = blog-alswl-com-202210
# CLOUDFRONT_ID := ABCDE12345678
CDN_HOST = https://d05fae.dijingchao.com
DOMAIN = blog.alswl.com
SITEMAP_URL = https://blog.alswl.com/sitemap.xml

# DEPLOY_LOG := deploy.log

.PHONY: build-production
build-production:
	HUGO_ENV=production $(HUGO)

deploy: build-production
	echo "Copying files to server..."
	# $(QSHELL) s3 sync $(PUBLIC_FOLDER) $(BUCKET) --size-only --delete | tee -a $(DEPLOY_LOG)
	# $(QSHELL) qupload2 --thread-count=5 --check-size --src-dir=$(shell pwd)/$(UPDATE_FOLDER) --bucket=$(BUCKET)

	gsed -i 's#src="/images/#src="$(CDN_HOST)/#g' $(shell grep -Rl 'src="/images/' public)
	gsed -i 's#href="/images/#href="$(CDN_HOST)/#g' $(shell grep -Rl 'href="/images/' public)


	# curl --silent "http://www.google.com/ping?sitemap=$(SITEMAP_URL)"
	# curl --silent "http://www.bing.com/webmaster/ping.aspx?siteMap=$(SITEMAP_URL)"

