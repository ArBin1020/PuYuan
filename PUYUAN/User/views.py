
from .models import account
from .serializers import accountSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.sessions.middleware import SessionMiddleware
from django.core.mail import EmailMessage
import random
import string

def generate_random_code(length=6):
    characters = string.ascii_letters + string.digits 
    code = ''.join(random.choice(characters) for _ in range(length))
    return code

def send_email(subject, email, content):
    subject = subject
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
                return Response({'status': 0, 'message': '成功'})
            return Response({'status': 1, 'message': '失敗 - {}'.format(serializer.errors)})
                
        except Exception as e:
            return Response({'status': 1, 'message': f'失敗 - {str(e)}'})
# token還沒做
# status = 2還沒做
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
            return Response({'status': 1, 'message': f'失敗 - {str(e)}'})

# complete
class accountSendCode(viewsets.ViewSet):
    def sendcode(self, request):
        email = request.data.get('email')
        try:
            existing_account = account.objects.filter(email=email).first()

            if existing_account:
                code = generate_random_code()
                subject = 'PUYUAN 驗證碼'
                content = f'您的驗證碼為:{code}'
                send_email(subject, email, content)
                existing_account.code = code
                existing_account.save()
                return Response({'status': 0, 'message': '成功'})
        except Exception as e:
            return Response({'status': 1, 'message': f'失敗 - {str(e)}'})
# complete
class accountCheckCode(viewsets.ViewSet):
    def checkcode(self,request):
        email = request.data.get('email')
        code  = request.data.get('code')
        try:
            existing_account = account.objects.filter(email=email).first()
            if existing_account:
                if existing_account.code == code:
                    return Response({'status': 0, 'message': '成功'})
                else:
                    return Response({'status': 1, 'message': '驗證碼錯誤'})
            return Response({'status': 0, 'message': '失敗'})
        except Exception as e:
            return Response({'status': 1, 'message': f'失敗 - {str(e)}'})
# 未完成        
class accountForget(viewsets.ViewSet):
    def forgot(self, request):
        email = request.data.get('email')
        try:
            existing_account = account.objects.filter(email=email).first()
            if existing_account:
                subject = 'PUYUAN 忘記密碼'
                content = f'您的密碼為:{existing_account.password}'
                send_email(subject, email, content)
                return Response({'status': 0, 'message': '成功'})
        except Exception as e:
            return Response({'status': 1, 'message': f'失敗 - {str(e)}'})
        

class accountRestPassword(viewsets.ViewSet):
    def restpassword(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            existing_account = account.objects.filter(email=email).first()
            if existing_account:
                encrypted_password = make_password(password)
                existing_account.password = encrypted_password
                existing_account.save()
                return Response({'status': 0, 'message': '成功'})
            return Response({'status': 1, 'message': '失敗'})
        except Exception as e:
            return Response({'status': 1, 'message': f'失敗 - {str(e)}'})

class accountRegisterCheck(viewsets.ViewSet):
    def registercheck(self, request):
        email = request.data.get('email')
        try:
            existing_account = account.objects.filter(email=email).first()
            if existing_account:
                return Response({'status': 1, 'message': '電子郵件已存在'})
            return Response({'status': 0, 'message': '成功'})
        except Exception as e:
            return Response({'status': 1, 'message': f'失敗 - {str(e)}'})

class otherNews(viewsets.ViewSet):
    def news(self, request):
        try:
            return Response({'status': 0, 'message': '成功'})
        except Exception as e:
            return Response({'status': 1, 'message': f'失敗 - {str(e)}'})