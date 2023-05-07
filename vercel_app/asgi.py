"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os

import django
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vercel_app.settings")
django.setup()
application = get_default_application()

from django.urls import URLPattern

websocket_urls = []
for url in application.url_router.urls:
    print(url.pattern, url.websocket)
    if isinstance(url, URLPattern) and url.websocket:
        websocket_urls.append(url.pattern)
print(websocket_urls)