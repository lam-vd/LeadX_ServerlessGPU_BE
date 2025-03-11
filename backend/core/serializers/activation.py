from rest_framework import serializers
from core.models.user import User

class ActivationSerializer(serializers.Serializer):
    token = serializers.UUIDField(required=True)
    activation_code = serializers.CharField(required=True, max_length=6)

    def validate(self, data):
        try:
            user = User.objects.get(activation_token=data['token'], activation_code=data['activation_code'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid activation token or activation code.")
        return data

    def save(self):
        user = User.objects.get(activation_token=self.validated_data['token'], activation_code=self.validated_data['activation_code'])
        user.is_active = True
        user.is_staff = True
        user.activation_code = None
        user.activation_token = None
        user.save()
        return user