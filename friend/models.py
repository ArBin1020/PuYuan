from django.db import models
from users.models import User

class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend')
    relation_id = models.IntegerField(default=1)
    type = models.IntegerField()
    status = models.IntegerField(default=0)
    read = models.IntegerField(default=0)
    # code = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.id
