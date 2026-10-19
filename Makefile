PYTHON ?= python3
BLOG := $(PYTHON) -B -m scripts
.DEFAULT_GOAL := help

export BLOG_POST_NAME = $(name)
export BLOG_POST = $(post)
export BLOG_VERIFY_URL = $(url)
ifneq ($(base),)
export CHANGED_FILES_BASE = $(base)
endif

.PHONY: help setup doctor new serve prepare format resize check check-changed audit build enrich sync-images warm-images verify clean test build-production resize-images-in-git-workdir

help:
	@$(BLOG) help

setup doctor serve prepare format resize check clean test sync-images warm-images:
	@$(BLOG) $@

new:
	@$(BLOG) new

enrich:
	@$(BLOG) enrich

check-changed:
	@$(BLOG) check --changed-only

audit:
	@$(BLOG) check --scope all

build:
	@$(BLOG) build

verify:
	@$(BLOG) verify

# Compatibility with existing author instructions.
build-production: build
resize-images-in-git-workdir: resize
