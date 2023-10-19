from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
import random
import string

# Create your views here.

from django.utils import timezone
from rest_framework import status
from User.models import news, account
from .serializers import NewsSerializer
from utils import *
class CreateRandomNews(viewsets.ViewSet):
    def createrandomnews(self, request):
        try:
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            if authorization_header:
                parts = authorization_header.split()
                if len(parts) == 2 and parts[0].lower() == 'bearer':
                    token = parts[1]
                    user_id = decode_session_data(token)
                    if user_id:
                        user = account.objects.get(id=user_id)
                    else:
                        return Response({'status': 1, 'message': '未找到用户ID。'})
                else:
                    return Response({'status': 1, 'message': '未提供授权头。'})

            # 創建一個新的 news 實例
            new_news = news(
                user=user,
                member_id=''.join(random.choice(string.digits) for _ in range(3)),
                group=''.join(random.choice(string.digits) for _ in range(3)),
                title=''.join(random.choice(string.ascii_letters) for _ in range(5)),
                message=''.join(random.choice(string.ascii_letters) for _ in range(5)),
                pushed_at=timezone.now(),
                created_at=timezone.now(),
                updated_at=timezone.now()
            )

            # 儲存這個 news 物件到資料庫
            new_news.save()

            # 使用序列化器將新增的 news 物件序列化成 JSON 格式
            serializer = NewsSerializer(new_news)

            # 返回成功的回應，包括新建的 news 資料
            return Response({'status': 0, 'message': '成功', 'data': serializer.data})

        except SuspiciousOperation as e:
            return Response({'status': 1, 'message': '失敗 - {}'.format(str(e))})



