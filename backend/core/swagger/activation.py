from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from core.messages import ERROR_MESSAGES, SUCCESS_MESSAGES
from core.serializers.activation import ActivationSerializer

activation_swagger_schema = swagger_auto_schema(
    operation_summary="Activate User Account",
    operation_description="Activates a user account using the provided token.",
    request_body=ActivationSerializer,
    responses={
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
)