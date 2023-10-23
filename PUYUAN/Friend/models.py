from django.db import models
from User.models import account
# Create your models here.
class Friend(models.Model):
    user = models.ForeignKey(account, on_delete=models.CASCADE, related_name='user')
    friend = models.ForeignKey(account, on_delete=models.CASCADE, related_name='friend', null=True)
    relation_id = models.IntegerField(default=1)
    type = models.IntegerField(null=True)
    status = models.IntegerField(default=0)
    read = models.IntegerField(default=0)
    code = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.id
    class Meta:
        db_table = 'Friend'
        verbose_name = '好友'
        verbose_name_plural = '好友'