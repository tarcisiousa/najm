from django.contrib import admin
from .models import CooperatorsModel

@admin.register(CooperatorsModel)
class CooperatorsAdmin(admin.ModelAdmin):
    search_fields = ('name_order',)
    filter = ('name_order',)
