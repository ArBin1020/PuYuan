from django.db import models
from User.models import User_Info
from datetime import datetime
# Create your models here.

class Friend(models.Model):
    user_id = models.ForeignKey(User_Info,on_delete=models.CASCADE)

    relation_id = models.IntegerField(null=True, default=0)
    name = models.CharField(max_length=255, null=True, default="")
    relation_type = models.IntegerField(null=True, default=0)
    status = models.IntegerField(null=True, default=0)
    read = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))