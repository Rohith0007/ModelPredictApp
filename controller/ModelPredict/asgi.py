"""
ASGI config for ModelPredict project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

settings_module = 'ModelPredict.deployment' if 'AZURE_EXTENSION_DIR' in os.environ else 'ModelPredict.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODUL', settings_module)

application = get_asgi_application()
