from drf_yasg import openapi

google_login_schema = {
    "operation_summary": "Google Login",
    "operation_description": "Authenticate user using Google OAuth2 token.",
    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'token': openapi.Schema(type=openapi.TYPE_STRING, description='Google OAuth2 token'),
        },
        required=['token'],
    ),
    "responses": {
        200: openapi.Response(
            description="User authenticated successfully.",
            examples={
                "application/json": {
                    "token": "abc123xyz",
                    "user": {
                        "username": "testuser",
                        "email": "testuser@example.com",
                        "is_active": True,
                        "avatar": None,
                        "phone_number": None,
                        "created_at": "2020-01-01T00:00:00Z",
                        "updated_at": "2020-01-01T00:00:00Z",
                    }
                }
            },
        ),
        400: openapi.Response(
            description="Invalid Google Token.",
            examples={
                "application/json": {
                    "error": "Invalid Google Token"
                }
            },
        ),
    },
}