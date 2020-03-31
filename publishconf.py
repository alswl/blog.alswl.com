#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://blog.alswl.com'
RELATIVE_URLS = False

#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

PLUGINS = [
    'pelican-toc',
    'summary',
    'footer_insert',
    'feed_footer_insert',
    'minify',
    'yuicompressor',
    'table_with_div',
    'render_math',
    'pandoc_reader',
]

# Following items are often useful when publishing

DISQUS_SITENAME = "log4d"
#GOOGLE_ANALYTICS = ""
