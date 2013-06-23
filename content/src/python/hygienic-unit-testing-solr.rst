Hygienic unit testing with Solr.
################################

:date: 2010/09/13
:tags: solr, python, unittest

Python unittest hygiene and Solr.
=================================

A sane methodology for testing an application that uses a database looks like this:

#.    Prop up an empty database, preferably using the same engine as production.
#.    Import some fixture data to play with (optional).
#.    Run tests that manipulate data in this database.
#.    Roll back the database (or otherwise reset it to a known state) between tests.
#.    Nuke the database when done.

Django does this very well, using transactions when possible to speed up step 4.  Pylons is a little more primitive and requires a bit more work, but is still relatively straightforward.

But what about Solr?  It's essentially a database, too.  If you're going to test your search engine, for example, test hygiene suggests you should start with a clean core (or set of cores) for each test.  Sadly, Solr is not quite as easy as most database engines to set up a new core dynamically.

There is a way, however.  First, you must already be running a solr server with multiple cores enabled, such as with the following solr.xml:

.. code-block:: xml

 <solr persistent="false">
    <cores adminPath="/admin/cores">
        <core name="core0" instanceDir="core0" />
        <core name="core1" instanceDir="core1" />
    </cores>
 </solr>

The 'adminPath' attribute enables managing cores via the API, which is necessary if you want to dynamically load and unload cores.

Next, copy your schema.xml and any other solr config files into your source tree.  You probably should have done this already; if you aren't keeping your solr config in source control, where are you keeping them?

Then, in your test running script (or subclass of unittest.TestRunner, or whatever):

.. code-block:: python

 import os, shutil, urllib2, urllib, time

 #example vars
 PATH_TO_CORE_CONFIGS = 'tests/fixtures/my_core'
 CORE_NAME = 'my_core_%s' % time.time() #or use a hudson job name/number, random number, whatever
 PATH_TO_SOLR_CORE = os.path.join('/path/to/solr/example/multicore', CORE_NAME)

 #set up solr cores
 shutil.copytree(src=PATH_TO_CORE_CONFIGS, dst=PATH_TO_SOLR_CORE)
 args = {'action': 'CREATE',
            'name': CORE_NAME,  
            'instanceDir': os.path.join(PATH_TO_SOLR_CORE)
 }
 urllib2.urlopen(url='%s/admin/cores' % SOLR_HOST, data=urllib.urlencode(args))

 #run tests here, e.g.:
 from lib.testing import MyTestRunner
 try:
     test_run = MyTestRunner()
 except Exception, e:
     print e #or whatever you want to do with catastrophic test failure

 #clean up solr cores
 args = {'action': 'UNLOAD',
            'core': CORE_NAME
           }
 urllib2.urlopen(url='%s/admin/cores' % SOLR_HOST, data=urllib.urlencode(args))
 shutil.rmtree(PATH_TO_SOLR_CORE)

To reset the cores to a known state (e.g. empty) between test cases, you have a couple options; one is to unload the core, copy the files over again and re-create the core.  Unless your config files are huge, this is actually reasonably fast compared to dropping and recreating an SQL database.

Another option is to issue a delete query, e.g.:

.. code-block:: python

 urllib2.urlopen(url='%s/admin/cores/%s/update?stream.body=%s' % (SOLR_HOST, CORE_NAME, urllib.quote('<delete><query>*:*</query></delete>')))


