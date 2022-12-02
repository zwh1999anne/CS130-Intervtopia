from django.test import TestCase
from interview.models import *
from external.leetCodeWrapper import leetCodeQuestionQuery, interviewQuestion
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
import random
import string
# Create your tests here.

def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))
 
username_chars = string.ascii_letters
password_chars = string.ascii_letters + string.punctuation

class addRandomQuestionTests(TestCase):

    def test_question_import_leetcode(self):
        q_count_prev = Problem.objects.all().count()
        query = leetCodeQuestionQuery()
        test_q_in_db = []
        for difficulty in range(1, 4):
            q = query.getRandomQuestion(difficulty)
            q_in_db = Problem.objects.create(name=q.getTitle(), difficulty=q.getDifficulty(), url=q.getURL())
            self.assertEqual(q_in_db.name, q.getTitle())
            self.assertEqual(q_in_db.difficulty, q.getDifficulty())
            self.assertEqual(q_in_db.url, q.getURL())
            test_q_in_db.append(q_in_db)
        q_count_now = Problem.objects.all().count()
        self.assertEqual(q_count_now - q_count_prev, 3)
        for q in test_q_in_db:
            q.delete()
        q_count_now = Problem.objects.all().count()
        self.assertEqual(q_count_now, q_count_prev)

class TestInterviewAPI(APITestCase):

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
        self.user = CustomUser.objects.get(pk=1)

        self.client = APIClient()
    
    def test_interviewee_confirm(self):
        self.assertEqual(len(self.user.todo.all()), 0)
        data = {
            "username": self.user.username,
            "viewer": CustomUser.objects.get(pk = 2).username,
            "viewee": self.user.username,
            "difficulty": "E",
            "datetime": "11/26/22 17:24:00"
        }
        self.client.force_authenticate(user=self.user)
        url = reverse('confirm')
        response = self.client.post(url, data, format='json').json()
        self.assertEqual(response['owner'], self.user.username)
        self.assertEqual(response['name'], CustomUser.objects.get(pk = 2).username)
        self.assertEqual(response['type'], 'I')
        self.assertEqual(response['role'], 'EE')
        self.assertNotEqual(response['link'], '')
        self.assertEqual(len(self.user.todo.all()), 1)
        # Get Interview object
        interview_response = self.client.get(response['link'], format='json').json()
        self.assertEqual(interview_response['problems'][0]['difficulty'], 'E')
        self.assertNotEqual(interview_response['problems'][0]['url'], '')
        self.assertNotEqual(interview_response['room_link'], '')
        self.assertNotEqual(interview_response['ide_link'], '')

    def test_interviewer_confirm(self):
        self.assertEqual(len(self.user.todo.all()), 0)
        data = {
            "username": self.user.username,
            "viewer": self.user.username,
            "viewee": CustomUser.objects.get(pk = 2).username,
            "difficulty": "H",
            "datetime": "11/26/22 17:24:00"
        }
        self.client.force_authenticate(user=self.user)
        url = reverse('confirm')
        response = self.client.post(url, data, format='json').json()
        self.assertEqual(response['owner'], self.user.username)
        self.assertEqual(response['name'], CustomUser.objects.get(pk = 2).username)
        self.assertEqual(response['type'], 'I')
        self.assertEqual(response['role'], 'ER')
        self.assertNotEqual(response['link'], '')
        self.assertEqual(len(self.user.todo.all()), 1)
        # Get Interview object
        interview_response = self.client.get(response['link'], format='json').json()
        self.assertEqual(interview_response['problems'][0]['difficulty'], 'H')
        self.assertNotEqual(interview_response['problems'][0]['url'], '')
        self.assertNotEqual(interview_response['room_link'], '')
        self.assertNotEqual(interview_response['ide_link'], '')

    def test_invalid_request_to_confirm(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('confirm')
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, 404)

    
    def test_complete(self):
        self.assertEqual(len(self.user.history.all()), 0)
        self.assertEqual(len(self.user.todo.all()), 0)

        # Create a todo object by calling the confirm API
        data = {
            "username": self.user.username,
            "viewer": self.user.username,
            "viewee": CustomUser.objects.get(pk = 2).username,
            "difficulty": "H",
            "datetime": "11/26/22 17:24:00"
        }
        self.client.force_authenticate(user=self.user)
        url = reverse('confirm')
        response = self.client.post(url, data, format='json').json()
        todo_id = response['id']
        
        # Examine the updated todo object
        url = reverse('complete')
        response = self.client.get(url, {"todo": todo_id}, format = 'json')
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data['type'], 'E')
        self.assertEqual(len(self.user.history.all()), 1)

        # Examine the created history object
        hist = self.user.history.all()[0]
        self.assertEqual(hist.owner.username, self.user.username)
        self.assertEqual(hist.name, CustomUser.objects.get(pk = 2).username)
        self.assertEqual(hist.role, 'ER')
        self.assertEqual(hist.evaluated, False)
    
    def test_invalid_request_to_complete(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('complete')
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, 404)

    def test_join_meeting(self):
        # Create a todo object by calling the confirm API
        data = {
            "username": self.user.username,
            "viewer": self.user.username,
            "viewee": CustomUser.objects.get(pk = 2).username,
            "difficulty": "H",
            "datetime": "11/26/22 17:24:00"
        }
        self.client.force_authenticate(user=self.user)
        url = reverse('confirm')
        response = self.client.post(url, data, format='json').json()
        todo_id = response['id']

        # Examine the returned interview object
        url = reverse('join')
        response = self.client.get(url, {"todo": todo_id}, format = 'json')
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data['viewer'], self.user.username)
        self.assertEqual(response_data['viewee'], CustomUser.objects.get(pk = 2).username)
        self.assertEqual(response_data['problems'][0]['difficulty'], 'H')
        self.assertNotEqual(response_data['problems'][0]['url'], '')
        self.assertNotEqual(response_data['room_link'], '')
        self.assertNotEqual(response_data['ide_link'], '')

    def test_invalid_request_to_join_meeting(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('join')
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, 404)