from django.contrib.sessions.models import Session
from django.core.exceptions import SuspiciousOperation

def decode_session_data(token):
    try:
        session = Session.objects.get(session_key=token)
        session_data = session.get_decoded()
        user_id = session_data.get('user_id')
        return user_id
    except Session.DoesNotExist:
        raise SuspiciousOperation("Session 不存在")

def get_user_id(request):
    try:
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