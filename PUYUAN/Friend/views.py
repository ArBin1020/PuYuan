from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
class FriendGetCode(viewsets.ViewSet):
    def getcode(self, request):
        pass


class FriendGetList(viewsets.ViewSet):
    def getlist(self, request):
        pass

class FriendGetRequest(viewsets.ViewSet):
    def getrequest(self, request):
        pass

class FriendSend(viewsets.ViewSet):
    def send(self, request):
        pass

