from django.db import models
from User.models import account
from django.db.models.fields.related import ForeignKey
# Create your models here.

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

    def __str__(self):
        return self.id
    class Meta:
        db_table = 'Body_User_Default'
        verbose_name = '使用者預設值'
        verbose_name_plural = '使用者預設值'

class UserSetting(models.Model):
    user = models.ForeignKey(account, on_delete=models.CASCADE)
    after_recording = models.BooleanField(default=False)
    no_recording_for_a_day = models.BooleanField(default=False)
    over_max_or_under_min = models.BooleanField(default=True)
    after_meal = models.BooleanField(default=True)
    unit_of_sugar = models.BooleanField(default=True)
    unit_of_weight = models.BooleanField(default=True)
    unit_of_height = models.BooleanField(default=True)

    def __str__(self):
        return self.id
    class Meta:
        db_table = 'Body_User_Setting'
        verbose_name = '使用者設定'
        verbose_name_plural = '使用者設定'

class UserProfile(models.Model):
    user = ForeignKey(account, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    birthday = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    gender = models.BooleanField()
    fcm_id = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Body_User_Profile'
        verbose_name = '使用者資料'
        verbose_name_plural = '使用者資料'


class BloodPressure(models.Model):
    user = ForeignKey(account, on_delete=models.CASCADE)
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    pulse = models.IntegerField()
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
        verbose_name = '體重'
        verbose_name_plural = '體重'

class BloodSuger(models.Model):
    user = ForeignKey(account, on_delete=models.CASCADE)
    sugar = models.FloatField()
    timeperiod = models.IntegerField()
    recorded_at = models.CharField(max_length=50)
    drug = models.IntegerField()
    exercise = models.IntegerField()

    def __str__(self):
        return self.id
    class Meta:
        db_table = 'Body_Blood_Suger'
        verbose_name = '血糖'
        verbose_name_plural = '血糖'

