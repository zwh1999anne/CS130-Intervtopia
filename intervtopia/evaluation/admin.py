from django.contrib import admin
from .models import Question, Choice, EvalForm, Response

admin.site.register(Question)
admin.site.register(Choice)

admin.site.register(EvalForm)
admin.site.register(Response)

# Register your models here.
