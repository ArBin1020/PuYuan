
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