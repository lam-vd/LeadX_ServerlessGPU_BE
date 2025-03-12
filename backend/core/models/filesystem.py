from django.db import models
from core.models.user import User

class FileSystem(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    storage_size = models.IntegerField()
    status = models.CharField(max_length=50)
    mount_point = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)