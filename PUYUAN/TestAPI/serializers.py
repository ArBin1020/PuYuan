from rest_framework import serializers
from User.models import news

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = news
        fields = '__all__'
