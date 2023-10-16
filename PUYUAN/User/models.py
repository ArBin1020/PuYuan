from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class account(AbstractUser):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    verify = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = 'password'


# class account(models.Model):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     code = models.CharField(max_length=50)
#     verify = models.BooleanField(default=False)
#     def __str__(self):
#         return self.username