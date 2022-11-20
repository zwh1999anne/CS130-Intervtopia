from django.shortcuts import render
from .serializers import PreferenceSerializer
from .models import CustomUser, Company
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
