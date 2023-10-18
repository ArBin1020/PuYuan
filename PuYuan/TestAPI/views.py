from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
import random
import string

# Create your views here.

from django.utils import timezone
from rest_framework import status
from User.models import news
from .serializers import NewsSerializer

class CreateRandomNews(viewsets.ViewSet):
    def createrandomnews(self, request):
        # 創建一個新的 news 實例
        new_news = news(
            member_id=''.join(random.choice(string.digits) for _ in range(3)), 
            group=''.join(random.choice(string.digits) for _ in range(3)),     
            title=''.join(random.choice(string.ascii_letters) for _ in range(5)),  
            message=''.join(random.choice(string.ascii_letters) for _ in range(5)),
            pushed_at=timezone.now().strftime("%Y-%m-%d %H:%M:%S"),  
            created_at=timezone.now().strftime("%Y-%m-%d %H:%M:%S"), 
            updated_at=timezone.now().strftime("%Y-%m-%d %H:%M:%S")  
        )
        
        # 儲存這個 news 物件到資料庫
        new_news.save()
        
        # 使用序列化器將新增的 news 物件序列化成 JSON 格式
        serializer = NewsSerializer(new_news)
        
        # 返回成功的回應，包括新建的 news 資料
        return Response(serializer.data, status=status.HTTP_201_CREATED)
