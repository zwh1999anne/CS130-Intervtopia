from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils.timezone import now
import math
import random
from django.core.exceptions import ObjectDoesNotExist
# from interview.models import *


class Language(models.Model):
    lang_name = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.lang_name


class Company(models.Model):
    company_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.company_name


class Position(models.Model):
    position_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.position_name


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

    def add_target_company(self, company: str):
        '''
        Add a new company to the target company list
        if the company is already in the database, simply add it to the user's target_companys 
        if the company is not in the database, first add it to the database, then include it in the user's target_companys
        return True if success, report error otherwise
        '''
        if company == '':
            raise ValueError("company cannot be empty string")
        comp, _ = Company.objects.get_or_create(company_name = company)
        self.target_companys.add(comp)

    def remove_target_company(self, company: str):
        '''
        Remove the specified company from the user's target company list, but keep it in the database
            return True if success, report error otherwise
        '''
        if company == '':
            raise ValueError("company cannot be empty string")
        try: 
            comp, _ = Company.objects.get(company_name = company)
            self.target_companys.remove(comp)
        except ObjectDoesNotExist:
            raise ValueError("company is not found in the database")

    def add_target_position(self, position: str):
        '''
        Add a new position to the target position list
            if the position is already in the database, simply add it to the user's target_positions 
            if the position is not in the database, first add it to the database, then include it in the user's target_positions
            return True if success, report error otherwise
        '''
        if position == '':
            raise ValueError("position cannot be empty string")
        pos, _ = Position.objects.get_or_create(position_name = position)
        self.target_positions.add(pos)

    def remove_target_position(self, position: str):
        '''
        Remove the specified company from the user's target company list, but keep it in the database
            return True if success, report error otherwise
        '''
        if position == '':
            raise ValueError("company cannot be empty string")
        try: 
            pos, _ = Position.objects.get(position_name = position)
            self.target_positions.remove(pos)
        except ObjectDoesNotExist:
            raise ValueError("position is not found in the database")

    def add_preferred_language(self, lang: str):
        '''
        Add a new Language to the preferred language list
        '''
        if lang == '':
            raise ValueError("lang cannot be empty string")
        language, _ = Language.objects.get_or_create(lang_name = lang)
        self.preferred_languages.add(language)

    def remove_preferred_language(self, lang: str) -> int:
        '''
        Remove the Language to the preferred language list
        '''
        if lang == '':
            raise ValueError("lang cannot be empty string")
        try: 
            language, _ = Language.objects.get(lang_name = lang)
            self.preferred_languages.remove(language)
        except ObjectDoesNotExist:
            raise ValueError("position is not found in the database")

    def set_preferred_difficulty(self, diff: str):
        '''
        Set the user's preferred difficulty
            return True if success, report error otherwise
        '''
        if diff not in ['E', 'M', 'H']:
            raise ValueError("Invalid input")
        self.preferred_difficulty = diff

    def update_history(self, new_interivew: dict):
        '''
        Add the new interview information to the history list
            return True if success, report error otherwise
        Note: the input param new_interview is ideally an object of Interview. 
            However, due to python's banning on cyclic import, we cannot import Interview here.
            Method to fix this problem is going to be lookup.
        new_interview = {
            name: xxx,
            role: xx,
        }
        '''
        HistoryItem.objects.create(owner = self, name = new_interivew['name'], role = new_interivew['role'])
        

    def add_availability(self, day: str, start_time: str, end_time: str):
        if day not in ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']:
            raise ValueError("Invalid input: day")
        st = datetime.strptime(start_time, "%H:%M").time()
        et = datetime.strptime(end_time, "%H:%M").time()
        if st >= et:
            raise ValueError(f"Invalid input: start_time ({start_time}) should be before end_time ({end_time})")
        
        avai, _ = Availability.objects.get_or_create(day = day, start_time = st, end_time = et)
        self.availability.add(avai)

    def remove_availability(self, day: str, start_time: str, end_time: str):
        if day not in ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']:
            raise ValueError("Invalid input: day")
        if start_time >= end_time:
            raise ValueError("Invalid input: start_time should be before end time")
        try: 
            st = datetime.strptime(start_time, "%H:%M").time()
            et = datetime.strptime(end_time, "%H:%M").time()
            avai, _ = Language.objects.get(day = day, start_time = st, end_time = et)
            self.availability.remove(avai)
        except ObjectDoesNotExist:
            raise ValueError("position is not found in the database")
        
    def get_historic_meetings(self) -> dict:
        '''
        Return the history of interviews
        '''
        return self.history.all()

    def set_rating(self, rating: float):
        '''
        Set user's rating
            return True if success, report error otherwise
        '''
        if rating >=0 and rating <= 5.0:
            self.rating = rating
        else:
            raise ValueError("Invalid input: {} is out of range [0, 5]".format(rating))

    def set_matching_strategy(self, strategy: str):
        '''
        Set user's matching strategy
            return True if success, report error otherwise
        '''
        if strategy not in ['random', 'preference', 'history']:
            raise ValueError("Invalid input")
        self.matchingStrategy = strategy

    def set_preferred_role(self, role: str):
        '''
        Set user's preferred role
        '''
        if role not in ['B', 'ER', 'EE']:
            raise ValueError("Invalid input")
        self.preferred_role = role
    
    def save_changes(self):
        self.save()



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
        choices = [u.pk for u in queryset]
        choices.remove(user.pk)
        idx = random.choice(choices)
        pair = CustomUser.objects.get(pk = idx)
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
        # print(self.feature_dict)
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