import json

from django.shortcuts import render
from rest_framework import viewsets
from chats.models import Chat
from .serializer import ChatSerializer
from rest_framework.response import Response
from bots.serializer import BotSerializer
# Create your views here.


class ChatsViewSet(viewsets.ViewSet):

    def list(self, request):
        # get userid from token if jwt will be added
        chats = Chat.objects.filter(user_id=1)
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = json.loads(request.body)
        bot_serializer = BotSerializer(data=data)
        if bot_serializer.is_valid():
            bot_serializer.save()
            bot = bot_serializer.data
            new_chat = {"bot": bot["id"], "user": 1}
            serializer = ChatSerializer(data=new_chat)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)

        return Response(bot_serializer.errors, status=400)



