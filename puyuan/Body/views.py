import json
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from utils import *

from User.models import *
from Body.models import *
from Friend.models import *

# Create your views here.
class User_Profile(viewsets.ViewSet):
    def update(self, request):
        try:
            user_id = get_user_id(request)
            datas = json.loads(request.data['data'])
            for data in datas:
                if datas[data] == '':
                    continue
                else:
                    User_Info.objects.filter(id=user_id).update(**{data:datas[data]})
        except Exception as e:
            return Response({'status':'1','message': 'error'}, status=400)
    
    def list(self, request):
        try:
            user_id = get_user_id(request)
            user = User_Info.objects.get(id=user_id)
            default = User_Default.objects.get(user_id=user_id)
            setting = User_Setting.objects.get(user_id=user_id)
            vip = vip.objects.get(user_id=user_id)
            resopnse = {
                "id": user.id,
                "name": user.name,
                "account": user.account,
                "email": user.email,
                "phone": user.phone,
                "fb_id": "未設置",
                "status": user.status,
                "group": user.groups,
                "birthday": user.birthday,
                "height": user.height,
                "weight": user.weight,
                "gender": user.gender,
                "address": user.address,
                'unread_records':[
                    0, 0, 0
                ],
                "verified": 1,
                "privacy_policy": 1,
                "must_change_password": user.must_change_password,
                "fcm_id": user.fcm_id,
                "login_times": user.login_times,
                "created_at": user.created_at,
                "updated_at": user.updated_at,
                "created_at": user.created_at,
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
                    "id": vip.id,
                    "user_id": user_id,
                    "level": vip.level,
                    "remark": vip.remark,
                    "started_at": vip.started_at,
                    "ended_at" : vip.ended_at,
                    "created_at" : vip.created_at,
                    "updated_at" : vip.updated_at
                }
            }
            return Response({'status':'0','message': 'success','user':resopnse}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)

class User_Default(viewsets.ViewSet):
    def update(self, request):
        try:
            user_id = get_user_id(request)
            datas = json.loads(request.data['data'])
            for data in datas:
                if datas[data] == '':
                    continue
                else:
                    User_Default.objects.filter(user_id=user_id).update(**{data:datas[data]})
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
    
class User_Setting(viewsets.ViewSet):
    def update(self, request):
        try:
            user_id = get_user_id(request)
            datas = json.loads(request.data['data'])
            for data in datas:
                if datas[data] == '':
                    continue
                else:
                    User_Setting.objects.filter(user_id=user_id).update(**{data:datas[data]})
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
        
class Blood_Pressure(viewsets.ViewSet):
    def create(self, request):
        try:
            user_id = get_user_id(request)
            Blood_Pressure.objects.create(
                user_id=user_id,
                systolic=request.data['systolic'],
                diastolic=request.data['diastolic'],
                pulse=request.data['pulse'],
                recorded_at=request.data['recorded_at']
            )
            return Response({'status':'0','message': 'success'}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
    
class Blood_Weight(viewsets.ViewSet):
    def create(self, request):
        try:
            user_id = get_user_id(request)
            Blood_Weight.objects.create(
                user_id=user_id,
                weight=request.data['weight'],
                body_fat=request.data['body_fat']
                bmi=request.data['bmi'],
                recorded_at=request.data['recorded_at']
            )
            return Response({'status':'0','message': 'success'}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)

class Blood_Sugar(viewsets.ViewSet):
    def create(self, request):
        try:
            user_id = get_user_id(request)
            Blood_Sugar.objects.create(
                user_id=user_id,
                sugar=request.data['sugar'],
                recorded_at=request.data['recorded_at'],
                drug = request.data['drug'],
                execrise = request.data['execrise'],
            )
            return Response({'status':'0','message': 'success'}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
        

class Records(viewsets.ViewSet):
    def list(self, request):
        try:
            user_id = get_user_id(request)
            records = []
            blood_pressures = Blood_Pressure.objects.filter(user_id=user_id).order_by('-id')
            blood_sugars = Blood_Sugar.objects.filter(user_id=user_id).order_by('-id')
            blood_weights = Blood_Weight.objects.filter(user_id=user_id).order_by('-id')
            for blood_pressure in blood_pressures:
                records.append({
                    'id': blood_pressure.id,
                    'user_id': blood_pressure.user_id,
                    'systolic': blood_pressure.systolic,
                    'diastolic': blood_pressure.diastolic,
                    'pulse': blood_pressure.pulse,
                    'recorded_at': blood_pressure.recorded_at,
                    'created_at': blood_pressure.created_at,
                    'updated_at': blood_pressure.updated_at,
                })
            for blood_sugar in blood_sugars:
                records.append({
                    'id': blood_sugar.id,
                    'user_id': blood_sugar.user_id,
                    'sugar': blood_sugar.sugar,
                    'timeperiod': blood_sugar.timeperiod,
                    'drug': blood_sugar.drug,
                    'exercise': blood_sugar.exercise,
                    'recorded_at': blood_sugar.recorded_at,
                    'created_at': blood_sugar.created_at,
                    'updated_at': blood_sugar.updated_at,
                })
            for blood_weight in blood_weights:
                records.append({
                    'id': blood_weight.id,
                    'user_id': blood_weight.user_id,
                    'weight': blood_weight.weight,
                    'body_fat': blood_weight.body_fat,
                    'bmi': blood_weight.bmi,
                    'recorded_at': blood_weight.recorded_at,
                    'created_at': blood_weight.created_at,
                    'updated_at': blood_weight.updated_at,
                })
            return Response({'status':'0','message': 'success','records':records}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)

class 

class Care:
    def create(self, request):
        try:
            user_id = get_user_id(request)
            message = request.data['message']
            User_Care.objects.filter(user_id=user_id).create(
                message=message,
                created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                updated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            return Response({'status':'0','message': 'success'}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
    def list(self, request):
        try:
            user_id = get_user_id(request)
            cares = User_Care.objects.filter(user_id=user_id).order_by('-id')
            cares_list = []
            for care in cares:
                cares_list.append({
                    'id': care.id,
                    'user_id': care.user_id,
                    'member_id': care.member_id,
                    'reply_id': care.reply_id,
                    'message': care.message,
                    'created_at': care.created_at,
                    'updated_at': care.updated_at,
                })
            return Response({'status':'0','message': 'success','cares':cares_list}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)

class Badge(viewsets.ViewSet):
    def create(self, request):
        try:
            user_id = get_user_id(request)
            User_Info.objects.filter(id=user_id).update(**{'badge':request.data['badge']})
            return Response({'status':'0','message': 'success'}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)