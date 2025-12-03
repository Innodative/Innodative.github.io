#!/usr/bin/env python
# -*- coding: utf-8 -*-

AUTHOR = 'Your Name'
SITENAME = 'The Innodative Disruptor'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'

# Plugin settings
PLUGIN_PATHS = ['plugins']
PLUGINS = ['tufte_tags']

# Feed generation (disabled for development)
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme settings
THEME = 'themes/tufte'

# Pagination
DEFAULT_PAGINATION = 10

# Static paths
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/.nojekyll': {'path': '.nojekyll'},
    'extra/CNAME': {'path': 'CNAME'},
}

# URL settings for clean URLs
ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Disable unnecessary pages
AUTHOR_SAVE_AS = ''
TAG_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''

# Category settings - each topic gets its own page
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'

# Menu items - we'll define custom navigation
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Define the topic categories for navigation (in display order)
# Research, Teaching, and Consulting are now static pages, not blog categories
TOPICS = [
    ('Thoughts', 'thoughts'),
    ('HowTos', 'howtos'),
]

# Default category for articles without one specified
DEFAULT_CATEGORY = 'uncategorized'

# Markdown extensions for sidenotes
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {
            'title': 'Contents',
        },
    },
    'output_format': 'html5',
}
