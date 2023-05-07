from channels.generic.websocket import AsyncWebsocketConsumer

class StreamConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("connected")
        await self.accept()
        
    async def disconnect(self, close_code):
        print("disconnected")
        pass
        
    async def receive(self, text_data):
        # Do something with the received message
        print("received")
        pass
