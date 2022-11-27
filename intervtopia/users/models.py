from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils.timezone import now
import math
import random
# from interview.models import *


class Language(models.Model):
    lang_name = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.lang_name

    @staticmethod
    def add(lang: str):
        if len(Language.objects.filter(lang_name=lang)) == 0:
            lang = Language.objects.create(lang_name=lang)
            return lang

    @staticmethod
    def remove(lang: str):
        filter_results = Language.objects.filter(lang_name=lang)
        if len(filter_results) != 0:
            filter_results.delete()

    @staticmethod
    def get(lang: str):
        return Language.objects.filter(lang_name=lang)


class Company(models.Model):
    company_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.company_name

    @staticmethod
    def add(company: str):
        if len(Company.objects.filter(company_name=company)) == 0:
            comp = Company.objects.create(company_name=company)
            return comp

    @staticmethod
    def remove(company: str):
        filter_results = Company.objects.filter(company_name=company)
        if len(filter_results) != 0:
            filter_results.delete()

    @staticmethod
    def update(old_name: str, new_name: str):
        filter_results = Company.objects.filter(company_name=old_name)
        if len(filter_results) != 0:
            filter_results[0].update(company_name=new_name)
        return Company.objects.filter(company_name=new_name)

    @staticmethod
    def get(company: str):
        return Company.objects.filter(company_name=company)


class Position(models.Model):
    position_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.position_name

    @staticmethod
    def add(position: str):
        if len(Position.objects.filter(position_name=position)) == 0:
            pos = Position.objects.create(position_name=position)
            return pos

    @staticmethod
    def remove(position: str):
        filter_results = Position.objects.filter(position_name=position)
        if len(filter_results) != 0:
            filter_results.delete()

    @staticmethod
    def update(old_name: str, new_name: str):
        filter_results = Position.objects.filter(position_name=old_name)
        if len(filter_results) != 0:
            filter_results[0].update(position_name=new_name)

    @staticmethod
    def get(position: str):
        return Position.objects.filter(position_name=position)

'''
class Calendar(models.Model):
    ext_url = models.URLField()

    def __str__(self) -> str:
        return self.ext_url

    @staticmethod
    def add(calendar_url: str):
        if len(Calendar.objects.filter(ext_url=calendar_url)) == 0:
            cal = Calendar.objects.create(ext_url=calendar_url)
            return cal

    @staticmethod
    def remove(calendar_url: str):
        filter_results = Calendar.objects.filter(ext_url=calendar_url)
        if len(filter_results) != 0:
            filter_results.delete()

    @staticmethod
    def update(old_calendar_url: str, new_calendar_url: str):
        filter_results = Calendar.objects.filter(ext_url=old_calendar_url)
        if len(filter_results) != 0:
            filter_results[0].update(ext_url=new_calendar_url)

    @staticmethod
    def get(calendar_url: str):
        return Calendar.objects.filter(ext_url=calendar_url)
''' 

class Availability(models.Model):
    day_choices = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday')
    ]
    day = models.CharField(max_length=3, choices= day_choices, default='')
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self) -> str:
        return self.day + ': {}-{}'.format(self.start_time, self.end_time)


class CustomUser(AbstractUser):
    difficulty_choices = [('E', 'Easy'), ('M', 'Medium'), ('H', 'Hard'), ('', 'Select a difficulty')]
    target_companys = models.ManyToManyField(Company)
    target_positions = models.ManyToManyField(Position)
    preferred_languages = models.ManyToManyField(Language)
    preferred_difficulty = models.CharField(max_length=1, choices=difficulty_choices, default='')
    availability = models.ManyToManyField(Availability)
    education = models.CharField(max_length=150, default='')
    role_choices = [
        ('B', 'Both'),
        ('ER', 'Interviewer'),
        ('EE', 'Interviewee'),
    ]
    matching_choices = [('random', 'RandomMatching'), ('preference', 'PreferenceMatching')]
    matchingStrategy = models.CharField(max_length=20, choices=matching_choices, default='random')
    preferred_role = models.CharField(max_length=2, choices= role_choices, default='')
    rating = models.FloatField(default=0)
    

    def __str__(self) -> str:
        return self.username

    @staticmethod
    def create_user_base(username: str, password: str, email: str):
        '''
        TODO: Create a base user object and store it in the database, return the object
        '''

    def add_target_company(self, company: str) -> int:
        '''
        TODO: add a new company to the target company list
            if the company is already in the database, simply add it to the user's target_companys 
            if the company is not in the database, first add it to the database, then include it in the user's target_companys
            return True if success, report error otherwise
        '''
        if company == '':
            return -1
        print("Adding {} to user's target company list".format(company))
        return 0

    def remove_target_company(self, company: str) -> int:
        '''
        TODO: remove the specified company from the user's target company list, but keep it in the database
            return True if success, report error otherwise
        '''
        if company == '':
            return False
        print("Remove {} from user's target company list".format(company))
        return True

    def add_target_position(self, position: str) -> int:
        '''
        TODO: add a new position to the target position list
            if the position is already in the database, simply add it to the user's target_positions 
            if the position is not in the database, first add it to the database, then include it in the user's target_positions
            return True if success, report error otherwise
        '''
        print("Add {} to user's target positions".format(position))
        return True

    def remove_target_position(self, position: str) -> int:
        '''
        TODO: remove the specified company from the user's target company list, but keep it in the database
            return True if success, report error otherwise
        '''
        print("Remove {} from user's target position".format(position))
        return True

    def add_preferred_language(self, lang: str) -> int:
        '''
        TODO: add a new Language to the target position list
            return True if success, report error otherwise
        '''
        print("Add {} to user's preferred language".format(lang))
        return True

    def remove_preferred_language(self, lang: str) -> int:
        '''
        TODO: add a new Language to the target position list
            return True if success, report error otherwise
        '''
        print("Remove {} from user's preferred language".format(lang))
        return True

    def set_preferred_difficulty(self, diff: str) -> int:
        '''
        TODO: set the user's preferred difficulty
            return True if success, report error otherwise
        '''

        print("Set user's preferred difficulty as {}".format(diff))
        return True

    def update_history(self, new_interivew: dict) -> int:
        '''
        TODO: add the new interview information to the history list
            return True if success, report error otherwise
        Note: the input param new_interview is ideally an object of Interview. 
            However, due to python's banning on cyclic import, we cannot import Interview here.
            Method to fix this problem is going to be lookup.
        '''
        print("Adding meeting {} to user's history".format(new_interivew))
        return True

    def get_historic_meetings(self) -> dict:
        '''
        TODO: return the history of interview in the JSON format
        '''
        print("This should report user's historic meetings")
        return True

    def set_calendar(self, calendar: str) -> int:
        '''
        TODO: set user's availability
            return True if success, report error otherwise
        '''
        print("Setting user's calendar to {}".format(calendar))
        return True

    def set_rating(self, rating: float) -> int:
        '''
        TODO: set user's rating
            return True if success, report error otherwise
        '''
        print("Setting user's rating to {}".format(rating))
        return True

    def set_matching_strategy(self, strategy: str) -> int:
        '''
        TODO: set user's matching strategy
            return True if success, report error otherwise
        '''
        print("Setting user's matching strategy to {}".format(strategy))
        return True


class ToDoItem(models.Model):
    '''
    name: "Yadi C",
    type: "interview",
    time: "Nov 7th, 10: 00"
    '''
    type_choices = [
        ('I', 'Interview'), 
        ('E', 'Evaluation')
    ]
    role_choices = [
        ('ER', 'Interviewer'),
        ('EE', 'Interviewee')
    ]
    owner = models.ForeignKey(CustomUser,  related_name='todo', on_delete=models.CASCADE)
    name = models.CharField(max_length=150, default='')
    type = models.CharField(max_length=1, choices=type_choices)
    role = models.CharField(max_length=2, choices=role_choices, null=True)
    time = models.DateTimeField(auto_now_add=True)
    link = models.URLField(null=True)
    
class HistoryItem(models.Model):
    '''
    id: "1",
    name: "Haofan L",
    time: "Nov 1st, 9: 00",
    evaluated: "No"
    '''
    role_choices = [
        ('ER', 'Interviewer'),
        ('EE', 'Interviewee')
    ]
    owner = models.ForeignKey(CustomUser, related_name='history', on_delete=models.CASCADE)
    name = models.CharField(max_length=150, default='')
    time = models.DateTimeField(default=now)
    role = models.CharField(max_length=2, choices=role_choices, null=True)
    evaluated = models.BooleanField(default=False)


'''
    The Matching Strategy interface
    Strategy Pattern
'''


class MatchingStrategy:
    strategy_name = ""

    def __str__(self) -> str:
        return self.strategy_name

    def getPair(self, user: CustomUser):
        '''
        TODO: to be implemented by subclasses
            return the another user object
        '''


class RandomMatching(MatchingStrategy):
    
    strategy_name = "Random Matching"

    def getPair(self, user: CustomUser):
        queryset = CustomUser.objects.all()
        idx = random.randint(1, len(queryset))
        pair = CustomUser.objects.get(pk = idx)
        print(pair.username)
        return pair


class PreferenceMatching(MatchingStrategy):
    strategy_name = "Preference Matching"
    feature_dict = {}

    def _get_feature_dict(self):
        '''
        Each feature vector is formatted as below:
        [
            language_1,
            language_2
            company,
            position,
            difficulty,
            role,
            availability_1,
            availability_2
        ]
        '''
        difficulty_lut = {
            'E':0,
            'M':1,
            'H':2
        }
        role_lut = {
            'B': 0,
            'ER': 1,
            'EE': -1
        }
        queryset = CustomUser.objects.all()
        feature_vecs = {}
        for u in queryset:
            vec = []
            lang = u.preferred_languages.all()
            if len(lang) == 0:
                vec += [-1,-1]
            elif len(lang) == 1:
                vec += [lang[0].pk,-1]
            else:
                vec += [lang[0].pk, lang[1].pk]

            comp = u.target_companys.all()
            if len(comp) == 0:
                vec.append(-1)
            else:
                vec.append(comp[0].pk)
            
            pos = u.target_positions.all()
            if len(pos) == 0:
                vec.append(-1)
            else:
                vec.append(pos[0].pk)

            if u.preferred_difficulty == '':
                vec.append(-1)
            else:
                vec.append(difficulty_lut[u.preferred_difficulty])

            role = 0 - role_lut[u.preferred_role] 
            vec.append(role)

            avai = u.availability.all()
            if len(avai) == 0:
                vec += [-1, -1]
            elif len(avai) == 1:
                vec += [avai[0].pk, -1]
            else:
                vec += [avai[0].pk, avai[1].pk]

            assert(len(vec) == 8)
            feature_vecs[u.username] = vec
        self.feature_dict = feature_vecs

    def getPair(self, user: CustomUser):
        '''
        Find matching based on feature vector
        '''
        self._get_feature_dict()
        print(self.feature_dict)
        usr_vec = self.feature_dict[user.username]
        score_dict = {}
        for k, v in self.feature_dict.items():
            if k != user.username:
                score_dict[k] = math.dist(v, usr_vec)
        sorted_score_dict = sorted(score_dict)
        return CustomUser.objects.get(username = sorted_score_dict[0])
        

class HistoryMatching(MatchingStrategy):
    strategy_name = "History Matching"

    def getPair(self, user: CustomUser):
        history = HistoryItem.objects.filter(owner__username = user.username)
        if len(history) == 0:
            return None # If the user has no history, return None. The frontend should call another matching strategy
        else:
            idx = random.randint(0, len(history)-1)
            pair = CustomUser.objects.get(username = history[idx].name)
            return pair