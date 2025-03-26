from rest_framework.views import APIView
from rest_framework import status
from core.serializers.forgot_password import ForgotPasswordSerializer
from core.serializers.reset_password import ResetPasswordSerializer
from core.swagger.password_reset import forgot_password_swagger_schema, reset_password_swagger_schema
from core.utils.response_formatter import success_response, error_response

class ForgotPasswordView(APIView):
    @forgot_password_swagger_schema
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(
                data={},
                message="password_reset_email_sent",
                status_code=status.HTTP_200_OK
            )
        return error_response(
            errors=serializer.errors,
            message="validation_error",
            status_code=status.HTTP_400_BAD_REQUEST
        )

class ResetPasswordView(APIView):
    @reset_password_swagger_schema
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(
                data={},
                message="password_reset_success",
                status_code=status.HTTP_200_OK
            )
        return error_response(
            errors=serializer.errors,
            message="validation_error",
            status_code=status.HTTP_400_BAD_REQUEST
        )