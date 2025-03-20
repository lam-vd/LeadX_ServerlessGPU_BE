import requests
from django.core.files.base import ContentFile
from django.contrib.auth import get_user_model
from allauth.account.models import EmailAddress
from rest_framework.authtoken.models import Token
from django.db import transaction
from core.utils.email.activation_email import send_activation_email
from core.serializers.user import UserSerializer
import logging
from urllib.parse import urlparse
import os

logger = logging.getLogger(__name__)

User = get_user_model()

class GoogleAuthService:
    @staticmethod
    def authenticate_google_user(token):
        try:
            response = requests.get(
                "https://www.googleapis.com/oauth2/v2/userinfo",
                headers={"Authorization": f"Bearer {token}"}
            )
            if response.status_code != 200:
                raise ValueError("Invalid Google access token")

            user_info = response.json()
            email = user_info.get("email")
            name = user_info.get("name", "GoogleUser")
            avatar_url = user_info.get("picture")
            if not email:
                raise ValueError("Email not found in Google response")

            existing_user = User.objects.filter(email=email).first()
            if existing_user:
                if existing_user.is_active:
                    token, _ = Token.objects.get_or_create(user=existing_user)
                    user_data = UserSerializer(existing_user).data
                    return token.key, user_data
                else:
                  raise ValueError("This email is already registered. Please log in using your credentials.")

            with transaction.atomic():
                user, created = User.objects.get_or_create(
                    email=email,
                    defaults={'username': name}
                )
                if created:
                    user.is_active = True
                    user.save()
                if avatar_url:
                    GoogleAuthService._save_avatar(user, avatar_url)
                email_address, email_created = EmailAddress.objects.get_or_create(
                    user=user,
                    email=user.email,
                    defaults={'verified': True}
                )
                if email_created:
                    email_address.verified = True
                    email_address.save()
                if not email_address.verified or not user.is_active:
                    send_activation_email(user)
                    raise Exception("User account is inactive. Activation email has been sent.")
                token, _ = Token.objects.get_or_create(user=user)

            user_data = UserSerializer(user).data
            return token.key, user_data
        except ValueError as e:
            logger.error(f"Google token validation failed: {str(e)}")
            raise ValueError(str(e))
        except Exception as e:
            logger.error(f"An unexpected error occurred: {str(e)}")
            raise Exception("An error occurred during Google authentication")

    @staticmethod
    def _save_avatar(user, avatar_url):
        try:
            avatar_response = requests.get(avatar_url)
            if avatar_response.status_code == 200:
                avatar_name = os.path.basename(urlparse(avatar_url).path)
                user.avatar.save(avatar_name, ContentFile(avatar_response.content), save=True)
        except Exception as e:
            logger.warning(f"Failed to save avatar for user {user.email}: {str(e)}")
