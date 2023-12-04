from django.urls import path
from .views import *

urlpatterns = [
    path('api/friend/code', Friend_Get_Code.as_view({'get': 'get_code'}), name='get-code'),
    path('api/friend/list', Friend_Get_List.as_view({'get': 'get_list'}), name='get-list'),
    path('api/friend/requests', Friend_Get_Request.as_view({'get': 'get_request'}), name='get-request'),
    path('api/friend/send', Friend_Send.as_view({'post': 'send'}), name='send'),
    path('api/friend/<int:inviteld>/accept',Friend_Accept.as_view({'get': 'accept'}),name='accept'),    
    path('api/friend/<int:inviteld>/refuse',Friend_Refuse.as_view({'get': 'refuse'}),name='refuse'),
    path('api/friend/remove',Friend_Remove.as_view({'DELETE': 'remove'}),name='remove'),
    path('api/friend/results',Friend_Get_Results.as_view({'get': 'get_results'}),name='get-results'),
]
