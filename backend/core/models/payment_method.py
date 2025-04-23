from django.db import models
from core.models.user import User

class PaymentMethod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stripe_payment_method_id = models.CharField(max_length=255, unique=True)
    brand = models.CharField(max_length=50)  # e.g., Visa, MasterCard
    last4 = models.CharField(max_length=4)  # Last 4 digits of the card
    exp_month = models.IntegerField()  # Expiration month
    exp_year = models.IntegerField()  # Expiration year
    is_default = models.BooleanField(default=False)  # Whether this is the default card
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)