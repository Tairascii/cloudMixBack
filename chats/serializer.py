from rest_framework import serializers

from chats.models import Chat
from message.models import Message
from message.serializer import MessageSerializer
from bots.models import Bot
from bots.serializer import BotSerializer

class ChatSerializer(serializers.ModelSerializer):
    last_message = MessageSerializer(read_only=True)

    class Meta:
        model = Chat
        fields = ['id', 'user', 'bot', 'last_message']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        last_message = Message.objects.filter(chat_id=instance.id).first()
        bot = Bot.objects.filter(id=instance.bot_id).first()
        if bot:
            representation['bot'] = BotSerializer(bot).data
        if last_message:
            representation['last_message'] = MessageSerializer(last_message).data
        return representation
