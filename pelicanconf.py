#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'George Dorn'
SITENAME = u'Circuitlocutious'
SITEURL = '/blog/'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None
FEED_RSS = 'rss.xml'
#FEED_ALL_RSS = 'rss/all.rss.xml'
CATEGORY_FEED_RSS = 'rss/%s.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)
LINKS = [
    ('RST WYSIWYG editor', 'http://rst.ninjs.org/'),

]


# Social widget
SOCIAL = (
        ('Mastodon', 'https://social.coop/GDorn'),
        ('Stack Overflow', 'http://stackoverflow.com/users/402605/gdorn'),
        ('Linkedin', 'http://www.linkedin.com/in/gdorn'),
        ('Github', 'https://github.com/georgedorn'),
        ('Gitlab', 'https://gitlab.com/u/georgedorn'),
        )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
#THEME = 'notmyidea'
#DISQUS_SITENAME = 'gdorn-blog'
COMMENTS_SITENAME = 'gdorn-tech-blog'
#GITHUB_URL = 'http://github.com/georgedorn/blog'
THEME = './themes/tuxlite_tbs'
