from django.contrib import admin
from .models import AgendaModel

@admin.register(AgendaModel)
class AgendaAdmin(admin.ModelAdmin):
    filter = ('name',)
    search_fields = ('name',)
