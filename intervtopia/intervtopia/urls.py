"""intervtopia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('evaluation/', include('evaluation.urls')),
#     path('accounts/', include('django.contrib.auth.urls')),
# ]

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users import views
from evaluation.views import EvalFormViewSet, QuestionViewSet
from interview.views import InterviewViewSet, confirm, complete, join_meeting
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'todo', views.ToDoViewSet)
router.register(r'history', views.HistoryViewSet)
router.register(r'interview', InterviewViewSet)
# router.register(r'eval-form-choice', ChoiceViewSet)
router.register(r'eval-form', EvalFormViewSet)
router.register(r'eval-form-question', QuestionViewSet)
# router.register(r'eval-form-response', ResponseViewSet)

urlpatterns = [
        path('admin/', admin.site.urls), 
        path('', include(router.urls)), 
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        path('confirm/', confirm, name='confirm'),
        path('matching/', views.match, name='matching'),
        path('complete/', complete, name = 'complete'),
        path('join/', join_meeting, name = 'join')
    ]
