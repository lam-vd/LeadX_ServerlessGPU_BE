from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
# from core.serializers.login_auth import CustomLoginSerializer

login_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=["email", "password"],
    properties={
        "email": openapi.Schema(
            type=openapi.TYPE_STRING,
            format=openapi.FORMAT_EMAIL,
            description="User's email address",
            example="user@example.com",
        ),
        "password": openapi.Schema(
            type=openapi.TYPE_STRING,
            format=openapi.FORMAT_PASSWORD,
            description="User's password",
            example="Password123!",
        ),
    },
)

login_response_200 = openapi.Response(
    description="Login successful",
    examples={
        "application/json": {
              "token": "abc123xyz",
              "user": {
                  "username": "user1",
                  "email": "user@example.com",
                  "is_active": True,
                  "avatar": "namedomain.com/media/avatars/avatar-user-default.png",
                  "phone_number": "123456789",
                  "created_at": "2023-01-01T00:00:00Z",
                  "updated_at": "2023-01-01T00:00:00Z",
            },
        }
    },
)

login_response_400 = openapi.Response(
    description="Login failed",
    examples={
        "application/json": {
            "email": ["This field is required.", "Invalid email address."],
            "password": ["This field is required.", "Password must include uppercase, lowercase, number, and special character."],
            "detail": ["Invalid email or password.", "This account is not active. Please verify your email."]
        }
    },
)

def login_swagger_schema():
    return swagger_auto_schema(
        operation_description="Login with email and password",
        request_body=login_request_body,
        responses={
            200: login_response_200,
            400: login_response_400,
        },
    )