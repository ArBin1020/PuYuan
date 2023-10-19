from rest_framework import serializers
from .models import account, news, share
from rest_framework.validators import UniqueValidator

class accountSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=account.objects.all())]
    )
    password = serializers.CharField()
    code = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = account
        fields = '__all__'

# class accountOtherSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#         validators=[UniqueValidator(queryset=account.objects.all())]
#     )
#     code = serializers.CharField(write_only=True, required=False)

#     class Meta:
#         model = account
#         fields = '__all__'
class OtherSerializer(serializers.ModelSerializer):

    pushed_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = news
        fields = '__all__'


class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = share
        fields = '__all__'