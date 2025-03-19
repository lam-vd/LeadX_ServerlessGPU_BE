from rest_framework import serializers
from core.models.user import User
from core.messages import SUCCESS_MESSAGES, ERROR_MESSAGES
from django.utils.timezone import now

class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.UUIDField(required=True)
    password_new = serializers.CharField(write_only=True, required=True)
    password_confirmation = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        if data['password_new'] != data['password_confirmation']:
            raise serializers.ValidationError({"password_confirmation": ERROR_MESSAGES['password_mismatch']})
        try:
            user = User.objects.get(reset_password_token=data['token'])
            if user.reset_password_expiry < now():
                raise serializers.ValidationError({"token": ERROR_MESSAGES['token_expired']})
        except User.DoesNotExist:
            raise serializers.ValidationError({"token": ERROR_MESSAGES['invalid_token']})
        return data

    def save(self):
        token = self.validated_data['token']
        password_new = self.validated_data['password_new']
        user = User.objects.get(reset_password_token=token)
        user.set_password(password_new)
        user.reset_password_token = None
        user.reset_password_expiry = None
        user.save()
        return {
            "data": {},
            "status": "success",
            "message": SUCCESS_MESSAGES['password_reset_success']
        }