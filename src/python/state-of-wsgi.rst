The State of WSGI and character encoding.
#########################################
:date: 2010/08/03
:tags: wsgi, rant, wtf

Imagine you've inherited a legacy codebase with urls that look like this:

::

 http://host.com/music/{band_name}
 http://host.com/music/{band_name}/{album_name}

Now imagine that you have over a million unique bands in your database, in dozens of languages with all sorts of weird punctuation.  Ignoring the special case of The Artist Formerly Known as Prince, there are literally thousands of bands that could cause problems.

Take the case of AC/DC.

The url to the band's page should be `http://host.com/music/AC%2FDC`.  The url to to their album "Highway To Hell" should be `http://host.com/music/AC%2FDC/Highway%20To%20Hell`.  Or you can use plusses for the spaces, but that's another gripe for another day.

Pylons uses the Routes library to handle routing to a controller.  Routes relies on PATH_INFO in the environ variable provided by the WSGI server. 

As far as I can tell, there is not a single WSGI server that doesn't run unquote() on PATH_INFO before passing it to your middleware stack.

That means by the time Routes sees it, AC/DC's band page url looks like `http://host.com/music/AC/DC`.  Routes will assume, therefore, that {band_name} is "AC" and {album_name} is "DC".

Thankfully, the app server I'm using (uWSGI) passes the raw url as REQUEST_URI.  So it should be a simple matter of wrapping the app in a middleware that substitutes REQUEST_URI for PATH_INFO in the environ object, passes it to the RoutesMiddleware, intercepts the extracted wsgiorg.routing_args and unquotes them.  Two problems with this, though:

1.  The testing framework (webtest) doesn't pass the REQUEST_URI, so this isn't particularly testable.  (There are several other key ways where webtest fails to behave correctly, particularly regarding unicode.)

2.  For some reason Routes mistakenly casts the raw url parts into unicode strings, when they are no such thing (see PEP333).  `u'\xCEoo'` is not the same string as `'\xCEoo'`.  Are there any bands with foreign characters in the url?  Those are now broken.

This is a well-known issue.  It's been a well-known issue since the WSGI spec (PEP 333) screwed this up seven years ago by not specifying that urls should be passed raw to the application.

The right way should be:

WSGI app server recieves the url.  WSGI app server passes the url, untouched, to the app.  The app's router (Routes, in the case of Pylons, or urlhandler in the case of Django) should assume the url is untouched.  If it wants to conveniently provide routing parameters to the controller ("view" in Django), it should unquote them after extracting them from the url, not before.

Furthermore, the router should use unquote_plus, not unquote, because + is still accepted to mean space in urls, or at least provide an option to specify a preference.   As far as I can tell, every wsgi app server screws this last one up, so that the url `/music/+%2B+` is passed to the router as `/music/+++`.
