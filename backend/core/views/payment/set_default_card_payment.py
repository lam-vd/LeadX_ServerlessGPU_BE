from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from core.models.payment_method import PaymentMethod
from core.utils.response_formatter import success_response, error_response
from core.swagger.set_default_card_swagger import set_default_card_swagger
import stripe

class SetDefaultCardView(APIView):
    permission_classes = [IsAuthenticated]

    @set_default_card_swagger
    def post(self, request):
        user = request.user
        payment_method_id = request.data.get("payment_method_id")

        if not payment_method_id:
            return self._validation_error_response("payment_method_id", "This field is required.")

        try:
            payment_method = self._get_payment_method(user, payment_method_id)
            if not payment_method:
                return self._card_not_found_response()

            self._set_default_card_on_stripe(user, payment_method_id)

            self._update_default_card_in_db(user, payment_method)

            return self._default_card_set_response()
        except stripe.error.StripeError as e:
            return self._stripe_error_response(e)
        except Exception as e:
            return self._unexpected_error_response(e)

    def _get_payment_method(self, user, payment_method_id):
        return PaymentMethod.objects.filter(user=user, stripe_payment_method_id=payment_method_id).first()

    def _set_default_card_on_stripe(self, user, payment_method_id):
        stripe.Customer.modify(
            user.stripe_id,
            invoice_settings={"default_payment_method": payment_method_id},
        )

    def _update_default_card_in_db(self, user, payment_method):
        PaymentMethod.objects.filter(user=user).update(is_default=False)
        payment_method.is_default = True
        payment_method.save()

    def _validation_error_response(self, field, message):
        return error_response(
            errors={field: [message]},
            message="validation_error",
            status_code=400
        )

    def _card_not_found_response(self):
        return error_response(
            errors={"payment_method_id": ["Card not found."]},
            message="card_not_found",
            status_code=404
        )

    def _default_card_set_response(self):
        return success_response(
            data={},
            message="default_card_set_successfully",
            status_code=200
        )

    def _stripe_error_response(self, error):
        return error_response(
            errors={"stripe_error": [str(error)]},
            message="stripe_error",
            status_code=400
        )

    def _unexpected_error_response(self, error):
        return error_response(
            errors={"unexpected_error": [str(error)]},
            message="unexpected_error",
            status_code=500
        )