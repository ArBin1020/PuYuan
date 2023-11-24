from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.
from .models import *

from utils import *
from User.models import account
from django.utils import timezone
from django.db import transaction

from User.models import account

DEFAULT_DIARY_DICT = {
    "id": 0,
    "user_id": 0,
    "systolic": 0,
    "diastolic": 0,
    "pulse": 0,
    "weight": 0.0,
    "body_fat": 0.0,
    "bmi": 0.0,
    "sugar": 0.0,
    "exercise": 0,
    "drug": 0,
    "timeperiod": 0,
    "description": "",
    "meal": 0,
    "tag": [{"name": [], "message": ""}],  # name: list[str]
    "image": ["http://www.example.com"],
    "location": {"lat": "", "lng": ""},
    "reply": "",
    "recorded_at": "",
    "type": "",
}

class BodyUserProfile(viewsets.ViewSet):
    # complete
    def setprofile(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))
            user_profile, created = UserProfile.objects.get_or_create(user_id=user_account)
            if not created:
                    if request.data.get('name'):
                        user_profile.name = request.data.get('name')
                        user_profile.birthday = request.data.get('birthday')
                        user_profile.height = request.data.get('height')
                        user_profile.weight = request.data.get('weight')
                        user_profile.phone = request.data.get('phone')
                        user_profile.email = request.data.get('email')
                        user_profile.gender = request.data.get('gender')
                        user_profile.fcm_id = request.data.get('fcm_id')
                        user_profile.address = request.data.get('address')
                        user_profile.save()
            else:
                user_profile = UserProfile(user_id=user_account)
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
            print(user_profile)
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
                "account" : user_account.email,
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
        # print(response)
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
            user_setting, created = UserProfile.objects.get_or_create(user_id=user_account)

            if not created:
                    user_setting.after_recording = request.data.get('after_recording')
                    print(request.data.get('after_recording'))
                    user_setting.no_recording_for_a_day = request.data.get('no_recording_for_a_day')
                    user_setting.over_max_or_under_min = request.data.get('over_max_or_under_min')
                    user_setting.after_meal = request.data.get('after_meal')
                    user_setting.unit_of_sugar = request.data.get('unit_of_sugar')
                    user_setting.unit_of_weight = request.data.get('unit_of_weight')
                    user_setting.unit_of_height = request.data.get('unit_of_height')
                    user_setting.updated_time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
                    user_setting.save()
            else:
                user_setting = UserSetting(user_id=user_account)
                user_setting.save()
            return Response({'status': "0", 'message': '成功'})
        except Exception as e:
            print(e)
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
    def delete_records(self, request):
        try:
            del_object = request.data['deleteObject']
            user_account = account.objects.get(id=get_token(request))
            print(del_object)
            blood_pressure_to_delete = del_object.get("blood_pressures", [])
            weight_to_delete = del_object.get("weights", [])
            blood_sugar_to_delete = del_object.get("blood_sugars", [])
            diets_to_delete = del_object.get("diets", [])
            print(blood_pressure_to_delete)
            BloodSuger.objects.filter(id__in=blood_sugar_to_delete, user_id=user_account).delete()
            BloodPressure.objects.filter(id__in=blood_pressure_to_delete, user_id=user_account).delete()
            Weight.objects.filter(id__in=weight_to_delete, user_id=user_account).delete()
            Diet.objects.filter(id__in=diets_to_delete, user_id=user_account).delete()
            return Response({'status':"0",'message':'成功'})
        except Exception as e:
            return Response({'status':"1",'message':f'失敗 - {str(e)}'}, status=400)
    
class BodyGetDiet(viewsets.ViewSet):
    def list(self, request):
        try:
            print(request.method)
            user_id = get_token(request)
            date_time = request.query_params["date"]
            # bloodpressures = BloodPressure.objects.filter(user_id=user_id)
            # weights = Weight.objects.filter(user_id=user_id)
            # bloodsugers = BloodSuger.objects.filter(user_id=user_id)
            # diets = Diet.objects.filter(user_id=user_id, recorded_at__startswith=date_time)
            # print(diets.meal)
            
            response = []

            print('tmp')
            if BloodPressure.objects.filter(user_id=user_id):
                for bloodpressure in BloodPressure.objects.filter(user_id=user_id, recorded_at__startswith=date_time):
                    bloodpressure_data = DEFAULT_DIARY_DICT.copy()
                    bloodpressure_data.update(
                        user_id=user_id,
                        systolic=bloodpressure.systolic,
                        diastolic=bloodpressure.diastolic,
                        pulse=bloodpressure.pulse,
                        recorded_at=bloodpressure.recorded_at,
                        type="blood_pressure"
                    )
                    response.append(bloodpressure_data)
            if Weight.objects.filter(user_id=user_id):
                for weight in Weight.objects.filter(user_id=user_id, recorded_at__startswith=date_time):
                    weight_data = DEFAULT_DIARY_DICT.copy()
                    weight_data.update(
                        user_id=user_id,
                        weight=weight.weight,
                        body_fat=weight.body_fat,
                        bmi=weight.bmi,
                        recorded_at=weight.recorded_at,
                        type="weight"
                    )
                    response.append(weight_data)
            if BloodSuger.objects.filter(user_id=user_id):
                for bloodsuger in BloodSuger.objects.filter(user_id=user_id, recorded_at__startswith=date_time):
                    bloodsuger_data = DEFAULT_DIARY_DICT.copy()
                    bloodsuger_data.update(
                        user_id=user_id,
                        sugar=bloodsuger.sugar,
                        exercise=bloodsuger.exercise,
                        drug=bloodsuger.drug,
                        timeperiod=bloodsuger.timeperiod,
                        recorded_at=bloodsuger.recorded_at,
                        type="blood_sugar"
                    )
                    response.append(bloodsuger_data)
            if Diet.objects.filter(user_id=user_id):
                for diet in Diet.objects.filter(user_id=user_id, recorded_at__startswith=date_time):
                    diet_data = DEFAULT_DIARY_DICT.copy()
                    
                    diet_data.update(
                        user_id=user_id,
                        description=diet.description,
                        meal=diet.meal,
                        tag = [{
                            "name": diet.tag.split(','),
                            "message": ""
                        }],
                        # image=diet.image,
                        location={
                            "lat": str(diet.lat),
                            "lng": str(diet.lng)
                        },
                            recorded_at=diet.recorded_at,
                            type="diet"
                        )
                    response.append(diet_data)

            # print(response)
            # for bloodpressure, weight, bloodsuger, diet in zip(bloodpressures, weights, bloodsugers, diets):
            #     diet_data = {
            #         "id": user_id,
            #         "user_id": user_id,
            #         "systolic": bloodpressure.systolic,
            #         "diastolic": bloodpressure.diastolic,
            #         "pulse": bloodpressure.pulse,
            #         "weight": weight.weight,
            #         "body_fat": weight.body_fat,
            #         "bmi": weight.bmi,
            #         "sugar": bloodsuger.sugar,
            #         "execrise": bloodsuger.execrise,
            #         "drug": bloodsuger.drug,
            #         "timeperiod": bloodsuger.timeperiod,
            #         "description": diet.description,
            #         "meal": diet.meal,
            #         "tag": diets.tag.split(','),
            #         "image": diet.image,
            #         "location": {
            #             "lat": diet.lat,
            #             "lng": diet.lng
            #         },
            #         "reply": "",
            #         "recorded_at": diet.recorded_at,
            #         "type": "blood_pressure",
            #     }
                
            #     response.append(diet_data)
                
            # print(date_time)
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
                      created_at=timezone.now().strftime("%Y-%m-%d %H:%M:%S"),
                      updated_at=timezone.now().strftime("%Y-%m-%d %H:%M:%S")
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
            print('medical'+str(response))
            return Response({'status':"0",'message':'成功','medical_info':response})
        except Medical.DoesNotExist:
            return Response({'status':"1",'message':'失敗 - 未找到醫療記錄'}, status=404)
        except Exception as e:
            print(e)
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
                                  created_at=timezone.now().strftime("%Y-%m-%d %H:%M:%S"),
                                  updated_at=timezone.now().strftime("%Y-%m-%d %H:%M:%S")
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
            # date_time = request.query_params["date"]
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
            time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
            user_account = account.objects.get(id=get_token(request))
            message = request.data.get('message')
            care = Care(user=user_account,
                        member_id=0,
                        reply_id=0,
                        message=message,
                        created_at=time,
                        updated_at=time,
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