from email.policy import default
from django.db import models
from users.models import *
from django.utils.timezone import now

# Create your models here.
class EvalForm(models.Model):
    name = models.CharField(max_length=100, default="")
    # questions = models.ManyToManyField(Question)
    targer_user = models.ForeignKey(CustomUser, related_name='evalform', on_delete=models.CASCADE)
    role_choices = [('ER', 'Interviewer'), ('EE', 'Interviewee')]
    target_role = models.CharField(max_length=2, choices=role_choices)
    time = models.DateTimeField(default=now)
    comments = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name

    @staticmethod
    def set_role(self, role: str):
        '''
        TODO: Set the role of this evaluation form
        '''

class Question(models.Model):
    """
    question_text: ask question
    target: who will answer this question
    question_ranking: use to rank question, the smaller number, the higher position
    question_name: use in the update method
    """
    # question_name = models.CharField(max_length=200)
    question_text = models.CharField(max_length=200)
    target_choices = [('ER', "Interviewer"), ('EE', "Interviewee")]
    target = models.CharField(max_length=2, default='ER', choices=target_choices)
    question_ranking = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    evalform = models.ForeignKey(EvalForm, related_name="questions", on_delete=models.CASCADE, null= True)

    def __str__(self) -> str:
        return self.question_text


# class Choice(models.Model):
#     """
#     question: ask question
#     choice_value: value for nthis choice
#     choice_text: the text of the chioce
#     selected: boolean for if selected
#     """

#     question = models.ForeignKey(Question, related_name= "choices", on_delete=models.CASCADE)
#     choice_value = models.IntegerField(default=0)
#     choice_text = models.CharField(max_length=200)
#     selected = models.BooleanField()

#     def __str__(self) -> str:
#         return self.question.__str__() + " "+ self.choice_text


# class Response(models.Model):
#     name = models.CharField(max_length=100, default="")
#     problem_solving = models.IntegerField(default=0)
#     communication = models.IntegerField(default=0)
#     coding_skill = models.IntegerField(default=0)
#     helpful = models.IntegerField(default=0)
#     comments = models.TextField(null=True, blank=True)
#     rating = models.IntegerField(default=0)
#     evalform = models.OneToOneField(EvalForm, related_name = 'response', on_delete=models.CASCADE, null=True)
#     def __str__(self) -> str:
#         return self.name

#     def get_overall_rating(self) -> int:
        # pass
