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
    problem_name = models.CharField(max_length=20)
    problem_url = models.URLField()
    problem_statement = models.TextField()
    problem_difficulty = models.CharField(max_length=1, choices=difficulty_choices)

    def __str__(self) -> str:
        return self.problem_name


class Interview(models.Model):
    name = models.CharField(max_length=20, default='')
    viewER = models.ForeignKey(Interviewer, on_delete=models.CASCADE)
    viewEE = models.ForeignKey(Interviewee, on_delete=models.CASCADE)
    problems = models.ManyToManyField(Problem)
    date_and_time = models.DateTimeField()
    room_link = models.URLField()


class ProblemDBUpdater():
    def addProblems(self, limit=None):
        query = leetCodeQuestionQuery()
        # TODO too many queries from the same ip will cause leetcode to close connection
        # TODO change to async queries
        if limit is not None:
            iter_limit = min(query.length(), limit)
        else:
            iter_limit = query.length()
        for i in range(iter_limit):
            q = query.getQuestion(i)
            Problem.objects.create(problem_name=q.getTitle(), problem_difficulty=q.getDifficulty(), problem_url=q.getURL(), problem_statement=q.getContent())
