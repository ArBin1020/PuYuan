from django.urls import path
from .views import *

urlpatterns = [
    path('api/register', accountRegister.as_view({ 'post': 'register'}), name='account-register'),
    path('api/auth', accountLogin.as_view({ 'post': 'login'}), name='account-login'),
    path('api/verification/send', accountSendCode.as_view({ 'post': 'sendcode'}), name='account-sendcode'),
    path('api/verification/check', accountCheckCode.as_view({ 'post': 'checkcode'}), name='account-checkcode'),
    path('api/password/forgot', accountForget.as_view({ 'post': 'forgot'}), name='account-forgot'),
    path('api/register/check', accountRegisterCheck.as_view({ 'get': 'registercheck'}), name='account-checkregister'),
    path('api/password/reset', accountResetPassword.as_view({ 'post': 'reset'}), name='account-reset'),
    
    path('api/news', Othernews.as_view({'get': 'news'}), name='get-news'),
    path('api/share', OtherShare.as_view({'post': 'share'}), name='share'),
    path('api/share/<int:relation_type>',OtherShare.as_view({'get': 'ViewShare'}), name='viewshare')
]
