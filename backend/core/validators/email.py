from rest_framework.exceptions import ValidationError
from django.core.validators import validate_email as django_validate_email
from core.messages import ERROR_MESSAGES
from core.models.user import User

MAX_EMAIL_LENGTH = 320

def validate_email(email):
    if not email:
        raise ValidationError(ERROR_MESSAGES['email_required'])
    if len(email) > MAX_EMAIL_LENGTH:
        raise ValidationError(ERROR_MESSAGES['email_too_long'])
    if User.objects.filter(email=email).exists():
        raise ValidationError(ERROR_MESSAGES['email_already_registered'])
    return email