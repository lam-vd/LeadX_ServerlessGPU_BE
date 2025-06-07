from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from core.serializers.login_auth import CustomLoginSerializer
from core.serializers.user import UserSerializer
from core.swagger.login import login_swagger_schema
from core.utils.response_formatter import success_response, error_response

class CustomLoginView(APIView):
    @login_swagger_schema()
    def post(self, request, *args, **kwargs):
        serializer = CustomLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token = self.generate_user_token(user)
            user_data = self.get_user_data(user, token)
            return success_response(
                data=user_data,
                message="login_success",
                status_code=status.HTTP_200_OK
            )
        return error_response(
            errors=serializer.errors,
            message="invalid_credentials",
            status_code=status.HTTP_400_BAD_REQUEST
        )

    def generate_user_token(self, user):
        token, _ = Token.objects.get_or_create(user=user)
        return token

    def get_user_data(self, user, token):
        user_data = UserSerializer(user, context={"request": self.request}).data
        return {
            "token": token.key,
            "user": user_data
        }