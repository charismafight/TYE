from django.contrib import admin
from .models import *


# Register your models here.
class ArchiveAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.get_days_of_born()
        super().save_model(request, obj, form, change)


admin.site.register(Archive, ArchiveAdmin)
