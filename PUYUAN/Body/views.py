from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.
from .models import *
from .serializers import *
from utils import *
from User.models import account
from django.utils import timezone
from django.db import transaction
from User.models import account
class BodyUserProfile(viewsets.ViewSet):
    # complete
    def setprofile(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))
            try:
                user_profile = UserProfile.objects.get(user=user_account)
                print(user_profile)
                user_profile.delete()
            except UserDefault.DoesNotExist:
                pass
            user_profile = UserProfile(user=user_account)
            user_profile.save()
            return Response({'status': "0", 'message': '成功'})
            
        except Exception as e:
            print(e)
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'}, status=400)

    def getuserprofile(self, request):
        user_id = get_token(request)
        print(user_id)
            # print(account.objects.get(id=get_token(request)))
        try:
            user_profile = UserProfile.objects.get(user_id=user_id)
            # unread_records = unread_records.objects.get(user_id=1)
            default = UserDefault.objects.get(user_id=user_id)
            setting = UserSetting.objects.get(user_id=user_id)
            user_vip = vip.objects.get(user_id=user_id)
            user_account = account.objects.get(id=user_id)
        except (UserProfile.DoesNotExist,
                 UserDefault.DoesNotExist,
                   UserSetting.DoesNotExist,
                    vip.DoesNotExist,
                    account.DoesNotExist) as e:
            print(f'data not found - {str(e)}')
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'}, status=400)
        except Exception as e:
            print(e)
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'}, status=400)

        response = {
                "id" : user_id,
                "name" : user_profile.name,
                "account" : user_account.username,
                "email" : user_profile.email,
                "phone" : user_profile.phone,
                "fb_id" : "未設置",
                "status" : "general", 
                "group" : "0",
                "birthday" : user_profile.birthday,
                "height" : user_profile.height,
                "weight" : user_profile.weight,
                "gender" : int(user_profile.gender),
                "address" : user_profile.address,
                "unread_records" : [
                    0,0,0
                ],
                "verified" : 1,
                "privacy_policy" : 1,
                "must_change_password" : 0,
                "fcm_id" : user_profile.fcm_id,
                "login_times" : 0,
                "created_at" : user_profile.created_at,
                "updated_at" : user_profile.updated_at,
                "default" : {
                    "id" : default.id,
                    "user_id" : default.user_id,
                    "sugar_delta_max" : default.sugar_delta_max,
                    "sugar_delta_min" : default.sugar_delta_min,
                    "sugar_morning_max" : default.sugar_morning_max,
                    "sugar_morning_min" : default.sugar_morning_min,
                    "sugar_evening_max" : default.sugar_evening_max,
                    "sugar_evening_min" : default.sugar_evening_min,
                    "sugar_before_max" : default.sugar_before_max,
                    "sugar_before_min" : default.sugar_before_min,
                    "sugar_after_max" : default.sugar_after_max,
                    "sugar_after_min" : default.sugar_after_min,
                    "systolic_max" : default.systolic_max,
                    "systolic_min" : default.systolic_min,
                    "diastolic_max" : default.diastolic_max,
                    "diastolic_min" : default.diastolic_min,
                    "pulse_max" : default.pulse_max,
                    "pulse_min" : default.pulse_min,
                    "weight_max" : default.weight_max,
                    "weight_min" : default.weight_min,
                    "bmi_max" : default.bmi_max,
                    "bmi_min" : default.bmi_min,
                    "body_fat_max" : default.body_fat_max,
                    "body_fat_min" : default.body_fat_min,
                    "created_at" : default.created_at,
                    "updated_at" : default.updated_at
                },
                "setting" : {
                    "id": setting.id,
                    "user_id": setting.user_id,
                    "after_recording": int(setting.after_recording),
                    "no_recording_for_a_day": int(setting.no_recording_for_a_day),
                    "over_max_or_under_min": int(setting.over_max_or_under_min),
                    "after_meal": int(setting.after_meal),
                    "unit_of_sugar": int(setting.unit_of_sugar),
                    "unit_of_weight": int(setting.unit_of_weight),
                    "unit_of_height": int(setting.unit_of_height),
                    "created_at" : setting.created_at,
                    "updated_at" : setting.updated_at    
                },
                "vip" : {
                    "id": user_vip.id,
                    "user_id": user_id,
                    "level": user_vip.level,
                    "remark": user_vip.remark,
                    "started_at": user_vip.started_at,
                    "ended_at" : user_vip.ended_at,
                    "created_at" : user_vip.created_at,
                    "updated_at" : user_vip.updated_at
                }
            }
        return Response({'status': "0", 'message': '成功', 'user': response})

# complete
class BodyUserDefault(viewsets.ViewSet):
    def userdefault(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))
            try:
                user_default = UserDefault.objects.get(user=user_account)
                user_default.delete()
            except UserDefault.DoesNotExist:
                pass
            user_default = UserDefault(user=user_account)
            user_default.save()
            return Response({'status': "0", 'message': '成功'})
                
        except Exception as e:
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'}, status=400)
        
# complete
class BodyUserSetting(viewsets.ViewSet):
    def usersetting(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))
            try:
                user_setting = UserSetting.objects.get(user=user_account)
                user_setting.delete()
            except UserSetting.DoesNotExist:
                pass
            user_setting = UserSetting(user=user_account,
                                       after_recording=request.data.get('after_recording'),
                                       no_recording_for_a_day=request.data.get('no_recording_for_a_day'),
                                       over_max_or_under_min=request.data.get('over_max_or_under_min'),
                                       after_meal=request.data.get('after_meal'),
                                       unit_of_sugar=request.data.get('unit_of_sugar'),
                                       unit_of_weight=request.data.get('unit_of_weight'),
                                       unit_of_height=request.data.get('unit_of_height')
                                    )
            user_setting.save()
            return Response({'status': "0", 'message': '成功'})
        except Exception as e:
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'}, status=400)

# complete      
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
                    return Response({'status': "0", 'message': '成功'})
                return Response({'status': "1", 'message': '失敗'})
        except Exception as e:
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'}, status=400)

# complete
class BodyWeight(viewsets.ViewSet):
    def weight(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))
            weight = request.data.get('weight')
            body_fat = request.data.get('body_fat')
            bmi = request.data.get('bmi')
            recorded_at = request.data.get('recorded_at')
            weight = Weight(user=user_account,
                            weight=weight,
                            body_fat=body_fat,
                            bmi=bmi,
                            recorded_at=recorded_at)
            weight.save()
            return Response({'status': "0", 'message': '成功'})
        except Exception as e:
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'}, status=400)

# complete
class BodyBloodSuger(viewsets.ViewSet):
    def bloodsuger(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))
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
                                     execrise=execrise)
            blood_suger.save()
            return Response({'status':0,'message':'成功'})
        except Exception as e:
            return Response({'status':1,'message':f'失敗 - {str(e)}'}, status=400)
        
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
#             return Response({'status':1,'message':f'失敗 - {str(e)}'}, status=400)

class BodyGetDiet(viewsets.ViewSet):
    def getdiet(self, request):
        try:
            user_id = get_token(request)
            bloodpressures = BloodPressure.objects.filter(user_id=user_id)
            weights = Weight.objects.filter(user_id=user_id)
            bloodsugers = BloodSuger.objects.filter(user_id=user_id)
            diets = Diet.objects.filter(user_id=user_id)

            response = []

            for bloodpressure, weight, bloodsuger, diet in zip(bloodpressures, weights, bloodsugers, diets):
                diet_data = {
                    "id": user_id,
                    "user_id": user_id,
                    "systolic": bloodpressure.systolic,
                    "diastolic": bloodpressure.diastolic,
                    "pulse": bloodpressure.pulse,
                    "weight": weight.weight,
                    "body_fat": weight.body_fat,
                    "bmi": weight.bmi,
                    "sugar": bloodsuger.sugar,
                    "execrise": bloodsuger.execrise,
                    "drug": bloodsuger.drug,
                    "timeperiod": bloodsuger.timeperiod,
                    "description": diet.description,
                    "meal": diet.meal,
                    "tag": diet.tag,
                    "image": diet.image,
                    "location": {
                        "lat": diet.lat,
                        "lng": diet.lng
                    },
                    "reply": "",
                    "recorded_at": diet.recorded_at,
                    "type": "blood_pressure",
                }

                response.append(diet_data)

            return Response({'status': "0", 'message': '成功', 'diet': response})
        except Exception as e:
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'}, status=400)


class BodyDiet(viewsets.ViewSet):
    def diet(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))
            description = request.data.get('description')
            meal = request.data.get('meal')
            tag = request.data.get('tag')
            image = request.data.get('image')
            lat = request.data.get('lat')
            lng = request.data.get('lng')
            recorded_at = request.data.get('recorded_at')
            diet = Diet(user=user_account,
                        description=description,
                        meal=meal,
                        tag=tag,
                        image=image,
                        lat=lat,
                        lng=lng,
                        recorded_at=recorded_at
                        )
            diet.save()
            return Response({'status':0,'message':'成功','image_url':'https://www.puyuan.tech/media'})
        except Exception as e:
            return Response({'status':1,'message':f'失敗 - {str(e)}'}, status=400)

class BodyDelDiet(viewsets.ViewSet):
    def deldiet(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))
            data = request.data.get('deleteObject')

            blood_sugar_id = data.get('blood_sugar_id')
            print(blood_sugar_id)
            diet = Diet.objects.filter(user=user_account)
            # diet.delete()
            return Response({'status':0,'message':'成功'})
        except Exception as e:
            return Response({'status':1,'message':f'失敗 - {str(e)}'}, status=400)



class BodyA1c(viewsets.ViewSet):
    def getA1c(self, request):
        try:
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            if authorization_header:
                parts=authorization_header.split()
                if len(parts)==2 and parts[0].lower()=='bearer':
                    token = parts[1]
                    user_id = decode_session_data(token)
                    user_account = account.objects.get(id=user_id)
                    A1c = A1c.objects.filter(user=user_account)
                    serializer = BodyA1cSerializer(A1c, many=True)
                    return Response({'status':0,'message':'成功','a1cs':serializer.data})

        except Exception as e:
            return Response({'status':1,'message':f'失敗 - {str(e)}'}, status=400)

    def postA1c(self, request):
        try:
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            if authorization_header:
                parts=authorization_header.split()
                if len(parts)==2 and parts[0].lower()=='bearer':
                    token = parts[1]
                    user_id = decode_session_data(token)
                    user_account = account.objects.get(id=user_id)

                    data_A1c = request.data.get('A1c')
                    recorded_at = request.data.get('recorded_at')

                    A1c = A1c(user=user_account,
                              a1c=data_A1c,
                              recorded_at=recorded_at,
                              created_at=timezone.now(),
                              updated_at=timezone.now()
                              )
                    A1c.save()
                    return Response({'status':0,'message':'成功'})
                return Response({'status':1,'message':'失敗'})
        except Exception as e:
            return Response({'status':1,'message':f'失敗 - {str(e)}'}, status=400)
        
    def delA1c(self, request):
        try:
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            if authorization_header:
                parts=authorization_header.split()
                if len(parts)==2 and parts[0].lower()=='bearer':
                    token = parts[1]
                    user_id = decode_session_data(token)
                    user_account = account.objects.get(id=user_id)

                    A1c = A1c.objects.filter(user=user_account)
                    A1c.delete()
                    return Response({'status':0,'message':'成功'})
                return Response({'status':1,'message':'失敗'})
        except Exception as e:
            return Response({'status':1,'message':f'失敗 - {str(e)}'}, status=400)
        

class BodyGetMedical(viewsets.ViewSet):
    def getmedical(self, request):
        try:
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            if authorization_header:
                parts=authorization_header.split()
                if len(parts)==2 and parts[0].lower()=='bearer':
                    token = parts[1]
                    user_id = decode_session_data(token)
                    user_account = account.objects.get(id=user_id)

                    medical = Medical.objects.filter(user=user_account)
                    serializer = BodyMedicalSerializer(medical, many=True)
                    return Response({'status':0,'message':'成功','medical':serializer.data})
        except Exception as e:
            return Response({'status':1,'message':f'失敗 - {str(e)}'}, status=400)
        
    def patchmedical(self, request):
        try:
            user_id = get_token(request)
        except Exception as e:
            print(e)
            return Response({'status':1,'message':f'失敗 - {str(e)}'}, status=400)
class BodyPostMedical(viewsets.ViewSet):
    def postmedical(self, request):
        try:
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            if authorization_header:
                parts=authorization_header.split()
                if len(parts)==2 and parts[0].lower()=='bearer':
                    token = parts[1]
                    user_id = decode_session_data(token)
                    user_account = account.objects.get(id=user_id)

                    medical = request.data.get('medical')
                    recordet_at = request.data.get('recordet_at')

                    medical = Medical(user=user_account,
                              medical=medical,
                              recordet_at=recordet_at,
                              created_at=timezone.now(),
                              updated_at=timezone.now()
                              )
                    medical.save()
                    return Response({'status':0,'message':'成功'})
                return Response({'status':1,'message':'失敗'})
        except Exception as e:
            return Response({'status':1,'message':f'失敗 - {str(e)}'}, status=400)


class BodyGetDrugUsed(viewsets.ViewSet):
    def getdrugused(self, request):
        try:
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            if authorization_header:
                parts = authorization_header.split()
                if len(parts)==2 and parts[0].lower()=='bearer':
                    token = parts[1]
                    user_id = decode_session_data(token)
                    user_account = account.objects.get(id=user_id)
                    drug_used = Drug_Used.objects.filter(user=user_account)
                    serializer = BodyDrugUsedSerializer(drug_used, many=True)
                    return Response({'status':0,'message':'成功','drug_used':serializer.data})
        except Exception as e:
            return Response({'status':1,'message':f'失敗 - {str(e)}'}, status=400)
        

class BodyPostDrugUsed(viewsets.ViewSet):
    def postdrugused(self, request):
        try:
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            if authorization_header:
                parts = authorization_header.split()
                if len(parts)==2 and parts[0].lower()=='bearer':
                    token = parts[1]
                    user_id = decode_session_data(token)
                    user_account = account.objects.get(id=user_id)

                    drug_used = request.data.get('drug_used')
                    recordet_at = request.data.get('recordet_at')

                    drug_used = Drug_Used(user=user_account,
                              drug_used=drug_used,
                              recordet_at=recordet_at,
                              created_at=timezone.now(),
                              updated_at=timezone.now()
                              )
                    drug_used.save()
                    return Response({'status':0,'message':'成功'})
                return Response({'status':1,'message':'失敗'})
        except Exception as e:
            return Response({'status':1,'message':f'失敗 - {str(e)}'}, status=400)
        
class BodyDelDrugUsed(viewsets.ViewSet):
    def deldrugused(self, request):
        try:
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            if authorization_header:
                parts = authorization_header.split()
                if len(parts)==2 and parts[0].lower()=='bearer':
                    token = parts[1]
                    user_id = decode_session_data(token)
                    user_account = account.objects.get(id=user_id)
                    drug_used = Drug_Used.objects.filter(user=user_account)
                    drug_used.delete()
                    return Response({'status':0,'message':'成功'})
                return Response({'status':1,'message':'失敗'})
        except Exception as e:
            return Response({'status':1,'message':f'失敗 - {str(e)}'}, status=400)
        

class BodyGetCare(viewsets.ViewSet):
    def getcare(self, request):
        try:
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            if authorization_header:
                parts = authorization_header.split()
                if len(parts)==2 and parts[0].lower()=='bearer':
                    token = parts[1]
                    user_id = decode_session_data(token)
                    # user_account = account.objects.get(id=user_id)
                    care = Care.objects.filter(user=user_id)
                    serializer = BodyCareSerializer(care, many=True)
                    return Response({'status':0,'message':'成功','care':serializer.data})
        except Exception as e:
            return Response({'status':1,'message':f'失敗 - {str(e)}'}, status=400)
        

class BodyPostCare(viewsets.ViewSet):
    def postcare(self, request):
        try:
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            if authorization_header:
                parts = authorization_header.split()
                if len(parts)==2 and parts[0].lower()=='bearer':
                    token = parts[1]
                    user_id = decode_session_data(token)
                    user_account = account.objects.get(id=user_id)
                    member_id = request.data.get('member_id')
                    reply_id = request.data.get('reply_id')
                    message = request.data.get('message')
                    care = Care(user=user_account,
                              member_id=member_id,
                              reply_id=reply_id,
                              message=message,
                              created_at=timezone.now(),
                              updated_at=timezone.now()
                              )
                    care.save()
                    return Response({'status':0,'message':'成功'})
                return Response({'status':1,'message':'失敗'})
        except Exception as e:
            return Response({'status':1,'message':f'失敗 - {str(e)}'}, status=400)
        

        