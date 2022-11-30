from rest_framework import serializers
from users.models import CustomUser
from .models import Friendship, Message


class FriendshipSerializer(serializers.HyperlinkedModelSerializer):
    sender = serializers.HyperlinkedRelatedField(many=False, view_name='customuser-detail', queryset=CustomUser.objects.all())
    receiver = serializers.HyperlinkedRelatedField(many=False, view_name='customuser-detail', queryset=CustomUser.objects.all())

    class Meta:
        model = Friendship
        fields = ['id', 'sender', 'receiver']


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    friendship = serializers.HyperlinkedRelatedField(many=False, view_name='friendship-detail', queryset=Friendship.objects.all())

    class Meta:
        model = Message
        fields = ['id', 'friendship', 'message_text', 'time']
