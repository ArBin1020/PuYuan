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
    path("api/user/diary",BodyGetDiet.as_view({'get':'list'}),name="bodygetdiet"),
    path('api/user/diet',BodyDiet.as_view({'post':'diet'}),name='bodydiet'),


    #04 糖化血色素
    path('api/user/a1c',BodyA1c.as_view({'post':'postA1c','get':'getA1c','delete':'delA1c'}),name='bodya1c'),
    path('api/user/weight',BodyWeight.as_view({'post':'weight'}),name='bodyweight'),
    path('api/user/blood/sugar',BodyBloodSuger.as_view({'post':'bloodsuger'}),name='bodysugar'),
    path('api/user/records',Records.as_view({'post':'post_records','delete':'delete_records'}),name='bodyrecords'),
    
    #05 就醫資訊
    path('api/user/medical',BodyGetMedical.as_view({'get':'getmedical','patch':'patchmedical'}),name='bodymedical'),

    #06 藥物資訊
    path('api/user/drug-used',BodyDrugUsed.as_view({'get':'getdrugused','post':'postdrugused','delete':'deldrugused'}),name='bodydrugused'),

    #07 關懷資訊
    path('api/user/care',BodyCare.as_view({'get':'getcare','post':'postcare'}),name='bodycare'),

    #08 其他
    path('api/user/badge',Body_Badge.as_view({'put':'put_badge'}),name='bodybadge'),
]
