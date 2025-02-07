"""
WSGI config for crud project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
settings_module = 'crud.deployment' if 'WBSITE_HOSTNAME' in os.environ else 'crud.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crud.settings')
from django.core.wsgi import get_wsgi_application


application = get_wsgi_application()
