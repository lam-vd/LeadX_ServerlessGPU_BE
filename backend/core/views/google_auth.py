from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers.google_auth import GoogleAuthSerializer
from core.services.google_auth import GoogleAuthService

class GoogleLoginView(APIView):
    def post(self, request):
        serializer = GoogleAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            token, user = GoogleAuthService.authenticate_google_user(serializer.validated_data['token'])
            return Response({
                'token': token,
                'user': {
                    'username': user.username,
                    'email': user.email,
                    'is_active': user.is_active,
                    'avatar': user.avatar,
                    'phone_number': user.phone_number,
                    'created_at': user.created_at,
                    'updated_at': user.updated_at,
                }
            }, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)