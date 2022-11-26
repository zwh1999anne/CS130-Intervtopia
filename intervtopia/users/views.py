from django.shortcuts import render
from .serializers import UserSerializer, ToDoSerializer, HistorySerializer, MatchingSerializer
from .models import CustomUser, ToDoItem, HistoryItem, RandomMatching
from rest_framework import viewsets
from rest_framework import permissions
from django.http import JsonResponse
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDoItem.objects.all().order_by('time')
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = HistoryItem.objects.all().order_by('time')
    serializer_class = HistorySerializer
    permission_classes = [permissions.IsAuthenticated]

def match(request):
    if request.type == "Random":
        # Do random matching
        pair = RandomMatching.getPair()
        serialized_data = MatchingSerializer(pair)


    elif request.type == "Preference":
        # Do preference matching
        pass
    else:
        # Do history matching
        pass