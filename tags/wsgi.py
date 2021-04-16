"""
WSGI config for tags project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, sys, site

from django.core.wsgi import get_wsgi_application

sys.path.append("/var/www/html")
sys.path.append("/var/www/html/tf2tags")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tags.settings")

application = get_wsgi_application()
