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