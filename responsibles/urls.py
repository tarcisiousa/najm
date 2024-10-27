from django.urls import path
from .views import ResponsiblesList, ResponsiblesCreate, ResponsiblesDetail, ResponsiblesUpdate, ResponsiblesDelete, \
    ResponsiblesUpdateUnic, ResponsiblesUpdateSearch, ResponsiblesUpdateDocuments

urlpatterns = [
    path('responsibles/list/', ResponsiblesList.as_view(), name='responsibles_list'),
    path('responsibles/create/', ResponsiblesCreate.as_view(), name='responsibles_create'),
    path('responsibles/<int:pk>/detail', ResponsiblesDetail.as_view(), name='responsibles_detail'),
    path('responsibles/update/<int:pk>', ResponsiblesUpdate.as_view(), name='responsibles_update'),
    path('responsibles/update/<int:pk>/search', ResponsiblesUpdateSearch.as_view(), name='responsibles_update_search'),
    path('responsibles/unic/update/<int:pk>', ResponsiblesUpdateUnic.as_view(), name='responsibles_update_unic'),
    path('responsibles/<int:pk>/delete', ResponsiblesDelete.as_view(), name='responsibles_delete'),
    path('responsibles/upload/documents/<int:pk>', ResponsiblesUpdateDocuments.as_view(), name='responsibles_update_documents'),
]