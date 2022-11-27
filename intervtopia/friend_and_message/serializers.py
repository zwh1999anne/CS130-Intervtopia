from rest_framework import serializers
from users.models import CustomUser
from .models import Friendship

class FriendshipSerializer(serializers.HyperlinkedModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')
    receiver = serializers.ReadOnlyField(source='receiver.username')
    class Meta:
        model = Friendship
        fields = [
            'id',
            'sender', 
            'receiver'
        ]


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    sender = serializers.ReadOnlyField(source='friendship.sender.username')
    receiver = serializers.ReadOnlyField(source='friendship.receiver.username')
    class Meta:
        model = Friendship
        fields = [
            'id',
            'sender', 
            'receiver',
            'message_text',
            'time'
        ]