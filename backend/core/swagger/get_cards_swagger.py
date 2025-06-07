from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

get_cards_response_200_with_cards = openapi.Response(
    description="List of cards retrieved successfully",
    examples={
        "application/json": {
            "data": {
                "cards": [
                    {
                        "id": "pm_1N2xY2P74YGSrBH5frvjVUEO",
                        "brand": "visa",
                        "last4": "4242",
                        "exp_month": 12,
                        "exp_year": 2026,
                        "is_default": True,
                    }
                ]
            },
            "message": "cards_retrieved_successfully",
            "status": 200
        }
    }
)

get_cards_response_200_no_cards = openapi.Response(
    description="No cards found",
    examples={
        "application/json": {
            "data": {
                "cards": []
            },
            "message": "no_cards_found",
            "status": 200
        }
    }
)

get_cards_swagger = swagger_auto_schema(
    operation_summary="Get User's Payment Cards",
    operation_description="Retrieve the list of payment cards linked to the authenticated user's account. If no cards are found, an empty list will be returned.",
    responses={
        200: get_cards_response_200_with_cards,
        200: get_cards_response_200_no_cards,
    }
)