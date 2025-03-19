from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers.forgot_password import ForgotPasswordSerializer
from core.serializers.reset_password import ResetPasswordSerializer
from core.messages import SUCCESS_MESSAGES
from core.swagger.password_reset import forgot_password_swagger_schema, reset_password_swagger_schema

class ForgotPasswordView(APIView):
    @forgot_password_swagger_schema
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data': {},
                'status': 'success',
                'message': SUCCESS_MESSAGES['password_reset_email_sent']
            }, status=status.HTTP_200_OK)
        return Response({
            'data': {},
            'status': 'error',
            'message': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordView(APIView):
    @reset_password_swagger_schema
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data': {},
                'status': 'success',
                'message': SUCCESS_MESSAGES['password_reset_success']
            }, status=status.HTTP_200_OK)
        return Response({
            'data': {},
            'status': 'error',
            'message': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)