from django.db import models
from User.models import User_Info
from datetime import datetime
# Create your models here.
class User_Default(models.Model):
    user_id = models.ForeignKey(User_Info, on_delete=models.CASCADE)

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
    
    created_at = models.CharField(max_length=50,default=datetime.now().strftime("%Y-%m-%d %H:%M:%S:%M:%S"))
    updated_at = models.CharField(max_length=50,default=datetime.now().strftime("%Y-%m-%d %H:%M:%S:%M:%S"))
    class Meta:
        db_table = 'User_Default'

class User_Setting(models.Model):
    user_id = models.ForeignKey(User_Info, on_delete=models.CASCADE)

    after_recording = models.BooleanField(default=False)
    no_recording_for_a_day = models.BooleanField(default=False)
    over_max_or_under_min = models.BooleanField(default=True)
    after_meal = models.BooleanField(default=True)
    unit_of_sugar = models.BooleanField(default=True)
    unit_of_weight = models.BooleanField(default=True)
    unit_of_height = models.BooleanField(default=True)

    created_at = models.CharField(max_length=50,default=datetime.now().strftime("%Y-%m-%d %H:%M:%S:%M:%S"))
    updated_at = models.CharField(max_length=50,default=datetime.now().strftime("%Y-%m-%d %H:%M:%S:%M:%S"))

    class Meta:
        db_table = 'User_Setting'

class User_VIP(models.Model):
    user_id = models.ForeignKey(User_Info, on_delete=models.CASCADE)

    level = models.IntegerField(default=0)
    remark = models.FloatField(default=0)

    started_at = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    ended_at = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    created_at = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = models.DateTimeField(default= datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    class Meta:
        db_table = 'User_VIP'


class User_Blood_Pressure(models.Model):    
    user_id = models.ForeignKey(User_Info, on_delete=models.CASCADE)

    systolic = models.IntegerField(default=0)
    diastolic = models.IntegerField(default=0)
    pulse = models.IntegerField(default=0)
    recorded_at = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


class User_Blood_Sugar(models.Model):    
    user_id = models.ForeignKey(User_Info, on_delete=models.CASCADE)

    sugar = models.FloatField(default=0)
    timeperiod = models.IntegerField(default=0)
    drug = models.IntegerField(default=0)
    exercise = models.IntegerField(default=0)
    recorded_at = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    class Meta:
        db_table = 'User_Blood_Sugar'

    
class User_Weight(models.Model):   
    user_id = models.ForeignKey(User_Info, on_delete=models.CASCADE)

    weight = models.FloatField(default=0)
    body_fat = models.FloatField(default=0)
    bmi = models.FloatField(default=0)
    recorded_at = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    class Meta:
        db_table = 'User_Weight'

class User_Diary(models.Model):
    user_id = models.ForeignKey(User_Info, on_delete=models.CASCADE)

    description = models.CharField(max_length=255, null=True, default="")
    meal = models.IntegerField(null=True, default=0)
    tag = models.CharField(max_length=255, blank=True, null=True, default="")
    image = models.CharField(max_length=255, blank=True, null=True, default="")
    lat = models.CharField(max_length=255, blank=True, null=True, default="")
    lng = models.CharField(max_length=255, blank=True, null=True, default="")
    recorded_at = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    class Meta:
        db_table = 'User_Diary'

class User_A1c(models.Model):  
    user_id = models.ForeignKey(User_Info, on_delete=models.CASCADE)

    a1c = models.FloatField(default=0)
    
    recorded_at = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    created_at = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    class Meta:
        db_table = 'User_A1c'

class User_Medical(models.Model):
    user_id = models.ForeignKey(User_Info, on_delete=models.CASCADE)

    diabetes_type = models.IntegerField(null=True, default=0)
    oad = models.IntegerField(null=True, default=0)
    insulin = models.IntegerField(null=True, default=0)
    anti_hypertensives = models.IntegerField(null=True, default=0)
    
    created_at = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    class Meta:
        db_table = 'User_Medical'

class User_Drug(models.Model):
    user_id = models.ForeignKey(User_Info, on_delete=models.CASCADE)

    data_type = models.IntegerField(default=0)
    name = models.CharField(max_length=50, null=True, default="")

    recorded_at = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    created_at = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    class Meta:
        db_table = 'User_Drug'

class User_Care(models.Model):
    user_id = models.ForeignKey(User_Info, on_delete=models.CASCADE)
    member_id = models.IntegerField(default=0)
    reply_id = models.IntegerField(default=0)
    message = models.CharField(max_length=255, null=True, default="")
    created_at = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    class Meta:
        db_table = 'User_Care'