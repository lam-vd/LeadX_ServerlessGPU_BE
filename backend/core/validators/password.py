import re
from rest_framework.exceptions import ValidationError
from core.messages import ERROR_MESSAGES

MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 30

def validate_password(password):
    if not password:
        raise ValidationError(ERROR_MESSAGES['password_required'])
    if len(password) < MIN_PASSWORD_LENGTH:
        raise ValidationError(ERROR_MESSAGES['password_too_short'])
    if len(password) > MAX_PASSWORD_LENGTH:
        raise ValidationError(ERROR_MESSAGES['password_too_long'])
    if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password):
        raise ValidationError(ERROR_MESSAGES['password_invalid'])
    return password