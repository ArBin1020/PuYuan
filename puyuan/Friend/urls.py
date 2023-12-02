from django.urls import path
from .views import *

urlpatterns = [
    path('code', Code.as_view({'get': 'list'}), name='code'),
    path('list', List.as_view({'get': 'list'}), name='list'),
    path('requests', Requests.as_view({'get': 'list'}), name='requests'),
    path('send', Send.as_view({'post': 'create'}), name='send'),
    path('<int:inviteld>/accept', Accept.as_view({'get': 'list'}), name='accept'),
    path('<int:inviteld>/refuse', Refuse.as_view({'get': 'list'}), name='refuse'),
    path('remove', Friend_Remove.as_view({'delete': 'remove'}), name='remove'),
    path('results', Friend_Results.as_view({'get': 'list'}), name='results'),
]
