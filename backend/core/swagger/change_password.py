from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from core.messages import SUCCESS_MESSAGES, ERROR_MESSAGES

change_password_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=["old_password", "new_password", "confirm_new_password"],
    properties={
        "old_password": openapi.Schema(
            type=openapi.TYPE_STRING,
            format=openapi.FORMAT_PASSWORD,
            description="The current password of the user.",
            example="OldPassword123!",
        ),
        "new_password": openapi.Schema(
            type=openapi.TYPE_STRING,
            format=openapi.FORMAT_PASSWORD,
            description="The new password for the user.",
            example="NewPassword123!",
        ),
        "confirm_new_password": openapi.Schema(
            type=openapi.TYPE_STRING,
            format=openapi.FORMAT_PASSWORD,
            description="Confirmation of the new password.",
            example="NewPassword123!",
        ),
    },
)

change_password_response_200 = openapi.Response(
    description=SUCCESS_MESSAGES['password_changed'],
    examples={
        "application/json": {
            "data": {},
            "status": status.HTTP_200_OK,
            "message": SUCCESS_MESSAGES['password_changed'],
        }
    },
)

change_password_response_400 = openapi.Response(
    description=ERROR_MESSAGES['validation_error'],
    examples={
        "application/json": {
            "data": {},
            "status": status.HTTP_400_BAD_REQUEST,
            "message": ERROR_MESSAGES['validation_error'],
            "errors": {
                "old_password": ["The old password is incorrect."],
                "new_password": ["The new password cannot be the same as the old password."],
                "confirm_new_password": ["Passwords do not match."],
            },
        }
    },
)

change_password_swagger_schema = swagger_auto_schema(
    operation_summary="Change Password",
    operation_description="Allows the user to change their password by providing the old password, new password, and confirmation of the new password.",
    request_body=change_password_request_body,
    responses={
        200: change_password_response_200,
        400: change_password_response_400,
    },
)