from dj_rest_auth.registration.views import RegisterView
from core.serializers.user import CustomRegisterSerializer, UserSerializer
from core.swagger.register import register_swagger_schema
from django.http import JsonResponse
from django.middleware.csrf import get_token
from core.messages import SUCCESS_MESSAGES, ERROR_MESSAGES, USER_MESSAGES
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

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
            return JsonResponse({
                'data': {},
                'status': 'success',
                'message': SUCCESS_MESSAGES['user_registered_successfully']
            }, status=status.HTTP_201_CREATED)
        return JsonResponse({
            'data': {},
            'status': 'error',
            'message': ERROR_MESSAGES['registration_failed'],
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class GetUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response({
            'data': serializer.data,
            'status': 'success',
            'message': USER_MESSAGES['get_user_success']
        }, status=200)