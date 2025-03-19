from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from core.messages import SUCCESS_MESSAGES, ERROR_MESSAGES

forgot_password_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=["email"],
    properties={
        "email": openapi.Schema(
            type=openapi.TYPE_STRING,
            format=openapi.FORMAT_EMAIL,
            description="The email address of the user requesting a password reset.",
            example="user@example.com",
        ),
    },
)

forgot_password_response_200 = openapi.Response(
    description=SUCCESS_MESSAGES['password_reset_email_sent'],
    examples={
        "application/json": {
            "data": {},
            "status": "success",
            "message": SUCCESS_MESSAGES['password_reset_email_sent'],
        }
    },
)

forgot_password_response_400 = openapi.Response(
    description=ERROR_MESSAGES['validation_error'],
    examples={
        "application/json": {
            "data": {},
            "status": "error",
            "message": {
                "email": ["This email is not registered."]
            }
        }
    },
)

forgot_password_swagger_schema = swagger_auto_schema(
    operation_summary="Forgot Password",
    operation_description="Request a password reset email by providing the user's email address.",
    request_body=forgot_password_request_body,
    responses={
        200: forgot_password_response_200,
        400: forgot_password_response_400,
    },
)

reset_password_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=["token", "password_new", "password_confirmation"],
    properties={
        "token": openapi.Schema(
            type=openapi.TYPE_STRING,
            format=openapi.FORMAT_UUID,
            description="The reset password token sent via email.",
            example="123e4567-e89b-12d3-a456-426614174000",
        ),
        "password_new": openapi.Schema(
            type=openapi.TYPE_STRING,
            format=openapi.FORMAT_PASSWORD,
            description="The new password for the user.",
            example="NewStrongPassword123!",
        ),
        "password_confirmation": openapi.Schema(
            type=openapi.TYPE_STRING,
            format=openapi.FORMAT_PASSWORD,
            description="Confirmation of the new password.",
            example="NewStrongPassword123!",
        ),
    },
)

reset_password_response_200 = openapi.Response(
    description=SUCCESS_MESSAGES['password_reset_success'],
    examples={
        "application/json": {
            "data": {},
            "status": "success",
            "message": SUCCESS_MESSAGES['password_reset_success'],
        }
    },
)

reset_password_response_400 = openapi.Response(
    description=ERROR_MESSAGES['validation_error'],
    examples={
        "application/json": {
            "data": {},
            "status": "error",
            "message": {
                "token": ["Invalid or expired token."],
                "password_confirmation": ["Passwords do not match."],
            }
        }
    },
)

reset_password_swagger_schema = swagger_auto_schema(
    operation_summary="Reset Password",
    operation_description="Reset the user's password using the reset token and new password.",
    request_body=reset_password_request_body,
    responses={
        200: reset_password_response_200,
        400: reset_password_response_400,
    },
)