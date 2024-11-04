from django.contrib import admin
from .models import AgendaModel

@admin.register(AgendaModel)
class AgendaAdmin(admin.ModelAdmin):
    filter = ('protocol',)
    search_fields = ('protocol',)
