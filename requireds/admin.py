from django.contrib import admin
from .models import RequiredsModel

@admin.register(RequiredsModel)
class RequiredsAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    filter = ('name',)
