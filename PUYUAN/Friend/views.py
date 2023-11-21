from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from utils import *
from User.models import account
from rest_framework.response import Response
# Create your views here.


class Friend_Get_Code(viewsets.ViewSet):
    def get_code(self, request):
        try:
            user_id = get_token(request)
            invite = Invite.objects.get(user_id=user_id)
            return Response({'status': "0", 'message': '成功', 'invite_code': invite.code})
        except Exception as e:
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'})

class Friend_Get_List(viewsets.ViewSet):
    def get_list(self, request):
        try:
            user_id = get_token(request)
            friend_list = Friend.objects.filter(user_id=user_id, status=1).only('friend','data_type')
            response = []
            for f in friend_list:
                friend = account.objects.get(id=f.friend_id)
                response.append({
                    'id': 1,
                    'name': "friend.name",
                    # 'account': friend.account,
                    # 'type': f.data_type,
                    'relation_type': 1
                })
            return Response({'status': "0", 'message': '成功', 'friends': response})
        except Exception as e:
            print(e)
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'},status=400)
        # if friend_list:


class Friend_Get_Request(viewsets.ViewSet):
    def get_request(self, request):
        try:
            user_id =  get_token(request)
            friend = Friend.objects.filter(friend_id=user_id, status=0)
            response = []
            for f in friend:
                response.append({
                    'id': f.id,
                    'user_id': f.user_id,
                    'relation_id': f.relation_id,
                    'type': f.data_type,
                    'status': f.status,
                    'read': f.read,
                    'created_at': f.created_at,
                    'updated_at': f.updated_at,
                    'relation' : {
                        'id' : 2,
                        'name': '',
                        'account': 'fb_2'
                    }
                })
            return Response({'status': "0", 'message': '成功', 'requests': response})
        except Exception as e:
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'})
        
class Friend_Send(viewsets.ViewSet):
    def send(self, request):
        try:
            user_id = get_token(request)

        except Exception as e:
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'})
        


class Friend_Accept(viewsets.ViewSet):
    def accept(self, request):
        authorization_header = request.META.get('HTTP_AUTHORIZATION')
        if authorization_header:
            parts = authorization_header.split()
            if len(parts) == 2 and parts[0].lower() == 'bearer':
                token = parts[1]
                user_id = decode_session_data(token)
                user_account = account.objects.get(id=user_id)


class Friend_Refuse(viewsets.ViewSet):
    def refuse(self, request):
        authorization_header = request.META.get('HTTP_AUTHORIZATION')
        if authorization_header:
            parts = authorization_header.split()
            if len(parts) == 2 and parts[0].lower() == 'bearer':
                token = parts[1]
                user_id = decode_session_data(token)
                user_account = account.objects.get(id=user_id)

class Friend_Remove(viewsets.ViewSet):
    def remove(self, request):
        authorization_header = request.META.get('HTTP_AUTHORIZATION')
        if authorization_header:
            parts = authorization_header.split()
            if len(parts) == 2 and parts[0].lower() == 'bearer':
                token = parts[1]
                user_id = decode_session_data(token)
                user_account = account.objects.get(id=user_id)


class Friend_Get_Results(viewsets.ViewSet):
    def get_results(self, request):
        authorization_header = request.META.get('HTTP_AUTHORIZATION')
        if authorization_header:
            parts = authorization_header.split()
            if len(parts) == 2 and parts[0].lower() == 'bearer':
                token = parts[1]
                user_id = decode_session_data(token)
                user_account = account.objects.get(id=user_id)
