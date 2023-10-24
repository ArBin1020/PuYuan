from rest_framework import serializers
from .models import *

# class (serializers.ModelSerializer):
#     class Meta:
#         model = news
#         fields = '__all__'
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        # exclude = ['user']

class UserSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSetting
        fields = '__all__'
        exclude = ['user']

class UserDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDefault
        fields = '__all__'
        exclude = ['user']

class UservipSerializer(serializers.ModelSerializer):
    class Meta:
        model = vip
        fields = '__all__'
        exclude = ['user']

class UserUnread_RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = unread_records
        fields = '__all__'
        exclude = ['user']

class UserSerializer(serializers.ModelSerializer):
    # class Meta:
    profile = UserProfileSerializer()
    setting = UserSettingSerializer()
    vip = UservipSerializer()
    unread_records = UserUnread_RecordsSerializer()
    fields = ['name', 'birthday', 'height', 'weight', 'phone', 'email', 'gender', 'fcm_id', 'address','setting','vip','unread_records']

class BodyA1cSerializer(serializers.ModelSerializer):
    class Meta:
        model = A1c
        fields = '__all__'


class BodyMedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medical
        fields = '__all__'

class BodyDrugUsedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug_Used
        fields = '__all__'


class BodyCareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Care
        fields = '__all__'