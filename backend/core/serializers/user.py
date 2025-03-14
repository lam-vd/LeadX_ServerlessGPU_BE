from django.db import transaction
from rest_framework import serializers
from core.models.user import User
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from core.utils.email.activation_email import send_activation_email
from core.validators.username import validate_username, MAX_USERNAME_LENGTH
from core.validators.email import validate_email, MAX_EMAIL_LENGTH
from core.validators.password import validate_password

class CustomRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        max_length=MAX_USERNAME_LENGTH,
        validators=[validate_username],
    )
    email = serializers.EmailField(
        required=True,
        max_length=MAX_EMAIL_LENGTH,
        validators=[validate_email],
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )

    class Meta:
        model = User
        fields = ("username", "email", "password")

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()

        user.username = self.cleaned_data.get("username")
        user.email = self.cleaned_data.get("email")
        user.set_password(self.cleaned_data["password"])
        try: 
          with transaction.atomic():
            user.save()
            user.generate_activation_token()
            send_activation_email(user)
            setup_user_email(request, user, [])
        except Exception as e:
            raise serializers.ValidationError(str(e))
        return user

    def get_cleaned_data(self):
        return {
            "username": self.validated_data.get("username", ""),
            "email": self.validated_data.get("email", ""),
            "password": self.validated_data.get("password", ""),
        }

# API getUserView
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_active']