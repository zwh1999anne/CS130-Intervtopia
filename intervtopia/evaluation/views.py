from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect

from evaluation.models import Question
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the evaluation forms")

def interviewer(request):
    question_list = Question.objects.filter(target__gte = 0)
    context = {'question_list': question_list}
    return render(request, 'evaluation/evalform.html', context)

def interviewee(request):
    question_list = Question.objects.filter(target__lte = 0)
    context = {'question_list': question_list}
    return render(request, 'evaluation/evalform.html', context)

def submit(request):
    # Handle the POST data
    return HttpResponse("Thank you for submitting your response!")
    # question = get_object_or_404(Question, pk=question_id)
    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'polls/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
    #     return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))