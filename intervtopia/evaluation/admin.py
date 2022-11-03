from django.contrib import admin
from .models import Question, Choice, EvalForm, Response

admin.site.register(Question)
admin.site.register(Choice)

# admin.site.register(InterviewER_EvaluationFormDB)
# admin.site.register(InterviewEE_EvaluationFormDB)

admin.site.register(EvalForm)
admin.site.register(Response)

# Register your models here.
