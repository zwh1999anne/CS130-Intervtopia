from django.http import HttpResponse, Http404
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect
# legacy import above
from django.shortcuts import render
from .serializers import ChoiceSerializer, EvalFormSerializer, QuestionSerializer, ResponseSerializer
from .models import Choice, EvalForm, Question, Response
from rest_framework import viewsets
from rest_framework import permissions
# Create your views here.


class ChoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Choice.objects.all().order_by('choice_value')
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class EvalFormViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = EvalForm.objects.all().order_by('name')
    serializer_class = EvalFormSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all().order_by('question_name')
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class ResponseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Response.objects.all().order_by('name')
    serializer_class = ResponseSerializer
    permission_classes = [permissions.IsAuthenticated]


# legacy code before using restframework


def index(request):
    return HttpResponse("Hello, world. You're at the evaluation forms")


def interviewer(request):
    try:
        question_list = Question.objects.filter(target__gte=0)
        question_list = question_list.order_by('question_ranking')

        context = {'question_list': question_list}
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'evaluation/evalform.html', context)


def interviewee(request):
    try:
        question_list = Question.objects.filter(target__lte=0)
        question_list = question_list.order_by('question_ranking')

        context = {'question_list': question_list}
    except:
        raise Http404('Question does not exist')
    return render(request, 'evaluation/evalform.html', context)


def submit(request):
    # Handle the POST data
    EvalForm.update(request)
    return HttpResponse("Thank you for submitting your response!")


def results(request):
    response = "You're looking at the results of evaluation"
    return HttpResponse(response)
