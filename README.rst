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
<http://docs.django-cms.org/en/latest/contributing/index.html>`_.

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


Configuration
-------------

* You can configure the sitename via the settings of the application
* Media and static is configured through Aldryn Django








CHECK THEIR TUTORIAL








Wagtail requires you to create a new application containing your new page type, based on its
provided ``Page`` class.

(From this point onwards, we're following more or less the same steps described in the `Extend the
HomePage model section in the official Wagtail documentation
<http://docs.wagtail.io/en/latest/getting_started/tutorial.html#extend-the-homepage-model>`_. We're
using the Divio Shell, so some operations are slightly different, but the general idea should be
familiar if you have used Wagtail already.)


Add a new ``home`` application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Change into your project's directory to work there, and create a new Django Application::

    docker-compose run --rm web python manage.py startapp home

This will generate a Django application called home, located in the project directory.


Configure settings
~~~~~~~~~~~~~~~~~~

Add your application to Django's ``INSTALLED_APPS`` settings. Open up ``settings.py`` inside the project root in your preferred code editor and replace::

    INSTALLED_APPS.extend([
        # add your project specific apps here
    ]

with::

    INSTALLED_APPS.extend([
        # add your project specific apps here
        'home',
    ])


Create a ``Page`` model
~~~~~~~~~~~~~~~~~~~~~~~

We need to extend the ``HomePage`` model. Open ``home/models.py`` and replace the entire file with::

    from __future__ import unicode_literals
    from django.db import models
    from wagtail.wagtailcore.models import Page
    from wagtail.wagtailcore.fields import RichTextField
    from wagtail.wagtailadmin.edit_handlers import FieldPanel

    class HomePage(Page):
        body = RichTextField(blank=True)
        content_panels = Page.content_panels + [
            FieldPanel('body', classname="full")
        ]


Create and run migrations
~~~~~~~~~~~~~~~~~~~~~~~~~

Now we need to create database migrations for our application, so Django knows which tables and
fields need to be added to the database. In the Terminal, run::

    docker-compose run --rm web python manage.py makemigrations home

Now run the migrations, to apply the changes to the database::

    docker-compose run --rm web python manage.py migrate home


Add templates
~~~~~~~~~~~~~

In the folder ``templates/home/``, add a file named ``home_page.html`` to create a template::

    {% extends "base.html" %}

    {% load wagtailcore_tags %}

    {% block body_class %} template-homepage {% endblock %}

    {% block content %}
    {{ page.body | richtext }}
    {% endblock %}

We also need to create a base template. In the folder templates, add a file base.html::

    {% load wagtailuserbar %}

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->    <title>{% block title %}{% if self.seo_title %}{{ self.seo_title }}{% else %}{{ self.title }}{% endif %}{% endblock %}{% block title_suffix %}{% endblock %}</title>

        <!-- Bootstrap -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

        <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
        <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        <![endif]-->

        {% block extra_css %}
          {# Override this in templates to add extra stylesheets #}
        {% endblock %}
      </head>
      <body class="{% block body_class %}{% endblock %}"> {# Override this block to set custom body classes on a template by template basis #}

        {% wagtailuserbar %}

        <div class="main container">
          {% block heading %}
          <div class="page-header">
            <h1>{{ self.title }}</h1>
          </div>
          {% endblock %}

          {% block content %}{% endblock %}
        </div>

        <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
        <!-- Include all compiled plugins (below), or include individual files as needed -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>

        {% block extra_js %}
          {# Override this in templates to add extra javascript #}
        {% endblock %}

      </body>
    </html>


Create a new Wagtail page
-------------------------

* Login to the **Django admin** at ``/django-admin`` in your site. Create a new user by
  hitting **Add user**,  then sign in. (`Learn more about how this works
  <http://support.divio.com/local-development/setup/how-to-login-on-aldryn-projects>`_.)
* In the **Wagtail admin** at ``/admin/pages/``, add a new page by clicking *Add Child Page*
* Add a title and some content and hit **Publish**
* Set the page as a root page in the Wagtail admin by going to *Settings > Sites > localhost*
  ``/admin/sites``. Select the localhost site.
* In the *Root Page* row select *Choose a different Root Page* and find the new sub-page of it that
  we just created
* Hit **Save** to continue.

Finally, go to your site - In the Wagtail Explorer, find your page and hit the Live button to see the published page.

Next steps
----------

You've now created a new Django Wagtail site on Divio Cloud, deployed it locally in the Divio
Shell, configured it at the Python level, and started editing it. The next step is to push your
changes to the Divio CLoud, and deploy them there.

See our `Developer tutorial <http://docs.divio.com/en/latest/introduction/index.html>`_to become
properly familiar with the system and what you can do with it.



Wagtail Support
===============

Divio does not offer support for Wagtail itself. Please check out `wagtail.io`_ for help.

.. _Control Panel: https://control.aldryn.com/control/
.. _issues: https://github.com/aldryn/aldryn-wagtail/issues
.. _pull requests: https://github.com/aldryn/aldryn-wagtail/pulls
.. _aldryn-wagtail: https://github.com/aldryn/aldryn-wagtail
.. _wagtail.io: https://wagtail.io/







Running Tests
-------------

You can run tests by executing::

    virtualenv env
    source env/bin/activate
    pip install -r tests/requirements.txt
    python setup.py test


.. |build| image:: https://travis-ci.org/divio/aldryn-wagtail.svg?branch=support/2.1.x
    :target: https://travis-ci.org/divio/aldryn-wagtail
.. |coverage| image:: https://codecov.io/gh/divio/aldryn-wagtail/branch/support/2.1.x/graph/badge.svg
    :target: https://codecov.io/gh/divio/aldryn-wagtail

.. |python| image:: https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%C2%A03.7-blue.svg
    :target: https://pypi.org/project/aldryn-wagtail/
.. |wagtail| image:: https://img.shields.io/badge/wagtail-1.5-blue.svg
    :target: https://www.wagtail.io/
