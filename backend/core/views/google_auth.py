from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers.google_auth import GoogleAuthSerializer
from core.services.google_auth import GoogleAuthService
from core.serializers.user import UserSerializer
from core.messages import SUCCESS_MESSAGES, ERROR_MESSAGES

class GoogleLoginView(APIView):
    def post(self, request):
        serializer = GoogleAuthSerializer(data=request.data)
        if serializer.is_valid():
            try:
                token, user = GoogleAuthService.authenticate_google_user(serializer.validated_data['token'])
                user_data = UserSerializer(user, context={'request': request}).data
                return Response({
                    'data': {'token': token, 'user': user_data},
                    'status': 'success',
                    'message': SUCCESS_MESSAGES['google_login_success']
                }, status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({
                    'data': {},
                    'status': 'error',
                    'message': str(e)
                }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'data': {},
            'status': 'error',
            'message': ERROR_MESSAGES['invalid_data'],
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)