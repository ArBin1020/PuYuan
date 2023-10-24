from django.urls import path
from .views import *

urlpatterns = [
    # 01 個人資訊
    path('api/user',BodyUserProfile.as_view({'patch':'setprofile','get':'getuserprofile'}),name='bodyuserprofile'),
    path('api/user/default',BodyUserDefault.as_view({'patch':'userdefault'}),name='bodyuserdefault'),
    path('api/user/setting',BodyUserSetting.as_view({'patch':'usersetting'}),name='bodyusersetting'),
    
    #02 測量上傳
    path('api/user/blood/pressure',BodyBloodPressure.as_view({'post':'bloodpressure'}),name='bodybloodpressure'),
    path('api/user/weight', BodyWeight.as_view({'post':'weight'}),name='bodyweight'),
    path('api/user/blood/sugar',BodyBloodSuger.as_view({'post':'bloodsuger'}),name='bodysugar'),

    #03 日記
    path('api/user/diet',BodyDiet.as_view({'post':'diet'}),name='bodydiet'),


    #04 糖化血色素
    path('api/user/a1c',BodyA1c.as_view({'post':'postA1c','get':'getA1c','delete':'delA1c'}),name='bodya1c'),
    path('api/user/weight',BodyWeight.as_view({'post':'weight'}),name='bodyweight'),
    path('api/user/blood/sugar',BodyBloodSuger.as_view({'post':'bloodsuger'}),name='bodysugar'),
]
