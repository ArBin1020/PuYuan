from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.
from .models import UserProfile
from .serializers import BodyUserProfileSerializer
class BodyUserProfile(viewsets.ViewSet):
    def bodyuserprofile(self, request):
        try:
            # 創建一個新的 news 實例
            name = request.data.get('name')
            birthday = request.data.get('birthday')
            height = request.data.get('height')
            weight = request.data.get('weight')
            phone = request.data.get('phone')
            email = request.data.get('email')
            gender = request.data.get('gender')
            fcm_id = request.data.get('fcm_id')
            address = request.data.get('address')
            
            user_profile = UserProfile(name=name,birthday=birthday,height=height,
                                      weight=weight,phone=phone,email=email,
                                      gender=gender,fcm_id=fcm_id,address=address)
            user_profile.save()            
            
            return Response({'status': 0, 'message': '成功'})
        except Exception as e:
            return Response({'status': 1, 'message': f'失敗 - {str(e)}'})    

    def getuserprofile(self, request):
        try:
            pass
        except Exception as e:
            return Response({'status': 1, 'message': f'失敗 - {str(e)}'})
