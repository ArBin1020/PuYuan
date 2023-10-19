from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ForeignKey
class account(AbstractUser):

    email = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50,unique=False)
    code = models.CharField(max_length=50)
    verify = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =  ['password']
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'account'
        verbose_name = 'account'
        verbose_name_plural = verbose_name
    
class news(models.Model):
    user = ForeignKey(account, on_delete=models.CASCADE)
    member_id  = models.IntegerField()
    group = models.IntegerField()
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    pushed_at = DateTimeField()
    created_at = DateTimeField()
    updated_at = DateTimeField()
    
    class Meta:
        db_table = 'news'
        verbose_name = 'news'
        verbose_name_plural = verbose_name

class share(models.Model):
    user = ForeignKey(account, on_delete=models.CASCADE)
    data_type = models.IntegerField()
    relation_type = models.IntegerField()
    # share_id = models.IntegerField()
    