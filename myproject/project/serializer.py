from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_jwt.settings import api_settings


from .models import User
class UserSerializer(ModelSerializer):
    cpwd = serializers.CharField(label='确认密码',write_only=True)
    token = serializers.CharField(label='token',read_only=True)
    class Meta:
        model = User
        fields = ['username','password','cpwd','token','phone','email','address']

    def validate(self, attrs):
        print(attrs)
        if attrs['password'] != attrs['cpwd']:
            raise serializers.ValidationError('请重新输入确认密码')

        return attrs

    def create(self, validated_data):
        del validated_data['cpwd']
        # 将用户信息存入数据库
        user = super(UserSerializer, self).create(validated_data)

        # 将密码进行加密
        user.set_password(validated_data['password'])
        user.save()
        # 注册成功之后，将用户状态进行保存
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user.token = token

        return user

class UserInfoSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','phone','email','address']