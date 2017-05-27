"""
WSGI config for bio_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
from os.path import join,dirname,abspath
import sys,site
PROJECT_DIR = dirname(dirname(abspath(__file__)))
sys.path.append(PROJECT_DIR)
sys.path.append('/home/eadric/桌面/database-bio/bio_database/lib/python3.5/site-packages/')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bio_website.settings")
from django.core.wsgi import get_wsgi_application



application = get_wsgi_application()
