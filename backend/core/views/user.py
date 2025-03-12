from dj_rest_auth.registration.views import RegisterView
from core.serializers.user import CustomRegisterSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework import status

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    @swagger_auto_schema(
        operation_description="Register a new user with username, email, and password.",
        request_body=CustomRegisterSerializer,
        responses={
            201: "User registered successfully.",
            400: "Validation error.",
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)