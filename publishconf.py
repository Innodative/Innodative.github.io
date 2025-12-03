#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Custom domain for GitHub Pages
SITEURL = 'https://innodative.com'
RELATIVE_URLS = False

# Enable feeds for production
FEED_ALL_ATOM = 'feeds/all.atom.xml'

# Delete output directory before regenerating
DELETE_OUTPUT_DIRECTORY = True
