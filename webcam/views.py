from django.shortcuts import render
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
from webcam.camera import VideoCamera

# Create your views here.
def index(request):
    return render(request, 'index.html')

@gzip.gzip_page
def video_feed(request):
    return StreamingHttpResponse(VideoCamera().generate(), content_type="multipart/x-mixed-replace;boundary=frame")