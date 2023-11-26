from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from utils import *
from User.models import *
from Body.models import *
from rest_framework.response import Response
import json
from datetime import datetime
# Create your views here.


class Friend_Get_Code(viewsets.ViewSet):
    def get_code(self, request):
        try:
            user_id = get_token(request)
            invite = UserProfile.objects.get(user_id=user_id)
            print(invite.invite_code)
            return Response({'status': "0", 'message': '成功', 'invite_code': str(invite.invite_code)})
        except Exception as e:
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'},status=400)

class Friend_Get_List(viewsets.ViewSet):
    def get_list(self, request):
        try:
            user_id = get_token(request)
            friend_list = Friend.objects.filter(user_id=user_id)
            print(friend_list)
            response = []
            for f in friend_list:
                # friend = account.objects.get(id=f.friend_id)
                response.append({
                    'id': 1,
                    'name': "friend.name",
                    'relation_type': 1
                })
            print(response)
            return Response({'status': "0", 'message': '成功', 'friends': response})
        except Exception as e:
            print(e)
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'},status=400)
        # if friend_list:


class Friend_Get_Request(viewsets.ViewSet):
    def get_request(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))
            friend = Friend.objects.filter(relation_id=user_account.id)
            print(user_account.id)
            user = UserProfile.objects.get(user=user_account)
            response = []
            for f in friend:
                if f.status == 1 or (f.id == user_account.id):
                    continue
                response.append({
                    'id': user_account.id,
                    'user_id': user_account.id,
                    'relation_id': f.relation_id,
                    'type': f.data_type,
                    'status': f.status,
                    'read': f.read,
                    'created_at': f.created_at,
                    'updated_at': f.updated_at,
                    'user' : {
                        'id' : user_account.id,
                        'name': user.name,
                        'account': 'fb_'+str(f.id)
                    }
                })
                print('====================')
                print(response)
            return Response({'status': "0", 'message': '成功', 'requests': response})
        except Exception as e:
            print(e)
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'},status=400)
        
class Friend_Send(viewsets.ViewSet):
    def send(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))
            data_type = request.data.get('type')
            invite_code = request.data.get('invite_code')

            user = UserProfile.objects.get(invite_code=invite_code).user_id
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if Friend.objects.filter(user=user,status=1):
                return Response({'status': "2", 'message': '已經是好友'})
            if UserProfile.objects.filter(invite_code=invite_code):
                Friend.objects.create(user=user_account,
                                      relation_id=user,
                                      data_type=data_type,
                                      created_at=time,
                                        updated_at=time
                                      )
            return Response({'status': "0", 'message': '成功'})
        except Exception as e:
            print(e)
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'},status=400)
        


class Friend_Accept(viewsets.ViewSet):
    def accept(self, request, inviteld):
        try:

            user_account = account.objects.get(id=get_token(request))
            inviteld = UserProfile.objects.get(user=user_account).invite_code
            print(inviteld)
            if UserProfile.objects.filter(user=user_account, invite_code=inviteld):
                Friend.objects.filter(relation_id=user_account.id).update(
                    status=1,read=1,
                    updated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )
                return Response({'status': "0", 'message': '成功'})
        except Exception as e:
            print(e)
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'},status=400)

class Friend_Refuse(viewsets.ViewSet):
    def refuse(self, request, inviteld):
        try:
            user_account = account.objects.get(id=get_token(request))
            inviteld = UserProfile.objects.get(user=user_account).invite_code
            if UserProfile.objects.filter(user=user_account, invite_code=inviteld):
                Friend.objects.filter(relation_id=user_account.id).update(
                    status=2,read=1,
                    updated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )
                return Response({'status': "0", 'message': '成功'})
        except Exception as e:
            print(e)
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'},status=400)
        
class Friend_Remove(viewsets.ViewSet):
    def remove(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))
            del_id = json.loads(request.body)['ids[]']
            
        except Exception as e:
            print(e)
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'},status=400)


class Friend_Get_Results(viewsets.ViewSet):
    def get_results(self, request):
        try:
            user_account = account.objects.get(id=get_token(request))
            friends = Friend.objects.filter(user=user_account)
            response = []
            print(friends)
            for f in friends:
                if f.status == 0:
                    continue
                else:
                    response.append({
                        'id': f.id,
                        'user_id': f.id,
                        'relation_id': f.relation_id,
                        'type': f.data_type,
                        'status': f.status,
                        'read': f.read,
                        'created_at': f.created_at,
                        'updated_at': f.updated_at,
                        'relation' : {
                            'id' : f.relation_id,
                            'name': user_account.username,
                            'account': user_account.email
                        }
                    })

            print(response)
            return Response({'status': "0", 'message': '成功', 'results': response})
        except Exception as e:
            print(e)
            return Response({'status': "1", 'message': f'失敗 - {str(e)}'},status=400)