from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers.google_auth import GoogleAuthSerializer
from core.services.google_auth import GoogleAuthService
from core.messages import SUCCESS_MESSAGES, ERROR_MESSAGES

class GoogleLoginView(APIView):
    def post(self, request):
        serializer = GoogleAuthSerializer(data=request.data)
        if serializer.is_valid():
            try:
                token, user_data = GoogleAuthService.authenticate_google_user(serializer.validated_data['token'])
                return Response({
                    'data': {'token': token.key, 'user': user_data},
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
            'message': ERROR_MESSAGES['invalid_data']
        }, status=status.HTTP_400_BAD_REQUEST)