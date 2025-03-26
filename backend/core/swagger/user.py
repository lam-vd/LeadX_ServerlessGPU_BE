from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from core.messages import USER_MESSAGES

get_user_swagger_schema =  swagger_auto_schema(
    operation_summary="Get Current User",
    operation_description="Retrieve the details of the currently authenticated user.",
    responses={
        200: openapi.Response(
            description=USER_MESSAGES["get_user_success"],
            examples={
                "application/json": {
                    "data": {
                        "username": "testuser",
                        "email": "testuser@example.com",
                        "is_active": True,
                        "avatar": "http://serverless-gpu-api.myzens.net/media/avatars/avatar-user-default.png",
                        "phone_number": "+123456789",
                        "created_at": "2023-01-01T00:00:00Z",
                        "updated_at": "2023-01-01T00:00:00Z",
                    },
                    "status": 200,
                    "message": USER_MESSAGES["get_user_success"]
                }
            },
        ),
        401: openapi.Response(
            description=USER_MESSAGES["auth_credentials_missing"],
            examples={
                "application/json": {
                    "data": {},
                    "status": 401,
                    "message": USER_MESSAGES["auth_credentials_missing"],
                }
            },
        ),
    },
)