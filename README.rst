==============
Aldryn Wagtail
==============

|build| |coverage|

An opinionated Wagtail setup bundled as a Divio Cloud Addon.

This package will auto configure Django, including admin and some other basic
packages. It also handles sane configuration of the database connection and
static and media files.

The goal is to keep the footprint inside the Django website project as small
as possible, so updating things usually just means bumping a version in
``requirements.txt`` and no other changes in the project.

This addon still uses the legacy "Aldryn" naming. You can read more about this in our
`support section <https://support.divio.com/general/faq/essential-knowledge-what-is-aldryn>`_.


Contributing
============

This is a an open-source project. We'll be delighted to receive your
feedback in the form of issues and pull requests. Before submitting your
pull request, please review our `contribution guidelines
<https://docs.wagtail.io/en/v2.5/contributing/>`_.

We're grateful to all contributors who have helped create and maintain this package.
Contributors are listed at the `contributors <https://github.com/divio/aldryn-wagtail/graphs/contributors>`_
section.


Documentation
=============

See ``REQUIREMENTS`` in the `setup.py <https://github.com/divio/aldryn-wagtail/blob/master/setup.py>`_
file for additional dependencies:

|python| |wagtail|


Installation
------------

Nothing to do. ``aldryn-wagtail`` is part of the Divio Cloud platform.

Have a look at our `support article <http://support.divio.com/academy/getting-started/get-started-with-wagtail>`_
on how to get started.


Configuration
-------------

* You can configure the ``WAGTAIL SITENAME`` in the addons configuration on Divio Cloud.
* Media and static paths are automatically configured through
  `Aldryn Django <https://github.com/divio/aldryn-django>`_.


Support
-------

Divio does not offer support for Wagtail itself. Please check out
`wagtail.io <https://wagtail.io/>`_ for help.


Running Tests
-------------

You can run tests by executing::

    virtualenv env
    source env/bin/activate
    pip install -r tests/requirements.txt
    python setup.py test


.. |build| image:: https://travis-ci.org/divio/aldryn-wagtail.svg?branch=master
    :target: https://travis-ci.org/divio/aldryn-wagtail
.. |coverage| image:: https://codecov.io/gh/divio/aldryn-wagtail/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/divio/aldryn-wagtail

.. |python| image:: https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%C2%A03.7-blue.svg
    :target: https://pypi.org/project/aldryn-wagtail/
.. |wagtail| image:: https://img.shields.io/badge/wagtail-1.5-blue.svg
    :target: https://www.wagtail.io/
