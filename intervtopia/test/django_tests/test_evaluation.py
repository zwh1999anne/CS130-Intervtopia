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
            self.assertEqual(q.score, 0)


    def test_invalid_request_to_evaluate(self):
        self.client.force_authenticate(user=self.viewer)
        url = reverse('evaluate')
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, 404)

    def test_submit(self):
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
        self.assertEqual(len(HistoryItem.objects.all()), 1)
        # hist_id = HistoryItem.objects.all()[0].pk

        # Make a new request to the evaluate API
        url = reverse('evaluate')
        response = self.client.get(url, {"todo": todo_id}, format = 'json')
        self.assertEqual(response.status_code, 200)
        eval_id = response.json()['id']
        self.assertEqual(eval_id, 1)

        questions = response.json()['questions']
        question_ids = [int(q.split('/')[-2]) for q in questions]
        question_scores = random.choices(list(range(1,6)), k = len(question_ids))
        cmmts = random_string_generator(50, password_chars)
        data = {
            "form":eval_id,
            "questions":[],
            "comments" : cmmts
        }
        for i in range(len(question_ids)):
            data['questions'].append({"id":question_ids[i], "score": question_scores[i]})
        
        url = reverse('submit')
        response = self.client.post(url, data, format='json')
        response_data = response.json()
        for i in range(len(question_ids)):
            self.assertEqual(Question.objects.get(pk = question_ids[i]).score, question_scores[i])
        self.assertEqual(response_data['comments'], cmmts)


    def test_invalid_request_to_submit(self):
        self.client.force_authenticate(user=self.viewer)
        url = reverse('submit')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, 404)
