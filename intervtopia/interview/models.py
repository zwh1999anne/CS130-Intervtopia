from django.db import models
# import sys, os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "..")
from users.models import *
# Create your models here.

class Interview:
    id = models.UUIDField()
    interviewer = models.JSONField()
    interviewee = models.JSONField()
    problems = models.JSONField()

    def toJSON():
        '''
        TODO: convert interview object to JSON format
        '''