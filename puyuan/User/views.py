import random

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from datetime import datetime
from django.core.mail import EmailMessage
from utils import *

from User.models import *
from Body.models import *
from Friend.models import *

# Create your views here.

class Register(viewsets.ViewSet):
    def create(self, request):
        try:
            email = request.data['email']

            if User_Info.objects.filter(email=email).exists():
                return Response({'status':'1','message': 'Email already exists'}, status=400)
            
            # create user
            User_Info.objects.create_user(
                email=email,
                password=make_password(request.data['password']),
                invite_code=random.randint(100000, 999999)
            )

            # create default data
            user_id = User_Info.objects.get(email=email).id
            
            User_Default.objects.create(user_id=user_id)
            User_Setting.objects.create(user_id=user_id)
            User_VIP.objects.create(user_id=user_id)
            User_Medical.objects.create(user_id=user_id)
            User_A1c.objects.create(user_id=user_id)
            Friend.objects.create(user_id=user_id)
            News_Share.objects.create(user_id=user_id)
            print(f'User ID: {user_id} created,Ivite Code: {User_Info.objects.get(email=email).invite_code} ')
            return Response({'status':'0','message': 'success'}, status=200)
        
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
        
class Login(viewsets.ViewSet):
    def create(self, request):
        try:
            email = request.data['email']
            password = request.data['password']

            if not User_Info.objects.filter(email=email).exists():
                return Response({'status':'1','message': 'Email does not exist'}, status=400)
            
            user = User_Info.objects.get(email=email)
            if not user.check_password(password):
                return Response({'status':'1','message': 'Password error'}, status=400)
            
            if user.is_verify == False:
                return Response({'status':'2','message': 'Account not verified'}, status=400)

            request.session["user_id"] = user.id
            request.session.save()
            user.last_login = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            user.login_times += 1
            user.save()

            return Response({'status':'0','message': 'success'}, status=200)
        
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
        
class Send_Verify_Code(viewsets.ViewSet):
    def create(self, request):
        try:
            email = request.data['email']
            verify_code = random.randint(100000, 999999)

            if User_Info.objects.filter(email=email).exists():
                subject = 'PUYUAN Verification Code'
                message = f'Your verification code is {verify_code}'
                email_from = 'PUYUAN'
                recipient_list = [email]
                email = EmailMessage(subject, message, email_from, recipient_list)
                email.send()
                User_Info.objects.filter(email=email).update(verify_code=verify_code)
                return Response({'status':'0','message': 'success'}, status=200)
            return Response({'status':'1','message': 'Send Verify Code Fail'}, status=400)
        
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)

class Check_Verify_Code(viewsets.ViewSet):
    def create(self, request):
        try:
            email = request.data['email']
            verify_code = request.data['code']

            if User_Info.objects.filter(email=email).exists():
                user = User_Info.objects.get(email=email)
                if user.verify_code == verify_code:
                    User_Info.objects.filter(email=email).update(is_verify=True)
                    return Response({'status':'0','message': 'success'}, status=200)
                return Response({'status':'1','message': 'Verify Code Error'}, status=400)
            return Response({'status':'1','message': 'Verify Code Error'}, status=400)
        
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
        
class Forget_Password(viewsets.ViewSet):
    def create(self, request):
        try:
            email = request.data['email']
            temp_password = random.randint(100000, 999999)
            if User_Info.objects.filter(email=email).exists():
                subject = 'PUYUAN Temporary Password'
                message = f'Your temporary password is {temp_password}'
                email_from = 'PUYUAN'
                recipient_list = [email]
                email = EmailMessage(subject, message, email_from, recipient_list)
                email.send()

                User_Info.objects.filter(email=email).update(
                    password=make_password(temp_password),
                    must_change_password=1,
                    updated_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                )

                return Response({'status':'0','message': 'success'}, status=200)
            return Response({'status':'1','message': 'Email does not exist'}, status=400)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
        
class Reset_Password(viewsets.ViewSet):
    def create(self, request):
        try:
            user_id = get_user_id(request)
            password = request.data['password']
            if user_id:
                User_Info.objects.filter(id=user_id).update(
                    password=make_password(password),
                    must_change_password=0,
                    updated_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                )
                return Response({'status':'0','message': 'success'}, status=200)
            return Response({'status':'1','message': 'Reset Fail'}, status=400)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
        
class Register_Check(viewsets.ViewSet):
    def create(self, request):
        try:
            email = request.data['email']
            if User_Info.objects.filter(email=email).exists():
                return Response({'status':'1','message': 'Email already exists'}, status=400)
            return Response({'status':'0','message': 'success'}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
        
class News(viewsets.ViewSet):
    def create(self, request):
        try:
            news = News_Share.objects.filter(user_id=get_user_id(request)).order_by('-id')
            data = []
            for new in news:
                data.append({
                    'id': new.id,
                    'member_id': new.member_id,
                    'group': new.group,
                    'title': new.title,
                    'message': new.message,
                    'data_type': new.data_type,
                    'relation_type': new.relation_type,
                    'pushed_at': new.pushed_at,
                    'created_at': new.created_at,
                    'updated_at': new.updated_at,
                })
            return Response({'status':'0','message': 'success','news':data}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)

class Share(viewsets.ViewSet):
    def create(self, request):
        try:
            user_id = get_user_id(request)
            member_id = request.data['member_id']
            group = request.data['group']
            title = request.data['title']
            message = request.data['message']
            data_type = request.data['data_type']
            relation_type = request.data['relation_type']
            pushed_at = request.data['pushed_at']
            created_at = request.data['created_at']
            updated_at = request.data['updated_at']

            News_Share.objects.create(
                user_id=user_id,
                member_id=member_id,
                group=group,
                title=title,
                message=message,
                data_type=data_type,
                relation_type=relation_type,
                pushed_at=pushed_at,
                created_at=created_at,
                updated_at=updated_at,
            )
            return Response({'status':'0','message': 'success'}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)