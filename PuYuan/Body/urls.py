from django.urls import path
from .views import *

urlpatterns = [
    path('api/user',BodyUserProfile.as_view({'patch':'bodyuserprofile'}),name='bodyuserprofile')
]
