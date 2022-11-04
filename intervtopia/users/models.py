from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils.timezone import now
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


class Calender(models.Model):
    ext_url = models.URLField()

    def __str__(self) -> str:
        return self.ext_url


class CustomUser(AbstractUser):
    difficulty_choices = [('E', 'Easy'), ('M', 'Medium'), ('H', 'Hard'), ('', 'Select a difficulty')]
    target_companys = models.ManyToManyField(Company)
    target_positions = models.ManyToManyField(Position)
    preferred_languages = models.ManyToManyField(Language)
    preferred_difficulty = models.CharField(max_length=1, choices=difficulty_choices, default='')
    availability = models.OneToOneField(Calender, on_delete=models.CASCADE, null=True)
    history = models.JSONField(blank=True, null=True)
    rating = models.FloatField(default=0)
    matching_choices = [('random', 'RandomMatching'), ('preference', 'PreferenceMatching')]
    matchingStrategy = models.CharField(max_length=20, choices=matching_choices, default='random')

    def __str__(self) -> str:
        return self.username

    def add_target_company(self, company: Company) -> bool:
        '''
        TODO: add a new company to the target company list
            if the company is already in the database, simply add it to the user's target_companys 
            if the company is not in the database, first add it to the database, then include it in the user's target_companys
            return True if success, report error otherwise
        '''

    def remove_target_company(self, company: Company) -> bool:
        '''
        TODO: remove the specified company from the user's target company list, but keep it in the database
            return True if success, report error otherwise
        '''

    def add_target_position(self, position: Position) -> bool:
        '''
        TODO: add a new position to the target position list
            if the position is already in the database, simply add it to the user's target_positions 
            if the position is not in the database, first add it to the database, then include it in the user's target_positions
            return True if success, report error otherwise
        '''

    def remove_target_position(self, position: Position) -> bool:
        '''
        TODO: remove the specified company from the user's target company list, but keep it in the database
            return True if success, report error otherwise
        '''

    def add_preferred_language(self, lang: Language) -> bool:
        '''
        TODO: add a new Language to the target position list
            return True if success, report error otherwise
        '''

    def remove_preferred_language(self, lang: Language) -> bool:
        '''
        TODO: add a new Language to the target position list
            return True if success, report error otherwise
        '''

    def set_preferred_difficulty(self, diff: str) -> bool:
        '''
        TODO: set the user's preferred difficulty
            return True if success, report error otherwise
        '''

    def update_history(self, new_interivew: str) -> bool:
        '''
        TODO: add the new interview information to the history list
            return True if success, report error otherwise
        '''

    def get_historic_meetings(self) -> dict:
        '''
        TODO: return the history of interview in the JSON format
        '''

    def set_availability(self, avail: datetime) -> bool:
        '''
        TODO: set user's availability
            return True if success, report error otherwise
        '''

    def set_rating(self, rating: float) -> bool:
        '''
        TODO: set user's rating
            return True if success, report error otherwise
        '''

    def set_matching_strategy(self, strategy: str) -> bool:
        '''
        TODO: set user's matching strategy
            return True if success, report error otherwise
        '''


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
        '''


class RandomMatching(MatchingStrategy):
    strategy_name = "Random Matching"

    def getPair(self, user: CustomUser):
        '''
        TODO: implement the random matching algorithm
        '''


class PreferenceMatching(MatchingStrategy):
    strategy_name = "Preference Matching"

    def getPair(self, user: CustomUser):
        '''
        TODO: implement the perference matching algorithm
        '''
