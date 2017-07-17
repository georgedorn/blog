Release Management with PyPI and GitHub
#######################################

:date: 2017-07-17
:tags: django, tastypie, release management, pypi
:category: python
:slug: release_management_pypi_github

I'm a core maintainer of Django-Tastypie, the oldest REST framework for Django.  It predates Django-Rest-Framework and comes from the very earliest days of Class-Based Views, from when they were still very controversial.  It's still in use by a lot of developers and companies, though these days the primary development efforts are in keeping it up-to-date with Django releases and bugfixing.  It's still in Beta for some legacy reasons, but it's exceptionally mature.

This isn't about DRF vs Tastypie; they both have their advantages and disadvantages.  If you're trying to decide on a REST framework,
my first suggestion is the same one I'd give for trying to find the right library for any project: figure out your needs, your team's needs,
pare your options down to a few viable ones, and then try building something with all of them.  Don't take any developer's word for which
is best; we all (myself included) have biases grown from out own projects and experiences and those are not your projects or experience.

Instead, this post is about something I do about once or two a year: releasing a new version of a (relatively) popular project via PyPI and Github.

Because release management is not part of my day job and because I only do it once or twice a year, I always get something wrong.

1. Version everything

Don't put your version number in ``setup.py``.  Thankfully the project did this already when I inherited it:
https://github.com/django-tastypie/django-tastypie/blob/master/setup.py#L11
Keep one centralized version number, then import it into ``setup.py`` and use it in ``setup()``.

But ``setup.py`` is almost certainly not the only reference to the current version.  Here's everywhere we need to bump the version number:

* `README <https://github.com/django-tastypie/django-tastypie/blob/master/README.rst>`_ - used by GitHub to show our project description at the top-level project page.
* `Documentation <https://github.com/django-tastypie/django-tastypie/tree/master/docs>`_ - and specifically our ``index.rst`` page. Our docs are automatically built and deployed to `Read The Docs <https://django-tastypie.readthedocs.io/en/latest/>`_ which saves us a lot of work.
* `Release notes <https://github.com/django-tastypie/django-tastypie/tree/master/docs/release_notes>`_ - these are included in the docs, and every new release gets a new notes file, which must also be linked from the ``release_notes/index.rst`` page.  More on that below.

2. Release Notes

Tracking everything that has changed since the last release is a difficult but necessary step. In a perfect world, you'd be tracking changes
as they are made, but this is hard enough for a single-developer project much less a community-maintained project.  Instead, GitHub provides
some tools for this on the `Releases <https://github.com/django-tastypie/django-tastypie/releases>`_ page.  By default, this page shows the
last release and, crucially, a link to show all commits made to ``master`` since this release.  I try to keep this to the broad strokes,
keeping the nitty-gritty details confined to our 
`Backwards-Incompatible Changes <https://github.com/django-tastypie/django-tastypie/blob/master/BACKWARDS-INCOMPATIBLE.txt>`_ file.

"Releasing" a Python library on GitHub is a bit of an anachromism; most users will be deploying from PyPI.  But it is a simple process
(just create a new Draft Release from the Releases page, pointing at either ``master`` or a release tag.) and worth it for the rollup
diffs and commit log alone.

3. Release to PyPI

Make sure everything is ready to go before this step.  It's not possible to change a release once published to PyPI.

Every time I do this, the toolchain has changed. Most recently, the preferred tool has changed to `Twine <https://pypi.python.org/pypi/twine>`_
which was relatively painless (if arcane):

.. code-block:: bash

  $ pip install twine
  $ python setup.py sdist
  $ twine upload dist/*

You can provide authentication for twine in a configuration file, but given the 
`recent NPM credential debacle <https://github.com/ChALkeR/notes/blob/master/Gathering-weak-npm-credentials.md>`_
it is probably a good idea to avoid putting your PyPI password in any cleartext file.
