# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from aldryn_wagtail import __version__

setup(
    name='aldryn-wagtail',
    version=__version__,
    description='An opinionated Wagtail setup bundled as an Aldryn Addon',
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/aldryn/aldryn-wagtail',
    packages=find_packages(),
    platforms=['OS Independent'],
    install_requires=(
        'aldryn-addons',
        'wagtail==2.4',
    ),
    include_package_data=True,
    zip_safe=False,
)
