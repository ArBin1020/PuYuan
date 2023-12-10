import json
# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from utils import *
from User.models import *
from Body.models import *
from Friend.models import *

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
    "tag": [{"name": [], "message": ""}],
    "image": ["http://www.example.com"],
    "location": {"lat": "", "lng": ""},
    "reply": "",
    "recorded_at": "",
    "type": "",
}

# 2-1 個人資訊設定, 個人資訊
class Profile(viewsets.ViewSet):
    def update(self, request):
        try:
            user_id = get_user_id(request)
            datas = json.loads(request.body)

            # 單獨更新 'username'，如果 'name' 存在的話
            if 'name' in datas:
                User_Info.objects.filter(id=user_id).update(username=datas['name'])

            # 更新除了 'username' 和 'name' 以外的欄位
            update_data = {key: value for key, value in datas.items() if key not in ['username', 'name'] and value != ''}
            User_Info.objects.filter(id=user_id).update(**update_data)

            return Response({'status': '0', 'message': 'success'}, status=200)
        except Exception as e:
            print(e)
            return Response({'status': '1', 'message': 'error'}, status=400)

    
    def list(self, request):
        try:
            # print(request.headers)
            user_id = get_user_id(request)
            user = User_Info.objects.filter(id=user_id).first()
            default = User_Default.objects.get(user_id=user_id)
            setting = User_Setting.objects.get(user_id=user_id)
            vip = User_VIP.objects.get(user_id=user_id)

            response = {
                "id": user.id,
                "name": user.username,
                "account": user.account,
                "email": user.email,
                "phone": user.phone,
                "fb_id": "未設置",
                "status": user.status,
                "group": "0",
                "birthday": user.birthday,
                "height": user.height,
                "weight": user.weight,
                "gender": int(user.gender),
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
                    "user_id" : user_id,
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
                    "id": user_id,
                    "user_id": user_id,
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
            
            return Response({'status':'0','message': 'success','user': response}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
# 2-2 個人預設值
class Default(viewsets.ViewSet):
    def update(self, request):
        try:
            user_id = get_user_id(request)
            datas = json.loads(request.body)
            # print(datas)
            for data, value in datas.items():
                if value == '' or value == 0:
                    continue
                else:
                    User_Default.objects.filter(user_id=user_id).update(**{data: value})

            return Response({'status': '0', 'message': 'success'}, status=200)
        except Exception as e:
            print(e)
            return Response({'status': '1', 'message': 'error'}, status=400)

# 2-3 個人設定
class Setting(viewsets.ViewSet):
    def update(self, request):
        try:
            user_id = get_user_id(request)
            datas = json.loads(request.body)
            for data in datas:
                if datas[data] == '':
                    continue
                else:
                    User_Setting.objects.filter(user_id=user_id).update(**{data:datas[data]})
            return Response({'status': '0', 'message': 'success'}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
        
# 2-4 血壓測量結果
class Blood_Pressure(viewsets.ViewSet):
    def create(self, request):
        try:
            user_id = get_user_id(request)
            user_id_instance = User_Info.objects.get(id=user_id)
            User_Blood_Pressure.objects.create(
                user_id=user_id_instance,
                systolic=request.data['systolic'],
                diastolic=request.data['diastolic'],
                pulse=request.data['pulse'],
                recorded_at=request.data['recorded_at']
            )
            return Response({'status':'0','message': 'success'}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
        
# 2-5 體重測量結果 
class Weight(viewsets.ViewSet):
    def create(self, request):
        try:
            user_id = get_user_id(request)
            user_id_instance = User_Info.objects.get(id=user_id)
            User_Weight.objects.create(
                user_id=user_id_instance,
                weight=request.data['weight'],
                body_fat=request.data['body_fat'],
                bmi=request.data['bmi'],
                recorded_at=request.data['recorded_at']
            )
            return Response({'status':'0','message': 'success'}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
        
# 2-6 血糖測量結果 
class Blood_Sugar(viewsets.ViewSet):
    def create(self, request):
        try:
            user_id = get_user_id(request)
            user_info_instance = User_Info.objects.get(id=user_id)
            User_Blood_Sugar.objects.create(
                user_id=user_info_instance,
                sugar=request.data['sugar'],
                timeperiod=request.data['timeperiod'],
                recorded_at=request.data['recorded_at'],
                drug = request.data['drug'],
                exercise = request.data['exercise'],
            )
            return Response({'status':'0','message': 'success'}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
        
# 2-7 上一筆紀錄資訊,  刪除日記記錄
class Records(viewsets.ViewSet):
    def create(self, request):
        try:
            user_id = get_user_id(request)
            if User_Blood_Sugar.objects.filter(user_id=user_id):
                blood_sugar = User_Blood_Sugar.objects.filter(user_id=user_id).latest('recorded_at')
                response_sugar = {
                    'sugar': blood_sugar.sugar,
                }
            else:
                response_sugar = {
                    'sugar': 0,
                }
            
            if User_Blood_Pressure.objects.filter(user_id=user_id):
                blood_pressure = User_Blood_Pressure.objects.filter(user_id=user_id).latest('recorded_at')
                response_pressure = {
                    'systolic': blood_pressure.systolic,
                    'diastolic': blood_pressure.diastolic,
                    'pulse': blood_pressure.pulse,
                }
            else:
                response_pressure = {
                    'systolic': 0,
                    'diastolic': 0,
                    'pulse': 0,
                }
            if User_Weight.objects.filter(user_id=user_id):
                weight = User_Weight.objects.filter(user_id=user_id).latest('recorded_at')
                response_weight = {
                    'weight': weight.weight,
                    'body_fat': weight.body_fat,
                    'bmi': weight.bmi,
                }
            else:
                response_weight = {
                    'weight': 0,
                    'body_fat': 0,
                    'bmi': 0,
                }
            return Response({'status':'0',
                             'message': 'success',
                             'blood_sugars':response_sugar,
                             'blood_pressures':response_pressure,
                             'weights':response_weight
                             }, status=200)
            
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)

    def remove(self, request):
        try:
            user_id = get_user_id(request)
            
            deleteObject = request.data['deleteObject']
            
            for data in deleteObject:
                if data == 'blood_sugars':
                    for i in deleteObject['blood_surgars']:
                        User_Blood_Sugar.objects.filter(id=i,user_id=user_id).delete()
                elif data == 'blood_pressures':
                    for i in deleteObject['blood_pressures']:
                        User_Blood_Pressure.objects.filter(id=i,user_id=user_id).delete()
                elif data == 'weights':
                    for i in deleteObject['weights']:
                        User_Weight.objects.filter(id=i,user_id=user_id).delete()
                elif data == 'diets':
                    for i in deleteObject['diets']:
                        User_Diary.objects.filter(id=i,user_id=user_id).delete()
                return Response({'status':'0','message': 'success'}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
        
# 2-8 日記列表
class Diary(viewsets.ViewSet):
    def list(self, request):
        try:
            user_id = get_user_id(request)
            date = request.query_params.get('date')
            response = []
            if User_Blood_Pressure.objects.filter(user_id=user_id).exists():
                for blood_pressure in User_Blood_Pressure.objects.filter(user_id=user_id, recorded_at__startswith=date):
                    blood_pressure_data = DEFAULT_DIARY_DICT.copy()
                    blood_pressure_data.update(
                        user_id=user_id,
                        systolic=blood_pressure.systolic,
                        diastolic=blood_pressure.diastolic,
                        pulse=blood_pressure.pulse,
                        recorded_at=blood_pressure.recorded_at.strftime('%Y-%m-%d %H:%M:%S'),
                        type="blood_pressure"
                    )
                    response.append(blood_pressure_data)
            if User_Weight.objects.filter(user_id=user_id).exists():
                for weight in User_Weight.objects.filter(user_id=user_id, recorded_at__startswith=date):
                    weight_data = DEFAULT_DIARY_DICT.copy()
                    weight_data.update(
                        user_id=user_id,
                        weight=weight.weight,
                        body_fat=weight.body_fat,
                        bmi=weight.bmi,
                        recorded_at=weight.recorded_at.strftime('%Y-%m-%d %H:%M:%S'),
                        type="weight"
                    )
                    response.append(weight_data)
            if User_Blood_Sugar.objects.filter(user_id=user_id).exists():
                for blood_sugar in User_Blood_Sugar.objects.filter(user_id=user_id, recorded_at__startswith=date):
                    blood_sugar_data = DEFAULT_DIARY_DICT.copy()
                    blood_sugar_data.update(
                        user_id=user_id,
                        sugar=blood_sugar.sugar,
                        exercise=blood_sugar.exercise,
                        drug=blood_sugar.drug,
                        timeperiod=blood_sugar.timeperiod,
                        recorded_at=blood_sugar.recorded_at.strftime('%Y-%m-%d %H:%M:%S'),
                        type="blood_sugar"
                    )
                    response.append(blood_sugar_data)
            if User_Diary.objects.filter(user_id=user_id).exists():
                for diary in User_Diary.objects.filter(user_id=user_id, recorded_at__startswith=date):
                    diary_data = DEFAULT_DIARY_DICT.copy()
                    diary_data.update(
                        user_id=user_id,
                        description=diary.description,
                        meal=diary.meal,
                        tag=[{
                            "name": diary.tag.split(","),
                            "message": ""
                        }],
                        location={
                            "lat": str(diary.lat),
                            "lng": str(diary.lng)
                        },
                        recorded_at=diary.recorded_at.strftime('%Y-%m-%d %H:%M:%S'),
                        type="diet"
                    )
                    response.append(diary_data)
            # print(response)
            return Response({'status':'0','message': 'success','diary':response}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
# 2-9 飲食日記
class Diet(viewsets.ViewSet):
    def create(self, request):
        try:
            user_id = get_user_id(request)
            user_info_instance = User_Info.objects.get(id=user_id)
            tag = request.data.get('tag[]')
            tags = ','.join(tag)
            User_Diary.objects.create(
                user_id=user_info_instance,
                description=request.data['description'],
                meal=request.data['meal'],
                tag=tags,
                lat=request.data['lat'],
                lng=request.data['lng'],
                recorded_at=request.data['recorded_at']
            )
            return Response({'status':'0','message': 'success','image_url':'https://www.puyuan.tech/media'}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
        
# 2-10 糖化血色素
class A1c(viewsets.ViewSet):
    def create(self, request):
        try:
            user_id = get_user_id(request)
            user_id_instance = User_Info.objects.get(id=user_id)
            User_A1c.objects.create(
                user_id=user_id_instance,
                a1c=request.data['a1c'],
                recorded_at=request.data['recorded_at']
            )
            return Response({'status':'0','message': 'success'}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)

    def list(self, request):
        try:
            user_id = get_user_id(request)
            a1cs = User_A1c.objects.filter(user_id=user_id).order_by('-id')
            a1cs_list = []
            for a1c in a1cs:
                a1cs_list.append({
                    'id': a1c.id,
                    'user_id': user_id,
                    'a1c': str(a1c.a1c),
                    'recorded_at': a1c.recorded_at,
                    'created_at': a1c.created_at,
                    'updated_at': a1c.updated_at,
                })
            return Response({'status':'0','message': 'success','a1cs':a1cs_list}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
    
    def remove(self, request):
        try:
            user_id = get_user_id(request)
            ids = request.data['ids[]']
            if User_A1c.objects.filter(user_id=user_id):
                for data_id in ids:
                    User_A1c.objects.filter(id=data_id).delete()
                return Response({'status':'0','message': 'success'}, status=200)

        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
# 2-11 就醫資訊
class Medical(viewsets.ViewSet):
    def update(self, request):
        try:
            user_id = get_user_id(request)
            datas = json.loads(request.body)
            for data in datas:
                if datas[data] == '':
                    continue
                else:
                    User_Medical.objects.filter(user_id=user_id).update(**{data:datas[data]})
            return Response({'status':'0','message': 'success'}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
        
    def list(self, request):
        try:
            user_id = get_user_id(request)
            medical = User_Medical.objects.get(user_id=user_id)
            response = {
                'id': medical.id,
                'user_id': user_id,
                'diabetes_type': medical.diabetes_type,
                'oad': medical.oad,
                'insulin': medical.insulin,
                'anti_hypertensives': medical.anti_hypertensives,
                'created_at': medical.created_at,
                'updated_at': medical.updated_at,
            }
            return Response({'status':'0','message': 'success','medical_info':response}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
        
# 2-12 藥物資訊     
class Drug(viewsets.ViewSet):
    def create(self, request):
        try:
            user_id = get_user_id(request)
            User_Care.objects.create(
                user_id=user_id,
                data_type=request.data['type'],
                name=request.data['name'],
                recorded_at=request.data['recorded_at'],
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
            drugs = User_Drug.objects.filter(user_id=user_id).order_by('-id')
            drugs_list = []
            for drug in drugs:
                drugs_list.append({
                    'id': drug.id,
                    'user_id': drug.user_id,
                    'data_type': drug.data_type,
                    'name': drug.name,
                    'recorded_at': drug.recorded_at,
                    'created_at': drug.created_at,
                    'updated_at': drug.updated_at,
                })
            return Response({'status':'0','message': 'success','drug_useds':drugs_list}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)

    def remove(self, request):
        try:
            user_id = get_user_id(request)
            ids = request.data['ids[]']
            if User_Drug.objects.filter(user_id=user_id):
                for data_id in ids:
                    User_Drug.objects.filter(id=data_id).delete()
                return Response({'status':'0','message': 'success'}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
        
# 2-13 關懷諮詢     
class Care(viewsets.ViewSet):
    def create(self, request):
        try:
            user_id = get_user_id(request)
            user_id_instance = User_Info.objects.get(id=user_id)
            User_Care.objects.create(
                user_id=user_id_instance,
                message=request.data['message'],
                created_at=datetime.now().strftime("%Y-%m-%d %H"),
                updated_at=datetime.now().strftime("%Y-%m-%d %H")
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
                    'user_id': user_id,
                    'member_id': care.member_id,
                    'reply_id': care.reply_id,
                    'message': care.message,
                    'created_at': care.created_at.strftime('%Y-%m-%d %H'),
                    'updated_at': care.updated_at.strftime('%Y-%m-%d %H'),
                })
            return Response({'status':'0','message': 'success','cares':cares_list}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)

    def remove(self, request):
        try:
            user_id = get_user_id(request)
            ids = request.data['ids[]']
            if User_Drug.objects.filter(user_id=user_id):
                for data_id in ids:
                    User_Drug.objects.filter(id=data_id).delete()
                return Response({'status':'0','message': 'success'}, status=200)

        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
        
# 2-14 更新 badge       
class Badge(viewsets.ViewSet):
    def update(self, request):
        try:
            user_id = get_user_id(request)
            User_Info.objects.filter(id=user_id).update(**{'badge':request.data['badge']})
            return Response({'status':'0','message': 'success'}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)