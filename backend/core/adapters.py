from allauth.account.adapter import DefaultAccountAdapter
from django.http import JsonResponse

class CustomAccountAdapter(DefaultAccountAdapter):
    def respond_user_inactive(self, request, user):
        return JsonResponse({"detail": "Your account is inactive. Please contact support."}, status=403)