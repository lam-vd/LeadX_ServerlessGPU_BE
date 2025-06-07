from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from core.utils.response_formatter import success_response, error_response
from core.swagger.logout import logout_swagger_schema

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    @logout_swagger_schema
    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return success_response(
                data={},
                message="logout_success",
                status_code=status.HTTP_200_OK
            )
        except Token.DoesNotExist:
            return error_response(
                errors={},
                message="token_not_found",
                status_code=status.HTTP_400_BAD_REQUEST
            )