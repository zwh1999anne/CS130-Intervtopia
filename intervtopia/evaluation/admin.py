from django.contrib import admin
from .models import Question, Choice, InterviewER_EvaluationFormDB, InterviewEE_EvaluationFormDB

admin.site.register(Question)
admin.site.register(Choice)

admin.site.register(InterviewER_EvaluationFormDB)
admin.site.register(InterviewEE_EvaluationFormDB)

# Register your models here.
