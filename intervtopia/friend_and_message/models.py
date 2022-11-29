from django.db import models
from datetime import datetime
from django.utils.timezone import now
from users.models import CustomUser


class Friendship(models.Model):
    sender = models.ForeignKey(CustomUser, related_name = 'usr1', on_delete=models.CASCADE, null=True)
    receiver = models.ForeignKey(CustomUser, related_name = 'usr2', on_delete=models.CASCADE, null=True)


class Message(models.Model):
    friendship = models.ForeignKey(Friendship, related_name = 'friendship', on_delete=models.CASCADE, null=True)
    message_text = models.CharField(max_length=200)
    time = models.DateTimeField(default=now)