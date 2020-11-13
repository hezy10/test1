from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from .views import RegisterView,UserInfoView


urlpatterns = [
    url(r'register/',RegisterView.as_view()),
    url(r'token/',obtain_jwt_token),
    url(r'userinfo/',UserInfoView.as_view()),
]