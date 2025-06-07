from rest_framework.views import APIView
from rest_framework import status
from core.serializers.activation import ActivationSerializer
from drf_yasg.utils import swagger_auto_schema
from core.swagger.activation import activation_swagger_schema
from core.utils.response_formatter import success_response, error_response

class ActivationView(APIView):
    @swagger_auto_schema(**activation_swagger_schema)
    def get(self, request):
        token = request.query_params.get('token')
        if not token:
            return error_response(
                errors={"token": ["missing_token"]},
                message="missing_token",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        serializer = ActivationSerializer(data={'token': token})
        if serializer.is_valid():
            serializer.save()
            return success_response(
                data={},
                message="account_activated",
                status_code=status.HTTP_200_OK
            )

        return error_response(
            errors=serializer.errors,
            message="invalid_token",
            status_code=status.HTTP_400_BAD_REQUEST
        )