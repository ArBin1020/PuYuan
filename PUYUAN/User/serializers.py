from rest_framework import serializers
from .models import account
from rest_framework.validators import UniqueValidator

class accountSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=account.objects.all())]
    )
    password = serializers.CharField()
    code = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = account
        fields = ['username', 'email', 'password', 'code']