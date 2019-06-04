# -*- coding: utf-8 -*-
from django.conf.urls import include, url

from wagtail.core import urls as wagtail_urls


urlpatterns = [
    # For anything not caught by a more specific rule, hand over to
    # Wagtail's serving mechanism
    url(r'', include(wagtail_urls)),
]
