from django.urls import path
from .views import NotesList, NotesCreate, NotesDetail, NotesUpdate, NotesDelete


urlpatterns = [
    path('notes/list/', NotesList.as_view(), name='notes_list'),
    path('notes/create/', NotesCreate.as_view(), name='notes_create'),
    path('notes/<int:pk>/detail', NotesDetail.as_view(), name='notes_detail'),
    path('notes/<int:pk>/update', NotesUpdate.as_view(), name='notes_update'),
    path('notes/<int:pk>/delete', NotesDelete.as_view(), name='notes_delete'),
]