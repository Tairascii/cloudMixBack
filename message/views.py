import json

from django.shortcuts import render
from rest_framework import viewsets
from .models import Message
from .serializer import MessageSerializer
from rest_framework.response import Response
from datetime import datetime
from bots.views import create_bot_reply
from time import sleep
import random
# Create your views here.


class MessagesViewSet(viewsets.ViewSet):

    def list(self, request, chat_id):
        # get userid from token if jwt will be added
        messages = Message.objects.filter(sender=1, chat_id=chat_id).order_by('timestamp')
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = json.loads(request.body)
        data["timestamp"] = datetime.now()
        data["read_status"] = True
        serializer = MessageSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def create_bot_reply(self, request):
        sleep(random.randint(1, 4))
        data = json.loads(request.body)
        bot_reply = create_bot_reply(data["content"])
        bot_reply = {**bot_reply, "chat": data["chat"], "bot": data["bot"], "sender": data["sender"]}
        serializer = MessageSerializer(data=bot_reply)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
