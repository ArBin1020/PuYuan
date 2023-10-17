from django.urls import path
from .views import *

urlpatterns = [
    # path('register/', accountRegister.as_view({ 'post': 'register'}), name='account-register'),
    # path('auth/', accountLogin.as_view({'post': 'auth'}), name='account-login'),
    path('api/register', accountRegister.as_view({ 'post': 'register'}), name='account-register'),
    path('api/auth', accountLogin.as_view({ 'post': 'login'}), name='account-login'),
    path('api/verification/send', accountSendCode.as_view({ 'post': 'sendcode'}), name='account-sendcode'),
    path('api/verification/check', accountCheckCode.as_view({ 'post': 'checkcode'}), name='account-checkcode'),
    path('api/password/forgot', accountForget.as_view({ 'post': 'forgot'}), name='account-forgot'),
    path('api/register/check', accountRegisterCheck.as_view({ 'get': 'registercheck'}), name='account-checkregister'),
    # path('api/password/reset', accountResetPassword.as_view({ 'post': 'reset'}), name='account-reset'),
    # path('reset_password/<str:uidb64>/<str:token>/', accountResetPassword.as_view({'post':'reset'}), name='reset_password'),
    path('api/news', OtherShare.as_view({'get': 'news'}), name='get-news'),
]
