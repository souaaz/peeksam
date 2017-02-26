#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

LOAD_CONTENT_CACHE = False
#DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".hg", ".git", ".bzr"]

AUTHOR = 'Samira Ouaaz'
SHOW_ARTICLE_AUTHOR=False

SITEURL = 'http://debza.ca'

SITENAME='Debza'
#SITESUBTITLE='Programming comments and some news'
FAVICON='extra'
SITESUBTITLE='Mostly Python'
#SITENAME =  u"""<span style="color:blue;">Debza</span>"""
SITELOG='images/favicon.png'


#THEME = 'themes/backdrop'
TYPOGRIFY = True
#THEME= 'themes/elegant'

THEME= 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME= 'simplex' #readable'
BOOTSTRAP_FLUID = True
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE=True
DISPLAY_BREADCRUMBS=False
BOOTSTRAP_NAVBAR_INVERSE=True
#DISPLAY_CATEGORIES_ON_MENU=True
PYGMENTS_STYLE='monokai'
RELATED_POSTS_MAX = 10
#PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}

PATH = 'content'
TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'
DEFAULT_PAGINATION = False
DATE_FORMATS = {'en': '%b %d, %Y'}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_RSS = None #'feeds/all.rss.xml'
CATEGORY_FEED_RSS = None #'feeds/%s.rss.xml'


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['theme', 'extra', 'css/pygments', 'images']

ARTICLE_PATHS = [ 'programming', 'jupyter', 'analytics']
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
PAGE_URL = u'{slug}'
PAGE_SAVE_AS = u'{slug}.html'

DEFAULT_CATEGORY = 'Miscellaneous'
CATEGORY_SAVE_AS = 'category/{slug}.html'
AUTHOR_SAVE_AS = ''
TAG_SAVE_AS = 'tag/{slug}.html'
TAG_URL= 'tag/{slug}.html'
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = 'categories.html'
TAGS_SAVE_AS = 'tags.html'
#TAGS_URL='tags.html'
ARCHIVES_SAVE_AS = 'archives.html'

FEED_MAX_ITEMS = 10

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
    'images' : { "path" : "images"},
}

ARTICLE_EXCLUDES = ['in_progress']

PLUGIN_PATHS = [ 'pelican-plugins']
PLUGINS = ['render_math', 
          'tipue_search', 
            'sitemap', 
            'extract_toc', 
            'liquid_tags.img',
           'neighbors', 
           'latex', 
           'related_posts', 
           #'assets', 
           'share_post',
           'multi_part',
           'optimize_images',
           'i18n_subsites',
           'tag_cloud',
           'series',
           ]

#DIRECT_TEMPLATES = ['index', 'search']
DIRECT_TEMPLATES =  ((  'index', 'categories', 'archives', 'search', '404')) # ['index',]


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
		'markdown.extensions.codehilite': {"css_class" : "highlight" },
    'markdown.extensions.extra': {} ,
    'markdown.extensions.headerid' : {},
    'markdown.extensions.toc' : { "permalink": True},

        },
    'output_format': 'html5',
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



# Elegant Labels  [elegant]
#SOCIAL_PROFILE_LABEL = u'Stay in Touch'
RELATED_POSTS_LABEL = 'Keep Reading'
SHARE_POST_INTRO = 'Like this post? Share on:'
COMMENTS_INTRO = u'So what do you think? Leave your comments below.'

USE_SHORTCUT_ICONS = True

# Mailchimp [elegant]
#EMAIL_SUBSCRIPTION_LABEL = u'Get Monthly Updates'
#EMAIL_FIELD_PLACEHOLDER = u'Enter your email...'
#SUBSCRIBE_BUTTON_TITLE = u'Send me Free updates'
#MAILCHIMP_FORM_ACTION = u'empty'

'''
#tag_cloud defaults
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100
AG_CLOUD_SORTING = 'random' # random, alphabetically, alphabetically-rev, size and size-rev
TAG_CLOUD_BADGE = True
'''

# SMO  [elegant]
TWITTER_USERNAME = u'souaaz'
FEATURED_IMAGE = SITEURL + '/theme/images/apple-touch-icon-152x152.png'

# Legal  [elegant]
#SITE_LICENSE = u'<span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">debza</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://debza.com" property="cc:attributionName" rel="cc:attributionURL">Samira Ouaaz</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.'

# SEO  [elegant]
SITE_DESCRIPTION = u'My name is Samira Ouaaz \u2015 a software engineer. This is my personal blog.'


DISQUS_SITENAME = u'debza-ca.disqus.com'
DISQUS_NO_ID=True
DISQUS_DISPLAY_COUNTS=True

# Landing Page  [elegant]
PROJECTS = [
        {
            'name': 'Elegant',
            'url':
            'http://oncrashreboot.com/pelican-elegant',
            'description': 'A nice Pelican theme, with'
            ' search and a'
            ' lot more unique features. Built with Jinja2 and Bootstrap'},
     
        {
            'name': 'Pelican',
            'url':
            'https://github.com/getpelican/pelican/',
            'description': 'Static site generator that supports Markdown and'
            ' reST syntax'
        },
       
            

        {
            'name': 'Analyticsvidhya',
            'url':
            'https://www.analyticsvidhya.com',
            'description': 'Analytics ',
            },

      ]


BANNER = '/images/islamic-world-collection-1-mod.png' #Lunar_eclipse_al-Biruni.jpg'
#BANNER_SUBTITLE ='Samira'
BANNER_ALL_PAGES= True



CC_LICENSE_DERIVATIVES="yes"
CC_LICENSE_COMMERCIAL="yes"
CC_ATTR_MARKUP=True

USE_OPEN_GRAPH=False

ADDTHIS_PROFILE='ra-58b27c5f0df764a8'
#THIS_FACEBOOK_LIKE, ADDTHIS_TWEET, ADDTHIS_GOOGLE_PLUSONE True by defaults
ADDTHIS_DATA_TRACK_ADDRESSBAR = True # Default
'''
Go to www.addthis.com/dashboard to customize your tools --> <script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-58b27c5f0df764a8"></script> 
'''


