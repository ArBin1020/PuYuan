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
    # 不需要再定义 username、password、email，因为 AbstractUser 已经包括了这些字段
    username = models.CharField(max_length=50,unique=False)
    code = models.CharField(max_length=50)
    verify = models.BooleanField(default=False)

    # 使用 email 作为登录用户名
    USERNAME_FIELD = 'email'

    # 这里的 REQUIRED_FIELDS 应该是一个列表，用于指定在创建用户时必须填写的字段
    REQUIRED_FIELDS =  'password'

    # 为 groups 和 user_permissions 添加 related_name 参数
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

