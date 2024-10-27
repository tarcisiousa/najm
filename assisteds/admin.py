from django.contrib import admin
from assisteds.models import AssistedsModel, AssistedDocumentModel

@admin.register(AssistedsModel)
class AssistedsAdmin(admin.ModelAdmin):
    filter = ('name',)
    search_fields = ('name',)

@admin.register(AssistedDocumentModel)
class AssistedDocumentAdmin(admin.ModelAdmin):
    filter = ('type_document',)
    search_fields = ('type_document',)
