from django.db import models
from django.contrib.auth.models import AbstractUser
# import sys, os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "..")
from interview.models import *
from evaluation.models import *

class CustomUser(AbstractUser):
    preference = models.JSONField()
    availability = models.DateTimeField()
    history = models.JSONField()
    rating = models.FloatField()
    matchingStrategy = models.CharField(max_length = 200)

    def __str__(self):
        return self.username

class Preference:
    languages = []
    targetCompanys = []
    targetPositions = []
    preferredDifficulty = []

    def toJSON(self):
        '''
        TODO: convert preferences to JSON Format, adapter to the CustomUser's perference field
        '''

    def setLanguages(self, lang: str):
        '''
        TODO: set preferred programming languages, need to check repetition, better to use a selection from a predefined list
        '''

    def setTargetCompanys(self, comp: str):
        '''
        TODO: set target companys, need to check repetition
        '''

    def setTargetPositions(self, pos: str):
        '''
        TODO: set target positions, need to check repetition
        '''

    def setDifficulty(self, diff: str):
        '''
        TODO: set preferred question difficulty level. Allow selection from easy, medium, hard
        '''

class History:
    interviews = []

    def toJSON(self):
        '''
        TODO: convert the history interviews to JSON format
        '''

    def addInterview(self, interview: Interview):
        self.interviews.append(interview)


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

class Interviewer(CustomUser):
    evalform = InterviewerForm()

class Interviewee(CustomUser):
    evalform = IntervieweeForm()