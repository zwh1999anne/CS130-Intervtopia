from email.policy import default
from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    '''
    target: who will answer this question
        value = 0: both interviewer and interviewee should answer
        value = 1: the question is for interviewer only
        value = -1: the question is for interviewee only
    '''
    target = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    selected = models.BooleanField()

    def __str__(self) -> str:
        return self.choice_text
