from rest_framework import serializers
from core.models.user import User
from core.utils.email.activation_password import send_reset_password_email

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.CharField(write_only=True)

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
            if not user.is_active:
                raise serializers.ValidationError('account_inactive')
        except User.DoesNotExist:
            raise serializers.ValidationError('email_not_found')
        return value

    def save(self):
        email = self.validated_data['email']
        user = User.objects.get(email=email)
        user.generate_reset_password_token()
        send_reset_password_email(user)
        return {
            "data": {},
            "status": "success",
            "message": 'password_reset_email_sent'
        }