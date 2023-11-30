from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.
class User_Info(AbstractUser):
    
    # register
    email = models.CharField(max_length=50,default='',unique=True)
    verify_code = models.CharField(max_length=50,default='')
    is_verify = models.BooleanField(default=False)
    account = models.CharField(max_length=50,default='')
    verification_code = models.CharField(max_length=50,default='')

    # profile
    name = models.CharField(max_length=50,default='USER')
    birthday = models.CharField(max_length=50,default='')
    height = models.FloatField(default=1.0)
    weight = models.FloatField(default=1.0)
    phone = models.CharField(max_length=50,default="")
    gender = models.BooleanField(default=True)
    fcm_id = models.CharField(max_length=100)
    address = models.CharField(max_length=100,default="")
    must_change_password = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default="VIP")
    created_at = models.CharField(max_length=50,default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = models.CharField(max_length=50,default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    login_times = models.IntegerField(default=0)
    badge = models.IntegerField(default=0)
    # friend_invite_code
    invite_code = models.CharField(max_length=10,default='')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =  ['password']
    class Meta:
        db_table = 'User_Info'

class News_Share(models.Model):
    user_id = models.ForeignKey(User_Info,on_delete=models.CASCADE)
    
    member_id  = models.IntegerField(default=0)
    group = models.IntegerField(default=0)
    title = models.CharField(max_length=50,default='0')
    message = models.CharField(max_length=50,default='0')

    data_type = models.IntegerField() # 0:血壓 1:體重 2:血糖 3:飲食
    relation_type = models.IntegerField() # 1:親友 2:糖友

    pushed_at = models.CharField(max_length=50,default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    created_at = models.CharField(max_length=50,default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = models.CharField(max_length=50,default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    class Meta:
        db_table = 'News_Share'
