from django.urls import path

from webcam.consumers import *

websocket_urlpatterns = [
    # path('', StreamConsumer.as_asgi()),
    path(r'ws/stream/', StreamConsumer.as_asgi()),
]