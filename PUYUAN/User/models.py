from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db.models.fields.related import ForeignKey
class account(AbstractUser):

    email = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    verify = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =  ['password']
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'User_Account'
    
class news(models.Model):
    user = ForeignKey(account, on_delete=models.CASCADE)
    member_id  = models.IntegerField(default=0)
    group = models.IntegerField(default=0)
    title = models.CharField(max_length=50,default='0')
    message = models.CharField(max_length=50,default='0')
    pushed_at = models.CharField(max_length=50,default='0')
    created_at = models.CharField(max_length=50,default='0')
    updated_at = models.CharField(max_length=50,default='0')
    
    class Meta:
        db_table = 'User_News'
        verbose_name = 'news'
        verbose_name_plural = verbose_name

class share(models.Model):
    user = ForeignKey(account, on_delete=models.CASCADE)
    member_id = models.IntegerField()
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    
    data_type = models.IntegerField() # 0:血壓 1:體重 2:血糖 3:飲食
    relation_type = models.IntegerField() # 1:親友 2:糖友
    # share_id = models.IntegerField()

    class Meta:
        db_table = 'User_Share'
        verbose_name = 'share'
        verbose_name_plural = verbose_name
    

