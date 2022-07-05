
import json
from random import randint
from asyncio import sleep
from channels.generic.websocket import AsyncWebsocketConsumer



class WSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        for i in range(100000):
            await self.send(json.dumps({'variable': randint(1,5)}))
            await sleep(1)