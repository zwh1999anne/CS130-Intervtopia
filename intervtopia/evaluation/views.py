from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect

from evaluation.models import Question
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the evaluation forms")


def interviewer(request):
    try:
        question_list = Question.objects.filter(target__gte=0)
        context = {'question_list': question_list}
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'evaluation/evalform.html', context)


def interviewee(request):
    try:
        question_list = Question.objects.filter(target__lte=0)
        context = {'question_list': question_list}
    except:
        raise Http404('Question does not exist')
    return render(request, 'evaluation/evalform.html', context)


def submit(request):
    # Handle the POST data
    return HttpResponse("Thank you for submitting your response!")


def results(request):
    response = "You're looking at the results of evaluation"
    return HttpResponse(response)
