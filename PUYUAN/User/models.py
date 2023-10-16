# from django.db import models
# from django.contrib.auth.models import AbstractUser
# # Create your models here.
# class account(AbstractUser):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     code = models.CharField(max_length=50)
#     verify = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = 'password'
    
#     def __str__(self):
#         return self.username

from django.db import models
from django.contrib.auth.models import AbstractUser

class account(AbstractUser):
    
    username = models.CharField(max_length=50,unique=False)
    code = models.CharField(max_length=50)
    verify = models.BooleanField(default=False)

    # 使用 email 作为登录用户名
    USERNAME_FIELD = 'email'

    # 这里的 REQUIRED_FIELDS 应该是一个列表，用于指定在创建用户时必须填写的字段
    REQUIRED_FIELDS =  ['password']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_groups',
        blank=True,
        verbose_name='groups'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_permissions',
        blank=True,
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username
    class Meta:
        db_table = 'account'
        verbose_name = 'account'
        verbose_name_plural = verbose_name
class news:
    member_id  = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    pushed_at = models.CharField(max_length=50)
    created_at = models.CharField(max_length=50)
    updated_at = models.CharField(max_length=50)

    class Meta:
        db_table = 'news'
        verbose_name = 'news'
        verbose_name_plural = verbose_name
