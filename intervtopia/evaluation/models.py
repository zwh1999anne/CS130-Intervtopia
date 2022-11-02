from email.policy import default
from django.db import models


# Create your models here.

class Question(models.Model):
    """
    question_text: ask question
    target: who will answer this question
        value = 0: both interviewer and interviewee should answer
        value = 1: the question is for interviewer only
        value = -1: the question is for interviewee only
    question_ranking: use to rank question, the smaller number, the higher position
    question_name: use in the update method
    """

    question_text = models.CharField(max_length=200)
    target = models.IntegerField(default=0)
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


class InterviewER_EvaluationFormDB(models.Model):
    interviewee = models.CharField(max_length=200, default="")
    score = models.IntegerField(default=0)
    problem_solving = models.CharField(max_length=200, default="")
    communication = models.CharField(max_length=200, default="")
    coding_skill = models.CharField(max_length=200, default="")

    def __str__(self) -> str:
        return self.interviewee

    def insert(self):
        raise NotImplementedError

    def remove(self):
        raise NotImplementedError

    def update(self, request):
        interviewee_text = request.POST['interviewee']
        score_int = request.POST['choice']
        problem_solving_sentence = request.POST['problem-solving']
        communication_sentence = request.POST['communication']
        coding_skill_sentence = request.POST['coding-skill']

        self.objects.create(interviewee=interviewee_text, score=score_int, problem_solving=problem_solving_sentence,
                            communication=communication_sentence, coding_skill=coding_skill_sentence)

    def query(self):
        raise NotImplementedError


class InterviewEE_EvaluationFormDB(models.Model):
    interviewer = models.CharField(max_length=200, default="")
    score = models.IntegerField(default=0)
    helpful = models.CharField(max_length=200, default="")
    communication = models.CharField(max_length=200, default="")

    def __str__(self) -> str:
        return self.interviewer

    def insert(self):
        raise NotImplementedError

    def remove(self):
        raise NotImplementedError

    def update(self, request):
        interviewer_text = request.POST['interviewer']
        score_int = request.POST['choice']
        helpful_sentence = request.POST['helpful']
        communication_sentence = request.POST['communication']

        self.objects.create(interviewer=interviewer_text, score=score_int,
                            helpful=helpful_sentence, communication=communication_sentence)

    def query(self):
        raise NotImplementedError


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

    @staticmethod
    def update(request):

        if 'interviewee' in request.POST:
            InterviewER_EvaluationFormDB.update(InterviewER_EvaluationFormDB, request)
        else:
            InterviewEE_EvaluationFormDB.update(InterviewEE_EvaluationFormDB, request)


class InterviewerForm(EvalForm):
    questions = Question.objects.filter(target__gte=0)


class IntervieweeForm(EvalForm):
    questions = Question.objects.filter(target__lte=0)
