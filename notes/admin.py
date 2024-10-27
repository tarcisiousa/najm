from django.contrib import admin
from .models import NotesModel

@admin.register(NotesModel)
class NotesAdmin(admin.ModelAdmin):
    search_fields = ('subject',)

