from django.db import models

# Create your models here.
class UserProfile(models.Model):
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
        db_table = 'user_profile'
        verbose_name = '使用者資料'
        verbose_name_plural = '使用者資料'

class UserDeafult(models.Model):
    user_id = models.IntegerField()
    suger_delta_max = models.FloatField()