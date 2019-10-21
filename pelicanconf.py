#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'George Dorn'
SITENAME = u'RPG Works and Sundry'
SITEURL = '/rpgblog/'

PATH = 'content'
STATIC_PATHS = ['images', 'files']
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
        ('Tabletop.Social (Mastodon)', 'https://tabletop.social/GDorn'),
        ('Social.Coop (Mastodon)', 'https://social.coop/GDorn'),
        )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
#THEME = 'notmyidea'
#DISQUS_SITENAME = 'gdorn-blog'
COMMENTS_SITENAME = 'gdorn-rpg-blog'
#GITHUB_URL = 'http://github.com/georgedorn/blog'
THEME = './themes/tuxlite_tbs'
