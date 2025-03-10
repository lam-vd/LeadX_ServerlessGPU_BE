from django.db import models
from core.models.user import User

class InstanceType(models.Model):
    name = models.CharField(max_length=100)
    cpu_cores = models.IntegerField()
    ram_gb = models.IntegerField()
    ssd_tb = models.FloatField()
    architecture = models.CharField(max_length=50)
    gpu_model = models.CharField(max_length=100)
    gpu_memory = models.IntegerField()
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)

class GPUInstance(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(InstanceType, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    region = models.CharField(max_length=50)
    ssh_key = models.ForeignKey('SSHKey', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)