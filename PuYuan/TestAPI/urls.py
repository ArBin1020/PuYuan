from django.urls import path
from .views import *

urlpatterns = [
    path('addNEWS', CreateRandomNews.as_view({ 'post': 'createrandomnews'}), name='create-random-news'),
]
