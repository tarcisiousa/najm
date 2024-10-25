from django.urls import path
from .views import (ProcessesList, ProcessesCreate, ProcessesDetail, ProcessesUpdate, ProcessesDelete, ProcessesProtocolDetail,
                    ProcessesUpdateDocument, ProcessesUpdateDocumentProcess, ProcessNotesCreate, open_document)

urlpatterns = [
    path('processes/list/', ProcessesList.as_view(), name='processes_list'),
    path('processes/create/', ProcessesCreate.as_view(), name='processes_create'),
    path('processes/<int:pk>/detail', ProcessesDetail.as_view(), name='processes_detail'),
    path('processes/<int:pk>/protocol', ProcessesProtocolDetail.as_view(), name='processes_protocol'),
    path('processes/<int:pk>/update', ProcessesUpdate.as_view(), name='processes_update'),
    path('processes/<int:pk>/update/document-partys', ProcessesUpdateDocument.as_view(), name='processes_update_documents'),
    path('processes/<int:pk>/update/document-process', ProcessesUpdateDocumentProcess.as_view(), name='processes_update_documents_process'),
    path('processes/<int:pk>/delete', ProcessesDelete.as_view(), name='processes_delete'),
    path('processes/create/notes', ProcessNotesCreate.as_view(), name='processes_create_notes'),
    path('processes/open-document/<int:pk>/', open_document, name='open_document'),
]