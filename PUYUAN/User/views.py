
from .models import account
from .serializers import accountSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.sessions.middleware import SessionMiddleware
from django.core.mail import EmailMessage

def send_email(email, content):
    subject = 'PUYUAN 驗證碼'
    message = content
    email_from = 'PUYUAN'
    recipient_list = [email]
    try:
        email = EmailMessage(subject, message, email_from, recipient_list)
        email.send()
    except:
        return False
class accountRegister(viewsets.ViewSet):
    def register(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        username = request.data.get('username')
        try:
            # existing_account = account.objects.filter(email=email).first()
            # if existing_account:
            #     return Response({'status': 1, 'message': '電子郵件已存在'})
            encrypted_password = make_password(password)
            serializer = accountSerializer(data=request.data)
            if serializer.is_valid():
                user = account(username=username, email=email, password=encrypted_password)
                user.save()
                send_email(email, f'username: {username}, password: {password}, email: {email}')
                return Response({'status': 0, 'message': '成功'})
            return Response({'status': 1, 'message': '失敗 - {}'.format(serializer.errors)})
                
        except Exception as e:
            return Response({'status': 1, 'message': '失敗 - {}'.format(str(e))})

# token還沒做
class accountLogin(viewsets.ViewSet):
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            existing_account = account.objects.filter(email=email).first()
            if existing_account and check_password(password, existing_account.password):
                # request.session.save()
                
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