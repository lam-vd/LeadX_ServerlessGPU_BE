from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from core.models.payment_method import PaymentMethod
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
            return self._validation_error("payment_method_id", "This field is required.")

        try:
            self._ensure_stripe_customer(user)

            if self._is_card_already_attached(user, payment_method_id):
                return success_response(
                    data={},
                    message="Card is already attached.",
                    status_code=200
                )

            payment_method = self._attach_card_to_customer(user, payment_method_id)

            self._save_payment_method(user, payment_method)

            return success_response(
                data={},
                message="Card added successfully.",
                status_code=200
            )
        except stripe.error.StripeError as e:
            return self._stripe_error_response(e)
        except Exception as e:
            return error_response(
                errors={"unexpected_error": [str(e)]},
                message="An unexpected error occurred",
                status_code=500
            )

    def _validation_error(self, field, message):
        return error_response(
            errors={field: [message]},
            message="Validation error",
            status_code=400
        )

    def _ensure_stripe_customer(self, user):
        if not user.stripe_id:
            customer = stripe.Customer.create(email=user.email)
            user.stripe_id = customer["id"]
            user.save()

    def _is_card_already_attached(self, user, payment_method_id):
        existing_methods = stripe.PaymentMethod.list(customer=user.stripe_id, type="card")
        return any(pm.id == payment_method_id for pm in existing_methods.data)

    def _attach_card_to_customer(self, user, payment_method_id):
        stripe.PaymentMethod.attach(
            payment_method_id,
            customer=user.stripe_id,
        )
        stripe.Customer.modify(
            user.stripe_id,
            invoice_settings={"default_payment_method": payment_method_id},
        )
        return stripe.PaymentMethod.retrieve(payment_method_id)

    def _save_payment_method(self, user, payment_method):
        PaymentMethod.objects.filter(user=user).update(is_default=False)
        PaymentMethod.objects.create(
            user=user,
            stripe_payment_method_id=payment_method.id,
            brand=payment_method.card.brand,
            last4=payment_method.card.last4,
            exp_month=payment_method.card.exp_month,
            exp_year=payment_method.card.exp_year,
            is_default=True,
        )

    def _stripe_error_response(self, error):
        return error_response(
            errors={"stripe_error": [str(error)]},
            message="Stripe error",
            status_code=400
        )