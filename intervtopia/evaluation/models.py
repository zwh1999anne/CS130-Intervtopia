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

class EvalForm:
    rating = None
    comments = ""

    def getRating(self):
        if self.rating is None:
            raise "Warning: rating is not available"
        else:
            return self.rating

    def setRating(self, r):
        self.rating = r

    def getComments(self):
        return self.comments

class InterviewerForm(EvalForm):
    questions = Question.objects.filter(target__gte = 0)

class IntervieweeForm(EvalForm):
    questions = Question.objects.filter(target__lte = 0)