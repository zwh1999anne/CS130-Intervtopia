from email.policy import default
from django.db import models
from users.models import *

# Create your models here.


class Question(models.Model):
    """
    question_text: ask question
    target: who will answer this question
    question_ranking: use to rank question, the smaller number, the higher position
    question_name: use in the update method
    """
    target_choices = [('ER', "Interviewer"), ('EE', "Interviewee")]
    question_text = models.CharField(max_length=200)
    target = models.CharField(max_length=2, default='ER', choices=target_choices)
    question_ranking = models.IntegerField(default=0)
    question_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.question_text


class Choice(models.Model):
    """
        question: ask question
        choice_value: value for nthis choice
        choice_text: the text of the chioce
        selected: boolean for if selected
        """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_value = models.IntegerField(default=0)
    choice_text = models.CharField(max_length=200)
    selected = models.BooleanField()

    def __str__(self) -> str:
        return self.choice_text


# class InterviewER_EvaluationFormDB(models.Model):
#     interviewee = models.CharField(max_length=200, default="")
#     score = models.IntegerField(default=0)
#     problem_solving = models.CharField(max_length=200, default="")
#     communication = models.CharField(max_length=200, default="")
#     coding_skill = models.CharField(max_length=200, default="")

#     def __str__(self) -> str:
#         return self.interviewee

#     def insert(self):
#         raise NotImplementedError

#     def remove(self):
#         raise NotImplementedError

#     def update(self, request):
#         interviewee_text = request.POST['interviewee']
#         score_int = request.POST['choice']
#         problem_solving_sentence = request.POST['problem-solving']
#         communication_sentence = request.POST['communication']
#         coding_skill_sentence = request.POST['coding-skill']

#         self.objects.create(interviewee=interviewee_text, score=score_int, problem_solving=problem_solving_sentence, communication=communication_sentence, coding_skill=coding_skill_sentence)

#     def query(self):
#         raise NotImplementedError

# class InterviewEE_EvaluationFormDB(models.Model):
#     interviewer = models.CharField(max_length=200, default="")
#     score = models.IntegerField(default=0)
#     helpful = models.CharField(max_length=200, default="")
#     communication = models.CharField(max_length=200, default="")

#     def __str__(self) -> str:
#         return self.interviewer

#     def insert(self):
#         raise NotImplementedError

#     def remove(self):
#         raise NotImplementedError

#     def update(self, request):
#         interviewer_text = request.POST['interviewer']
#         score_int = request.POST['choice']
#         helpful_sentence = request.POST['helpful']
#         communication_sentence = request.POST['communication']

#         self.objects.create(interviewer=interviewer_text, score=score_int, helpful=helpful_sentence, communication=communication_sentence)

#     def query(self):
#         raise NotImplementedError


class Response(models.Model):
    name = models.CharField(max_length=100, default="")
    problem_solving = models.IntegerField(default=0)
    communication = models.IntegerField(default=0)
    coding_skill = models.IntegerField(default=0)
    helpful = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

    def update(self, request):
        '''
        TODO: update the response
        '''


class EvalForm(models.Model):
    name = models.CharField(max_length=100, default="")
    questions = models.ManyToManyField(Question)
    rating = models.IntegerField(default=0)
    comments = models.TextField(null=True, blank=True)
    response = models.ForeignKey(Response, on_delete=models.CASCADE, default=None)
    targer_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role_choices = [('ER', 'Interviewer'), ('EE', 'Interviewee')]
    target_role = models.CharField(max_length=2, choices=role_choices)

    def __str__(self) -> str:
        return self.name

    def onSubmit(self):
        '''
        TODO: update the response and write to DB
        '''

    def getReport(self):
        '''
        TODO: generate report from the response
        '''

    def getQuestions(self):
        '''
        TODO: return the questions
        '''

    @staticmethod
    def update(request):
        '''
        TODO: update the response to the evaluation form
        '''

        # if 'interviewee' in request.POST:
        #     InterviewER_EvaluationFormDB.update(InterviewER_EvaluationFormDB, request)
        # else:
        #     InterviewEE_EvaluationFormDB.update(InterviewEE_EvaluationFormDB, request)
