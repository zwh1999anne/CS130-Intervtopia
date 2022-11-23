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
