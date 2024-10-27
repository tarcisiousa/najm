from django.urls import path
from .views import AgendaList, AgendaCreate, AgendaDetail, AgendaUpdate, AgendaDelete, eventos_view, horary_vagos_view, AgendaDetailProtocol

urlpatterns = [
    path('agendas/list/', AgendaList.as_view(), name='agendas_list'),
    path('agendas/create/', AgendaCreate.as_view(), name='agendas_create'),
    path('agendas/<int:pk>/detail', AgendaDetail.as_view(), name='agendas_detail'),
    path('agendas/<int:pk>/detail/', AgendaDetailProtocol.as_view(), name='agendas_detail_protocol'),
    path('agendas/<int:pk>/update', AgendaUpdate.as_view(), name='agendas_update'),
    path('agendas/<int:pk>/delete', AgendaDelete.as_view(), name='agendas_delete'),
    path('eventos_view/', eventos_view, name='eventos_view'),
    path('horary_vagos/', horary_vagos_view, name='horary_vagos'),
]