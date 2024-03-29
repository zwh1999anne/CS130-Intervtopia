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
from users.views import update_preference, match, UserViewSet, ToDoViewSet, HistoryViewSet
from friend_and_message.views import FriendshipViewSet, MessageViewSet
from evaluation.views import EvalFormViewSet, QuestionViewSet, evaluate, submit
from interview.views import InterviewViewSet, complete, join_meeting
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'todo', ToDoViewSet)
router.register(r'history', HistoryViewSet)
router.register(r'interview', InterviewViewSet)
# router.register(r'eval-form-choice', ChoiceViewSet)
# router.register(r'eval-form-response', ResponseViewSet)

router.register(r'eval-form', EvalFormViewSet)
router.register(r'eval-form-question', QuestionViewSet)
router.register(r'friendship', FriendshipViewSet)
router.register(r'friend-and-message', MessageViewSet)

# snippet_highlight = InterviewViewSet.as_view({
#     'post': 'confirm'
# })
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('matching/', match, name='matching'),
    # path('confirm/', confirm, name='confirm'),
    path('preference/', update_preference, name='preference'),
    path('complete/', complete, name='complete'),
    path('join/', join_meeting, name='join'),
    path('evaluate/', evaluate, name='evaluate'),
    path('submit/', submit, name='submit'),
    # Schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
