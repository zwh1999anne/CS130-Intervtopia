from django.shortcuts import render
from .serializers import ProblemSerializer, InterviewSerializer
from .models import Problem, Interview
from rest_framework import viewsets
from rest_framework import permissions
# Create your views here.

class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    permission_classes = [permissions.IsAuthenticated]