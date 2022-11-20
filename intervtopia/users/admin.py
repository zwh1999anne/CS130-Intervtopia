from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Language)
admin.site.register(Company)
admin.site.register(Position)
admin.site.register(Availability)