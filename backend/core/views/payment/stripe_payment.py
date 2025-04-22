from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from core.swagger.payment import add_card_swagger
from core.utils.response_formatter import success_response, error_response
import stripe

class AddCardView(APIView):
    permission_classes = [IsAuthenticated]

    @add_card_swagger
    def post(self, request):
        user = request.user
        payment_method_id = request.data.get("payment_method_id")

        if not payment_method_id:
            return error_response(
                errors={"payment_method_id": ["This field is required."]},
                message="Validation error",
                status_code=400
            )

        try:
            if not user.stripe_id:
                customer = stripe.Customer.create(email=user.email)
                user.stripe_id = customer["id"]
                user.save()

            existing_methods = stripe.PaymentMethod.list(customer=user.stripe_id, type="card")
            if any(pm.id == payment_method_id for pm in existing_methods.data):
                return success_response(
                    data={},
                    message="Card is already attached.",
                    status_code=200
                )

            stripe.PaymentMethod.attach(
                payment_method_id,
                customer=user.stripe_id,
            )

            stripe.Customer.modify(
                user.stripe_id,
                invoice_settings={"default_payment_method": payment_method_id},
            )

            return success_response(
                data={},
                message="Card added successfully.",
                status_code=200
            )
        except stripe.error.CardError as e:
            return error_response(
                errors={"stripe_error": [str(e)]},
                message="Card error",
                status_code=400
            )
        except stripe.error.InvalidRequestError as e:
            return error_response(
                errors={"stripe_error": [str(e)]},
                message="Invalid request",
                status_code=400
            )
        except stripe.error.AuthenticationError as e:
            return error_response(
                errors={"stripe_error": [str(e)]},
                message="Authentication error",
                status_code=400
            )
        except stripe.error.APIConnectionError as e:
            return error_response(
                errors={"stripe_error": [str(e)]},
                message="Network error",
                status_code=400
            )
        except stripe.error.StripeError as e:
            return error_response(
                errors={"stripe_error": [str(e)]},
                message="Stripe error",
                status_code=400
            )
        except Exception as e:
            return error_response(
                errors={"unexpected_error": [str(e)]},
                message="An unexpected error occurred",
                status_code=500
            )