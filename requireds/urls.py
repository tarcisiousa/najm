from django.urls import path
from .views import RequiredsList, RequiredsCreate, RequiredsDetail, RequiredsUpdate, RequiredsDelete, RequiredsUpdateUnic

urlpatterns = [
    path('requireds/list/', RequiredsList.as_view(), name='requireds_list'),
    path('requireds/create/', RequiredsCreate.as_view(), name='requireds_create'),
    path('requireds/<int:pk>/detail', RequiredsDetail.as_view(), name='requireds_detail'),
    path('requireds/<int:pk>/update', RequiredsUpdate.as_view(), name='requireds_update'),
    path('requireds/unic/<int:pk>/update', RequiredsUpdateUnic.as_view(), name='requireds_update_unic'),
    path('requireds/<int:pk>/delete', RequiredsDelete.as_view(), name='requireds_delete'),
]