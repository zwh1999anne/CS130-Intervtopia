from django.test import TestCase
from users.models import Language, Company, Position, Availability, CustomUser, RandomMatching, PreferenceMatching, HistoryMatching
import random
import string
from users.serializers import UserSerializer
from datetime import datetime
from django.http import JsonResponse
from users.views import UserViewSet
from django.urls import reverse
from rest_framework.parsers import JSONParser

from rest_framework.test import APIClient, APITestCase

# Create your tests here.
def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))
 
username_chars = string.ascii_letters
password_chars = string.ascii_letters + string.punctuation

class TestCustomUser(TestCase):
    # Test create a user
    def setUp(self):
        uname = random_string_generator(10, username_chars)
        pwd = random_string_generator(15, password_chars)
        if len(CustomUser.objects.filter(username = uname)) == 0:
            self.user = CustomUser.objects.create(username = uname, password = pwd)
            self.assertEqual(self.user.password, pwd)
        else:
            self.user = CustomUser.objects.get(username = uname)
        self.assertEqual(self.user.username, uname)

        self.comp_name = random_string_generator(6, string.ascii_letters)
        self.comp_name_2 = random_string_generator(5, string.ascii_letters)

        self.lang_name = random_string_generator(6, string.ascii_letters)
        self.lang_name_2 = random_string_generator(5, string.ascii_letters)

        self.pos_name = random_string_generator(20, string.ascii_letters)
        self.available_day = 'Mon'
        self.available_start_time = "12:00"
        self.available_end_time = "14:00"

        self.additional_day = 'Fri'
        self.additional_start_time = '17:00'
        self.additional_end_time = '19:00'

        self.difficulty = 'M'
        self.role = 'ER'
        self.matching = 'preference'
        
        self.rating = 0.5

        self.client = APIClient()
        

    def test_create_user(self):
        self.assertEqual(self.user.first_name, '')
        self.assertEqual(self.user.last_name, '')
        self.assertQuerysetEqual(self.user.target_companys.all(), [])
        self.assertQuerysetEqual(self.user.target_positions.all(), [])
        self.assertQuerysetEqual(self.user.preferred_languages.all(), [])
        self.assertQuerysetEqual(self.user.availability.all(), [])
        self.assertEqual(self.user.preferred_difficulty, '')
        self.assertEqual(self.user.education, '')
        self.assertEqual(self.user.matchingStrategy, 'random')
        self.assertEqual(self.user.rating, 0.0)

    def test_set_target_company(self):
        comp, created = Company.objects.get_or_create(company_name = self.comp_name)
        self.user.target_companys.add(comp)
        self.assertQuerysetEqual(self.user.target_companys.all(), [comp])
        comp_2, created = Company.objects.get_or_create(company_name = self.comp_name_2)
        self.user.target_companys.add(comp_2)
        self.assertQuerysetEqual(self.user.target_companys.all(), [comp, comp_2], ordered=False)

    def test_set_preferred_language(self):
        lang, created = Language.objects.get_or_create(lang_name = self.lang_name)
        self.user.preferred_languages.add(lang)
        self.assertQuerysetEqual(self.user.preferred_languages.all(), [lang])
        lang_2, created = Language.objects.get_or_create(lang_name = self.lang_name_2)
        self.user.preferred_languages.add(lang_2)
        self.assertQuerysetEqual(self.user.preferred_languages.all(), [lang, lang_2], ordered=False)

    def test_set_target_position(self):
        pos, created = Position.objects.get_or_create(position_name = self.pos_name)
        self.user.target_positions.add(pos)
        self.assertQuerysetEqual(self.user.target_positions.all(), [pos])

    def test_set_availability(self):
        st = datetime.strptime(self.available_start_time, "%H:%M").time()
        et = datetime.strptime(self.available_end_time, "%H:%M").time()
        avai_1, created = Availability.objects.get_or_create(day = self.available_day, start_time = st, end_time = et)
        self.user.availability.add(avai_1)
        self.assertQuerysetEqual(self.user.availability.all(), [avai_1])

        st = datetime.strptime(self.additional_start_time, "%H:%M").time()
        et = datetime.strptime(self.additional_end_time, "%H:%M").time()
        avai_2, created = Availability.objects.get_or_create(day = self.additional_day, start_time = st, end_time = et)
        self.user.availability.add(avai_2)
        self.assertQuerysetEqual(self.user.availability.all(), [avai_1, avai_2], ordered=False)

    def test_set_difficulty_role_matching_strategy_rating(self):
        self.user.preferred_difficulty = self.difficulty
        self.user.matchingStrategy = self.matching
        self.user.preferred_role = self.role
        self.user.rating = self.rating
        self.user.save()
        self.assertEqual(self.user.preferred_difficulty, self.difficulty)
        self.assertEqual(self.user.matchingStrategy, self.matching)
        self.assertEqual(self.user.preferred_role, self.role)
        self.assertEqual(self.user.rating, self.rating)

class TestUserAPI(APITestCase):

    def setUp(self):
        uname = random_string_generator(10, username_chars)
        pwd = random_string_generator(15, password_chars)
        if len(CustomUser.objects.filter(username = uname)) == 0:
            self.user = CustomUser.objects.create(username = uname, password = pwd)
            self.assertEqual(self.user.password, pwd)
        else:
            self.user = CustomUser.objects.get(username = uname)
        self.assertEqual(self.user.username, uname)


    def test_update_preference(self):
        data = {
            "username":self.user.username,
            "email":"test@example.com",
            "school":"UCLA Computer Science",
            "job_role":"software engineer",
            "interview_role":"B",
            "first_language":"C++",
            "second_language":"Python",
            "desired_difficulty":"H",
            "available_day":"Tue",
            "available_time":"10:00 - 11:00",
            "additional_available_day":"Thu",
            "additional_available_time":"14:00 - 15:00"
        }

        self.client.force_authenticate(user=self.user)
        url = reverse('preference')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(CustomUser.objects.count(), 1)

        updated_user = CustomUser.objects.get(pk = self.user.pk)
        self.assertEqual(updated_user.email, "test@example.com")
        self.assertEqual(updated_user.education, "UCLA Computer Science")
        self.assertEqual(len(updated_user.target_positions.all()), 1)
        self.assertEqual(updated_user.target_positions.all()[0].position_name, "Software engineer")
        self.assertEqual(updated_user.preferred_role, 'B')
        self.assertQuerysetEqual(updated_user.preferred_languages.all(), [Language.objects.get(lang_name='C++'), Language.objects.get(lang_name='Python')], ordered=False)
        self.assertEqual(updated_user.preferred_difficulty, 'H')

        
        st = datetime.strptime("10:00", "%H:%M").time()
        et = datetime.strptime("11:00", "%H:%M").time()
        avai_1, _ = Availability.objects.get_or_create(day = 'Tue', start_time = st, end_time = et)

        st = datetime.strptime("14:00", "%H:%M").time()
        et = datetime.strptime("15:00", "%H:%M").time()
        avai_2, _ = Availability.objects.get_or_create(day = 'Thu', start_time = st, end_time = et)
        self.assertQuerysetEqual(updated_user.availability.all(), [avai_1, avai_2], ordered=False)
        
class TestMatching(APITestCase):

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

        for i in range(10):
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

        self.assertEqual(len(CustomUser.objects.all()), 10)
        self.user = CustomUser.objects.get(pk=1)

    def test_random_matching(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('matching')
        response = self.client.get(url, {'type': 'random', 'user': self.user.username}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.json()['name'], self.user.username)

    def test_preference_matching(self):
        # Create a perfect matching profile
        uname = random_string_generator(10, username_chars)
        pwd = random_string_generator(15, password_chars)
        u = CustomUser.objects.create(username = uname, password = pwd)
        u.add_target_company(self.user.target_companys.all()[0].company_name)
        u.add_target_position(self.user.target_positions.all()[0].position_name)
        u.add_preferred_language(self.user.preferred_languages.all()[0].lang_name)
        role = 'EE' if self.user.preferred_role == 'ER' else 'ER'
        u.set_preferred_role(role=role)
        u.set_preferred_difficulty(self.user.preferred_difficulty)
        avai = self.user.availability.all()[0]
        u.add_availability(day = avai.day, start_time=str(avai.start_time)[:5], end_time= str(avai.end_time)[:5])
        u.save_changes()
        self.client.force_authenticate(user=self.user)
        url = reverse('matching')
        response = self.client.get(url, {'type': 'preference', 'user': self.user.username}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.json()['name'], self.user.username)

    def test_history_matching(self):
        self.assertEqual(len(self.user.history.all()), 0)
        self.client.force_authenticate(user=self.user)
        url = reverse('matching')
        response = self.client.get(url, {'type': 'history', 'user': self.user.username}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.json())
        
        self.user.update_history({"name": CustomUser.objects.get(pk = 2).username, "role": "ER"})
        self.assertEqual(len(self.user.history.all()), 1)

        url = reverse('matching')
        response = self.client.get(url, {'type': 'history', 'user': self.user.username}, format='json')
        self.assertEqual(response.status_code, 200)
        response_name = response.json()['name']
        self.assertNotEqual(response_name, self.user.username)
        self.assertEqual(response_name, CustomUser.objects.get(pk = 2).username)

