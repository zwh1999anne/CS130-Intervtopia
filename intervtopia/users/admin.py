from django.contrib import admin
from .models import *
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'type', 'role','time')

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'role', 'time', 'evaluated')

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('pk', "lang_name")

admin.site.register(CustomUser)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Company)
admin.site.register(Position)
admin.site.register(Availability)
admin.site.register(ToDoItem, TodoAdmin)
admin.site.register(HistoryItem, HistoryAdmin)
