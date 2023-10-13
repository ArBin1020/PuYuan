from .models import account
from .serializers import accountSerializer
# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response

class accountViewSet(viewsets.ModelViewSet):
    queryset = account.objects.all()
    serializer_class = accountSerializer
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = account.objects.create_user(email=email, password=password)
            return Response({'status': 0,'message': '成功'})
        except: 
            return Response({'status': 1, 'message': '失敗'})