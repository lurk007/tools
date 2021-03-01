from django.db import models
from time import time


# 数据库迁移步骤
# python manage.py makemigrations appname
# python manage.py sqlmigrate appname 0001
# python manage.py migrate
# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=11)  # md5
    password = models.CharField(max_length=32, default='')  # md5
    uid_card = models.CharField(max_length=24, default='')  # base64加密
    login_name = models.CharField(max_length=24, default='')  # base64加密
    phone = models.CharField(max_length=16, default='')  # base64加密
    email = models.CharField(max_length=80, default='')  # base64加密
    power = models.CharField(max_length=1, default=2)  # 权限
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return F'uid:{self.uid},login_name:{self.login_name},password:{self.password},phone:{self.phone},email:{self.email},uid_card:{self.uid_card},power:{self.power}'
