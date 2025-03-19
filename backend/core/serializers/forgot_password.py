from rest_framework import serializers
from core.models.user import User
from core.utils.email.activation_password import send_reset_password_email
from core.messages import SUCCESS_MESSAGES, ERROR_MESSAGES

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
            if not user.is_active:
                raise serializers.ValidationError(ERROR_MESSAGES['account_inactive'])
        except User.DoesNotExist:
            raise serializers.ValidationError(ERROR_MESSAGES['email_not_found'])
        return value

    def save(self):
        email = self.validated_data['email']
        user = User.objects.get(email=email)
        user.generate_reset_password_token()
        send_reset_password_email(user)
        return {
            "data": {},
            "status": "success",
            "message": SUCCESS_MESSAGES['password_reset_email_sent']
        }