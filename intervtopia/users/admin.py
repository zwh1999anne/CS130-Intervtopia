from django.contrib import admin
from .models import *
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'type', 'time')

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'time', 'evaluated')

admin.site.register(CustomUser)
admin.site.register(Language)
admin.site.register(Company)
admin.site.register(Position)
admin.site.register(Availability)
admin.site.register(ToDoItem, TodoAdmin)
admin.site.register(HistoryItem, HistoryAdmin)
