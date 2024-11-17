import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Присоединение клиента к группе
        await self.channel_layer.group_add("notifications", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Отключение клиента от группы
        await self.channel_layer.group_discard("notifications", self.channel_name)

    async def receive(self, text_data):
        # Обработка сообщений от клиента (если нужно)
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message')

        # Отправка сообщения обратно
        await self.channel_layer.group_send(
            "notifications",
            {
                "type": "send_notification",
                "message": message,
            },
        )

    async def send_notification(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({"message": message}))
