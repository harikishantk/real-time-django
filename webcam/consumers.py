from channels.generic.websocket import AsyncWebsocketConsumer
from io import BytesIO
from PIL import Image
import base64

class StreamConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
    async def disconnect(self, close_code):
        pass
        
    async def receive(self, text_data):
        if text_data == 'start_stream':
            # Do something when the webcam stream starts
            pass
        else:
            # Convert the received base64 encoded JPEG image to a PIL image
            data = BytesIO(base64.b64decode(text_data.split(',')[1]))
            image = Image.open(data)

            # Save the image to the media directory
            image.save('media/stream.jpg')
            
            # Do something with the received image
            pass
