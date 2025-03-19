from rest_framework import serializers
from django.contrib.auth import authenticate
from django.core.validators import validate_email as django_validate_email
from core.models.user import User
from core.messages import ERROR_MESSAGES
from core.validators.email import MAX_EMAIL_LENGTH
from core.validators.password import validate_password

class CustomLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if len(email) > MAX_EMAIL_LENGTH:
            raise serializers.ValidationError({"email": ERROR_MESSAGES['email_too_long']})

        try:
            django_validate_email(email)
        except serializers.ValidationError:
            raise serializers.ValidationError({"email": ERROR_MESSAGES['email_invalid']})

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({"email": ERROR_MESSAGES['incorrect_email']})

        user = authenticate(username=email, password=password)
        if not user:
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError({"password": ERROR_MESSAGES['incorrect_password']})
            raise serializers.ValidationError({"detail": ERROR_MESSAGES['invalid_credentials']})

        if not user.is_active:
            raise serializers.ValidationError({"detail": ERROR_MESSAGES['account_inactive']})

        data["user"] = user
        return data