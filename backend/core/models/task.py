from django.db import models
from core.models.gpu_instance import GPUInstance
from core.models.user import User

class Task(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    container_image = models.CharField(max_length=255)
    cuda_version = models.CharField(max_length=50)
    logs = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    gpu_instance = models.ForeignKey(GPUInstance, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)