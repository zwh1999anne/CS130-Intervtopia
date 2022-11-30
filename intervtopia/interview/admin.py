from django.contrib import admin
from .models import Interview, Problem
# Register your models here.

class InterviewAdmin(admin.ModelAdmin):
    list_display = ('viewER', 'viewEE', 'date_and_time')

admin.site.register(Interview, InterviewAdmin)
# admin.site.register(Interviewee)
# admin.site.register(Interviewer)
admin.site.register(Problem)