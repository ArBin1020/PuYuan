
from django.contrib.sessions.models import Session
from django.core.exceptions import SuspiciousOperation
from django.core.mail import EmailMessage
from rest_framework.response import Response

def extract_user_id(view_func):
    def _wrapped_view(request, *args, **kwargs):
        authorization_header = request.META.get('HTTP_AUTHORIZATION')
        if authorization_header:
            parts = authorization_header.split()
            if len(parts) == 2 and parts[0].lower() == 'bearer':
                token = parts[1]
                user_id = decode_session_data(token)
                request.user_id = user_id  # 将user_id添加到请求对象中
            else:
                return Response({'status': 1, 'message': '授权标头格式无效'})
        else:
            return Response({'status': 1, 'message': '缺少授权标头'})

        return view_func(request, *args, **kwargs)

    return _wrapped_view

def decode_session_data(token):
    try:
        session = Session.objects.get(session_key=token)
        session_data = session.get_decoded()
        user_id = session_data.get('user_id')
        return user_id
    except Session.DoesNotExist:
        raise SuspiciousOperation("Session 不存在")

    

def send_email(subject, email, content):
    subject = subject
    message = content
    email_from = 'PUYUAN'
    recipient_list = [email]
    try:
        email = EmailMessage(subject, message, email_from, recipient_list)
        email.send()
    except:
        return False