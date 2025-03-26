from dj_rest_auth.registration.views import RegisterView
from core.serializers.user import CustomRegisterSerializer, UserSerializer
from core.swagger.register import register_swagger_schema
from django.http import JsonResponse
from django.middleware.csrf import get_token
from core.messages import SUCCESS_MESSAGES, ERROR_MESSAGES, USER_MESSAGES
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from core.utils.response_formatter import success_response, error_response
from core.swagger.user import register_swagger_schema, get_user_swagger_schema

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    @register_swagger_schema
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return success_response(
                data={},
                message=SUCCESS_MESSAGES['user_registered_successfully'],
                status_code=status.HTTP_201_CREATED
            )
        return error_response(
            errors=serializer.errors,
            message=ERROR_MESSAGES['registration_failed'],
            status_code=status.HTTP_400_BAD_REQUEST
        )

class GetUserView(APIView):
    permission_classes = [IsAuthenticated]

    @get_user_swagger_schema
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return success_response(
            data=serializer.data,
            message=USER_MESSAGES['get_user_success'],
            status_code=status.HTTP_200_OK
        )