from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

set_default_card_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=["payment_method_id"],
    properties={
        "payment_method_id": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="The ID of the payment method to set as default.",
            example="pm_1N2xY2P74YGSrBH5frvjVUEO"
        )
    }
)

set_default_card_responses = {
    200: openapi.Response(
        description="Default card set successfully",
        examples={
            "application/json": {
                "data": {},
                "message": "default_card_set_successfully",
                "status": 200
            }
        }
    ),
    404: openapi.Response(
        description="Card not found",
        examples={
            "application/json": {
                "errors": {"payment_method_id": ["Card not found."]},
                "message": "card_not_found",
                "status": 404
            }
        }
    ),
    400: openapi.Response(
        description="Validation error or Stripe error",
        examples={
            "application/json": {
                "errors": {"payment_method_id": ["This field is required."]},
                "message": "validation_error",
                "status": 400
            }
        }
    )
}

set_default_card_swagger = swagger_auto_schema(
    operation_summary="Set Default Card",
    operation_description="Set a payment method as the default card for the authenticated user.",
    request_body=set_default_card_request_body,
    responses=set_default_card_responses
)