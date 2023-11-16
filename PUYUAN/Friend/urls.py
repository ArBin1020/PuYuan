from django.urls import path
from .views import *

urlpatterns = [
    path('api/friend/code', Friend_Get_Code.as_view({'get': 'get_code'}), name='get-code'),
    path('api/friend/list', Friend_Get_List.as_view({'get': 'get_list'}), name='get-list'),
    path('api/friend/request', Friend_Get_Request.as_view({'get': 'get_request'}), name='get-request'),
]
