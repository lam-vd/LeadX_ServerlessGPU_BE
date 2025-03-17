from drf_yasg import openapi
from core.messages import USER_MESSAGES

get_user_swagger_schema = {
    "operation_summary": "Get Current User",
    "operation_description": "Retrieve the details of the currently authenticated user.",
    "responses": {
        200: openapi.Response(
            description=USER_MESSAGES["get_user_success"],
            examples={
                "application/json": {
                    "username": "testuser",
                    "email": "testuser@example.com",
                    "is_active": True,
                    "avatar": None,
                    "phone_number": None,
                    "created_at": "2021-01-01T00:00:00Z",
                    "updated_at": "2021-01-01T00:00:00Z",
                }
            },
        ),
        401: openapi.Response(
            description=USER_MESSAGES["auth_credentials_missing"],
            examples={
                "application/json": {
                    "detail": USER_MESSAGES["auth_credentials_missing"]
                }
            },
        ),
    },
}