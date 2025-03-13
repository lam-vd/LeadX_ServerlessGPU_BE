from drf_yasg import openapi
from core.messages import ERROR_MESSAGES, SUCCESS_MESSAGES

activation_swagger_schema = {
    "operation_summary": "Activate User Account",
    "operation_description": "Activates a user account using the provided token.",
    "manual_parameters": [
        openapi.Parameter(
            name="token",
            in_=openapi.IN_QUERY,
            description="Activation token",
            type=openapi.TYPE_STRING,
            required=True,
        )
    ],
    "responses": {
        200: openapi.Response(
            description=SUCCESS_MESSAGES['account_activated'],
            examples={
                "application/json": {"detail": SUCCESS_MESSAGES['account_activated']}
            },
        ),
        400: openapi.Response(
            description=ERROR_MESSAGES['invalid_token'],
            examples={
                "application/json": {
                    "token": [ERROR_MESSAGES['invalid_token']]
                }
            },
        ),
    },
}