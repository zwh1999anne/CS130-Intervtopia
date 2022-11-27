from django.contrib import admin
from .models import Question, EvalForm

# class ChoiceAdmin(admin.ModelAdmin):
#     list_display = ('question', 'choice_text', 'choice_value')

class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'question_text',
        'target',
        'question_ranking',
        'score'
    )
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice, ChoiceAdmin)

admin.site.register(EvalForm)
# admin.site.register(Response)

# Register your models here.
