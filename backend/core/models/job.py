from django.db import models
from core.models.task import Task
from core.models.gpu_type import GpuType

class Job(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    job_id = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.SmallIntegerField()
    total_time = models.FloatField()
    gpu_type = models.ForeignKey(GpuType, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)