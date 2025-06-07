from django.conf import settings
from django.db import models

class Task(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column='user_id'
    )
    task_name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image_path = models.CharField(max_length=255)
    endpoint = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, default="tokyo")
    source_path = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "core_task"