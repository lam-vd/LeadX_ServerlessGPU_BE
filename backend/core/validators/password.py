import re
from rest_framework.exceptions import ValidationError

MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 30

def validate_password(password):
    if not password:
        raise ValidationError('password_required')
    if len(password) < MIN_PASSWORD_LENGTH:
        raise ValidationError('password_too_short')
    if len(password) > MAX_PASSWORD_LENGTH:
        raise ValidationError('password_too_long')
    if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*?()])[A-Za-z\d!@#$%^&*?()]{8,}$", password):
        raise ValidationError('password_invalid')
    return password