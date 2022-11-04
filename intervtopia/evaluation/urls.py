from django.urls import path

from . import views

app_name = 'evaluation'
urlpatterns = [
    path('', views.index, name='index'),
    path('interviewer/', views.interviewer, name='interviewer'),
    path('interviewee/', views.interviewee, name='interviewee'),
    path('submit/', views.submit, name='submit'),
    path('results/', views.results, name='results')
]
