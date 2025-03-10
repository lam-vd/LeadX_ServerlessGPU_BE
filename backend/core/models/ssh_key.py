from django.db import models
from core.models.user import User

class SSHKey(models.Model):
    name = models.CharField(max_length=100)
    public_key = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)