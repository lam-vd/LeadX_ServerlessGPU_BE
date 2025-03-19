from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from core.messages import SUCCESS_MESSAGES, ERROR_MESSAGES
from core.swagger.logout import logout_swagger_schema

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    @logout_swagger_schema
    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({
                'data': {},
                'status': 'success',
                'message': SUCCESS_MESSAGES['logout_success']
            }, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({
                'data': {},
                'status': 'error',
                'message': ERROR_MESSAGES['token_not_found']
            }, status=status.HTTP_400_BAD_REQUEST)