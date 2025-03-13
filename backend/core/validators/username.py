from rest_framework.exceptions import ValidationError
from core.messages import ERROR_MESSAGES

MAX_USERNAME_LENGTH = 150

def validate_username(username):
    if len(username) > MAX_USERNAME_LENGTH:
        raise ValidationError(ERROR_MESSAGES['username_too_long'])
    return username