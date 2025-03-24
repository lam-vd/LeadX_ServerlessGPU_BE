from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers.change_password import ChangePasswordSerializer
from core.messages import SUCCESS_MESSAGES, ERROR_MESSAGES
from core.swagger.change_password import change_password_swagger_schema

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    @change_password_swagger_schema
    def post(self, request):
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data, context={'user': user})
        if serializer.is_valid():
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({
                'data': {},
                'status': status.HTTP_200_OK,
                'message': SUCCESS_MESSAGES['password_changed']
            }, status=status.HTTP_200_OK)

        return Response({
            'data': {},
            'status': status.HTTP_400_BAD_REQUEST,
            'message': ERROR_MESSAGES['validation_error'],
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)