SHELL := /bin/bash
HUGO := hugo
QSHELL := qshell
PUBLIC_FOLDER := public/
UPDATE_FOLDER := static/images/
BUCKET = blog-alswl-com-202210
# CLOUDFRONT_ID := ABCDE12345678
DOMAIN = blog.alswl.com
SITEMAP_URL = https://blog.alswl.com/sitemap.xml

# DEPLOY_LOG := deploy.log

.PHONY: build-production
build-production:
	HUGO_ENV=production $(HUGO)

deploy: build-production
	echo "Copying files to server..."
	# $(QSHELL) s3 sync $(PUBLIC_FOLDER) $(BUCKET) --size-only --delete | tee -a $(DEPLOY_LOG)
	echo $(QSHELL) qupload2 --src-dir=$(shell pwd)/$(UPDATE_FOLDER) --bucket=$(BUCKET)

	# filter files to invalidate cdn
	# grep "upload\|delete" $(DEPLOY_LOG) | sed -e "s|.*upload.*to $(S3_BUCKET)|/|" | sed -e "s|.*delete: $(S3_BUCKET)|/|" | sed -e 's/index.html//' | sed -e 's/\(.*\).html/\1/' | tr '\n' ' ' | xargs aws cloudfront create-invalidation --distribution-id $(CLOUDFRONT_ID) --paths


	# curl --silent "http://www.google.com/ping?sitemap=$(SITEMAP_URL)"
	# curl --silent "http://www.bing.com/webmaster/ping.aspx?siteMap=$(SITEMAP_URL)"

