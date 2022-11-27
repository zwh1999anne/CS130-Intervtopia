from django.db import models
from users.models import *
from evaluation.models import *
from external.leetCodeWrapper import interviewQuestion, leetCodeQuestionQuery


class Interviewer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    evalForm = models.ForeignKey(EvalForm, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username


class Interviewee(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    evalForm = models.ForeignKey(EvalForm, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username


class Problem(models.Model):
    difficulty_choices = [('E', 'Easy'), ('M', 'Medium'), ('H', 'Hard'), ('', 'Select a difficulty')]
    name = models.CharField(max_length=150)
    url = models.URLField()
    difficulty = models.CharField(max_length=1, choices=difficulty_choices)

    def __str__(self) -> str:
        return self.name


class Interview(models.Model):
    # name = models.CharField(max_length=150, default='')
    viewER = models.ForeignKey(CustomUser, related_name = 'viewer', on_delete=models.CASCADE)
    viewEE = models.ForeignKey(CustomUser, related_name = 'viewee', on_delete=models.CASCADE)
    problems = models.ManyToManyField(Problem)
    date_and_time = models.DateTimeField()
    room_link = models.URLField()
    ide_link = models.URLField(null=True)

