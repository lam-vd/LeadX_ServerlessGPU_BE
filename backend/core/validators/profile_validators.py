import re
from rest_framework.exceptions import ValidationError
from core.messages import ERROR_MESSAGES
import imghdr

def validate_phone_number(value):
    if not re.match(r'^\+?\d{7,15}$', value):
        raise ValidationError(ERROR_MESSAGES['invalid_phone_number'])
    return value

def validate_avatar(avatar):
    max_size_mb = 2
    if avatar.size > max_size_mb * 1024 * 1024:
        raise ValidationError(ERROR_MESSAGES['avatar_size_exceeded'])

    allowed_types = ['png', 'jpg', 'jpeg']
    file_type = imghdr.what(avatar)
    if file_type not in allowed_types:
        raise ValidationError(ERROR_MESSAGES['avatar_invalid_type'])

    return avatar