from dj_rest_auth.registration.views import RegisterView
from core.serializers.user import CustomRegisterSerializer
from core.swagger.register import register_swagger_schema
from django.http import JsonResponse
from django.middleware.csrf import get_token

def get_csrf_token(request):
  csrf_token = get_token(request)
  return JsonResponse({'csrfToken': csrf_token})

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    @register_swagger_schema
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)