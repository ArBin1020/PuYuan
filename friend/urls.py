from django.urls import path, include
from .views import *

friend_patterns = [
    path('code', FriendCodeViewSet.as_view(), name='friendcode'),
    path('send', FriendSendViewSet.as_view(), name='friendsend'),
    path('requests', FriendRequestViewSet.as_view(), name='friendrequest'),
    path('results', FriendResultViewSet.as_view(), name='friendresult'),
    path('<int:inviteid>/accept', FriendAcceptViewSet.as_view(), name='friendaccept'),
    path('<int:inviteid>/refuse', FriendRejectViewSet.as_view(), name='friendreject'),
    path('list', FriendListViewSet.as_view(), name='friendlist'),
    path('remove', FriendRemoveViewSet.as_view(), name='friendremove'),
]

urlpatterns = [
    path('friend/', include(friend_patterns), name='friend'),
]