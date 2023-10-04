# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.AccountList.as_view(), name='account-list'),
]
