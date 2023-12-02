from django.urls import path
from .views import *

urlpatterns = [
    # 01 帳號
    path('register', Register.as_view({'post': 'create'}), name='register'),
    path('auth', Login.as_view({'post': 'create'}), name='login'),
    path('verification/send', Send_Verify_Code.as_view({'post': 'create'}), name='verify'),
    path('verification/check', Check_Verify_Code.as_view({'post': 'create'}), name='check'),
    path('password/forgot', Forgot_Password.as_view({'post': 'create'}), name='forgot'),
    path('password/reset', Reset_Password.as_view({'post': 'create'}), name='reset'),
    path('register/check', Register_Check.as_view({'get': 'list'}), name='register_check'),

    # 02 其他
    path('news', News.as_view({'get': 'list'}), name='news'),
    path('share', Share.as_view({'post': 'create'}), name='share'),
    path('share/<int:type>', Share_Check.as_view({'get': 'list'}), name='share_check'),

]
