from dj_rest_auth.registration.views import RegisterView
from core.serializers.user import CustomRegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from core.messages import ERROR_MESSAGES
from core.swagger.register import register_swagger_schema

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    @register_swagger_schema
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)