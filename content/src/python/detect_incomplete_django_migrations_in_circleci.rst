Detecting Incomplete or Missing Migrations with Django and CircleCI
###################################################################

:date: 2016-10-04
:tags: django, migrations, circleci, continuous integration
:category: python
:slug: detect_incomplete_migration_django_circleci

It's pretty easy to put together a pull request for a change in a model and then forget to create a migration for it.
If you are using a CI server, here's a one-liner (for django 1.8 and above) that returns an error if there would be
any migrations created by ``manage.py makemigrations``:

.. code-block:: bash

  ! python manage.py makemigrations --dry-run --no-input --exit


The NOT (!) is important.  The ``--exit`` flag to makemigrations causes it to return an error code when there are no migrations to
make, and we're trying to detect the opposite situation.

In a circle.yml file, you could do this:

::

  test:
      pre:
          - python manage.py makemigrations --dry-run --no-input --exit && echo "missing migrations" && false
  [snip]

Note that starting a command with the NOT (!) operator doesn't appear to work; perhaps that has a different meaning in circle.yml.
The ``&& false`` serves the same purpose and lets us chain an echo to explain the situation to the reader.
Now when your CircleCI-enhanced django project gets a pull request, it'll see if migrations are complete and automatically
mark the PR as broken if any are missing.

See the `django-admin makemigrations docs <https://docs.djangoproject.com/en/1.9/ref/django-admin/#django-admin-makemigrations>`_, particularly the ``--exit`` flag.

