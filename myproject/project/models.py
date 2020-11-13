from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    GENDER = (
        ('male','男'),
        ('female','女'),
        ('secret','保密'),
    )
    gender = models.CharField(max_length=32,choices=GENDER,default='男',verbose_name='性别')
    phone = models.CharField(max_length=11,verbose_name='手机号码')
    c_time = models.DateTimeField(auto_now_add=True,verbose_name='注册时间')
    isDelete = models.BooleanField(default=False)
    address = models.CharField(max_length=200,verbose_name='住址',default=None)


    class Meta:
        db_table = 'at_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Areas(models.Model):
    name = models.CharField(max_length=50,verbose_name='行政区域的名字')
    pid = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'areas'
        verbose_name = '行政区域'
        verbose_name_plural = verbose_name


