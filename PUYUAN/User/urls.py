from django.urls import path
from .views import *

urlpatterns = [
    # path('register/', accountRegister.as_view({ 'post': 'register'}), name='account-register'),
    # path('auth/', accountLogin.as_view({'post': 'auth'}), name='account-login'),
    path('api/register', accountRegister.as_view({ 'post': 'register'}), name='account-register'),
    path('api/auth', accountLogin.as_view({ 'post': 'login'}), name='account-login'),
    path('api/verification/send', accountSendCode.as_view({ 'post': 'sendcode'}), name='account-sendcode'),
]
