from rest_framework import serializers
from .models import *
from users.models import User
from body.models import UserProfile
from datetime import datetime

class UserSerializer(serializers.ModelSerializer):
    account = serializers.CharField(source='email', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'account']

# class FriendRequestSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)

#     class Meta:
#         model = Friend
#         fields = ['id', 'user_id', 'relation_id', 'type', 'status', 'read', 'created_at', 'updated_at', 'user']

class FriendResultSerializer(serializers.ModelSerializer):
    relation = UserSerializer(source='friend', read_only=True)

    class Meta:
        model = Friend
        fields = ['id', 'user_id', 'relation_id', 'type', 'status', 'read', 'created_at', 'updated_at', 'relation']

    def __init__(self, *args, **kwargs):
        self.api_type = kwargs.pop('api_type', None)
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if self.api_type == 'list':
            return {
                'id': ret['relation']['id'],
                'name': UserProfile.objects.get(user_id=ret['relation']['id']).name,
                'relation_type': ret['type']
            }
        if self.api_type == 'requests':
            ret['user'] = ret.pop('relation')
            ret['user']['name'] = UserProfile.objects.get(user_id=ret['user']['id']).name
            return ret
        
        ret['relation']['name'] = UserProfile.objects.get(user_id=ret['relation']['id']).name
        return ret