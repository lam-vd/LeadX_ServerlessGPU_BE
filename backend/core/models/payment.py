from django.db import models
from core.models.user import User

class PaymentAccount(models.Model):
    card_number = models.CharField(max_length=16)
    expiry_date = models.DateField()
    card_holder = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)