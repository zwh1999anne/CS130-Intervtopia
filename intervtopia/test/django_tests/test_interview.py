from django.test import TestCase, Client
from interview.models import Problem, ProblemDBUpdater
from external.leetCodeWrapper import leetCodeQuestionQuery, interviewQuestion
from django.urls import reverse
# Create your tests here.

def import_questions_leetcode(number_qs: int):
    pb = ProblemDBUpdater()
    pb.addProblems(number_qs)


class QuestionModelTests(TestCase):

    def test_question_import_leetcode(self):
        import_questions_leetcode(40)
        q_count= Problem.objects.all().count()
        self.assertEqual(q_count, 40)
