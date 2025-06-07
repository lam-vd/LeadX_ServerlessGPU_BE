from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from core.models.payment_method import PaymentMethod
from core.utils.response_formatter import success_response
from core.swagger.get_cards_swagger import get_cards_swagger

class GetCardsView(APIView):
    permission_classes = [IsAuthenticated]

    @get_cards_swagger
    def get(self, request):
        user = request.user
        payment_methods = self._get_payment_methods(user)

        if not payment_methods:
            return self._no_cards_response()

        cards = self._format_cards(payment_methods)
        return self._cards_response(cards)

    def _get_payment_methods(self, user):
        return PaymentMethod.objects.filter(user=user)

    def _no_cards_response(self):
        return success_response(
            data={"cards": []},
            message="no_cards_found",
            status_code=200
        )

    def _format_cards(self, payment_methods):
        return [
            {
                "id": payment.stripe_payment_method_id,
                "brand": payment.brand,
                "last4": payment.last4,
                "exp_month": payment.exp_month,
                "exp_year": payment.exp_year,
                "is_default": payment.is_default,
            }
            for payment in payment_methods
        ]

    def _cards_response(self, cards):
        return success_response(
            data={"cards": cards},
            message="cards_retrieved_successfully",
            status_code=200
        )