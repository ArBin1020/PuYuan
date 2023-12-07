import json
# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from utils import *

from User.models import *
from Body.models import *
from Friend.models import *

class Code(viewsets.ViewSet):
    def list(self, request):
        user_id = get_user_id(request)
        invite_code = User_Info.objects.get(id=user_id).invite_code
        return Response({'status':'0','message': 'success','invite_code':invite_code}, status=200)
    
class List(viewsets.ViewSet):
    def list(self, request):
        try:
            user_id = get_user_id(request)
            friend_list = []
            friends = Friend.objects.filter(user_id=user_id)
            
            for friend in friends:
                friend_list.append({
                    'id':friend.id,
                    'name':friend.name,
                    'relation_type':friend.relation_type,
                })

            return Response({'status':'0','message': 'success','friends':friend_list}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
        
class Requests(viewsets.ViewSet):
    def list(self, request):
        try:
            user_id = get_user_id(request)
            response = []
            requests = Friend.objects.filter(relation_id=user_id,status=0).all()
            for friend_request in requests:
                user_info = User_Info.objects.get(id=friend_request.user_id)
                response.append({
                    'id':friend_request.id,
                    'user_id':friend_request.user_id,
                    'relation_id':friend_request.relation_id,
                    'type':request.relation_type,
                    'status':request.status,
                    'read':request.read,
                    'created_at':request.created_at,
                    'updated_at':request.updated_at,
                    'user':{
                        'id':user_info.user_id,
                        'name':user_info.name,
                        'account':user_info.account,
                    }
                })
            return Response({'status':'0','message': 'success','requests':response}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
        

class Send(viewsets.ViewSet):
    def create(self, request):
        try:
            user_id = get_user_id(request)
            data_type = request.data['type']
            invite_code = request.data['invite_code']
            # 取得要加的朋友的資料
            friend = User_Info.objects.get(invite_code=invite_code)
            user_id_instance = User_Info.objects.get(id=user_id)
            # 檢查是否已經有加過
            if Friend.objects.filter(user_id=user_id,relation_id=friend.id,status=1):
                return Response({'status':'2','message': 'already added'}, status=400)
            Friend.objects.create(
                user_id=user_id_instance,
                relation_id=friend.id,
                relation_type=data_type,
                read=0,
            )
            return Response({'status':'0','message': 'success'}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)

class Accept(viewsets.ViewSet):
    def list(self, request, inviteld):
        try:
            user_id = get_user_id(request)
            if Friend.objects.filter(id=inviteld,relation_id=user_id,status=0).exists():
                Friend.objects.filter(id=inviteld).update(status=1,
                                                          read=1,
                                                          updated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                return Response({'status':'0','message': 'success'}, status=200)
            
            return Response({'status':'1','message': 'error'}, status=400)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)

class Refuse(viewsets.ViewSet):
    def list(self, request, inviteld):
        try:
            user_id = get_user_id(request)
            if Friend.objects.filter(id=inviteld,relation_id=user_id,status=0).exists():
                Friend.objects.filter(id=inviteld).update(status=2,
                                                          read=1,
                                                          updated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                return Response({'status':'0','message': 'success'}, status=200)
            return Response({'status':'1','message': 'error'}, status=400)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
    
class Friend_Remove(viewsets.ViewSet):
    def remove(self, request):
        try:
            user_id = get_user_id(request)
            ids = request.data.get('ids[]')

            for rm_id in ids:
                if Friend.objects.filter(id=user_id, relation_id=rm_id, status=1):
                    Friend.objects.filter(id=user_id, relation_id=rm_id, status=1).delete()
                elif Friend.objects.filter(id=rm_id, relation_id=user_id, status=1):
                    Friend.objects.filter(id=rm_id, relation_id=user_id, status=1).delete()
                else:
                    return Response({'status':'1','message': 'error'}, status=400)
            return Response({'status':'0','message': 'success'}, status=200)
        except Exception as e:
            print(e)
            return Response({'status':'1','message': 'error'}, status=400)
        
class Friend_Results(viewsets.ViewSet):
    def list(self, request):
        try:
            user_id = get_user_id(request)
            response = []
            friend_list = Friend.objects.filter(user_id=user_id)
            for friend in friend_list:
                if friend.relation_id == 0:
                    continue
                friend_info = User_Info.objects.get(id=friend.relation_id)
                friend_info_instance = User_Info.objects.get(id=friend.user_id)
                response.append({
                    'id': friend.id,
                    'user_id': friend.user_id,
                    'relation_id': friend.relation_id,
                    'type': friend.relation_type,
                    'status': friend.status,
                    'read': friend.read,
                    'created_at': friend.created_at,
                    'updated_at': friend.updated_at,
                    'relation': {
                        'id': friend_info_instance.id,
                        'name': friend_info.username,
                        'account': friend_info.account,
                    }
                })
            return Response({'status': '0', 'message': '成功', 'results': response}, status=200)
        except Exception as e:
            print(e)
            return Response({'status': '1', 'message': '錯誤'}, status=400)
