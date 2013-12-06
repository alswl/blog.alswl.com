#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'alswl'
SITENAME = u'Log4D'
SITEURL = ''

THEME = 'pelican-bootstrap3'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (
    ('Weibo', 'http://weibo.com/alswlx'),
    ('Github', 'https://github.com/alswl'),
    ('Twitter', 'http://twitter.com/alswl'),
)

# Social widget
SOCIAL = (
    #('You can add links in your config file', '#'),
    #('Another social link', '#'),
)

DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'

FEED_ATOM = 'atom.xml'
FEED_RSS = 'rss.xml'
FEED_MAX_ITEMS = 20

DISPLAY_PAGES_ON_MENU = True

AUTHOR_BIO = 'Computers can change your life for the better.'
DISQUS_SITENAME = 'log4d'
GOOGLE_ANALYTICS = 'UA-8822123-3'
