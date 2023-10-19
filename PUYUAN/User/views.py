
from .models import account, news, share
from .serializers import accountSerializer, OtherSerializer, ShareSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.tokens import default_token_generator

import random
import string

from utils import *

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
                request.session['user_id'] = existing_account.id
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

# complete
class accountResetPassword(viewsets.ViewSet):
    def reset(self, request):
        password = request.data.get('password')
        try:
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            if authorization_header:
                parts = authorization_header.split()
                if len(parts) == 2 and parts[0].lower() == 'bearer':
                    token = parts[1]
                    user_id = decode_session_data(token)
                    if user_id:
                        try:
                            user = account.objects.get(id=user_id)
                            user.password = make_password(password)
                            user.save()
                            return Response({'status': 0, 'message': '密碼已更新'})
                        except account.DoesNotExist:
                            return Response({'status': 1, 'message': '用戶不存在'})
                    return Response({'status': 1, 'message': '失敗'})
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
class Othernews(viewsets.ViewSet):
    def news(self, request):
        try:
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            if authorization_header:
                parts = authorization_header.split()
                if len(parts) == 2 and parts[0].lower() == 'bearer':
                    token = parts[1]
                    user_id = decode_session_data(token)
            latest_news = news.objects.filter(user=user_id).latest('created_at', 'pushed_at', 'updated_at')
            serializer = OtherSerializer(latest_news)
            return Response({'status': 0, 'message': '成功', 'news': serializer.data})
        
        except Exception as e:
            return Response({'status': 1, 'message': f'失敗 - {str(e)}'})


class OtherShare(viewsets.ViewSet):
    def share(self, request):
        try:
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            if authorization_header:
                parts = authorization_header.split()
                if len(parts) == 2 and parts[0].lower() == 'bearer':
                    token = parts[1]
                    user_id = decode_session_data(token)
            data_type = request.data.get('type')
            share_id = request.data.get('id')
            relation_type = request.data.get('relation_type')
            user_account = account.objects.get(id=user_id)

            user_share = share(user=user_account, data_type=data_type, relation_type=relation_type)
            user_share.save()
            
            return Response({'status': 0, 'message': '成功'})
        except account.DoesNotExist:
            return Response({'status': 1, 'message': '失敗'})
        except Exception as e:
            return Response({'status': 1, 'message': f'分享失敗 - {str(e)}'})

    def ViewShare(self, request):
        try:
            
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            if authorization_header:
                parts = authorization_header.split()
                if len(parts) == 2 and parts[0].lower() == 'bearer':
                    token = parts[1]
                    user_id = decode_session_data(token)
                    data_type = request.data.get('type')
                    shares = share.objects.filter(user=user_id,data_type=data_type)

                    # 使用Serializer将数据序列化为JSON
                    serializer = ShareSerializer(shares, many=True)

                    return Response({'status': 0, 'message': '成功', 'records': serializer.data})
                else:
                    return Response({'status': 1, 'message': '授权标头格式无效'})
            else:
                return Response({'status': 1, 'message': '缺少授权标头'})
        except Exception as e:
            return Response({'status': 1, 'message': f'失敗 - {str(e)})'})
