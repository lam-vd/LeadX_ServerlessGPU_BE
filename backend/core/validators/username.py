from rest_framework.exceptions import ValidationError

MAX_USERNAME_LENGTH = 150

def validate_username(username):
    if not username:
        raise ValidationError('username_required')
    if len(username) > MAX_USERNAME_LENGTH:
        raise ValidationError('username_too_long')
    return username