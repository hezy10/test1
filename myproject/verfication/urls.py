from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from .views import PhoneView,EmailView

urlpatterns = [
    url(r'phone/(?P<phone>\d{11})/$',PhoneView.as_view()),
    url(r'email/',EmailView.as_view()),
]