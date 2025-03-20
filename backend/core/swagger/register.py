from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from core.messages import ERROR_MESSAGES, SUCCESS_MESSAGES
from core.validators.username import MAX_USERNAME_LENGTH
from core.validators.email import MAX_EMAIL_LENGTH
from core.validators.password import MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH

register_swagger_schema = swagger_auto_schema(
    operation_description="Register a new user with username, email, and password.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["username", "email", "password"],
        properties={
            "username": openapi.Schema(
                type=openapi.TYPE_STRING,
                description=f"The username of the user (max length: {MAX_USERNAME_LENGTH}).",
                example="john_doe",
                maxLength=MAX_USERNAME_LENGTH,
            ),
            "email": openapi.Schema(
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_EMAIL,
                description=f"The email address of the user (max length: {MAX_EMAIL_LENGTH}).",
                example="john.doe@example.com",
                maxLength=MAX_EMAIL_LENGTH,
            ),
            "password": openapi.Schema(
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_PASSWORD,
                description=f"The password for the user account (min length: {MIN_PASSWORD_LENGTH}, max length: {MAX_PASSWORD_LENGTH}).",
                example="StrongPassword123!",
                minLength=MIN_PASSWORD_LENGTH,
                maxLength=MAX_PASSWORD_LENGTH,
            ),
        },
    ),
    responses={
        201: openapi.Response(
            description=SUCCESS_MESSAGES['user_registered_successfully'],
            examples={
                "application/json": {
                    "data": {},
                    "status": "success",
                    "message": SUCCESS_MESSAGES['user_registered_successfully']
                }
            },
        ),
        400: openapi.Response(
            description=ERROR_MESSAGES['registration_failed'],
            examples={
                "application/json": {
                    "data": {
                        "email": ["This email is already taken."],
                        "password": ["Ensure this field has at least 8 characters."]
                    },
                    "status": "error",
                    "message": ERROR_MESSAGES['registration_failed']
                    "errors": {
                        "email": ["This email is already taken."],
                        "password": ["Ensure this field has at least 8 characters."]
                    }
                }
            },
        ),
    }
)