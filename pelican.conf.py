#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"George Dorn"
SITENAME = u"Circuitlocutious"
SITEURL = 'http://gdorn.circuitlocution.com/blog'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG='en'

# Blogroll
#LINKS =  (
#    ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
#    ('Python.org', 'http://python.org'),
#    ('Jinja2', 'http://jinja.pocoo.org'),
#    ('You can modify those links in your config file', '#')
#         )

# Social widget
SOCIAL = (
        ('Twitter', 'http://twitter.com/GDorn'),
        ('Stack Overflow', 'http://stackoverflow.com/users/402605/gdorn'),
        ('Linkedin', 'http://www.linkedin.com/in/gdorn'),
        ('Github', 'https://github.com/georgedorn'),
        )

DEFAULT_PAGINATION = 5

ARTICLE_PERMALINK_STRUCTURE = "%Y/%m/%d/"
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100

#import os
#project_path = os.path.abspath(os.path.dirname(__file__))
#STATIC_ROOT = os.path.join(project_path, '..', 'static')
#THEME = './simple' 
THEME = './themes/tuxlite_tbs'
CSS_FILE = 'main.css'

DISQUS_SITENAME = 'gdorn-blog'
GITHUB_URL = 'http://github.com/georgedorn/blog'
