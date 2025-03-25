import re
import imghdr
from PIL import Image
from rest_framework.exceptions import ValidationError
from core.messages import ERROR_MESSAGES

uploaded_images = set()

def validate_phone_number(value):
    if not re.match(r'^\+?\d{7,15}$', value):
        raise ValidationError(ERROR_MESSAGES['invalid_phone_number'])
    return value

def validate_avatar(avatar):
    _validate_file_size(avatar)
    _validate_file_type(avatar)
    _check_duplicate_upload(avatar)
    _validate_image_dimensions(avatar)

    return avatar

def _validate_file_size(avatar):
    max_size_mb = 2
    if avatar.size > max_size_mb * 1024 * 1024:
        raise ValidationError(ERROR_MESSAGES['avatar_size_exceeded'])

def _validate_file_type(avatar):
    allowed_types = ['jpg', 'jpeg', 'png', 'gif', 'webp']
    file_type = imghdr.what(avatar)
    if file_type not in allowed_types:
        raise ValidationError(ERROR_MESSAGES['avatar_invalid_type'])

def _check_duplicate_upload(avatar):
    if avatar.name in uploaded_images:
        raise ValidationError(ERROR_MESSAGES['avatar_already_uploaded'])
    uploaded_images.add(avatar.name)

def _validate_image_dimensions(avatar):
    try:
        image = Image.open(avatar)
        width, height = image.size
        required_size = (1000, 1000)

        if width < required_size[0] or height < required_size[1]:
            raise ValidationError(ERROR_MESSAGES['avatar_too_small'])
        if width > required_size[0] or height > required_size[1]:
            raise ValidationError(ERROR_MESSAGES['avatar_too_large'])
        if width != required_size[0] or height != required_size[1]:
            raise ValidationError(ERROR_MESSAGES['avatar_invalid_dimensions'])
    except Exception:
        raise ValidationError(ERROR_MESSAGES['avatar_unreadable'])