from django.urls import path
from .views import (AssistedsList, AssistedsCreate, AssistedsDetail, AssistedsUpdate, AssistedsDelete, AssistedsCreateIncapaz
, AssistedsUpdateSearch, AssistedsUpdateSearchIcapaz, AssistedsUpdateDocuments)

urlpatterns = [
    path('assisteds/list/', AssistedsList.as_view(), name='assisteds_list'),
    path('assisteds/create/', AssistedsCreate.as_view(), name='assisteds_create'),
    path('assisteds/create/incapaz/', AssistedsCreateIncapaz.as_view(), name='assisteds_create_incapaz'),
    path('assisteds/<int:pk>/detail', AssistedsDetail.as_view(), name='assisteds_detail'),
    path('assisteds/<int:pk>/update', AssistedsUpdate.as_view(), name='assisteds_update'),
    path('assisteds/<int:pk>/delete', AssistedsDelete.as_view(), name='assisteds_delete'),
    path('assisteds/<int:pk>/search/update', AssistedsUpdateSearch.as_view(), name='assisteds_update_search'),
    path('assisteds/search/<int:pk>/update', AssistedsUpdateSearchIcapaz.as_view(), name='assisteds_update_search_incapaz'),
    path('assisteds/upload/documents/<int:pk>', AssistedsUpdateDocuments.as_view(), name='assisteds_update_documents'),
]