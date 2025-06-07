from rest_framework.exceptions import ValidationError
from core.models.user import User

MAX_EMAIL_LENGTH = 254

def validate_email(email):
    if not email:
        raise ValidationError('email_required')
    if len(email) > MAX_EMAIL_LENGTH:
        raise ValidationError('email_too_long')
    if User.objects.filter(email=email).exists():
        raise ValidationError('email_already_registered')
    return email