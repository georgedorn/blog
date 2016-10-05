Werkzeug DebuggedApplication with uWSGI under lighttpd.
#######################################################

:date: 2010-07-08
:tags: bugfix, lighttpd, python, uwsgi
:category: python
:slug: werkzeug-debuggedapplication-uwsgi-under-lighttpd

uWSGI is a fairly awesome app server; it's lightweight and fast, yet highly stable.

Unfortunately, mod_uwsgi for lighttpd is somewhat half-baked.  Aside from yet another app server using the equivalent of urllib.unquote instead of urllib.unquote_plus, it also behaves differently than most app servers in dealing with query parameters.

This led to headaches when trying to use Werkzeug's awesome 
`Ajax-based python interpreter-in-a-page <http://werkzeug.pocoo.org/docs/debug/#enabling-the-debugger>`_, as the static asset requests were not getting caught by Werkzeug's middleware.
If you watch it with firebug, you'll see 404's for a bunch of requests:

:: 

 __debugger__/?cmd=resource&f=style.css
 __debugger__/?cmd=resource&f=jquery.js
 __debugger__/?cmd=resource&f=debugger.js
 __debugger__/?cmd=resource&f=console.png
 __debugger__/?cmd=resource&f=source.png


What's the fix?  Rewrite some of the environ coming from uWSGI, using a middleware in your wsgi handler module:

.. code-block:: python

 if condition_to_enable_werkzeug:
    try:
        from werkzeug.debug import DebuggedApplication

        class WerkzeugDebugger(DebuggedApplication):

            def __call__(self, environ, start_response):
                #fix uwsig's environ
                environ['QUERY_STRING'] = environ['QUERY_STRING'].split('?')[0]
                environ['REQUEST_URI'] = environ['REQUEST_URI'].split('?')[0]
                environ['PATH_INFO'] = environ['PATH_INFO'].split('?')[0]
                return super(WerkzeugDebugger, self).__call__(environ, start_response)

        #wrap this middleware around the your application
        application = WerkzeugDebugger(application, evalex=True)
        application.werkzeug = True #or whatever, if you need to disable your own error handler
    except ImportError, e: #werkzeug not found
        pass

