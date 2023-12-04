from User.models import account
from django.contrib.sessions.models import Session
from django.core.exceptions import SuspiciousOperation
from django.core.mail import EmailMessage

def decode_session_data(token):
    try:
        session = Session.objects.get(session_key=token)
        session_data = session.get_decoded()
        user_id = session_data.get('user_id')
        return user_id
    except Session.DoesNotExist:
        raise SuspiciousOperation("Session 不存在")

def get_token(request):
    try:
        print(request.headers)
        authorization_header = request.META.get('HTTP_AUTHORIZATION')
        if authorization_header:
            parts = authorization_header.split()
            if len(parts) == 2 and parts[0].lower() == 'bearer':
                token = parts[1]
                user_id = decode_session_data(token)
                # user_account = account.objects.get(id=user_id)
                return user_id
    except Exception as e:
        print(e)
        return False

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