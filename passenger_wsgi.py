# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1276130/data/www/codo.academy/user_project')
sys.path.insert(1, '/var/www/u1276130/data/djangoenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'user_project.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
