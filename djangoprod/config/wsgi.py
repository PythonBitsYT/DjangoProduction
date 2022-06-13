"""
#! TODO-Boilerplate: Fix this name

WSGI config for djangoprod project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
#! TODO-Boilerplate: Fix this name
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoprod.config.settings')

application = get_wsgi_application()
