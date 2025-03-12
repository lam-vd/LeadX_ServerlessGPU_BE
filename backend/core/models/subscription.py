from django.db import models
from core.models.user import User

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    payment_plan = models.CharField(max_length=50)
    payment_due = models.DateTimeField()
    hours_used = models.IntegerField()
    total_hours = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Invoice(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    status = models.CharField(max_length=50)
    payment_date = models.DateTimeField()
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)