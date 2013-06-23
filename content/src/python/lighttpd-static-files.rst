uWSGI + lighttpd: Serving static files.
#######################################

:date: 2010/07/08
:tags: lighttpd, python, uwsgi

Serving both static and dynamic files with lighttpd + uWSGI.
============================================================

A common situation:  you have one domain and one application, but the app contains both static files (images, js, etc) and dynamic code (e.g. python modules).  Lighttpd's configuration is not trivial, and there's an added complication from how uwsgi behaves.

The typical solution for this problem is to use a combination of mod_rewrite and mod_alias, like so:

::

 $HTTP["host"] == "www.server.com"{
        url.rewrite-once = (
               #rewrite /images to /static/images.  
                "^(/images.*)$" => "/static/$1",
                #rewrite /js to /static/js
                "^(/js.*)$" => "/static/$1",
                #rewrite everything else to start with /uwsgi
                "^(/.*)$" => "/uwsgi$1",
        )
        #point everything prefixed with /static to a document root
        alias.url = ( "/static" => "/path/to/static/files")
        #set up uwsgi server connection
        uwsgi.server = (
                "/uwsgi" => (( "host" => "127.0.0.1", "port" => 3033, ))
        )
 }

However, if you were used to having uwsgi proxy to your_wsgi_module.application, you'll suddenly get errors:

::

 uWSGI Error
 application not found

This is because if the uwsgi.server configuration specifies a name ("/uwsgi"), it expects to find the application in your_wsgi_module.applications[name].  Simple fix in your_wsgi_module:

.. code-block:: python

 from myapp import MyApp, SomeMiddleWare
 application = MyApp()
 application = SomeMiddleWare(MyApp)

 applications = {"/uwsgi":application}

Incidentally, make sure you are using the latest mod_uwsgi.c; now that people are using it, a lot of bugs are becoming exposed and getting fixed.
