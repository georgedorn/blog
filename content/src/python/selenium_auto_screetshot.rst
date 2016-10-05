Auto Screenshot Selenium Test Failures (In Django)
##################################################
:date: 2016/09/22
:tags: python, testing, circle, unittest

These days, every codebase I work on runs tests under some form of third-party continuous integration.  This is great,
because people are lazy and don't always run all of their tests before pushing.  But it's not so great when trying to debug
why a test failed on the CI server but not locally.  Even moreso when the test is a Selenium test; even a live SSH build
on the CI server is of limited use, especially for an intermittent failure.

So, I had the idea to automatically take a screenshot of the current browser state whenever a selenium test failed or encountered an exception.
That's easier said than done.  Unless you are building your own test runner from scratch, hooking into unittest can be tricky.  After
much research and pain, this is what I came up with:

.. code-block:: python

  class SeleniumTestCase(StaticLiveServerTestCase):  # StaticLiveServerTestCase from django.contrib.staticfiles
      live_server_url = 'http://localhost:8081'

      @classmethod
      def setUpClass(cls):
          '''
          One example of creating the test browser.  You could do it per-function as well, in setUp() instead.
          We'll be using cls.browser or self.browser later to get at the screenshot-saving mechanism.
          I'm omitting the corresponding tearDownClass or tearDown, which needs to close the browser.
          '''
          cls.browser = Browser()

      def run(self, result=None):
          '''
          Run is called on every test function, and an aggregate TestResult object
          is maintained across every test function.
          '''
          self.currentResult = result # remember result for use in tearDown
          super(SeleniumTestCase, self).run(result)

      def tearDown(self):
          '''
          tearDown is called after every test function.
          unittest.TestCase.run() handles errors and failures by appending each
          to the aggregate TestResult lists (TestResult.errors and TestResult.failures)
          so after a test just failed or errored, it'll be the last one in the list.
          '''
          result = self.currentResult  # currentResult contains running results for every test in a TestCase
          if result.errors:
              last_error = result.errors[-1]
              last_error_case, _ = last_error  # extract test method from tuple
              if last_error_case.id() == self.id():
                  self._save_screenshot(last_error)
          elif result.failures:
              last_fail = result.failures[-1]
              last_fail_case, _ = last_fail  # extract test method from tuple
              if last_fail_case.id() == self.id():
                  self._save_screenshot(last_fail)

          return super(SeleniumTestCase, self).tearDown()

      def _save_screenshot(self, error=None):
          '''
          At this point, we can use the browser object to save a screenshot.
          We can also do this directly from test functions.
          Screenshots will be saved with the python path to the test method
          as a filename.
          '''
          path = settings.SELENIUM_SCREENSHOTS_PATH
          import os
          if not os.path.exists(path):
              os.makedirs(path)
          filename = "%s.jpg" % self.id()
          full_path = os.path.join(path, filename)
          self.browser.save_screenshot(full_path)


That tearDown() method is really gross, but the best approach I could find. It's also only compatible with Python 2.6 and 2.7, as unittest
changes after 3.x., but see the sources below for some 3.x-compatible approaches.

It's also probably not compatible with Nose.

If I could wave a magic wand and update the unittest API, it would be far easier to do this if there were a post-failure hook, or if
TestCase.run() returned the last test function's result.

Sources:

http://stackoverflow.com/questions/12290336/how-to-execute-code-only-on-test-failures-with-python-unittest2

http://stackoverflow.com/questions/4414234/getting-pythons-unittest-results-in-a-teardown-method
