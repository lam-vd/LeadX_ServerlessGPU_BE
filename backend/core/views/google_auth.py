from rest_framework.views import APIView
from rest_framework import status
from core.serializers.google_auth import GoogleAuthSerializer
from core.services.google_auth import GoogleAuthService
from core.serializers.user import UserSerializer
from core.utils.response_formatter import success_response, error_response

class GoogleLoginView(APIView):
    def post(self, request):
        serializer = GoogleAuthSerializer(data=request.data)
        if serializer.is_valid():
            try:
                token, user = GoogleAuthService.authenticate_google_user(serializer.validated_data['token'])
                user_data = UserSerializer(user, context={'request': request}).data
                return success_response(
                    data={'token': token, 'user': user_data},
                    message="google_login_success",
                    status_code=status.HTTP_200_OK
                )
            except ValueError:
                return error_response(
                    errors={},
                    message="invalid_data",
                    status_code=status.HTTP_400_BAD_REQUEST
                )
        return error_response(
            errors=serializer.errors,
            message="validation_error",
            status_code=status.HTTP_400_BAD_REQUEST
        )