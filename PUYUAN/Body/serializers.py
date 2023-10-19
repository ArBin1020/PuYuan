from rest_framework import serializers
from .models import UserProfile

# class (serializers.ModelSerializer):
#     class Meta:
#         model = news
#         fields = '__all__'
class BodyUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'