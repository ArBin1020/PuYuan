from rest_framework import serializers
from rest_framework.fields import empty
from .models import *
from users.serializers import *
from .basemetadata import UserDiaryMetadata, UserProfileVipMetadata, UserTestMetadata
from datetime import datetime

class UserDefaultSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', read_only=True)

    class Meta:
        model = UserDefault
        exclude = ['user']
        read_only_fields = ['id', 'user_id', 'created_at', 'updated_at']
        
class UserSettingSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', read_only=True)
    
    class Meta:
        model = UserSetting
        exclude = ['user']
        read_only_fields = ['id', 'user_id', 'created_at', 'updated_at']
        
# class UserProfileWriteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ['name', 'birthday', 'height', 'weight', 'phone', 'email', 'gender', 'fcm_id', 'address']

class UserProfileSerializer(serializers.ModelSerializer):
    default = UserDefaultSerializer(read_only=True)
    setting = UserSettingSerializer(read_only=True)

    class Meta:
        model = UserProfile
        exclude = ['user']

    def get_fields(self):
        fields = super().get_fields()
        write_fields = ['name', 'birthday', 'height', 'weight', 'phone', 'email', 'gender', 'fcm_id', 'address']
        for field_name, field in fields.items():
            if field_name not in write_fields:
                field.read_only = True
        return fields
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        default = ret.pop('default')
        setting = ret.pop('setting')
        
        ret['gender'] = int(ret['gender'])
        ret['unread_records'] = [0, 0, 0]
        ret['default'] = default
        ret['setting'] = {k: int(v) if isinstance(v, bool) else v for k, v in setting.items()}
        ret['vip'] = UserProfileVipMetadata.copy()
        return ret

class BloodPressureSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodPressure
        fields = ['id', 'user_id', 'systolic', 'diastolic', 'pulse', 'recorded_at']
        read_only_fields = ['id', 'user_id']

    def __init__(self, *args, **kwargs):
        self.api_type = kwargs.pop('api_type', None)
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if self.api_type == 'diary':
            metadata = UserDiaryMetadata.copy()
            metadata.update(ret)
            metadata['type'] = 'blood_pressure'
            return metadata
        ret = {key: ret[key] for key in ret.keys() if key not in ['id', 'user_id', 'recorded_at']}
        return ret

class UserWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWeight
        fields = ['id', 'user_id', 'weight', 'body_fat', 'bmi', 'recorded_at']
        read_only_fields = ['id', 'user_id']

    def __init__(self, *args, **kwargs):
        self.api_type = kwargs.pop('api_type', None)
        super().__init__(*args, **kwargs)
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if self.api_type == 'diary':
            metadata = UserDiaryMetadata.copy()
            metadata.update(ret)
            metadata['type'] = 'weight'
            return metadata
        return {'weight': ret['weight']}

class BloodSugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodSugar
        fields = ['id', 'user_id', 'sugar', 'timeperiod', 'recorded_at', 'drug', 'exercise']
        read_only_fields = ['id', 'user_id']

    def __init__(self, *args, **kwargs):
        self.api_type = kwargs.pop('api_type', None)
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if self.api_type == 'diary':
            metadata = UserDiaryMetadata.copy()
            metadata.update(ret)
            metadata['type'] = 'blood_sugar'
            return metadata
        return {'sugar': ret['sugar']}
    
class UserDietSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', read_only=True)

    class Meta:
        model = UserDiet
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        self.api_type = kwargs.pop('api_type', None)
        super().__init__(*args, **kwargs)

    def to_representation(self, data):
        ret = super().to_representation(data)
        ret['tag'] = ret['tag'].split(',')
        if self.api_type == 'diary':
            lat, lng = ret.pop('lat'), ret.pop('lng')
            ret['location'] = {'lat': str(lat), 'lng': str(lng)}
            ret['tag'] = [{'name': ret['tag'], 'message': ""}]
            ret['image'] = ["http://www.example.com"]

            metadata = UserDiaryMetadata.copy()
            metadata.update(ret)
            metadata['type'] = 'diet'
            return metadata
        ret.pop('user_id')
        return ret
    
class UserA1cSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserA1c
        fields = ['id', 'user_id', 'a1c', 'recorded_at', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user_id', 'created_at', 'updated_at']

    def to_representation(self, instance):
        ret = super().to_representation(instance)

        ret['a1c'] = str(ret['a1c'])
        return ret

class UserMedicalSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', read_only=True)

    class Meta:
        model = UserMedical
        exclude = ['user']
        read_only_fields = ['id', 'user_id', 'created_at', 'updated_at']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        
        ret = {k: int(v) if isinstance(v, bool) else v for k, v in ret.items()}
        return ret

class UserDrug_UsedSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', read_only=True)

    class Meta:
        model = UserDrugUsed
        exclude = ['user']
        read_only_fields = ['id', 'user_id', 'created_at', 'updated_at']

class UserCareSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', read_only=True)

    class Meta:
        model = UserCare
        exclude = ['user']
        read_only_fields = [f.name for f in UserCare._meta.get_fields() if f.name != 'message']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ca_dt = datetime.strptime(ret['created_at'], '%Y-%m-%dT%H:%M:%S.%f%z')
        ua_dt = datetime.strptime(ret['updated_at'], '%Y-%m-%dT%H:%M:%S.%f%z')
        ret['created_at'] = ca_dt.strftime('%Y-%m-%d %H:%M:%S')
        ret['updated_at'] = ua_dt.strftime('%Y-%m-%d %H:%M:%S')

        return ret