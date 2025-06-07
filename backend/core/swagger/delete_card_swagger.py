from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

delete_card_responses = {
    200: openapi.Response(
        description="Card deleted successfully",
        examples={
            "application/json": {
                "data": {},
                "message": "card_deleted_successfully",
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
        description="Stripe error",
        examples={
            "application/json": {
                "errors": {"stripe_error": ["Stripe error details."]},
                "message": "stripe_error",
                "status": 400
            }
        }
    )
}

delete_card_swagger = swagger_auto_schema(
    operation_summary="Delete Card",
    operation_description="Delete a payment method from the authenticated user's account.",
    responses=delete_card_responses
)