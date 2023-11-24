from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

# userdata = DefaultRouter()
# userdata.register(r'user', UserProfileViewSet, basename='user')

user_blood_patterns = [
    path('pressure', BloodPressureViewSet.as_view(), name='bloodpressure'),
    path('sugar', BloodSugarViewSet.as_view(), name='bloodsugar'),
]

user_patterns = [
    path('default', UserDefaultViewSet.as_view(), name='userdefault'),
    path('setting', UserSettingViewSet.as_view(), name='usersetting'),
    path('blood/', include(user_blood_patterns)),
    path('weight', UserWeightViewSet.as_view(), name='userweight'),
    path('records', UserRecordsViewSet.as_view(), name='userrecords'),
    path('diet', UserDietViewSet.as_view(), name='userdiet'),
    path('diary', UserDiaryViewSet.as_view(), name='userdiary'),
    path('a1c', UserA1cViewSet.as_view(), name='usera1c'),
    path('medical', UserMedicalViewSet.as_view(), name='usermedical'),
    path('drug-used', UserDrugUsedViewSet.as_view(), name='userdrugused'),
    path('care', UserCareViewSet.as_view(), name='usercare'),
    path('badge', UserBadgeViewSet.as_view(), name='userbadge'),
]

urlpatterns = [
    path('user', UserProfileViewSet.as_view(), name='userprofile'),
    path('user/', include(user_patterns)),
]