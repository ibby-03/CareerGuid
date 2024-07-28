# middleware.py
from django.utils.deprecation import MiddlewareMixin
from firebase_admin import auth
from django.contrib.auth import get_user_model

class FirebaseAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        id_token = request.headers.get('Authorization')
        if id_token:
            try:
                decoded_token = auth.verify_id_token(id_token)
                uid = decoded_token['uid']
                User = get_user_model()
                user, created = User.objects.get_or_create(username=uid)
                request.user = user
            except Exception:
                pass
