#!/usr/bin/env python
# -*- coding: utf-8 -*-

AUTHOR = 'Robert J. Brunner'
SITENAME = 'The Innodative Disruptor'
SITEURL = ''

# Google Analytics
GOOGLE_ANALYTICS = 'G-Y2E20JE6P5'

PATH = 'content'
TIMEZONE = 'America/Indiana/Indianapolis'
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

ARTICLE_PATHS = ['thoughts', 'howtos', 'notebook', 'archive']
# Static paths
# Static paths — includes category dirs so co-located images are copied to output
STATIC_PATHS = ['images', 'tools', 'extra', 'thoughts', 'howtos', 'notebook']
EXTRA_PATH_METADATA = {
    'extra/.nojekyll': {'path': '.nojekyll'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.svg': {'path': 'favicon.svg'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'},
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

# Direct templates: homepage plus the combined Writing landing page
DIRECT_TEMPLATES = ['index', 'writing', 'sitemap']
SITEMAP_SAVE_AS = 'sitemap.xml'
WRITING_SAVE_AS = 'writing/index.html'

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
    ('Notebook', 'notebook'),
]

# Use explicit Category in frontmatter, not folder names
USE_FOLDER_AS_CATEGORY = False

# Default category for articles without one specified
DEFAULT_CATEGORY = 'uncategorized'

# Markdown extensions for sidenotes
from pymdownx import emoji as pymdownx_emoji

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.smarty': {},
        'markdown.extensions.toc': {
            'title': 'Contents',
        },
        'pymdownx.emoji': {
            'emoji_index': pymdownx_emoji.twemoji,
            'emoji_generator': pymdownx_emoji.to_alt,
        },
    },
    'output_format': 'html5',
}
