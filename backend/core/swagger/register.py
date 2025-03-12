from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from core.messages import ERROR_MESSAGES
from core.serializers.user import CustomRegisterSerializer

register_swagger_schema = swagger_auto_schema(
    operation_description="Register a new user with username, email, and password.",
    request_body=CustomRegisterSerializer,
    responses={
        201: openapi.Response(
            description=ERROR_MESSAGES['user_registered_successfully'],
            examples={
                "application/json": {"detail": ERROR_MESSAGES['user_registered_successfully']}
            },
        ),
        400: openapi.Response(
            description=ERROR_MESSAGES['validation_error'],
            examples={
                "application/json": {"detail": ERROR_MESSAGES['validation_error']}
            },
        ),
    }
)