from django.db import models

class Plan(models.Model):
    plan_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    compute_units = models.FloatField()
    status = models.CharField(max_length=50, default="Active")
    used_units = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)