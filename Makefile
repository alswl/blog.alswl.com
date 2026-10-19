PYTHON ?= python3
BLOG := $(PYTHON) -B -m scripts
.DEFAULT_GOAL := help

export BLOG_POST_NAME = $(name)
export BLOG_POST = $(post)
export BLOG_VERIFY_URL = $(url)
ifneq ($(base),)
export CHANGED_FILES_BASE = $(base)
endif

.PHONY: help doctor init-theme install-hooks new serve format-markdown resize-images check-content check-changed-content audit-content build-site build-publication enrich sync-images warm-images verify clean test build-production resize-images-in-git-workdir

help doctor serve format-markdown resize-images check-content build-site build-publication clean test sync-images warm-images:
	@$(BLOG) $@

init-theme:
	git submodule sync -- themes/hugo-PaperMod
	git submodule update --init -- themes/hugo-PaperMod

install-hooks:
	lefthook install

new:
	@$(BLOG) new

enrich:
	@$(BLOG) enrich

check-changed-content:
	@$(BLOG) check-content --changed-only

audit-content:
	@$(BLOG) check-content --scope all

verify:
	@$(BLOG) verify

# Compatibility with author commands that predate the toolchain refactor.
build-production: build-site
resize-images-in-git-workdir: resize-images
