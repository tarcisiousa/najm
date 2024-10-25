from django.contrib import admin
from .models import SubModel

@admin.register(SubModel)
class SubAdmin(admin.ModelAdmin):
    search_fields = ('processes_number',)
    filter = ('processes_number',)
