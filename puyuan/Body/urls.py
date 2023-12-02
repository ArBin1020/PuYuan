from django.urls import path
from .views import *

urlpatterns = [
    # 01 個人資訊
    path('', User_Profile.as_view({'patch': 'update',
                                   'get': 'list'}),
                                   name='user_profile'),

    path('default', User_Default.as_view({'patch': 'update'}),name='user_default'),
    path('setting', User_Setting.as_view({'patch': 'update'}),name='user_setting'),
    
    #02 測量上傳
    path('blood/pressure', Blood_Pressure.as_view({'post': 'create',}),name='blood_pressure'),
    path('weight', Weight.as_view({'post': 'create',}),name='weight'),
    path('blood/sugar', Blood_Sugar.as_view({'post': 'create',}),name='blood_sugar'),
    path('records', Records.as_view({'post': 'create',
                                      'delete': 'remove'}),
                                      name='records'),

    #03 日記
    path('diary', Diary.as_view({'get': 'list',}), name='diary'),
    path('diet', Diet.as_view({'post': 'create'}), name='diet'),

    #04 糖化血色素
    path('a1c', A1c.as_view({'post': 'create',
                              'get': 'list',
                              'delete': 'remove'}),
                               name='a1c'),
    
    #05 就醫資訊
    path('nedical', Medical.as_view({'patch': 'update',
                                      'get': 'list'}),
                                      name='medical'),

    #06 藥物資訊
    path('drug-used', Drug.as_view({'post': 'create',
                                    'get': 'list',
                                    'delete': 'remove'}),
                                     name='drug'),

    #07 關懷資訊
    path('care', Care.as_view({'post': 'create',
                                'get': 'list'}),
                                 name='care'),
    #08 其他
    path('badge', Badge.as_view({'put': 'update'}), name='badge'),
]
