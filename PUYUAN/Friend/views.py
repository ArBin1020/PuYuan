from django.shortcuts import render
from rest_framework import viewsets
from .models import Friend
from utils import *
from User.models import account
from rest_framework.response import Response
# Create your views here.
class Friend_Get_Code(viewsets.ViewSet):
    def get_code(self, request):
        try:
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            if authorization_header:
                parts = authorization_header.split()
                if len(parts) == 2 and parts[0].lower() == 'bearer':
                    token = parts[1]
                    user_id = decode_session_data(token)
                    user_account = account.objects.get(id=user_id)
                    
        except Exception as e:
            return Response({'status': 1, 'message': f'失敗 - {str(e)}'})

class Friend_Get_List(viewsets.ViewSet):
    def get_list(self, request):
        authorization_header = request.META.get('HTTP_AUTHORIZATION')
        if authorization_header:
            parts = authorization_header.split()
            if len(parts) == 2 and parts[0].lower() == 'bearer':
                token = parts[1]
                user_id = decode_session_data(token)
                user_account = account.objects.get(id=user_id)

class Friend_Get_Request(viewsets.ViewSet):
    def get_request(self, request):
        authorization_header = request.META.get('HTTP_AUTHORIZATION')
        if authorization_header:
            parts = authorization_header.split()
            if len(parts) == 2 and parts[0].lower() == 'bearer':
                token = parts[1]
                user_id = decode_session_data(token)
                user_account = account.objects.get(id=user_id)


class Friend_Send(viewsets.ViewSet):
    def send(self, request):
        authorization_header = request.META.get('HTTP_AUTHORIZATION')
        if authorization_header:
            parts = authorization_header.split()
            if len(parts) == 2 and parts[0].lower() == 'bearer':
                token = parts[1]
                user_id = decode_session_data(token)
                user_account = account.objects.get(id=user_id)


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
                user_account = account.objects.get(id=user_id`