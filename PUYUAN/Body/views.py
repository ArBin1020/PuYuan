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
            if UserProfile.objects.filter(user=user_account):
                user_profile = UserProfile.objects.get(user=user_account)
                # user_profile.delete()
                if request.data.get('name') != '':
                    
                    user_profile = UserProfile(user=user_account,
                                               name = request.data.get('name'),
                                               birthday = request.data.get('birthday'),
                                               height = request.data.get('height'),
                                               weight = request.data.get('weight'),
                                               phone = request.data.get('phone'),
                                               email = request.data.get('email'),
                                               gender = request.data.get('gender'),
                                               fcm_id = request.data.get('fcm_id'),
                                               address = request.data.get('address')
                                               )
                    user_profile.save()
            else:
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
                "status" : "VIP", 
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

            blood_suger = BloodSuger(user=user_account,
                                     sugar=request.data.get('sugar'),
                                     timeperiod=request.data.get('timeperiod'),
                                     recorded_at=request.data.get('recorded_at'),
                                     drug=request.data.get('drug'),
                                     exercise = request.data.get('exercise'))
            blood_suger.save()
            return Response({'status':"0",'message':'成功'})
        except Exception as e:
            print(e)
            return Response({'status':"1",'message':f'失敗 - {str(e)}'}, status=400)
        
class Records(viewsets.ViewSet):
    def post_records(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))
            if BloodSuger.objects.filter(user=user_account):
                bloodsuger = BloodSuger.objects.filter(user=user_account).latest('recorded_at')
                response_sugar = {
                    'sugar': bloodsuger.sugar,
                }
            else:
                response_sugar = {
                    'sugar': 0,
                }
            if BloodPressure.objects.filter(user=user_account):
                bloodpressures = BloodPressure.objects.filter(user=user_account).latest('recorded_at')
                response_blood_pressure = {
                    'systolic': bloodpressures.systolic,
                    'diastolic': bloodpressures.diastolic,
                    'pulse': bloodpressures.pulse
                }
            else:
                response_blood_pressure = {
                    'systolic': 0,
                    'diastolic': 0,
                    'pulse': 0
                }
            if Weight.objects.filter(user=user_account):
                weights = Weight.objects.filter(user=user_account).latest('recorded_at')
                response_weight = {
                    'weight': weights.weight,
                }
            else:
                response_weight = {
                    'weight': 0,
                }
            return Response({'status':"0",'message':'成功','blood_sugars':response_sugar,'blood_pressures':response_blood_pressure,'weights':response_weight})
        except Exception as e:
            print(e)
            return Response({'status':"1",'message':f'失敗 - {str(e)}'}, status=400)
    # def delete_records(self, request):
    #     try:
    #         if request.data.get()
    #         user_account = account.objects.get(id=get_token(request))
    #         bloodsuger = BloodSuger.objects.filter(user=user_account)
    #         bloodsuger.delete()
    #         bloodpressures = BloodPressure.objects.filter(user=user_account)
    #         bloodpressures.delete()
    #         weights = Weight.objects.filter(user=user_account)
    #         weights.delete()
    #         return Response({'status':"0",'message':'成功'})
    #     except Exception as e:
    #         return Response({'status':"1",'message':f'失敗 - {str(e)}'}, status=400)
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
                    "tag": diets.tag.split(','),
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
                
            print(response)
            return Response({'status': "0", 'message': '成功', 'diary': response})
        except Exception as e:
            print(e)
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'}, status=400)


class BodyDiet(viewsets.ViewSet):
    def diet(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))
            description = request.data.get('description')
            meal = request.data.get('meal')
            tag = request.data.get('tag[]')
            tags = ','.join(tag)
            image = request.data.get('image')
            
            lat = request.data.get('lat')
            lng = request.data.get('lng')
            recorded_at = request.data.get('recorded_at')
            diet = Diet(user=user_account,
                        description=description,
                        meal=meal,
                        tag=tags,
                        image=image,
                        lat=lat,
                        lng=lng,
                        recorded_at=recorded_at
                        )
            diet.save()
            return Response({'status':"0",'message':'成功','image_url':'https://www.puyuan.tech/media'})
        except Exception as e:
            print(e)
            return Response({'status':"1",'message':f'失敗 - {str(e)}'}, status=400)

class BodyDelDiet(viewsets.ViewSet):
    def deldiet(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))
            data = request.data.get('deleteObject')

            blood_sugar_id = data.get('blood_sugar_id')
            print(blood_sugar_id)
            diet = Diet.objects.filter(user=user_account)
            # diet.delete()
            return Response({'status':"0",'message':'成功'})
        except Exception as e:
            return Response({'status':"1",'message':f'失敗 - {str(e)}'}, status=400)



class BodyA1c(viewsets.ViewSet):
    def getA1c(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))
            a1c = A1c.objects.filter(user=user_account)
            response = []
            for a in a1c:
                a1c_data = {
                    "id": user_account.id,
                    "user_id": user_account.id,
                    "a1c": a.a1c,
                    "recorded_at": a.recorded_at,
                    "created_at": a.created_at,
                    "updated_at": a.updated_at
                }
                response.append(a1c_data)
            # serializer = BodyA1cSerializer(A1c, many=True)
            return Response({'status':"0",'message':'成功','a1cs':response})

        except Exception as e:
            return Response({'status':"1",'message':f'失敗 - {str(e)}'}, status=400)

    def postA1c(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))

            data_A1c = request.data.get('a1c')
            recorded_at = request.data.get('recorded_at')

            a1c = A1c(user=user_account,
                      a1c=data_A1c,
                      recorded_at=recorded_at,
                      created_at=timezone.now(),
                      updated_at=timezone.now()
                      )
            a1c.save()
            return Response({'status':"0",'message':'成功'})
        except Exception as e:
            print(e)
            return Response({'status':"1",'message':f'失敗 - {str(e)}'}, status=400)
        
    def delA1c(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))
            a1c = A1c.objects.filter(user=user_account)
            a1c.delete()
            return Response({'status':"0",'message':'成功'})
         
        except Exception as e:
            print(e)
            return Response({'status':"1",'message':f'失敗 - {str(e)}'}, status=400)
        

class BodyGetMedical(viewsets.ViewSet):
    def getmedical(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))

            medical = Medical.objects.get(user=user_account)
            response = {
                "id" : user_account.id,
                "user_id" : user_account.id,
                "diabetes_type" : medical.diabetes_type,
                "oad" : medical.oad,
                "insulin" : medical.insulin,
                "anti_hypertensives" : medical.anti_hypertensives,
                "created_at" : medical.created_at,
                "updated_at" : medical.updated_at
            }
            print(response)
            return Response({'status':"0",'message':'成功','medical_info':response})
        except Medical.DoesNotExist:
            return Response({'status':"1",'message':'失敗 - 未找到醫療記錄'}, status=404)
        except Exception as e:
            return Response({'status':"1",'message':f'失敗 - {str(e)}'}, status=400)
        
    def patchmedical(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))
            try:
                medical = Medical.objects.get(user=user_account)
                print(medical)
                medical.delete()
            except UserDefault.DoesNotExist:
                pass
            medical = Medical(user=user_account)
            medical.save()
            return Response({'status': "0", 'message': '成功'})
            
        except Exception as e:
            print(e)
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'}, status=400)

# complete
class BodyDrugUsed(viewsets.ViewSet):
    def getdrugused(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))
            drug_used = Drug_Used.objects.filter(user=user_account)
            response = []
            for d in drug_used:
                drug_used_data = {
                    "id": user_account.id,
                    "user_id": user_account.id,
                    "type": d.data_type,
                    "name": d.name,
                    "recorded_at": d.recorded_at,
                    "created_at": d.created_at,
                    "updated_at": d.updated_at
                }
                response.append(drug_used_data)
            return Response({'status':"0",'message':'成功','drug_useds':response})
        except Exception as e:
            print(e)
            return Response({'status':"1",'message':f'失敗 - {str(e)}'}, status=400)
        
    def postdrugused(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))
            data_type = request.data.get('type')
            name = request.data.get('name')
            recorded_at = request.data.get('recorded_at')

            drug_used = Drug_Used(user=user_account,
                                  data_type=data_type,
                                  name=name,
                                  recorded_at=recorded_at,
                                  created_at=timezone.now(),
                                  updated_at=timezone.now()
                                  )
            drug_used.save()
            return Response({'status':"0",'message':'成功'})
        except Exception as e:
            print(e)
            return Response({'status':"1",'message':f'失敗 - {str(e)}'}, status=400)
        
    def deldrugused(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))
            drug_used = Drug_Used.objects.filter(user=user_account)
            drug_used.delete()
            return Response({'status':"0",'message':'成功'})
        except Exception as e:
            return Response({'status':"1",'message':f'失敗 - {str(e)}'}, status=400)
        


class BodyCare(viewsets.ViewSet):
    def getcare(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))
            care = Care.objects.filter(user=user_account)
            response = []
            for c in care:
                care_data = {
                    "id": user_account.id,
                    "user_id": user_account.id,
                    "member_id": c.member_id,
                    "reply_id": c.reply_id,
                    "message": c.message,
                    "created_at": c.created_at,
                    "updated_at": c.updated_at
                }
                response.append(care_data)
            print(response)
            return Response({'status':"0",'message':'成功','cares':response})
        except Exception as e:
            return Response({'status':"1",'message':f'失敗 - {str(e)}'}, status=400)
        
    def postcare(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))
            message = request.data.get('message')
            care = Care(user=user_account,
                        member_id=0,
                        reply_id=0,
                        message=message,
                        created_at=timezone.now(),
                        updated_at=timezone.now()
                        )
            care.save()
            return Response({'status':"0",'message':'成功'})
        except Exception as e:
            print(e)
            return Response({'status':"1",'message':f'失敗 - {str(e)}'}, status=400)
        

class Body_Badge(viewsets.ViewSet):
    def put_badge(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))
            badge = request.data.get('badge')
            if badge is None:
                return Response({'status': '1', 'message': '參數錯誤'}, status=400)
            return Response({'status': '0', 'message': '成功'})
        except Exception as e:
            print(e)
            return Response({'status': '1', 'message': '參數錯誤'}, status=400)