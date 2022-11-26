from rest_framework import serializers
from .models import CustomUser, ToDoItem, HistoryItem

class UserSerializer(serializers.HyperlinkedModelSerializer):
    target_companys = serializers.StringRelatedField(many=True)
    target_positions = serializers.StringRelatedField(many=True)
    preferred_languages = serializers.StringRelatedField(many=True)
    availability = serializers.StringRelatedField(many = True)
    todo = serializers.HyperlinkedRelatedField(many=True,  view_name='todoitem-detail', read_only=True)
    history = serializers.HyperlinkedRelatedField(many=True,  view_name='historyitem-detail', read_only=True)
    evalform = serializers.HyperlinkedRelatedField(many=True, view_name='evalform-detail', read_only=True)
    class Meta:
        model = CustomUser
        fields = [
            'url', 
            'username', 
            'email', 
            'education',
            'target_companys', 
            'target_positions', 
            'matchingStrategy', 
            'preferred_languages', 
            'preferred_difficulty',
            'availability', 
            'preferred_role',
            'rating',
            'todo',
            'history',
            'evalform'
        ]

class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = ToDoItem
        fields = ['id', 'owner', 'name', 'type', 'time', 'link']

class HistorySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = HistoryItem
        fields = [
            'id',
            'owner',
            'name',
            'time',
            'evaluated',
        ]

class MatchingSerializer():
    '''
    name: "Wendy Y",
    first_language: "JavaScipt",
    second_language: "Python",
    desired_difficulty: "hard",
    available_day: "Tuesday",
    available_time: "10:00 - 11:00 A.M.",
    evaluation_score: "4.7"
    '''

    def __init__(self, user: CustomUser) -> None:
        self.user = user
    
    def serialize(self):
        if self.user is not None:
            difficulty_lut = {
                'E': 'easy',
                'M': 'medium',
                'H': 'hard'
            }

            name = self.user.username
            languages = [l.lang_name for l in self.user.preferred_languages.all()]
            difficulty = self.user.preferred_difficulty
            avaliability = [(a.day, a.start_time.strftime("%H:%M"), a.end_time.strftime("%H:%M")) for a in self.user.availability.all()]
            score = self.user.rating
            obj = {
                'name': name,
                'languages': languages,
                'difficulty': difficulty_lut[difficulty],
                'availability': avaliability,
                'evaluation_score': score
            }
            return obj
        else:
            return None
        
