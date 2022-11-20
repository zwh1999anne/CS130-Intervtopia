from django.shortcuts import render
from .serializers import PreferenceSerializer, ToDoSerializer, HistorySerializer
from .models import CustomUser, ToDoItem, HistoryItem
from rest_framework import viewsets
from rest_framework import permissions
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = PreferenceSerializer
    permission_classes = [permissions.IsAuthenticated]

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDoItem.objects.all().order_by('time')
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = HistoryItem.objects.all().order_by('id')
    serializer_class = HistorySerializer
    permission_classes = [permissions.IsAuthenticated]
