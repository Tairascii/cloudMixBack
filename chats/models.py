from django.db import models
from django.contrib.auth.models import User
from bots.models import Bot

# Create your models here.


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
