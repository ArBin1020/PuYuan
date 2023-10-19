from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.
from .models import *
from .serializers import UserProfileSerializer
from utils import *
from User.models import account
# from rest_framework.views import APIView

class BodyUserProfile(viewsets.ViewSet):
    def setprofile(self, request):
        try:
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            if authorization_header:
                parts = authorization_header.split()
                if len(parts) == 2 and parts[0].lower() == 'bearer':
                    token = parts[1]
                    user_id = decode_session_data(token)
                    user_account = account.objects.get(id=user_id)
            try:
                user_profile = UserProfile.objects.get(user=user_account)
                user_profile.delete()
            except UserProfile.DoesNotExist:
                pass
            name = request.data.get('name')
            birthday = request.data.get('birthday')
            height = request.data.get('height')
            weight = request.data.get('weight')
            phone = request.data.get('phone')
            email = request.data.get('email')
            gender = request.data.get('gender')
            fcm_id = request.data.get('fcm_id')
            address = request.data.get('address')
            
            user_profile = UserProfile(user=user_account,name=name,birthday=birthday,height=height,
                                    weight=weight,phone=phone,email=email,
                                    gender=gender,fcm_id=fcm_id,address=address)
            user_profile.save()            
            
            return Response({'status': 0, 'message': '成功'})
        except Exception as e:
            return Response({'status': 1, 'message': f'失敗 - {str(e)}'})

    def getuserprofile(self, request):
        try:
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            if authorization_header:
                parts = authorization_header.split()
                if len(parts) == 2 and parts[0].lower() == 'bearer':
                    token = parts[1]
                    user_id = decode_session_data(token)
                    user_account = account.objects.get(id=user_id)

        except Exception as e:
            return Response({'status': 1, 'message': f'失敗 - {str(e)}'})


class BodyUserDefault(viewsets.ViewSet):
    def userdefault(self, request):
        try:
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            if authorization_header:
                parts = authorization_header.split()
                if len(parts) == 2 and parts[0].lower() == 'bearer':
                    token = parts[1]
                    user_id = decode_session_data(token)
                    user_account = account.objects.get(id=user_id)
                    try:
                        user_default = UserDefault.objects.get(user=user_account)
                        user_default.delete()
                    except UserDefault.DoesNotExist:
                        pass
                    user_default = UserDefault(user=user_account)
                    user_default.save()
                    return Response({'status': 0, 'message': '成功'})
                
        except Exception as e:
            return Response({'status': 1, 'message': f'失敗 - {str(e)}'})
        

class BodyUserSetting(viewsets.ViewSet):
    def usersetting(self, request):
        try:
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            if authorization_header:
                parts = authorization_header.split()
                if len(parts) == 2 and parts[0].lower() == 'bearer':
                    token = parts[1]
                    user_id = decode_session_data(token)
                    user_account = account.objects.get(id=user_id)
                    try:
                        user_setting = UserSetting.objects.get(user=user_account)
                        user_setting.delete()
                    except UserSetting.DoesNotExist:
                        pass
                    after_recording = request.data.get('after_recording')
                    no_recording_for_a_day = request.data.get('no_recording_for_a_day')
                    over_max_or_under_min = request.data.get('over_max_or_under_min')
                    after_meal = request.data.get('after_meal')
                    unit_of_sugar = request.data.get('unit_of_sugar')
                    unit_of_weight = request.data.get('unit_of_weight')
                    unit_of_height = request.data.get('unit_of_height')
                    user_setting = UserSetting(user=user_account,
                                               after_recording=after_recording,
                                               no_recording_for_a_day=no_recording_for_a_day,
                                               over_max_or_under_min=over_max_or_under_min,
                                               after_meal=after_meal,
                                               unit_of_sugar=unit_of_sugar,
                                               unit_of_weight=unit_of_weight,
                                               unit_of_height=unit_of_height
                                               )
                    user_setting.save()
                    return Response({'status': 0, 'message': '成功'})
                return Response({'status': 1, 'message': '失敗'})
        except Exception as e:
            return Response({'status': 1, 'message': f'失敗 - {str(e)}'})
        
class BodyBloodPressure(viewsets.ViewSet):
    def bloodpressure(self, request):
        try:
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            if authorization_header:
                parts = authorization_header.split()
                if len(parts) == 2 and parts[0].lower() == 'bearer':
                    token = parts[1]
                    user_id = decode_session_data(token)
                    user_account = account.objects.get(id=user_id)
                    try:
                        blood_pressure = BloodPressure.objects.get(user=user_account)
                        blood_pressure.delete()
                    except BloodPressure.DoesNotExist:
                        pass
                    systolic = request.data.get('systolic')
                    diastolic = request.data.get('diastolic')
                    pulse = request.data.get('pulse')
                    recorded_at = request.data.get('recorded_at')
                    blood_pressure = BloodPressure(user=user_account,
                                                   systolic=systolic,
                                                   diastolic=diastolic,
                                                   pulse=pulse,
                                                   recorded_at=recorded_at
                                                   )
                    blood_pressure.save()
                    return Response({'status': 0, 'message': '成功'})
                return Response({'status': 1, 'message': '失敗'})
        except Exception as e:
            return Response({'status': 1, 'message': f'失敗 - {str(e)}'})

class BodyWeight(viewsets.ViewSet):
    def weight(self, request):
        try:
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            if authorization_header:
                parts = authorization_header.split()
                if len(parts) == 2 and parts[0].lower() == 'bearer':
                    token = parts[1]
                    user_id = decode_session_data(token)
                    user_account = account.objects.get(id=user_id)
                    try:
                        weight = Weight.objects.get(user=user_account)
                        weight.delete()
                    except Weight.DoesNotExist:
                        pass
                    weight = request.data.get('weight')
                    recorded_at = request.data.get('recorded_at')
                    weight = Weight(user=user_account,
                                    weight=weight,
                                    recorded_at=recorded_at
                                    )
                    weight.save()
                    return Response({'status': 0, 'message': '成功'})
                return Response({'status': 1, 'message': '失敗'})
        except Exception as e:
            return Response({'status': 1, 'message': f'失敗 - {str(e)}'})

class BodyBloodSuger(viewsets.ViewSet):
    def bloodsuger(self, request):
        try:
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            if authorization_header:
                parts = authorization_header.split()
                if len(parts)==2 and parts[0].lower()=='bearer':
                    token = parts[1]
                    user_id = decode_session_data(token)
                    user_account = account.objects.get(id=user_id)
                    try:
                        blood_suger = BloodSuger.objects.get(user=user_account)
                        blood_suger.delete()
                    except BloodSuger.DoesNotExist:
                        pass
                    sugar = request.data.get('sugar')
                    timeperiod = request.data.get('timeperiod')
                    recorded_at = request.data.get('recorded_at')
                    drug = request.data.get('drug')
                    execrise = request.data.get('execrise')
                    blood_suger = BloodSuger(user=user_account,
                                             sugar=sugar,
                                             timeperiod=timeperiod,
                                             recorded_at=recorded_at,
                                             drug=drug,
                                             execrise=execrise
                                             )
                    blood_suger.save()
                    return Response({'status':0,'message':'成功'})
                return Response({'status':1,'message':'失敗'})
        except Exception as e:
            return Response({'status':1,'message':f'失敗 - {str(e)}'})
        
# class Records(viewsets.ViewSet):
#     def records(self, request):
#         try:
#             authorization_header = request.META.get('HTTP_AUTHORIZATION')
#             if authorization_header:
#                 parts=authorization_header.split()
#                 if len(parts)==2 and parts[0].lower()=='bearer':
#                     token = parts[1]
#                     user_id = decode_session_data(token)
#                     user_account = account.objects.get(id=user_id)
#                     try:
#                         records = Records.objects.get(user=user_account)
#                         records.delete()
#                     except Records.DoesNotExist:
#                         pass
#                     type = request.data.get('type')
#                     value = request.data.get('value')
#                     recorded_at = request.data.get('recorded_at')
#                     records = Records(user=user_account,
#                                        type=type,
#                                        value=value,
#                                        recorded_at=recorded_at
#                                        )
#                     records.save()
#                     return Response({'status':0,'message':'成功'})
#                 return Response({'status':1,'message':'失敗'})
#         except Exception as e:
#             return Response({'status':1,'message':f'失敗 - {str(e)}'})