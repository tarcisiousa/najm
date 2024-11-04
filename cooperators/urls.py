from django.urls import path
from .views import CooperatorsList, CooperatorsCreate, CooperatorsDelete, CooperatorsDetail, CooperatorsUpdate, \
    CooperatorsUpdateUnic

urlpatterns = [
    path('cooperators/list/', CooperatorsList.as_view(), name='cooperators_list'),
    path('cooperators/new/', CooperatorsCreate.as_view(), name='cooperators_create'),
    path('cooperators/<int:pk>/detail', CooperatorsDetail.as_view(), name='cooperators_detail'),
    path('cooperators/<int:pk>/update', CooperatorsUpdate.as_view(), name='cooperators_update'),
    path('cooperators/<int:pk>/delete', CooperatorsDelete.as_view(), name='cooperators_delete'),
    path('cooperators/<int:pk>/update/user', CooperatorsUpdateUnic.as_view(), name='cooperators_update_unic')
]