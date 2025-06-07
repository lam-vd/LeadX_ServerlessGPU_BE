from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from core.messages import SUCCESS_MESSAGES, ERROR_MESSAGES

logout_response_200 = openapi.Response(
    description=SUCCESS_MESSAGES['logout_success'],
    examples={
        "application/json": {
            "data": {},
            "status": "success",
            "message": SUCCESS_MESSAGES['logout_success'],
        }
    },
)

logout_response_400 = openapi.Response(
    description=ERROR_MESSAGES['token_not_found'],
    examples={
        "application/json": {
            "data": {},
            "status": "error",
            "message": ERROR_MESSAGES['token_not_found'],
        }
    },
)

logout_swagger_schema = swagger_auto_schema(
    operation_summary="Logout",
    operation_description="Logout the currently authenticated user by deleting their authentication token.",
    responses={
        200: logout_response_200,
        400: logout_response_400,
    },
)