from django.shortcuts import render
from django.http.response import HttpResponse
from celery_tasks.msm import tasks
# Create your views here.


from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework.response import Response
from django.conf import settings
from celery_tasks.email.tasks import send_email_task

class PhoneView(APIView):
    def get(self,request,phone):
        tasks.send_msg_code.delay(phone,'1234',1,1)
        # tasks.send_msg_code(phone,'1234',1,1)
        return HttpResponse(phone)


class EmailView(APIView):
    def get(self,request):
        '''
        当前用于发送邮件
        :param request:
        :return:
        '''
        # subject = '邮箱验证'
        # message = '<<**>>'
        # from_email = settings.EMAIL_FROM
        # recipient_list = ['179644835@qq.com']
        # send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)
        print('------------->')
        send_email_task.delay('<*__*>',['179644835@qq.com'])
        print('***********')
        return Response('ok')