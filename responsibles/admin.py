from django.contrib import admin
from .models import ResponsiblesModel, ResponsiblesDocumentsModel

@admin.register(ResponsiblesModel)
class ResponsiblesAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(ResponsiblesDocumentsModel)
class ResponsiblesDocumentAdmin(admin.ModelAdmin):
    search_fields = ('id_responsible',)
    list_filter = ('id_responsible',)

# Register your models here.
