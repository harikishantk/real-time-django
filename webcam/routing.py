from django.urls import path

from webcam.consumers import *

websocket_urlpatterns = [
    path(r'ws/stream/', StreamConsumer.as_asgi()),
]