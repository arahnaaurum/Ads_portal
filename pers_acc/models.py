from django.contrib.auth.models import User
from django.db import models


class OneTimeCode(models.Model):
    user = models.CharField(max_length=24, unique=False) #сделала поле неуникальным только для проверки работы регистрации!
    username = models.CharField(max_length=24, unique=False) #сделала поле неуникальным только для проверки работы регистрации!
    code = models.IntegerField(default = 0)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=128)