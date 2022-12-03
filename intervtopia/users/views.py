from django.shortcuts import render
from .serializers import UserSerializer, ToDoSerializer, HistorySerializer, MatchingSerializer
from .models import CustomUser, ToDoItem, HistoryItem, RandomMatching, PreferenceMatching, HistoryMatching, Position, Company, Language, Availability
from rest_framework import viewsets
from rest_framework import permissions
from django.http import JsonResponse
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from datetime import datetime
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True)
    def match(self,request):
        usr = CustomUser.objects.get(username = request.GET['user'])
        # print(request.GET['type'])
        if request.GET['type'] == "random":
            # Do random matching
            rand_match = RandomMatching()
            pair = rand_match.getPair(usr)
        elif request.GET['type'] == "preference":
            # Do preference matching
            pref_match = PreferenceMatching()
            pair = pref_match.getPair(usr)
        else:
            # Do history matching
            hist_match = HistoryMatching()
            pair = hist_match.getPair(usr)
        serializer = MatchingSerializer(pair)
        data = serializer.serialize()
        return JsonResponse(data, safe=False)

    @action(detail=True, methods=['post'])
    def update_preference(self,request):
        '''
        HTTP POST Request 
        Request Body:
        {
        "username":"haofan",
        "email":"haofan@example.com",
        "school":"UCLA Computer Science",
        "job_role":"software engineer",
        "interview_role":"B",
        "first_language":"C++",
        "second_language":"Python",
        "desired_difficulty":"H",
        "available_day":"Tue",
        "available_time":"10:00 - 11:00",
        "additional_available_day":"Thu",
        "additional_available_time":"14:00 - 15:00"
        }
        '''
        if request.method == 'POST':
            data = JSONParser().parse(request)
            user = CustomUser.objects.get(username = data['username'])
            if user.email != data['email']: user.email = data['email']
            if user.education != data['school']: user.education = data['school']
            # Update target positions
            positions = [pos.position_name.lower() for pos in user.target_positions.all()]
            if data['job_role'].lower() not in positions:
                new_role = Position.objects.get_or_create(position_name = data['job_role'].capitalize())[0]
                user.target_positions.add(new_role)
            # Update target companies
            # companys = [comp.company_name.lower() for comp in user.target_companys.all()]
            # if data['companys'].lower() not in companys:
            #     new_comp = Company.objects.get_or_create(company_name = data['companys'].capitalize())[0]
            #     user.target_companys.add(new_comp)

            if data['interview_role'] != user.preferred_role: user.preferred_role = data['interview_role']

            # Update language
            lanuages = [lang.lang_name.capitalize() for lang in user.preferred_languages.all()]
            if data['first_language'].capitalize() not in lanuages:
                new_lang = Language.objects.get_or_create(lang_name = data['first_language'].capitalize())[0]
                user.preferred_languages.add(new_lang)
            if data['second_language'].capitalize() not in lanuages:
                new_lang = Language.objects.get_or_create(lang_name = data['second_language'].capitalize())[0]
                user.preferred_languages.add(new_lang)

            # Update preferred difficulty
            if data['desired_difficulty'] != user.preferred_difficulty: user.preferred_difficulty = data['desired_difficulty']

            # Update availability
            st_str, _, et_str = data['available_time'].split()
            st = datetime.strptime(st_str, "%H:%M").time()
            et = datetime.strptime(et_str, "%H:%M").time()
            avai_1 = Availability.objects.get_or_create(day = data['available_day'], start_time = st, end_time = et)[0]
            user.availability.add(avai_1)

            st_str, _, et_str = data['additional_available_time'].split()
            st = datetime.strptime(st_str, "%H:%M").time()
            et = datetime.strptime(et_str, "%H:%M").time()
            avai_2 = Availability.objects.get_or_create(day = data['additional_available_day'], start_time = st, end_time = et)[0]
            user.availability.add(avai_2)
            user.save()
        serializer = UserSerializer(user, context={'request': request})
        return JsonResponse(serializer.data, safe=False)


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDoItem.objects.all().order_by('time')
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = HistoryItem.objects.all().order_by('time')
    serializer_class = HistorySerializer
    permission_classes = [permissions.IsAuthenticated]

