from django.contrib import admin
from .models import Question, EvalForm

# class ChoiceAdmin(admin.ModelAdmin):
#     list_display = ('question', 'choice_text', 'choice_value')

admin.site.register(Question)
# admin.site.register(Choice, ChoiceAdmin)

admin.site.register(EvalForm)
# admin.site.register(Response)

# Register your models here.
