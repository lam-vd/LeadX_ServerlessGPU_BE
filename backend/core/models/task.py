from django.db import models
from core.models.user import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image_path = models.CharField(max_length=255, blank=True, null=True)
    endpoint = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=50, default="tokyo")
    source_path = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)