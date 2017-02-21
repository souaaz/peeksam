#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

LOAD_CONTENT_CACHE = False

AUTHOR = 'Samira Ouaaz'

SITEURL = '.'
THEME = 'themes/backdrop'
#THEME= '/home/vagrant/pelican-themes/pelican-themes/backdrop'

PATH = 'content'


TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

DEFAULT_PAGINATION = False


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME', 'extra/favicon.ico']

ARTICLE_PATHS = ['regex', 'python', 'linux', 'jupyter', 'sql', ]
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

FEED_MAX_ITEMS = 10

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
}

ARTICLE_EXCLUDES = ['in_progress']

PLUGIN_PATHS = ['plugins']
PLUGINS = ['render_math', 'tipue_search', 'sitemap']

#DIRECT_TEMPLATES = ['index', 'search']
DIRECT_TEMPLATES = ['index',]

CATEGORY_SAVE_AS = 'category/{slug}.html'
AUTHOR_SAVE_AS = ''
TAG_SAVE_AS = 'tag/{slug}.html'
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = 'categories.html'
TAGS_SAVE_AS = 'tags.html'
ARCHIVES_SAVE_AS = ''

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


MARKDOWN = {
	'extension_configs' : { 
		'markdown.extensions.codehilite': {},
                'markdown.extensions.extra': {} ,
        },
}


SOCIAL = (('twitter', 'http://twitter.com/souaaz'),
          ('facebook', 'https://www.facebook.com/souaaz'),
          ('linkedin', 'https://www.linkedin.com/in/souaaz'),
          ('github', 'http://github.com/souaaz'),
          )


PELICAN_COMMENT_SYSTEM = True
PELICAN_COMMENT_SYSTEM_IDENTICON_DATA = ('author', 'email')

#backdrop
#PROFILE_IMAGE = '/images/Algerie-Ancienne.GIF'
BACKDROP_IMAGE = '/images/cordobamosque.jpg'
MAIN_MENU = True
USE_FOLDER_AS_CATEGORY = True
BLOGKEYWORDS='Python, Linux, Matplotlib, SQL, Postgresql, MySQL'
TAG_CLOUD_MAX_ITEMS=3
YEAR=2017

SITE_DESCRIPTION='Articles about programming languages, especially anything around Python. Plus news and reporting about culture and science.'
FAVICON='extra'
SITESUBTITLE='Mostly Python'
SITENAME = 'Technology and Culture'