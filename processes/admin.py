from django.contrib import admin
from .models import ProcessesModel, ProcessesNotesModel

@admin.register(ProcessesModel)
class ProcessesAdmin(admin.ModelAdmin):
    search_fields = ('protocol',)
    filter = ('protocol',)

@admin.register(ProcessesNotesModel)
class ProcessesNotesAdmin(admin.ModelAdmin):
    search_fields = ('subject',)
    filter = ('subject',)