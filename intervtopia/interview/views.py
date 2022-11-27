from django.shortcuts import render
from .serializers import ProblemSerializer, InterviewSerializer
from .models import Problem, Interview
from users.models import CustomUser
from rest_framework import viewsets
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from external.leetCodeWrapper import leetCodeQuestionQuery
from external.meeting import meetingRoom
from external.IDE import IDE
from datetime import datetime
from django.http import HttpResponse
# Create your views here.

class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
def confirm(request):
    difficulty_lut = {
        'E': 1,
        'M': 2,
        'H': 3
    }
    if request.method == 'POST':
        data = JSONParser().parse(request)
        viewer_id = CustomUser.objects.get(username = data['viewer']).pk
        viewee_id = CustomUser.objects.get(username = data['viewee']).pk
        diff = data['difficulty']
        dt = data['datetime']
        query = leetCodeQuestionQuery()
        q = query.getRandomQuestion(difficulty_lut[diff])
        prob = Problem.objects.get_or_create(name = q.getTitle(), url = q.getURL(), difficulty = q.getDifficulty())[0]
        print(prob)
        mr = meetingRoom(viewer_id, viewee_id)
        ide = IDE(viewer_id, viewee_id)
        interview = Interview(
            viewER = CustomUser.objects.get(pk=viewer_id),
            viewEE = CustomUser.objects.get(pk=viewee_id),
            date_and_time = datetime.strptime(dt, '%m/%d/%y %H:%M:%S'),
            room_link = mr.getRoom(),
            ide_link = ide.getRoom()
        )
        interview.save()
        interview.problems.add(prob)

        print(interview)
        return HttpResponse()
        