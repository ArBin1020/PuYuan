from django.db import models
from users.usermodel import User
    
class UserDefault(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
    
class UserSetting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    after_recording = models.BooleanField(default=False)
    no_recording_for_a_day = models.BooleanField(default=False)
    over_max_or_under_min = models.BooleanField(default=False)
    after_meal = models.BooleanField(default=True)
    unit_of_sugar = models.BooleanField(default=True)
    unit_of_weight = models.BooleanField(default=True)
    unit_of_height = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
    
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    default = models.OneToOneField(UserDefault, on_delete=models.CASCADE)
    setting = models.OneToOneField(UserSetting, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="")
    account = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, default='0910888888')
    fb_id = models.CharField(max_length=100, default='未設置')
    status = models.CharField(max_length=50, default='normal')
    group = models.CharField(max_length=50, default='0')
    birthday = models.CharField(max_length=50, default='1990-01-01')
    height = models.FloatField(default=0.0)
    weight = models.FloatField(default=0.0)
    gender = models.BooleanField(default=True)
    address = models.CharField(max_length=100, default='未設置')
    unread_records = models.CharField(max_length=100)
    verified = models.IntegerField(default=0)
    privacy_policy = models.IntegerField(default=1)
    must_change_password = models.IntegerField(default=0)
    fcm_id = models.CharField(max_length=100, default='未設置')
    login_times = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class BloodPressure(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    pulse = models.IntegerField()
    recorded_at = models.CharField(max_length=50)

    def __str__(self):
        return self.id
    
class UserWeight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    body_fat = models.FloatField()
    bmi = models.FloatField()
    recorded_at = models.CharField(max_length=50)

    def __str__(self):
        return self.id
    
class BloodSugar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sugar = models.FloatField()
    timeperiod = models.IntegerField()
    recorded_at = models.CharField(max_length=50)
    drug = models.IntegerField()
    exercise = models.IntegerField()

    def __str__(self):
        return self.id

class UserDiet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, blank=True, null=True)
    meal = models.IntegerField()
    tag = models.CharField(max_length=200, blank=True, null=True)
    image = models.IntegerField()
    lat = models.FloatField()
    lng = models.FloatField()
    recorded_at = models.CharField(max_length=50)

    def __str__(self):
        return self.id
    
class UserA1c(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    a1c = models.IntegerField()
    recorded_at = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
    
class UserMedical(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    diabetes_type = models.IntegerField(default=0)
    oad = models.BooleanField(default=False)
    insulin = models.BooleanField(default=False)
    anti_hypertensives = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
    
class UserDrugUsed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.IntegerField()
    name = models.CharField(max_length=100)
    recorded_at = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
    
class UserCare(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    member_id = models.IntegerField(default=1)
    reply_id = models.IntegerField(default=1)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id