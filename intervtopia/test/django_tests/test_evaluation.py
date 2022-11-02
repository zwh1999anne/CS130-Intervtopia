from django.test import TestCase, Client
from evaluation.models import Question
from django.urls import reverse
# Create your tests here.

def create_question(question_text, target):
    '''
    target: who will answer this question
        value = 0: both interviewer and interviewee should answer
        value = 1: the question is for interviewer only
        value = -1: the question is for interviewee only
    '''
    return Question.objects.create(question_text = question_text, target = target)

class QuestionModelTests(TestCase):

    def test_creating_a_question_for_interviewee(self):
        question = create_question("Test Question for interviewee", target=-1)
        self.assertEqual(question.target, -1)

class IndexViewTests(TestCase):

    def test_default_index_view(self):
        response = self.client.get(reverse('evaluation:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You're at the evaluation forms")


class EvaluationFormTests(TestCase):

    def test_interviewer_form_view(self):
        response = self.client.get(reverse('evaluation:interviewer'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['question_list'], Question.objects.filter(target__gte = 0))

class EvaluationFormTests2(TestCase):

    def test_interviewer_form_view(self):
        response = self.client.get(reverse('evaluation:interviewer'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['question_list'], Question.objects.filter(target__gte = 0))
