from django.db import models
from User.models import account
from django.db.models.fields.related import ForeignKey
# Create your models here.
from django.db.models.fields import DateTimeField
import pytz

tz = pytz.timezone('America/Sao_Paulo')
class UserDefault(models.Model):
    user = models.ForeignKey(account, on_delete=models.CASCADE)
    sugar_delta_max = models.FloatField(default=10.0)
    sugar_delta_min = models.FloatField(default=1.0)
    sugar_morning_max = models.FloatField(default=10.0)
    sugar_morning_min = models.FloatField(default=1.0)
    sugar_evening_max = models.FloatField(default=10.0)
    sugar_evening_min = models.FloatField(default=1.0)
    sugar_before_max = models.FloatField(default=10.0)
    sugar_before_min = models.FloatField(default=1.0)
    sugar_after_max = models.FloatField(default=10.0)
    sugar_after_min = models.FloatField(default=1.0)
    systolic_max = models.IntegerField(default=10)
    systolic_min = models.IntegerField(default=1)
    diastolic_max = models.IntegerField(default=10)
    diastolic_min = models.IntegerField(default=1)
    pulse_max = models.IntegerField(default=10)
    pulse_min = models.IntegerField(default=1)
    weight_max = models.FloatField(default=10.0)
    weight_min = models.FloatField(default=1.0)
    bmi_max = models.FloatField(default=10.0)
    bmi_min = models.FloatField(default=1.0)
    body_fat_max = models.FloatField(default=10.0)
    body_fat_min = models.FloatField(default=1.0)
    
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
    
    class Meta:
        db_table = 'Body_User_Default'

class UserSetting(models.Model):
    user = models.ForeignKey(account, on_delete=models.CASCADE)
    after_recording = models.BooleanField(default=False)
    no_recording_for_a_day = models.BooleanField(default=False)
    over_max_or_under_min = models.BooleanField(default=True)
    after_meal = models.BooleanField(default=True)
    unit_of_sugar = models.BooleanField(default=True)
    unit_of_weight = models.BooleanField(default=True)
    unit_of_height = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.id
    class Meta:
        db_table = 'Body_User_Setting'
        verbose_name = '使用者設定'
        verbose_name_plural = '使用者設定'


class unread_records(models.Model):
    user = ForeignKey(account, on_delete=models.CASCADE)
    unread_1 = models.IntegerField()
    unread_2 = models.IntegerField()
    unread_3 = models.IntegerField()



class vip(models.Model):
    user = ForeignKey(account, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    remark = models.FloatField(max_length=100, default=1.0)
    started_at = models.DateTimeField(auto_now_add=True)

    ended_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserProfile(models.Model):
    user = ForeignKey(account, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    birthday = models.CharField(max_length=50,default="2020-01-01")
    height = models.FloatField(default=1.0)
    weight = models.FloatField(default=1.0)
    phone = models.CharField(max_length=50,default="2020-01-01 01:01:00")
    email = models.CharField(max_length=100,default="2020-01-01 01:01:00")
    gender = models.BooleanField(default=True)
    fcm_id = models.CharField(max_length=100)
    address = models.CharField(max_length=100,default="abc")

    invite_code = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Body_User_Profile'

class BloodPressure(models.Model):
    user = ForeignKey(account, on_delete=models.CASCADE)
    systolic = models.IntegerField(default=1)
    diastolic = models.IntegerField(default=1)
    pulse = models.IntegerField(default=1)
    recorded_at = models.CharField(max_length=50)

    def __str__(self):
        return self.id
    class Meta:
        db_table = 'Body_Blood_Pressure'
        verbose_name = '血壓'
        verbose_name_plural = '血壓'

class Weight(models.Model):
    user = ForeignKey(account, on_delete=models.CASCADE)
    weight = models.FloatField()
    body_fat = models.FloatField()
    bmi = models.FloatField()
    recorded_at = models.CharField(max_length=50)

    def __str__(self):
        return self.id
    
    class Meta:
        db_table = 'Body_Weight'
class BloodSuger(models.Model):
    user = ForeignKey(account, on_delete=models.CASCADE)
    sugar = models.FloatField()
    timeperiod = models.IntegerField()
    recorded_at = models.CharField(max_length=50)
    drug = models.IntegerField()
    execrise = models.IntegerField()

    def __str__(self):
        return self.id
    
    class Meta:
        db_table = 'Body_Blood_Suger'

class Diet(models.Model):
    user = ForeignKey(account, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    meal = models.IntegerField()
    tag = models.CharField(max_length=100)
    image = models.IntegerField()
    lat = models.FloatField()
    lng = models.FloatField()
    recorded_at = models.CharField(max_length=50)

    def __str__(self):
        return self.id
    
    class Meta:
        db_table = 'Body_Diet'


class A1c(models.Model):
    user = ForeignKey(account, on_delete=models.CASCADE)
    a1c = models.CharField(max_length=50)
    recorded_at = DateTimeField(auto_now_add=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
    
    class Meta:
        db_table = 'Body_A1c'
        verbose_name = 'A1c'
        verbose_name_plural = 'A1c'

class Medical(models.Model):
    user = ForeignKey(account, on_delete=models.CASCADE)
    diabetes_type = models.IntegerField(default=1)
    oad = models.IntegerField(default=1)
    insulin = models.IntegerField(default=1)
    anti_hypertensives = models.IntegerField(default=1)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.id
    
    class Meta:
        db_table = 'Body_Medical'

class Drug_Used(models.Model):
    user = ForeignKey(account, on_delete=models.CASCADE)
    data_type = models.IntegerField()
    name = models.CharField(max_length=100)
    recorded_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now_add=True)
    created_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
    
    class Meta:
        db_table = 'Body_Drug_Used'
        verbose_name = '藥物使用紀錄'
        verbose_name_plural = '藥物使用紀錄'

class Care(models.Model):
    user = ForeignKey(account, on_delete=models.CASCADE)
    member_id = models.IntegerField()
    reply_id = models.IntegerField()
    message = models.CharField(max_length=100)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
    
    class Meta:
        db_table = 'Body_Care'
        verbose_name = '照護者'
        verbose_name_plural = '照護者'