from django.test import TestCase
from evaluation.models import *
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
import random
import string
# Create your tests here.
def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))
 
username_chars = string.ascii_letters
password_chars = string.ascii_letters + string.punctuation

class TestEvaluationAPI(APITestCase):

    def setUp(self):
        company_list = ["Google", "Amazon", "Meta", "Apple", "Microsoft"]
        position_list = ["Software Engineer", "Software Intern", "Product Manager", "Software Specialist"]
        language_list = ["Python", "C++", "C#", "Java", "JavaScript", "PHP"]
        role_list = ['B', 'ER', 'EE']
        difficulty_list = ['E', 'M', 'H']
        day_list = ['Mon',
            'Tue',
            'Wed',
            'Thu',
            'Fri',
            'Sat',
            'Sun'
        ]
        time_list = ["{}:00".format(hour) for hour in range(0, 24) ]

        for i in range(2):
            uname = random_string_generator(10, username_chars)
            pwd = random_string_generator(15, password_chars)
            u = CustomUser.objects.create(username = uname, password = pwd)
            u.add_target_company(random.choice(company_list))
            u.add_target_position(random.choice(position_list))
            u.add_preferred_language(random.choice(language_list))
            u.set_preferred_role(random.choice(role_list))
            u.set_preferred_difficulty(random.choice(difficulty_list))
            selected_time_index =random.randint(0, 22)
            u.add_availability(random.choice(day_list), time_list[selected_time_index], time_list[selected_time_index+1])
            u.save_changes()

        self.assertEqual(len(CustomUser.objects.all()), 2)
        self.viewer = CustomUser.objects.get(pk=1)
        self.viewee = CustomUser.objects.get(pk=2)

        self.client = APIClient()

    def test_interviewer_evaluate(self):
        self.assertEqual(len(EvalForm.objects.all()), 0)
        # Create a todo object by calling the confirm API
        data = {
            "username": self.viewer.username,
            "viewer": self.viewer.username,
            "viewee": self.viewee.username,
            "difficulty": "H",
            "datetime": "11/26/22 17:24:00"
        }
        self.client.force_authenticate(user=self.viewer)
        url = reverse('confirm')
        response = self.client.post(url, data, format='json').json()
        todo_id = response['id']

        # Make a request to complete to update the todo
        url = reverse('complete')
        response = self.client.get(url, {"todo": todo_id}, format = 'json')
        self.assertEqual(response.status_code, 200)

        # Make a new request to the evaluate API
        url = reverse('evaluate')
        response = self.client.get(url, {"todo": todo_id}, format = 'json')
        self.assertEqual(response.status_code, 200)

        response_data = response.json()
        self.assertEqual(len(EvalForm.objects.all()), 1)
        self.assertNotEqual(response_data['name'], '')
        self.assertEqual(response_data['target_user'], self.viewer.username)
        self.assertEqual(response_data['target_role'], 'ER')
        questions = response_data['questions']
        self.assertEqual(len(questions), 4)
        self.assertEqual(response_data['comments'], "")
        question_list = [
            "How was the interviewee's problem-solving skill?",
            "How was the interviewee's communication?",
            "How was the interviewee's coding skill?",
            "How was the interview over all?"
        ]
        for q in EvalForm.objects.get(pk=1).questions.all():
            assert(q.question_text in question_list)

    def test_interviewee_evaluate(self):
        self.assertEqual(len(EvalForm.objects.all()), 0)
        # Create a todo object by calling the confirm API
        data = {
            "username": self.viewee.username,
            "viewer": self.viewer.username,
            "viewee": self.viewee.username,
            "difficulty": "H",
            "datetime": "11/26/22 17:24:00"
        }
        self.client.force_authenticate(user=self.viewee)
        url = reverse('confirm')
        response = self.client.post(url, data, format='json').json()
        todo_id = response['id']

        # Make a request to complete to update the todo
        url = reverse('complete')
        response = self.client.get(url, {"todo": todo_id}, format = 'json')
        self.assertEqual(response.status_code, 200)

        # Make a new request to the evaluate API
        url = reverse('evaluate')
        response = self.client.get(url, {"todo": todo_id}, format = 'json')
        self.assertEqual(response.status_code, 200)

        response_data = response.json()
        self.assertEqual(len(EvalForm.objects.all()), 1)
        self.assertNotEqual(response_data['name'], '')
        self.assertEqual(response_data['target_user'], self.viewee.username)
        self.assertEqual(response_data['target_role'], 'EE')
        questions = response_data['questions']
        self.assertEqual(len(questions), 4)
        self.assertEqual(response_data['comments'], "")
        question_list = [
            "How was the interviewer's description of problem?",
            "How was the interviewer's ability to create follow up questions?",
            "How was the interviewer's feedback?",
            "How was the interview over all?"
        ]
        for q in EvalForm.objects.get(pk=1).questions.all():
            assert(q.question_text in question_list)


    def test_invalid_request_to_evaluate(self):
        self.client.force_authenticate(user=self.viewer)
        url = reverse('evaluate')
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, 404)

    def test_submit(self):
        pass

    def test_invalid_request_to_submit(self):
        pass









# class QuestionModelTests(TestCase):
#     def test_crud_a_question(self):
#         test_dict = {'question_text': "Test Question for interviewee", 'target': 'EE', 'question_ranking': 99, 'question_name': 'test_q_for_ee'}

#         # create
#         question = Question.objects.create(**test_dict)

#         self.assertEqual(question.target, 'EE')
#         self.assertEqual(question.question_ranking, 99)
#         self.assertEqual(question.question_name, 'test_q_for_ee')

#         # read
#         question_set = Question.objects.filter(**test_dict)

#         for question in question_set.all():
#             self.assertEqual(question.target, 'EE')
#             self.assertEqual(question.question_ranking, 99)
#             self.assertEqual(question.question_name, 'test_q_for_ee')

#         # update
#         update_dict = {'target': 'ER', 'question_ranking': 79}

#         test_dict.update(update_dict)

#         question_set.update(**update_dict)
#         question_set = Question.objects.filter(**test_dict)

#         for question in question_set.all():
#             self.assertEqual(question.target, 'ER')
#             self.assertEqual(question.question_ranking, 79)
#             self.assertEqual(question.question_name, 'test_q_for_ee')

#         # delete
#         question_set.delete()

#         question_set = Question.objects.filter(**test_dict)

#         self.assertEqual(question_set.count(), 0)


# class EvalFormModelTests(TestCase):
#     def test_crud_a_eval_form(self):
#         test_dict_response = {'name': "Test response", 'problem_solving': 2, 'communication': 3, 'coding_skill': 4, 'helpful': 1}
#         test_dict_question1 = {'question_text': "Test Question 1 for interviewee", 'target': 'EE', 'question_ranking': 99, 'question_name': 'test_q_for_ee'}
#         test_dict_question2 = {'question_text': "Test Question 2 for interviewee", 'target': 'EE', 'question_ranking': 99, 'question_name': 'test_q_for_ee'}

#         response = Response.objects.create(**test_dict_response)
#         question1 = Question.objects.create(**test_dict_question1)
#         question2 = Question.objects.create(**test_dict_question2)
#         user = CustomUser.objects.create(username='carlo')

#         test_dict_eval = {'name': "Test response", 'rating': 2, 'comments': 'no comment', 'response': response, 'target_user': user, 'target_role': 'EE'}

#         # create
#         evalform = EvalForm.objects.create(**test_dict_eval)

#         evalform.questions.set([question1, question2])

#         self.assertEqual(evalform.name, "Test response")
#         self.assertEqual(evalform.rating, 2)
#         self.assertEqual(evalform.comments, 'no comment')
#         self.assertEqual(evalform.target_role, 'EE')
#         self.assertEqual(evalform.response.coding_skill, 4)
#         self.assertEqual(evalform.target_user.username, 'carlo')

#         # read
#         eval_set = EvalForm.objects.filter(**test_dict_eval)

#         for evalform in eval_set.all():
#             self.assertEqual(evalform.name, "Test response")
#             self.assertEqual(evalform.rating, 2)
#             self.assertEqual(evalform.comments, 'no comment')
#             self.assertEqual(evalform.target_role, 'EE')
#             self.assertEqual(evalform.response.coding_skill, 4)

#         # update
#         update_dict = {'rating': 5, 'comments': 'pretty good'}

#         test_dict_eval.update(update_dict)

#         eval_set.update(**update_dict)
#         eval_set = EvalForm.objects.filter(**test_dict_eval)

#         for evalform in eval_set.all():
#             self.assertEqual(evalform.name, "Test response")
#             self.assertEqual(evalform.rating, 5)
#             self.assertEqual(evalform.comments, 'pretty good')
#             self.assertEqual(evalform.target_role, 'EE')
#             self.assertEqual(evalform.response.coding_skill, 4)

#         # delete
#         response.delete()
#         question1.delete()
#         question2.delete()
#         user.delete()
#         eval_set.delete()

#         eval_set = EvalForm.objects.filter(**test_dict_eval)

#         self.assertEqual(eval_set.count(), 0)
