import json
from random import randint
from asyncio import sleep

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(10):
            self.send(json.dumps({'message':randint(1,100)}))
            sleep(1)

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name='test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        
    
    def receive(self, text_data):
        text_data_json=json.loads(text_data)
        message=text_data_json['message']
        
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message
            }
        )
    def chat_message(self,event):
        message=event['message']

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message
        }))

class GraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        for i in range(1000):
            await self.send(json.dumps({'value':randint(-20,20)}))
            await sleep(1)