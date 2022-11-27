from rest_framework import serializers
from .models import Interview, Problem

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = [
            'name',
            'url',
            'difficulty'
        ]

class InterviewSerializer(serializers.ModelSerializer):
    viewer = serializers.ReadOnlyField(source = 'viewER.username')
    viewee = serializers.ReadOnlyField(source = 'viewEE.username')
    problems = ProblemSerializer(many = True)

    class Meta:
        model = Interview
        fields = [
            'viewer',
            'viewee',
            'problems',
            'date_and_time',
            'room_link',
            'ide_link'
        ]




