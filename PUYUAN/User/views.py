
from .models import account
from .serializers import accountSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class accountRegister(viewsets.ViewSet):
    def register(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            existing_account = account.objects.filter(email=email).first()
            if existing_account:
                return Response({'status': 1, 'message': '電子郵件已存在'})
            serializer = accountSerializer(data=request.data)
            if serializer.is_valid() is False:
                return Response({'status': 1, 'message': '失敗 - {}'.format(serializer.errors)})
            serializer.save()
            return Response({'status': 0, 'message': '成功'})
        except Exception as e:
            return Response({'status': 1, 'message': '失敗 - {}'.format(str(e))})

class accountLogin(viewsets.ViewSet):
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            existing_account = account.objects.filter(email=email, password=password).first()
            if existing_account:
                return Response({'status': 0, 'message': '成功', 'token': "token123"})
            else:
                return Response({'status': 1, 'message': '電子郵件或密碼錯誤'})
        except Exception as e:
            return Response({'status': 1, 'message': '失敗 - {}'.format(str(e))})
        
class accountSendCode(viewsets.ViewSet):
    def sendcode(self, request):
        email = request.data.get('email')
        try:
            existing_account = account.objects.filter(email=email).first()
            if existing_account:
                return Response({'status': 0, 'message': '成功'})
        except Exception as e:
            return Response({'status': 1, 'message': '失敗 - {}'.format(str(e))})

class accountCheckCode(viewsets.ViewSet):
    def checkcode(self,request):
        email = request.data.get('email')
        code  = request.data.get('code')
        try:
            existing_account = account.objects.filter(email=email).first()
            if existing_account:
                return Response({'status': 0, 'message': '成功'})
        except Exception as e:
            return Response({'status': 1, 'message': '失敗 - {}'.format(str(e))})
        
class accountForget(viewsets.ViewSet):
    def forgot(self, request):
        email = request.data.get('email')
        try:
            existing_account = account.objects.filter(email=email).first()
            if existing_account:
                return Response({'status': 0, 'message': '成功'})
        except Exception as e:
            return Response({'status': 1, 'message': '失敗 - {}'.format(str(e))})