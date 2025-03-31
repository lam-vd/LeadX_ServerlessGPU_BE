from django.db import models

class Plan(models.Model):
    plan_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    compute_units = models.FloatField()