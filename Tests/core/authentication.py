# authentication.py
from firebase_admin import auth
from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend

class FirebaseAuthenticationBackend(BaseBackend):
    def authenticate(self, request, uid=None):
        if uid is None:
            return None
        try:
            user = User.objects.get(username=uid)
        except User.DoesNotExist:
            user = User(username=uid)
            user.save()
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
