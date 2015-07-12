from django.conf import settings
from django.contrib.auth import get_user_model
from .models import Member

class MyBBMemberBackend(object):
    """Backend compatible with MyBB"""
    def authenticate(self, username=None, password=None):
        try:
            member = Member.objects.get(email=username)
            if member.check_password(password):
                Exception(member)
                return member.get_django_user_model()
        except Member.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None
