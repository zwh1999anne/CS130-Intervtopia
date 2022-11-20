from django.test import TestCase, Client
from interview.models import *
from external.leetCodeWrapper import leetCodeQuestionQuery, interviewQuestion
from django.urls import reverse
# Create your tests here.


class addRandomQuestionTests(TestCase):

    def test_question_import_leetcode(self):
        q_count_prev = Problem.objects.all().count()
        query = leetCodeQuestionQuery()
        test_q_in_db = []
        for difficulty in range(1, 4):
            q = query.getRandomQuestion(difficulty)
            q_in_db = Problem.objects.create(problem_name=q.getTitle(), problem_difficulty=q.getDifficulty(), problem_url=q.getURL(), problem_id=q.getFrontendID())
            self.assertEqual(q_in_db.problem_name, q.getTitle())
            self.assertEqual(q_in_db.problem_difficulty, q.getDifficulty())
            self.assertEqual(q_in_db.problem_url, q.getURL())
            self.assertEqual(q_in_db.problem_id, q.getFrontendID())
            test_q_in_db.append(q_in_db)
        q_count_now = Problem.objects.all().count()
        self.assertEqual(q_count_now - q_count_prev, 3)
        for q in test_q_in_db:
            q.delete()
        q_count_now = Problem.objects.all().count()
        self.assertEqual(q_count_now, q_count_prev)


class InterviewerModelTests(TestCase):

    def test_crud_a_interviewer(self):

        test_dict_response = {'name': "Test response", 'problem_solving': 2, 'communication': 3, 'coding_skill': 4, 'helpful': 1}

        response = Response.objects.create(**test_dict_response)
        user1 = CustomUser.objects.create(username='carlo')
        user2 = CustomUser.objects.create(username='david')

        test_dict_eval = {'name': "Test response", 'rating': 2, 'comments': 'no comment', 'response': response, 'targer_user': user1, 'target_role': 'EE'}

        evalform = EvalForm.objects.create(**test_dict_eval)

        test_dict = {'user': user1, 'evalForm': evalform}

        # create
        interviewer = Interviewer.objects.create(**test_dict)

        self.assertEqual(interviewer.user.username, "carlo")
        self.assertEqual(interviewer.evalForm.name, "Test response")

        # read
        interviewer_set = Interviewer.objects.filter(**test_dict)

        for interviewer in interviewer_set.all():
            self.assertEqual(interviewer.user.username, "carlo")
            self.assertEqual(interviewer.evalForm.name, "Test response")

        # update
        update_dict = {'user': user2}

        test_dict.update(update_dict)

        interviewer_set.update(**update_dict)
        interviewer_set = Interviewer.objects.filter(**test_dict)

        for interviewer in interviewer_set.all():
            self.assertEqual(interviewer.user.username, "david")
            self.assertEqual(interviewer.evalForm.name, "Test response")

        # delete

        interviewer_set.delete()

        interviewer_set = Interviewer.objects.filter(**test_dict)

        self.assertEqual(interviewer_set.count(), 0)

        user1.delete()
        user2.delete()
        response.delete()

        evalform.delete()


class InterviewModelTests(TestCase):

    def test_crud_a_interview(self):

        test_dict_response = {'name': "Test response", 'problem_solving': 2, 'communication': 3, 'coding_skill': 4, 'helpful': 1}

        response = Response.objects.create(**test_dict_response)

        user1 = CustomUser.objects.create(username='carlo')
        user2 = CustomUser.objects.create(username='david')

        test_dict_eval_ee = {'name': "Test response", 'rating': 2, 'comments': 'no comment', 'response': response, 'targer_user': user1, 'target_role': 'EE'}

        test_dict_eval_er = {'name': "Test response", 'rating': 2, 'comments': 'no comment', 'response': response, 'targer_user': user2, 'target_role': 'ER'}

        evalform_ee = EvalForm.objects.create(**test_dict_eval_ee)
        evalform_er = EvalForm.objects.create(**test_dict_eval_er)

        interviewer = Interviewer.objects.create(user=user1, evalForm=evalform_er)
        interviewee = Interviewee.objects.create(user=user2, evalForm=evalform_ee)

        test_dict = {'name': "Test interview", 'viewER': interviewer, 'viewEE': interviewee, 'date_and_time': '2022-11-04 14:30', 'room_link': 'www.google.com'}

        # create
        interview = Interview.objects.create(**test_dict)

        self.assertEqual(interview.viewER.user.username, "carlo")
        self.assertEqual(interview.viewEE.user.username, "david")
        self.assertEqual(interview.name, "Test interview")

        # read
        interview_set = Interview.objects.filter(**test_dict)

        for interview in interview_set.all():
            self.assertEqual(interview.viewER.user.username, "carlo")
            self.assertEqual(interview.viewEE.user.username, "david")
            self.assertEqual(interview.name, "Test interview")

        # update
        update_dict = {'date_and_time': '2022-11-04 14:50'}

        test_dict.update(update_dict)

        interview_set.update(**update_dict)
        interview_set = Interview.objects.filter(**test_dict)

        for interview in interview_set.all():
            self.assertEqual(interview.viewER.user.username, "carlo")
            self.assertEqual(interview.viewEE.user.username, "david")
            self.assertEqual(interview.name, "Test interview")
            self.assertEqual(interview.date_and_time, '2022-11-04 14:50')

        # delete

        interview_set.delete()

        interview_set = Interview.objects.filter(**test_dict)

        self.assertEqual(interview_set.count(), 0)

        interviewer.delete()
        interviewee.delete()

        user1.delete()
        user2.delete()
        response.delete()


class ProblemModelTests(TestCase):

    def test_crud_a_problem(self):

        test_dict = {'problem_name': "Test problem", 'problem_url': 'www.google.com', 'problem_statement': 'this is a test problem', 'problem_difficulty': 'M'}

        # create
        problem = Problem.objects.create(**test_dict)

        self.assertEqual(problem.problem_name, "Test problem")
        self.assertEqual(problem.problem_url, "www.google.com")
        self.assertEqual(problem.problem_statement, "this is a test problem")
        self.assertEqual(problem.problem_difficulty, "M")

        # read
        problem_set = Problem.objects.filter(**test_dict)

        for problem in problem_set.all():
            self.assertEqual(problem.problem_name, "Test problem")
            self.assertEqual(problem.problem_url, "www.google.com")
            self.assertEqual(problem.problem_statement, "this is a test problem")
            self.assertEqual(problem.problem_difficulty, "M")

        # update
        update_dict = {'problem_url': 'www.baidu.com', 'problem_difficulty': 'H'}

        test_dict.update(update_dict)

        problem_set.update(**update_dict)
        problem_set = Problem.objects.filter(**test_dict)

        for problem in problem_set.all():
            self.assertEqual(problem.problem_name, "Test problem")
            self.assertEqual(problem.problem_url, "www.baidu.com")
            self.assertEqual(problem.problem_statement, "this is a test problem")
            self.assertEqual(problem.problem_difficulty, "H")

        # delete
        problem_set.delete()

        problem_set = Problem.objects.filter(**test_dict)

        self.assertEqual(problem_set.count(), 0)
