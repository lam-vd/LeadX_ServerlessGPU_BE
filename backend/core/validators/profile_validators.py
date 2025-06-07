import re
import imghdr
from rest_framework.exceptions import ValidationError

uploaded_images = set()

def validate_phone_number(value):
    if not re.match(r'^\+?\d{7,15}$', value):
        raise ValidationError('invalid_phone_number')
    return value

def validate_avatar(avatar):
    _validate_file_size(avatar)
    _validate_file_type(avatar)

    return avatar

def _validate_file_size(avatar):
    max_size_mb = 5
    if avatar.size > max_size_mb * 1024 * 1024:
        raise ValidationError('avatar_size_exceeded')

def _validate_file_type(avatar):
    allowed_types = ['jpg', 'jpeg', 'png', 'gif']
    file_type = imghdr.what(avatar)
    if file_type not in allowed_types:
        raise ValidationError('avatar_invalid_type')