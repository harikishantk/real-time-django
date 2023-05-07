# webcam/urls.py
from django.urls import path

from webcam.views import *


urlpatterns = [
    path('', index),
    path('video_feed', video_feed, name='video_feed')
]