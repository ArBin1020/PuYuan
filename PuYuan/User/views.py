
from .models import account, news
from .serializers import accountSerializer, OtherSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.sessions.middleware import SessionMiddleware
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sessions.models import Session
import random
import string

from django.contrib.sessions.models import Session
from django.contrib.auth import get_user_model
from django.core.exceptions import SuspiciousOperation
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
# complete
class accountRegister(viewsets.ViewSet):
    def register(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        username = request.data.get('username')
        try:
            encrypted_password = make_password(password)
            serializer = accountSerializer(data=request.data)
            if serializer.is_valid():
                user = account(username=username, email=email, password=encrypted_password)
                user.save()
                return Response({'status': 0, 'message': '成功'})
            return Response({'status': 1, 'message': '失敗 - {}'.format(serializer.errors)})
                
        except Exception as e:
            return Response({'status': 1, 'message': f'失敗 - {str(e)}'})
        
# complete
class accountLogin(viewsets.ViewSet):
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            existing_account = account.objects.filter(email=email).first()
            if existing_account and check_password(password, existing_account.password):
                request.session.flush()
                request.session['user_id'] = existing_account.email
                request.session.save()
                session_key = request.session.session_key

                if existing_account.verify == False:
                    return Response({'status': 2, 'message': '信箱未驗證'})
                return Response({'status': 0, 'message': '成功', 'token': session_key})
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
                code = ''.join(random.choice(string.ascii_letters) for _ in range(5))
                subject = 'PUYUAN 驗證碼'
                content = f'您的驗證碼為:{code}'
                send_email(subject, email, content)
                existing_account.code = code
                existing_account.save()
                return Response({'status': 0, 'message': '成功'})
            return Response({'status': 1, 'message': '失敗'})
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
                    existing_account.verify = True
                    existing_account.save()
                    return Response({'status': 0, 'message': '成功'})
                else:
                    return Response({'status': 1, 'message': '驗證碼錯誤'})
            return Response({'status': 0, 'message': '失敗'})
        except Exception as e:
            return Response({'status': 1, 'message': f'失敗 - {str(e)}'})

# complete
class accountForget(viewsets.ViewSet):
    def forgot(self, request):
        email = request.data.get('email')
        try:
            existing_account = account.objects.filter(email=email).first()
            if existing_account:
                token = default_token_generator.make_token(existing_account)
                subject = 'PUYUAN 忘記密碼'
                content = f'您的用戶token為:{token}'
                send_email(subject, email, content)
                return Response({'status': 0, 'message': '成功'})
            return Response({'status': 1, 'message': '失敗'})
        except Exception as e:
            return Response({'status': 1, 'message': f'失敗 - {str(e)}'})

# 還沒做
class accountResetPassword(viewsets.ViewSet):
    def reset(self, request):
        password = request.data.get('password')
        try:
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            if authorization_header:
                print(authorization_header)
                parts = authorization_header.split()
                if len(parts) == 2 and parts[0].lower() == 'bearer':
                    token = parts[1]
                    user_or_session_data = decode_session_data(token)
            print(token)
            print(user_or_session_data)

            return Response({'status': 1, 'message': '失敗'})
        except Exception as e:
            return Response({'status': 1, 'message': '失敗 - {}'.format(str(e))})

# complete
class accountRegisterCheck(viewsets.ViewSet):
    def registercheck(self, request):
        email = request.data.get('email')
        try:
            existing_account = account.objects.filter(email=email).first()
            if existing_account and existing_account.verify == 1:
                return Response({'status': 0, 'message': '成功'})
            return Response({'status': 1, 'message': '失敗'})
        except Exception as e:
            return Response({'status': 1, 'message': f'失敗 - {str(e)}'})
        
# complete
class OtherShare(viewsets.ViewSet):
    def news(self, request):
        try:            
            latest_news = news.objects.latest('created_at', 'pushed_at', 'updated_at')
            serializer = OtherSerializer(latest_news)
            return Response({'status': 0, 'message': '成功', 'news': serializer.data})
        
        except Exception as e:
            return Response({'status': 1, 'message': f'失敗 - {str(e)}'})
        


def decode_session_data(token):
    try:
        session = Session.objects.get(session_key=token)
        # 检查 session 是否已过期
        
        # 获取 session 数据
        session_data = session.get_decoded()
        
        # 假设您存储了用户的 ID 在会话数据中
        user_id = session_data.get('user_id')
        
        # 使用用户 ID 获取用户对象
        User = get_user_model()
        user = User.objects.get(pk=user_id)
        
        # 返回用户对象或会话数据，或二者组合
        return user  # 或者 return session_data
    except Session.DoesNotExist:
        raise SuspiciousOperation("Session 不存在")