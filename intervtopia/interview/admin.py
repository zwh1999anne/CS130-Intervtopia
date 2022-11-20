from django.contrib import admin
from .models import Interview, Interviewee, Interviewer, Problem
# Register your models here.

admin.site.register(Interview)
admin.site.register(Interviewee)
admin.site.register(Interviewer)
admin.site.register(Problem)