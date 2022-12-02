from django.shortcuts import render
from .serializers import ProblemSerializer, InterviewSerializer
from .models import Problem, Interview
from users.models import CustomUser, ToDoItem, HistoryItem
from users.serializers import ToDoSerializer
from rest_framework import viewsets
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from external.leetCodeWrapper import leetCodeQuestionQuery
from external.meeting import meetingRoom
from external.IDE import IDE
from datetime import datetime
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from rest_framework.reverse import reverse
from django.conf import settings
from django.utils.timezone import make_aware

# Create your views here.

class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
def confirm(request):
    '''
    Handler function invoked when user click the confirm button
    The function handles a HTTP POST request
    With request body:
    {
        "username": "Alice"
        "viewer": "Alice",
        "viewee": "Bob",
        "difficulty": "E",
        "datetime": "11/26/22 17:24:00"
    }
    in JSON format
    This Handler function will generate a new interview object and also update user's todo list
    The function will eventually return a serialized todo object, which can be used by frontend to popup the todo list
    '''
    difficulty_lut = {
        'E': 1,
        'M': 2,
        'H': 3
    }
    if request.method == 'POST':
        # Create interview object based on the post data
        data = JSONParser().parse(request)
        viewer_id = CustomUser.objects.get(username = data['viewer']).pk
        viewee_id = CustomUser.objects.get(username = data['viewee']).pk
        diff = data['difficulty']
        dt = data['datetime']
        query = leetCodeQuestionQuery()
        q = query.getRandomQuestion(difficulty_lut[diff])
        prob = Problem.objects.get_or_create(name = q.getTitle(), url = q.getURL(), difficulty = q.getDifficulty())[0]
        # print(prob)
        mr = meetingRoom(viewer_id, viewee_id)
        ide = IDE(viewer_id, viewee_id)
        dt = datetime.strptime(dt, '%m/%d/%y %H:%M:%S')
        aware_datetime = make_aware(dt)
        interview = Interview(
            viewER = CustomUser.objects.get(pk=viewer_id),
            viewEE = CustomUser.objects.get(pk=viewee_id),
            date_and_time = aware_datetime,
            room_link = mr.getRoom(),
            ide_link = ide.getRoom()
        )
        interview.save()
        interview.problems.add(prob)
        
        # Update Todo List
        todo_viewer = ToDoItem.objects.create(
                owner = CustomUser.objects.get(username = data['viewer']),
                name = data['viewee'],
                role = 'ER',
                type = 'I',
                link = reverse('interview-detail', args=[interview.pk], request=request)             # link to the interview object
            )
        todo_viewee = ToDoItem.objects.create(
                owner = CustomUser.objects.get(username = data['viewee']),
                name = data['viewer'],
                role = 'EE',
                type = 'I',
                link = reverse('interview-detail', args=[interview.pk], request=request)             # link to the interview object
            )
        if data['username'] == data['viewer']:
            serializer = ToDoSerializer(todo_viewer)
        elif data['username'] == data['viewee']:
            serializer = ToDoSerializer(todo_viewee)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponseNotFound()
        
    
@csrf_exempt
def complete(request):
    '''
    This is the handler function when user click button complete
    after the meeting is completed.
    This function accepts a HTTP GET request
    with parameter: {"todo": id}
    This function will update the todo type from "I" to "E", 
    indicating the interview is done, the user should then evaluate the interview
    The function will also create a history object
    The function will return a updated todo object in JSON format
    '''
    if request.method == 'GET':
        id = request.GET['todo']
        todo = ToDoItem.objects.get(pk = id)
        if todo.type == 'I':
            todo.type = 'E'
            todo.save()
        serializer = ToDoSerializer(todo, context={'request': request})
        # Create a history item
        HistoryItem.objects.create(
            owner = CustomUser.objects.get(username = todo.owner.username),
            name = todo.name,
            role = todo.role,
            evaluated = False
        )
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponseNotFound()

@csrf_exempt
def join_meeting(request):
    '''
    This is the handler function when user click the button join meeting
    This function take a input parameter: {"todo": id}
    This function returns the serialized interview object
    '''
    if request.method == 'GET':
        id = request.GET['todo']
        todo = ToDoItem.objects.get(pk = id)
        interview_id = int(str(todo.link).split('/')[-2])
        interview = Interview.objects.get(pk = interview_id)
        serializer = InterviewSerializer(interview)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponseNotFound()