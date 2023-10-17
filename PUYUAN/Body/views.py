from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.

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

            
            
            return Response({'status': 0, 'message': '成功'})
        except Exception as e:
            return Response({'status': 1, 'message': f'失敗 - {str(e)}'})    

