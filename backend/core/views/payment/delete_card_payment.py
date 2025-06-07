from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from core.models.payment_method import PaymentMethod
from core.utils.response_formatter import success_response, error_response
from core.swagger.delete_card_swagger import delete_card_swagger
import stripe

class DeleteCardView(APIView):
    permission_classes = [IsAuthenticated]

    @delete_card_swagger
    def delete(self, request, payment_method_id):
        user = request.user

        try:
            payment_method = self._get_payment_method(user, payment_method_id)
            if not payment_method:
                return self._card_not_found_response()
            self._detach_card_from_stripe(payment_method_id)
            self._delete_payment_method(payment_method)

            return self._card_deleted_response()
        except stripe.error.StripeError as e:
            return self._stripe_error_response(e)
        except Exception as e:
            return self._unexpected_error_response(e)

    def _get_payment_method(self, user, payment_method_id):
        return PaymentMethod.objects.filter(user=user, stripe_payment_method_id=payment_method_id).first()

    def _detach_card_from_stripe(self, payment_method_id):
        stripe.PaymentMethod.detach(payment_method_id)

    def _delete_payment_method(self, payment_method):
        payment_method.delete()

    def _card_not_found_response(self):
        return error_response(
            errors={"payment_method_id": ["Card not found."]},
            message="card_not_found",
            status_code=404
        )

    def _card_deleted_response(self):
        return success_response(
            data={},
            message="card_deleted_successfully",
            status_code=200
        )

    def _stripe_error_response(self, error):
        """Xử lý lỗi từ Stripe."""
        return error_response(
            errors={"stripe_error": [str(error)]},
            message="stripe_error",
            status_code=400
        )

    def _unexpected_error_response(self, error):
        """Xử lý lỗi không mong muốn."""
        return error_response(
            errors={"unexpected_error": [str(error)]},
            message="unexpected_error",
            status_code=500
        )