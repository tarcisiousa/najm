from django.urls import path
from subs.views import SubList, SubCreate, SubSearchSub, SubDetail

urlpatterns = [
    path('sub/list/', SubList.as_view(), name='sub_list'),
    path('sub/search/', SubSearchSub.as_view(), name='sub_search_sub'),
    path('sub/create/<int:pk>', SubCreate.as_view(), name='sub_create'),
    path('sub/detail/<int:pk>', SubDetail.as_view(), name='sub_detail'),
]