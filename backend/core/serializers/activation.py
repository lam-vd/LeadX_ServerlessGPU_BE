from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from core.models.user import User
from core.messages import SUCCESS_MESSAGES, ERROR_MESSAGES

class ActivationSerializer(serializers.Serializer):
    token = serializers.UUIDField(required=True)

    def validate(self, data):
        try:
            user = User.objects.get(activation_token=data['token'])
            if user.is_active:
              return Response({"message": ERROR_MESSAGES['account_already_active']}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            raise serializers.ValidationError(ERROR_MESSAGES['invalid_token'])
        data['user'] = user
        return data

    def save(self):
        user = self.validated_data['user']
        user.is_active = True
        user.activation_token = user.generate_activation_token()
        user.save()
        return Response({"message": SUCCESS_MESSAGES['account_activated']}, status=status.HTTP_200_OK)