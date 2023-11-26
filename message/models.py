from django.db import models
from chats.models import Chat
from django.contrib.auth.models import User
from bots.models import Bot

# Create your models here.


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    bot = models.ForeignKey(Bot, on_delete=models.DO_NOTHING)
    content = models.TextField()
    timestamp = models.DateTimeField(blank=True)
    read_status = models.BooleanField()
    is_from_bot = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']
