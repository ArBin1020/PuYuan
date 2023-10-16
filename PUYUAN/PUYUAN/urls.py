"""
URL configuration for PUYUAN project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from User.views import *
# from User import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api', include('User.urls')),
    path('api/register', accountRegister.as_view({ 'post': 'register'}), name='account-register'),
    path('api/auth', accountLogin.as_view({ 'post': 'login'}), name='account-login'),
    path('api/verification/send', accountSendCode.as_view({ 'post': 'sendcode'}), name='account-sendcode'),
    path('api/verification/check', accountCheckCode.as_view({ 'post': 'verify'}), name='account-verify'),
    path('api/password/forgot', accountForgot.as_view({ 'post': 'resendcode'}), name='account-resendcode'),
    path('api/password/reset', accountResetPassword.as_view({ 'post': 'resetpassword'}), name='account-resetpassword'),
]
