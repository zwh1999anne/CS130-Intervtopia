from django.shortcuts import render
from .serializers import FriendshipSerializer
from .models import Friendship, Message
from rest_framework import viewsets
from rest_framework import permissions
from django.http import JsonResponse
from rest_framework.decorators import action
# Create your views here.

class FriendshipViewSet(viewsets.ModelViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer
    permission_classes = [permissions.IsAuthenticated]


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = FriendshipSerializer
    permission_classes = [permissions.IsAuthenticated]