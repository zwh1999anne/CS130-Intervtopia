from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from django.urls import reverse
# legacy import above
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .serializers import EvalFormSerializer, QuestionSerializer
from .models import EvalForm, Question
from users.models import ToDoItem
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import JSONParser
# Create your views here.


# class ChoiceViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Choice.objects.all().order_by('choice_value')
#     serializer_class = ChoiceSerializer
#     permission_classes = [permissions.IsAuthenticated]


class EvalFormViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = EvalForm.objects.all().order_by('time')
    serializer_class = EvalFormSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all().order_by('question_ranking')
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


@csrf_exempt
def evaluate(request):
    '''
    This is the handler function on clicking the evaluate button
    This function handles a HTTP GET request with parameter: {"todo": "id"}
    This function will create a new evaluation form object with predefined questions
    This function then return the created evaluation form in JSON format
    '''
    if request.method == 'GET':
        id = request.GET['todo']
        todo = ToDoItem.objects.get(pk = id)
        assert(todo.type == 'E')
        role_lut = {
            'ER': 'interviewer',
            'EE': 'interviewee'
        }
        evalform = EvalForm.objects.create(
            name = todo.owner.username + '\'s evaluation to ' + todo.name + ' as a '+ role_lut[todo.role],
            target_user = todo.owner,
            target_role = todo.role,
            comments = ""
        )
        todo.link = reverse('evalform-detail', args=[evalform.pk])
        # evalform.target_user = todo.owner
        # evalform.save()
        if todo.role == 'ER':
            question_list = [
                "How was the interviewee's problem-solving skill?",
                "How was the interviewee's communication?",
                "How was the interviewee's coding skill?",
                "How was the interview over all?"
            ]
            
        elif todo.role == 'EE':
            question_list = [
                "How was the interviewer's description of problem?",
                "How was the interviewer's ability to create follow up questions?",
                "How was the interviewer's feedback?",
                "How was the interview over all?"
            ]
        for i in range(len(question_list)):
            Question.objects.create(
                question_text = question_list[i],
                target = 'ER',
                question_ranking = i,
                score = 0,
                evalform = evalform
            )
        serializer = EvalFormSerializer(evalform, context={'request': request})
        return JsonResponse(serializer.data, safe = False)
    else:
        return HttpResponseNotFound()
    
@csrf_exempt
def submit(request):
    '''
    TODO: need parameters: todo and history
    '''
    # data = JSONParser().parse(request)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        # print(data)
        form_id = data['form']
        question_data = data['questions']
        compressed_question_data = {}
        for q in question_data:
            compressed_question_data[q['id']] = q['score']
        comments = data['comments']
        form = EvalForm.objects.get(pk = form_id)
        qs = form.questions.all()
        for q in qs:
            if q.pk in compressed_question_data.keys():
                q.score = compressed_question_data[q.pk]
                q.save()
        form.comments = comments
        form.save()
        serializer = EvalFormSerializer(form, context={'request': request})
        return JsonResponse(serializer.data, safe = False)
    else:
        return HttpResponseNotFound()
# class ResponseViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Response.objects.all().order_by('name')
#     serializer_class = ResponseSerializer
#     permission_classes = [permissions.IsAuthenticated]


# legacy code before using restframework


# def index(request):
#     return HttpResponse("Hello, world. You're at the evaluation forms")


# def interviewer(request):
#     try:
#         question_list = Question.objects.filter(target__gte=0)
#         question_list = question_list.order_by('question_ranking')

#         context = {'question_list': question_list}
#     except Question.DoesNotExist:
#         raise Http404('Question does not exist')
#     return render(request, 'evaluation/evalform.html', context)


# def interviewee(request):
#     try:
#         question_list = Question.objects.filter(target__lte=0)
#         question_list = question_list.order_by('question_ranking')

#         context = {'question_list': question_list}
#     except:
#         raise Http404('Question does not exist')
#     return render(request, 'evaluation/evalform.html', context)


# def submit(request):
#     # Handle the POST data
#     EvalForm.update(request)
#     return HttpResponse("Thank you for submitting your response!")


# def results(request):
#     response = "You're looking at the results of evaluation"
#     return HttpResponse(response)
