from django.db import models
from datetime import datetime
from django.utils.timezone import now
from users.models import CustomUser


class Friendship(models.Model):
    sender = models.ForeignKey(CustomUser, related_name = 'sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name = 'receiver', on_delete=models.CASCADE)

class Message(models.Model):
    friendship = models.ForeignKey(Friendship, on_delete=models.CASCADE)
    message_text = models.CharField(max_length=200)
    time = models.DateTimeField(default=now)

