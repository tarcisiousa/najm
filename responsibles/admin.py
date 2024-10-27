from django.contrib import admin
from .models import ResponsiblesModel

@admin.register(ResponsiblesModel)
class ResponsiblesAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('name',)

# Register your models here.
