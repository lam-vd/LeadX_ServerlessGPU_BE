from drf_yasg import openapi
from core.messages import ERROR_MESSAGES, SUCCESS_MESSAGES

activation_swagger_schema = {
    "operation_summary": "Activate User Account",
    "operation_description": "Activates a user account using the provided token.",
    "manual_parameters": [
        openapi.Parameter(
            name="token",
            in_=openapi.IN_QUERY,
            description="Activation token sent via email.",
            type=openapi.TYPE_STRING,
            required=True,
            example="123e4567-e89b-12d3-a456-426614174000",
        )
    ],
    "responses": {
        200: openapi.Response(
            description=SUCCESS_MESSAGES['account_activated'],
            examples={
                "application/json": {
                    "message": SUCCESS_MESSAGES['account_activated']
                }
            },
        ),
        400: openapi.Response(
            description="Invalid or missing token.",
            examples={
                "application/json": {
                    "error": ERROR_MESSAGES['invalid_token']
                }
            },
        ),
    },
}