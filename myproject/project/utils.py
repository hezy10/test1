from django.contrib.auth.backends import ModelBackend
from .models import User
import re

# 返回token，username,phone,id
def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'username':user.username,
        'phone':user.phone,
        'name_id':user.id
    }

# 重写登录方法
class MyAuthLoginBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print('************重写登录方法**************')
        try:
            if re.match('^1[3,5,6,7,8]\d{9}$',username):
                user = User.objects.get(phone=username)
            elif re.match('^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$',username):
                user = User.objects.get(email=username)
            else:
                user = User.objects.get(username=username)
        except Exception as e:
            user=None
        if username is not None and user.check_password(password):
            return user