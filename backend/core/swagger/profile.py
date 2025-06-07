from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from core.messages import SUCCESS_MESSAGES, ERROR_MESSAGES

update_profile_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "username": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="The new username for the user.",
            example="new_username",
        ),
        "phone_number": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="The new phone number for the user. Must be between 7 and 15 digits and can optionally start with a '+'.",
            example="+123456789",
        ),
        "avatar": openapi.Schema(
            type=openapi.TYPE_STRING,
            format=openapi.FORMAT_BINARY,
            description="The new avatar image for the user. Only PNG, JPG, and JPEG files are allowed.",
        ),
    },
    required=[]
)

update_profile_response_200 = openapi.Response(
    description=SUCCESS_MESSAGES['profile_updated'],
    examples={
        "application/json": {
            "data": {
                "username": "new_username",
                "phone_number": "+123456789",
                "avatar": "/media/avatars/new-avatar.png"
            },
            "status": 200,
            "message": SUCCESS_MESSAGES['profile_updated']
        }
    },
)

update_profile_response_400 = openapi.Response(
    description=ERROR_MESSAGES['validation_error'],
    examples={
        "application/json": {
            "data": {},
            "status": 400,
            "message": ERROR_MESSAGES['validation_error'],
            "errors": {
                "username": [ERROR_MESSAGES['username_too_long']],
                "phone_number": [ERROR_MESSAGES['invalid_phone_number']],
                "avatar": [
                    ERROR_MESSAGES['avatar_size_exceeded'],
                    ERROR_MESSAGES['avatar_invalid_type']
                ]
            }
        }
    },
)

update_profile_swagger_schema = swagger_auto_schema(
    operation_summary="Update Profile",
    operation_description="Allows the user to update their profile information, including username, phone number, and avatar. Only the fields provided in the request will be updated.",
    request_body=update_profile_request_body,
    responses={
        200: update_profile_response_200,
        400: update_profile_response_400,
    },
)