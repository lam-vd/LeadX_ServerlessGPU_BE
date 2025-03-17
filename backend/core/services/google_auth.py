from google.oauth2 import id_token
from google.auth.transport import requests
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress
from rest_framework.authtoken.models import Token
from django.db import transaction
from core.utils.email.activation_email import send_activation_email
import logging

logger = logging.getLogger(__name__)

class GoogleAuthService:
    @staticmethod
    def authenticate_google_user(token):
        try:
            idinfo = id_token.verify_oauth2_token(token, requests.Request())
            email = idinfo.get('email')
            name = idinfo.get('name', 'GoogleUser')
            with transaction.atomic():
                user, created = User.objects.get_or_create(
                    email=email,
                    defaults={'username': name}
                )
                if created:
                    user.is_active = True
                    user.save()
                email_address, email_created = EmailAddress.objects.get_or_create(
                    user=user,
                    email=user.email,
                    defaults={'verified': True}
                )
                if email_created:
                    email_address.verified = True
                    email_address.save()
                if not email_address.verified:
                    send_activation_email(user)
                if not user.is_active:
                    send_activation_email(user)
                    raise Exception("User account is inactive. Activation email has been sent.")
                token, _ = Token.objects.get_or_create(user=user)

            return token.key, user
        except ValueError as e:
            logger.error(f"Google token validation failed: {str(e)}")
            raise ValueError("Invalid Google Token")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {str(e)}")
            raise Exception("An error occurred during Google authentication")