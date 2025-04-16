from django.db import models
from core.models.task import Task
from core.models.gpu_type import GpuType

class Job(models.Model):
    class Status(models.IntegerChoices):
        PENDING = 0, "Pending"
        RUNNING = 1, "Running"
        COMPLETED = 2, "Completed"
        FAILED = 3, "Failed"
        STOPPED = 4, "Stopped"

    job_id = models.CharField(max_length=255, unique=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="jobs")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.SmallIntegerField(choices=Status.choices, default=Status.PENDING)
    total_time = models.FloatField()
    gpu_type = models.ForeignKey(GpuType, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)