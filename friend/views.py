from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# from django.db import IntegrityError
from django.db.models import Q
from .models import *
from .serializers import *
from .basemetadata import *
from users.utils import *

# from django.core.cache import cache
# import secrets


class FriendCodeViewSet(APIView):

    @check_token()
    def get(self, request):
        user_id = request.token_data['user_id']

        # invite_code_num = 3
        # while True:
        #     invite_code = secrets.token_hex(invite_code_num)
        #     try:
        #         Friend.objects.create(
        #             user_id=user_id,
        #             code=invite_code,
        #         )
        #         # cache.set(invite_code, user_id, timeout=60*60*24)
        #         break
        #     except IntegrityError:
        #         invite_code_num += 1
        #         continue
        
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'status': '1', 'message': '用戶不存在'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            print(user.invite_code)
            return Response({'status': '0', 'message': '成功', 'invite_code': user.invite_code}, status=status.HTTP_200_OK)

class FriendSendViewSet(APIView):
    metadata_class = FriendSendMetadata

    @check_token()
    def post(self, request):
        user_id = request.token_data['user_id']
        print(user_id)
        type = request.data.get('type', None)
        invite_code = request.data.get('invite_code', "")
        if invite_code == "" or type is None:
            return Response({'status': '1', 'message': '類型或邀請碼不可為空'}, status=status.HTTP_400_BAD_REQUEST)
        
        friend = User.objects.filter(invite_code=invite_code).first()
        if friend:
            if friend.id == user_id:
                return Response({'status': '1', 'message': '不能邀請自己'}, status=status.HTTP_400_BAD_REQUEST)
            
            invite, _ = Friend.objects.get_or_create(user_id=user_id, friend_id=friend.id, type=type)
            if invite.status == 1:
                return Response({'status': '1', 'message': '已經成為好友'}, status=status.HTTP_400_BAD_REQUEST)
            if invite.status == 2:
                invite.status = 0
                invite.read = 0
                invite.save()
            return Response({'status': '0', 'message': '成功'}, status=status.HTTP_200_OK)
        return Response({'status': '1', 'message': '邀請碼無效'}, status=status.HTTP_400_BAD_REQUEST)
            # try:
            #     invite = Friend.objects.get(user_id=user_id, code=invite_code)
            # except Friend.DoesNotExist:
            #     return Response({'status': '1', 'message': '邀請碼無效'}, status=status.HTTP_400_BAD_REQUEST)
            # else:
            #     if invite.status == 1:
            #         return Response({'status': '1', 'message': '已經成為好友'}, status=status.HTTP_400_BAD_REQUEST)
            #     elif invite.status == 2:
            #         return Response({'status': '1', 'message': '邀請碼無效'}, status=status.HTTP_400_BAD_REQUEST)
                
            #     invite.type = type
            #     invite.save()

        #     return Response({'status': '0', 'message': '成功'}, status=status.HTTP_200_OK)
        # return Response({'status': '1', 'message': '邀請碼無效'}, status=status.HTTP_400_BAD_REQUEST)
    
class FriendRequestViewSet(APIView):
    @check_token()
    def get(self, request):
        user_id = request.token_data['user_id']
        friend_list = Friend.objects.filter(friend_id=user_id, status=0)
        # friend_list = Friend.objects.filter(user_id=user_id, status=0).exclude(type__isnull=True)

        serializer = FriendResultSerializer(friend_list, many=True, api_type='requests')
        print(serializer.data)
        test =   [{
            "id": 1,
            "user_id": 3,
            "relation_id": 4,
            "type": 1,
            "status": 1,
            "read": 1,
            "created_at": "2017-10-30 19:08:26",
            "updated_at": "2017-10-30 19:18:18",
            "relation": {
                "id": 4,
                "name": "",
                "account": "fb_1"
            }
        }]

        return Response({'status': '0', 'message': '成功', 'requests': serializer.data}, status=status.HTTP_200_OK)
    
class FriendResultViewSet(APIView):
    @check_token()
    def get(self, request):
        user_id = request.token_data['user_id']
        friend_list = Friend.objects.filter(user_id=user_id).exclude(status=0)

        serializer = FriendResultSerializer(friend_list, many=True)
        print("===========================")
        print(serializer.data)
        print("===========================")
        test =   [{
            "id": 1,
            "user_id": 3,
            "relation_id": 4,
            "type": 1,
            "status": 1,
            "read": 1,
            "created_at": "2017-10-30 19:08:26",
            "updated_at": "2017-10-30 19:18:18",
            "relation": {
                "id": 4,
                "name": "",
                "account": "fb_1"
            }
        }]

        return Response({'status': '0', 'message': '成功', 'results': serializer.data}, status=status.HTTP_200_OK)
    
class FriendAcceptViewSet(APIView):
    @check_token()
    def get(self, request, inviteid):
        user_id = request.token_data['user_id']
        try:
            invite = Friend.objects.get(pk=inviteid, status=0, friend_id=user_id)
        except Friend.DoesNotExist:
            return Response({'status': '1', 'message': '邀請不存在'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if invite.user_id == user_id:
                return Response({'status': '1', 'message': '不能接受自己的邀請'}, status=status.HTTP_400_BAD_REQUEST)\
                
            # if (
            #     Friend.objects.filter(user_id=user_id, friend_id=invite.user_id, status=1, type=invite.type).exists() or
            #     Friend.objects.filter(user_id=invite.user_id, friend_id=user_id, status=1, type=invite.type).exists()
            # ):
            #     return Response({'status': '1', 'message': '已經成為好友'}, status=status.HTTP_400_BAD_REQUEST
            # )
            
            invite.relation_id = user_id
            # invite.friend_id = user_id
            invite.status = 1
            invite.read = 1
            invite.save()

            reverse_invite_data = invite.__dict__.copy()
            reverse_invite_data.pop('_state')
            reverse_invite_data.pop('id')

            reverse_invite_data.update({
                'user_id': invite.friend_id,
                'friend_id': invite.user_id,
                'relation_id': invite.user_id
            })
            Friend.objects.create(**reverse_invite_data)
            Friend.objects.filter(
                Q(status=0) | Q(status=2),
                type=invite.type,
                user_id=user_id,
                friend_id=invite.user_id
            ).delete()

        return Response({'status': '0', 'message': '成功'}, status=status.HTTP_200_OK)
    
class FriendRejectViewSet(APIView):
    @check_token()
    def get(self, request, inviteid):
        user_id = request.token_data['user_id']
        try:
            invite = Friend.objects.get(pk=inviteid, status=0, friend_id=user_id)
        except Friend.DoesNotExist:
            return Response({'status': '1', 'message': '邀請不存在'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if invite.user_id == user_id:
                return Response({'status': '1', 'message': '不能拒絕自己的邀請'}, status=status.HTTP_400_BAD_REQUEST)
            
            invite.relation_id = user_id
            # invite.friend_id = user_id
            invite.status = 2
            invite.read = 1
            invite.save()

        return Response({'status': '0', 'message': '成功'}, status=status.HTTP_200_OK)
    
class FriendListViewSet(APIView):
    @check_token()
    def get(self, request):
        user_id = request.token_data['user_id']
        friend_list = Friend.objects.filter(user_id=user_id, status=1).only('type', 'friend')
        if friend_list:
            serializers = FriendResultSerializer(friend_list, api_type='list', many=True)
            print(serializers.data)
            return Response({'status': '0', 'message': '成功', 'friends': serializers.data}, status=status.HTTP_200_OK)
        # return Response({'status': '1', 'message': '失敗'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': '0', 'message': '成功', 'friends': []}, status=status.HTTP_200_OK)
    
class FriendRemoveViewSet(APIView):
    @check_token()
    def delete(self, request):
        user_id = request.token_data['user_id']
        friend_id = request.data.get('ids[]', [])
        if friend_id == []:
            return Response({'status': '1', 'message': 'ids[]不可為空'}, status=status.HTTP_400_BAD_REQUEST)
        # if user_id in friend_id:
        #     return Response({'status': '1', 'message': '不能刪除自己'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Friend.objects.filter(user_id=user_id, friend_id__in=friend_id, status=1).delete()
        # Friend.objects.filter(user_id__in=friend_id, friend_id=user_id, status=1).delete()
        
        Friend.objects.filter(
            Q(user_id=user_id, friend_id__in=friend_id) | 
            Q(user_id__in=friend_id, friend_id=user_id), 
            status=1
        ).delete()

        return Response({'status': '0', 'message': '成功'}, status=status.HTTP_200_OK)
        