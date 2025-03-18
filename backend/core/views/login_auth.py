from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from core.serializers.login_auth import CustomLoginSerializer
from core.serializers.user import UserSerializer
from core.swagger.login import login_swagger_schema

class CustomLoginView(APIView):
    @login_swagger_schema()
    def post(self, request, *args, **kwargs):
        serializer = CustomLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token = self.generate_user_token(user)
            user_data = self.get_user_data(user, token)
            return Response(user_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def generate_user_token(self, user):
        try:
            token = Token.objects.get(user=user)
            return token
        except Token.DoesNotExist:
            return None

    def get_user_data(self, user, token):
        user_data = UserSerializer(user)
        return {
            "token": token.key,
            "user": user_data.data
        } 