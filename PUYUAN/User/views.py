
from .models import *
from Body.models import *
from Friend.models import *
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
        try:
            encrypted_password = make_password(password)
            serializer = accountSerializer(data=request.data)
            if serializer.is_valid():
                user = account(email=email, password=encrypted_password)
                user.save()
                user_id = account.objects.filter(email=email).first().id
                print(user_id)
                UserProfile.objects.create(user_id=user_id, name="USER_"+str(user_id), invite_code=random.randint(100000, 999999))
                UserDefault.objects.create(user_id=user_id)
                UserSetting.objects.create(user_id=user_id)
                vip.objects.create(user_id=user_id)
                Medical.objects.create(user_id=user_id)
                Friend.objects.create(user_id=user_id, friend_id=user_id, relation_id=1, data_type=1, status=1, read=1)
                return Response({'status': "0", 'message': '成功'})
            return Response({'status': "1", 'message': '失敗 - {}'.format(serializer.errors)})
                
        except Exception as e:
            print(e)
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'}, status=400)
        
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
                    return Response({'status': "2", 'message': '信箱未驗證', 'token': ""})
                return Response({'status': "0", 'message': '成功', 'token': session_key})
            else:
                return Response({'status': "1", 'message': '電子郵件或密碼錯誤', 'token': ""})
        except Exception as e:
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'}, status=400)

# complete
class accountSendCode(viewsets.ViewSet):
    def sendcode(self, request):
        email = request.data.get('email')
        try:
            existing_account = account.objects.filter(email=email).first()

            if existing_account:
                code = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
                print(code)
                subject = 'PUYUAN 驗證碼'
                content = f'您的驗證碼為:{code}'
                send_email(subject, email, content)
                existing_account.code = code
                existing_account.save()
                return Response({'status': "0", 'message': '成功'})
            return Response({'status': "1", 'message': '失敗'})
        except Exception as e:
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'}, status=400)

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
                    return Response({'status': "0", 'message': '成功'})
                else:
                    return Response({'status': "1", 'message': '驗證碼錯誤'})
            return Response({'status': "0", 'message': '失敗'})
        except Exception as e:
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'}, status=400)

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
                print(token)
                return Response({'status': "0", 'message': '成功'})
            return Response({'status': "1", 'message': '失敗'})
        except Exception as e:
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'}, status=400)

# complete
class accountResetPassword(viewsets.ViewSet):
    def reset(self, request):
        password = request.data.get('password')
        try:
            user_id = get_token(request)
            if user_id:
                try:
                    user = account.objects.get(id=user_id)
                    user.password = make_password(password)
                    user.save()
                    return Response({'status': "0", 'message': '密碼已更新'})
                except account.DoesNotExist:
                    return Response({'status': "1", 'message': '用戶不存在'})
            return Response({'status': "1", 'message': '失敗'})
        except Exception as e:
            return Response({'status': "1", 'message': '失敗 - {}'.format(str(e))})


# complete
class accountRegisterCheck(viewsets.ViewSet):
    def registercheck(self, request):
        try:
            existing_account = account.objects.filter(email=request.data.get('email')).first()
            if existing_account:
                return Response({'status': "1", 'message': '失敗'})
            return Response({'status': "0", 'message': '成功'})
        except Exception as e:
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'}, status=400)
        
# complete
class Othernews(viewsets.ViewSet):
    def news(self, request):
        try:

            latest_news = news.objects.filter(user=get_token(request)).latest('created_at', 'pushed_at', 'updated_at')
            print(latest_news)

            response = {
                "id": latest_news.id,
                "member_id": latest_news.member_id,
                "group": latest_news.group,
                "title": latest_news.title,
                "message": latest_news.message,
                "pushed_at": latest_news.pushed_at,
                "created_at": latest_news.created_at,
                "updated_at": latest_news.updated_at
            }

            return Response({'status': "0", 'message': '成功', 'news': [response]})
        except Exception as e:
            print(e)
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'}, status=400)


class OtherShare(viewsets.ViewSet):
    def share(self, request):
        try:
            data_type = request.data.get('type')
            share_id = request.data.get('id')
            relation_type = request.data.get('relation_type')
            user_account = account.objects.get(id=get_token(request))

            user_share = share(user=user_account, data_type=data_type, relation_type=relation_type)
            user_share.save()
            
            return Response({'status': "0", 'message': '成功'})
        except account.DoesNotExist:
            return Response({'status': "1", 'message': '失敗'})
        except Exception as e:
            return Response({'status': "1", 'message': f'分享失敗 - {str(e)}'}, status=400)

    def ViewShare(self, request,relation_type):
        try:
            user_id = get_token(request)
            shares = share.objects.filter(user=user_id, relation_type=relation_type)
            data = {
                "id": "1,"
            }
            # data = []
            # for share_check in shares:
            #     if share_check.data_type == 0:
            #         bloodpressure = BloodPressure.objects.filter(user=user_id)
            #         r = {
            #                 "id": user_id,
            #                 "user_id": user_id,
            #                 "weight": float(bloodpressure.weight),
            #                 "body_fat": float(bloodpressure.body_fat),
            #                 "bmi": float(bloodpressure.bmi),
            #                 "recorded_at": recorded_at,
            #                 "created_at": created_at,
            #                 "type": 1,
            #                 "user": {
            #                     "id": user_pro.UUID,
            #                     "name": user.name,
            #                     "account": user.email,
            #                     "email": user.email,
            #                     "phone": user.phone,
            #                     "fb_id": user_pro.fb_id,
            #                     "status": user.status,
            #                     "group": user.group,
            #                     "birthday": user.birthday,
            #                     "height": user.height,
            #                     "gender": user.gender,
            #                     "verified": user.verified,
            #                     "privacy_policy": user.privacy_policy,
            #                     "must_change_password": user.must_change_password,
            #                     "badge": user.badge,
            #                     "created_at": created_at_userfile,
            #                     "updated_at": updated_at_userfile
            #                 }
            #             }
            #     elif share_check.data_type == 1:
            #         data.append(share_check)
            #     elif share_check.data_type == 2:
            #         data.append(share_check)
            #     elif share_check.data_type == 3:
            #         data.append(share_check)
            
            return Response({'status': "0", 'message': '成功', 'records': []})
        except Exception as e:
            print(e)
            return Response({'status': "1", 'message': f'失敗 - {str(e)})'}, status=400)
