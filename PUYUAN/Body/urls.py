from django.urls import path
from .views import *

urlpatterns = [
    path('api/user',BodyUserProfile.as_view({'patch':'setprofile','get':'getuserprofile'}),name='bodyuserprofile'),
    
    path('api/user/default',BodyUserDefault.as_view({'patch':'userdefault'}),name='bodyuserdefault'),
    path('api/user/setting',BodyUserSetting.as_view({'patch':'usersetting'}),name='bodyusersetting'),
    path('api/user/blood/pressure',BodyBloodPressure.as_view({'post':'bloodpressure'}),name='bodybloodpressure'),
    path('api/user/weight',BodyWeight.as_view({'post':'weight'}),name='bodyweight'),
    path('api/user/blood/sugar',BodyBloodSuger.as_view({'post':'bloodsuger'}),name='bodysugar'),
]
