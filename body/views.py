from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from .basemetadata import *
from users.utils import *


class UserProfileViewSet(APIView):
    metadata_class = UserProfileMetadata

    @check_token()
    def get(self, request):
        try:
            userpf = UserProfile.objects.get(user_id=request.token_data['user_id'])
        except UserProfile.DoesNotExist:
            return Response({'status': '1', 'message': '資料不存在'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = UserProfileSerializer(userpf)
            print(serializer.data)
            return Response({'status': '0', 'message': '成功', 'user': serializer.data}, status=status.HTTP_200_OK)

    @check_token()
    def patch(self, request):
        try:
            userpf = UserProfile.objects.get(user_id=request.token_data['user_id'])
        except UserProfile.DoesNotExist:
            # serializer = UserProfileSerializer(data=request.data)
            # if serializer.is_valid():
            #     default = UserDefault.objects.get_or_create(user_id = request.user_id)
            #     setting = UserSetting.objects.get_or_create(user_id = request.user_id)
            #     serializer.save(user_id=request.token_data['user_id'], default_id=default[0].id, setting_id=setting[0].id)
            #     return Response({'status': '0', 'message': '成功'}, status=status.HTTP_201_CREATED)
            return Response({'status': '1', 'message': '資料不存在'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            print({k: v for k, v in request.data.items() if v is not None and v != ''})
            serializer = UserProfileSerializer(userpf,
                                               data={k: v for k, v in request.data.items() if v is not None and v != ''},
                                               partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': '0', 'message': '成功'}, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response({'status': '1', 'message': '失敗'}, status=status.HTTP_400_BAD_REQUEST)
            
class UserDefaultViewSet(APIView):
    @check_token()
    def patch(self, request):
        try:
            userdf = UserDefault.objects.get(user_id=request.token_data['user_id'])
        except UserDefault.DoesNotExist:
            serializer = UserDefaultSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user_id=request.token_data['user_id'])
                return Response({'status': '0', 'message': '成功'}, status=status.HTTP_201_CREATED)
        else:
            serializer = UserDefaultSerializer(userdf, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': '0', 'message': '成功'}, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response({'status': '1', 'message': '失敗'}, status=status.HTTP_400_BAD_REQUEST)
        
            
class UserSettingViewSet(APIView):
    @check_token()
    def patch(self, request):
        try:
            userset = UserSetting.objects.get(user_id=request.token_data['user_id'])
        except UserSetting.DoesNotExist:
            serializer = UserSettingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user_id=request.token_data['user_id'])
                return Response({'status': '0', 'message': '成功'}, status=status.HTTP_201_CREATED)
        else:
            serializer = UserSettingSerializer(userset, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': '0', 'message': '成功'}, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response({'status': '1', 'message': '失敗'}, status=status.HTTP_400_BAD_REQUEST)
    
class BloodPressureViewSet(APIView):
    metadata_class = BloodPressureMetadata

    @check_token()
    def post(self, request):
        serializer = BloodPressureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.token_data['user_id'])
            return Response({'status': '0', 'message': '成功', 'records': '成功'}, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response({'status': '1', 'message': '失敗', 'records': '失敗'}, status=status.HTTP_400_BAD_REQUEST)
    
class UserWeightViewSet(APIView):
    metadata_class = UserWeightMetadata

    @check_token()
    def post(self, request):
        serializer = UserWeightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.token_data['user_id'])
            return Response({'status': '0', 'message': '成功'}, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response({'status': '1', 'message': '失敗', 'records': '失敗'}, status=status.HTTP_400_BAD_REQUEST)
    
class BloodSugarViewSet(APIView):
    metadata_class = BloodSugarMetadata

    @check_token()
    def post(self, request):
        serializer = BloodSugarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.token_data['user_id'])
            print("========================================")
            return Response({'status': '0', 'message': '成功'}, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response({'status': '1', 'message': '失敗'}, status=status.HTTP_400_BAD_REQUEST)
    
class UserRecordsViewSet(APIView):
    metadata_class = UserRecordsMetadata

    @check_token()
    def post(self, request):
        diet = request.data.get('diet')
        if diet is None:
            return Response({'status': '1', 'message': '參數錯誤'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer_BS = {'sugar': 0.0} if not(bs := BloodSugar.objects.filter(user_id=request.token_data['user_id'], 
                                                                  recorded_at__icontains=diet).last()
                        )  else BloodSugarSerializer(bs).data
        serializer_BP = {'systolic': 0,
                         'diastolic': 0,
                         'pulse': 0} if not(bp := BloodPressure.objects.filter(user_id=request.token_data['user_id'],
                                                                      recorded_at__icontains=diet).last()
                        ) else BloodPressureSerializer(bp).data
        serializer_UW = {'weight': 0.0} if not(uw := UserWeight.objects.filter(user_id=request.token_data['user_id'],
                                                                   recorded_at__icontains=diet).last()
                        ) else UserWeightSerializer(uw).data
        return Response({'status': '0', 'message': '成功',
                         'blood_sugars': serializer_BS,
                         'blood_pressures': serializer_BP,
                         'weights': serializer_UW}, status=status.HTTP_200_OK)
    
    @check_token()
    def delete(self, request):
        data = request.data.get('deleteObject')
        print(data)
        blood_sugar_id = data.get('blood_sugars', [])
        blood_pressure_id = data.get('blood_pressures', [])
        user_weight_id = data.get('weights', [])
        user_diet_id = data.get('diets', [])
        if not(blood_sugar_id or blood_pressure_id or user_weight_id or user_diet_id):
            return Response({'status': '1', 'message': '參數錯誤'}, status=status.HTTP_400_BAD_REQUEST)
        BloodSugar.objects.filter(id__in=blood_sugar_id, user_id=request.token_data['user_id']).delete()
        BloodPressure.objects.filter(id__in=blood_pressure_id, user_id=request.token_data['user_id']).delete()
        UserWeight.objects.filter(id__in=user_weight_id, user_id=request.token_data['user_id']).delete()
        UserDiet.objects.filter(id__in=user_diet_id, user_id=request.token_data['user_id']).delete()
        return Response({'status': '0', 'message': '成功'}, status=status.HTTP_200_OK)
    
class UserDietViewSet(APIView):
    metadata_class = UserDietMetadata

    @check_token()
    def post(self, request):
        if 'tag[]' in request.data:
            request.data['tag'] = ','.join(request.data.pop('tag[]'))
        serializer = UserDietSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.token_data['user_id'])
            return Response({'status': '0', 'message': '成功', 'image_url': 'http://img.test.com'}, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response({'status': '1', 'message': '失敗'}, status=status.HTTP_400_BAD_REQUEST)
    
class UserDiaryViewSet(APIView):
    @check_token()
    def get(self, request):
        date = request.query_params.get('date')
        if date is None:
            return Response({'status': '1', 'message': '參數錯誤'}, status=status.HTTP_400_BAD_REQUEST)

        data = combined_model([BloodPressure, UserWeight, BloodSugar, UserDiet], 
                              {'user_id': request.token_data['user_id'], 'recorded_at__icontains': date}, 
                              [BloodPressureSerializer, UserWeightSerializer, BloodSugarSerializer, UserDietSerializer], 
                              {'api_type': 'diary'})
        print(data)
        
        return Response({'status': '0', 'message': '成功', 'diary': data}, status=status.HTTP_200_OK)
    
class UserA1cViewSet(APIView):
    metadata_class = UserA1cMetadata

    @check_token()
    def get(self, request):
        usera1c = UserA1c.objects.filter(user_id=request.token_data['user_id'])
        if usera1c.count() == 0:
            # return Response({'status': '1', 'message': '資料不存在'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'status': '0', 'message': '成功', 'a1cs': []}, status=status.HTTP_200_OK)
        serializer = UserA1cSerializer(usera1c, many=True)
        print(serializer.data)
        return Response({'status': '0', 'message': '成功', 'a1cs': serializer.data}, status=status.HTTP_200_OK)
        
    @check_token()
    def post(self, request):
        serializers = UserA1cSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save(user_id=request.token_data['user_id'])
            return Response({'status': '0', 'message': '成功'}, status=status.HTTP_201_CREATED)
        print(serializers.errors)
        return Response({'status': '1', 'message': '失敗'}, status=status.HTTP_400_BAD_REQUEST)
    
    @check_token()
    def delete(self, request):
        a1c_id = request.data.get('ids[]', [])
        if not(a1c_id):
            return Response({'status': '1', 'message': '參數錯誤'}, status=status.HTTP_400_BAD_REQUEST)
        UserA1c.objects.filter(id__in=a1c_id, user_id=request.token_data['user_id']).delete()
        return Response({'status': '0', 'message': '成功'}, status=status.HTTP_200_OK)
    
class UserMedicalViewSet(APIView):
    metadata_class = UserMedicalMetadata

    @check_token()
    def patch(self, request):
        try:
            usermd = UserMedical.objects.get(user_id=request.token_data['user_id'])
        except UserMedical.DoesNotExist:
            serializer = UserMedicalSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user_id=request.token_data['user_id'])
                return Response({'status': '0', 'message': '成功'}, status=status.HTTP_201_CREATED)
            return Response({'status': '1', 'message': '資料不存在'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = UserMedicalSerializer(usermd, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': '0', 'message': '成功'}, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response({'status': '1', 'message': '失敗'}, status=status.HTTP_400_BAD_REQUEST)
    
    @check_token()
    def get(self, request):
        try:
            usermd = UserMedical.objects.get(user_id=request.token_data['user_id'])
        except UserMedical.DoesNotExist:
            return Response({'status': '1', 'message': '資料不存在'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = UserMedicalSerializer(usermd)
            print(serializer.data)
            return Response({'status': '0', 'message': '成功', 'medical_info': serializer.data}, status=status.HTTP_200_OK)
        
class UserDrugUsedViewSet(APIView):
    metadata_class = UserDrugUsedMetadata

    @check_token()
    def post(self, request):
        serializer = UserDrug_UsedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.token_data['user_id'])
            return Response({'status': '0', 'message': '成功'}, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response({'status': '1', 'message': '失敗'}, status=status.HTTP_400_BAD_REQUEST)
    
    @check_token()
    def get(self, request):
        userdrug = UserDrugUsed.objects.filter(user_id=request.token_data['user_id'])
        if userdrug.count() == 0:
            return Response({'status': '1', 'message': '資料不存在'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserDrug_UsedSerializer(userdrug, many=True)
        return Response({'status': '0', 'message': '成功', 'drug_useds': serializer.data}, status=status.HTTP_200_OK)
    
    @check_token()
    def delete(self, request):
        drug_used_id = request.data.get('ids[]', [])
        if not(drug_used_id):
            return Response({'status': '1', 'message': '參數錯誤'}, status=status.HTTP_400_BAD_REQUEST)
        UserDrugUsed.objects.filter(id__in=drug_used_id, user_id=request.token_data['user_id']).delete()
        return Response({'status': '0', 'message': '成功'}, status=status.HTTP_200_OK)
    
class UserCareViewSet(APIView):
    metadata_class = UserCareMetadata

    @check_token()
    def post(self, request):
        print(request.data)
        print("========================================")
        serializer = UserCareSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.token_data['user_id'])
            return Response({'status': '0', 'message': '成功'}, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response({'status': '1', 'message': '失敗'}, status=status.HTTP_400_BAD_REQUEST)
    
    @check_token()
    def get(self, request):
        usercare = UserCare.objects.filter(user_id=request.token_data['user_id'])
        if usercare.count() == 0:
            # return Response({'status': '1', 'message': '資料不存在'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'status': '0', 'message': '成功', 'cares': []}, status=status.HTTP_200_OK)
        serializer = UserCareSerializer(usercare, many=True)
        return Response({'status': '0', 'message': '成功', 'cares': serializer.data}, status=status.HTTP_200_OK)
    
class UserBadgeViewSet(APIView):
    metadata_class = UserBadgeMetadata

    @check_token()
    def put(self, request):
        badge = request.data.get('badge')
        if badge is None:
            return Response({'status': '1', 'message': '參數錯誤'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': '0', 'message': '成功'}, status=status.HTTP_200_OK)
