from django.db import models
from users.models import *
from evaluation.models import *
# Create your models here.

class Interviewer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    evalForm = models.ForeignKey(EvalForm, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.user.username

class Interviewee(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    evalForm = models.ForeignKey(EvalForm, on_delete = models.CASCADE)
    
    def __str__(self) -> str:
        return self.user.username


class Interview(models.Model):
    viewER = models.ForeignKey(Interviewer, on_delete = models.CASCADE)
    viewEE = models.ForeignKey(Interviewee, on_delete = models.CASCADE)
    problems = models.JSONField()
    date_and_time = models.DateTimeField()

    def toJSON():
        '''
        TODO: convert interview object to JSON format
        '''
