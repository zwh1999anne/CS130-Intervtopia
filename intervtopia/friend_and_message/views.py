from django.shortcuts import render
from .serializers import FriendshipSerializer
from .models import Friendship
from rest_framework import viewsets
from rest_framework import permissions
from django.http import JsonResponse
from rest_framework.decorators import action
# Create your views here.

class FriendshipViewSet(viewsets.ModelViewSet):
    queryset = Friendship.objects.all().order_by('pub_date')
    serializer_class = FriendshipSerializer
    permission_classes = [permissions.IsAuthenticated]