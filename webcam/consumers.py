from channels.generic.websocket import AsyncWebsocketConsumer
from io import BytesIO
from PIL import Image, ImageFilter
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

            # save the received image
            image.save('media/received_image.jpg')

            # Process the image by changing to grayscale
            image = image.convert('L')

            # Save the processed image
            image.save('media/processed_image.jpg')
            
            # Send the processed image back to the client if image is not empty
            if image:
                # Convert the PIL image to base64 encoded JPEG image
                buffered = BytesIO()
                image.save(buffered, format="JPEG")
                encoded_image = base64.b64encode(buffered.getvalue()).decode("utf-8")
                
                # Send the base64 encoded JPEG image to the client
                await self.send(encoded_image)
