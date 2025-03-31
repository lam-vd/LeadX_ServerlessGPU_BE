from django.db import models
from core.models.user import User
from core.models.plan import Plan

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    amount_paid = models.FloatField()
    payment_date = models.DateTimeField()
    remaining_units = models.FloatField()
    used_units = models.FloatField()