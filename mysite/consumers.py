import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import datetime

class ClockConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            await self.send(json.dumps({'clock': current_time}))
            await asyncio.sleep(1)