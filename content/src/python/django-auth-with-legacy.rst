Using Django Auth with a legacy app
###################################

:date: 2010/11/09
:tags: django, python, 

One strategy for integrating a legacy python application with Django.
=====================================================================

At work, we're planning to switch to Django.  Rather than doing a complete feature freeze for six months while we rewrite the site in Django, the decision has been made to run two codebases and migrate features to Django slowly.

In this case, the legacy app is in python, with some libraries from pylons and several homebrew components.  But because it is python, the parallel codebases are easier than in other situations (say, php-to-Django).

The solution that works for us consists of running both codebases within the same app space (powered by uWSGI), switching routing methods in a WSGI middleware, and using a Django middleware to make old credentials work with Django packages.
WSGI Site-Switching Middleware

Normally, a WSGI middleware stack is implemented like this:

.. code-block:: python

 application = RoutingMiddleware(MyApp(), etc)
 application = SomeOtherMiddleware(my_app)

To handle having two applications, I added another middleware to the stack:

.. code-block:: python

 class SiteSwitcher(object):
     def __init__(self, apps):
         self.apps = apps

     def __call__(self, environ, start_response):
         request_uri = environ.get('REQUEST_URI') or environ.get('PATH_INFO')
         for route, app in self.apps.items():
             if route is not '*' and request_uri.startswith(route):
                 return app(environ, start_response)
         return self.apps['*'](environ, start_response)

And then used it like this:

.. code-block:: python

 #set up legacy app
 legacy_app = RoutingMiddleware(MyApp(), m)

 #set up django
 import os
 os.environ['DJANGO_SETTINGS_MODULE'] = 'path.to.settings'
 from django.core.handlers import wsgi
 django_app = wsgi.WSGIHandler()

 #set up primitive routing
 my_apps = {'/django_url_prefix': django_app, '*':legacy_app}

 #wrap them in the site switcher
 application = SiteSwitcher(apps)

This approach does mean maintaining three silos of routing info - one in django's urls.py, one in the legacy app's routing, and one primitive one in your wsgi handler module.  The more you can partition the app domains with a short substring, the less headache this will be, but let's face it, it's going to be a headache.


Authentication using Django Middleware
======================================

If your app has pages that require the user to be authenticated, you're going to run into some problems as logging into your legacy site won't auth users for the new site.  One choice is to port all of the auth from the old system over to using Django, but for a gradual rollout, that's a really big obstacle in the way.  Instead, we decided to keep the legacy auth system in place and convince Django to play nice.

Django's auth system revolves around the request.user object.  Django's own auth features (e.g. @login_required) and many packages for Django expect that request.user be a Django User model.  After spending some time monkeying with various quacks-like-a-duck ideas, the simplest solution presented itself:  make request.user be a Django User model.  This is done with a custom middleware:

.. code-block:: python

 from legacy_app.models import LegacyUser #example model from old app; could also use a raw cursor
 from django.contrib.auth.models import User

 class LegacyAuthenticationMiddleware(object):
 
     def process_request(self, request):
         luser = LegacyUser.get_by_cookie(request.COOKIES) #or however you do your legacy session auth
         if luser:
             try:
                 user = User.objects.get(username=luser.username) #see if Django user already exists
             except User.DoesNotExist:
                 #No user?  Create one on the fly
                 user = User(username=luser.username, email=luser.email, 
                             first_name=luser.first_name, last_name=luser.last_name)
                 user.set_password(luser.password) #password not actually used
                 user.pk = luser.uid #this allows users to keep the same ID when you finish migrating
 
                 if luser.is_admin():  #if your legacy admin system is user-based
                     user.is_staff = True
                     user.is_superuser = True
                 user.save()
             request.user = user

 
Note that the password field is not actually used yet, since the login form is part of the legacy app.  If passwords are only stored hashed, you'll need to come up with another way to copy passwords over as users log in to the legacy site.
