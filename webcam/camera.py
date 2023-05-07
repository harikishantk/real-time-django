import cv2
import threading

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.current_frame = None
        self.is_running = False

        # start the background thread to read frames from the camera
        self.thread = threading.Thread(target=self._capture_frames)
        self.thread.daemon = True
        self.thread.start()
    
    def __del__(self):
        self.video.release()
    
    def _capture_frames(self):
        while True:
            if self.is_running:
                ret, frame = self.video.read()
                if ret:
                    self.current_frame = frame
    
    def generate(self):
        while True:
            if self.current_frame is not None:
                ret, jpeg = cv2.imencode('.jpg', self.current_frame)
                frame = jpeg.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')