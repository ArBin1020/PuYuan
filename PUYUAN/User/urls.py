# urls.py
from django.urls import path
from views import accountViewSet
from . import views

urlpatterns = [
    path('api/', views.AccountList.as_view(), name='account-list'),
    # path('api/register/', accountViewSet.as_view(), name='account-register')
]
