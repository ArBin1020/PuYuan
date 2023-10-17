from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db.models.fields import DateTimeField

class account(AbstractUser):
    email = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50,unique=False)
    code = models.CharField(max_length=50)
    verify = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =  ['password']

    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     related_name='user_groups',
    #     blank=True,
    #     verbose_name='groups'
    # )
    
    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     related_name='user_permissions',
    #     blank=True,
    #     verbose_name='user permissions'
    # )

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'account'
        verbose_name = 'account'
        verbose_name_plural = verbose_name
    
class news(models.Model):
    member_id  = models.IntegerField()
    group = models.IntegerField()
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    pushed_at = DateTimeField(max_length=50)
    created_at = DateTimeField(max_length=50)
    updated_at = DateTimeField(max_length=50)
    
    class Meta:
        db_table = 'news'
        verbose_name = 'news'
        verbose_name_plural = verbose_name
