from dj_rest_auth.registration.views import RegisterView
from core.serializers.user import CustomRegisterSerializer
from core.swagger.register import register_swagger_schema
from django.http import JsonResponse
from django.middleware.csrf import get_token
from core.messages import SUCCESS_MESSAGES
from rest_framework import status

def get_csrf_token(request):
  csrf_token = get_token(request)
  return JsonResponse({'csrfToken': csrf_token})

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    @register_swagger_schema
    def post(self, request, *args, **kwargs):
        response =  super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            return JsonResponse(
                {
                    "status": "success",
                    "message": SUCCESS_MESSAGES['user_registered_successfully'],
                    "redirect_to": "/login",
                },
                status=status.HTTP_201_CREATED
            )
        return response