from django.db import models
from datetime import datetime
from django.utils.timezone import now
from users.models import *


class Friendship(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self) -> str:
        return self.question_text

    #user1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    #user2 = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    #def __str__(self) -> str:
    #    return self.user1.username + "&" + self.user2.username