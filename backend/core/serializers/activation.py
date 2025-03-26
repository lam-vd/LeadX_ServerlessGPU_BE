from rest_framework import serializers
from allauth.account.models import EmailAddress
from core.models.user import User

class ActivationSerializer(serializers.Serializer):
    token = serializers.UUIDField(required=True)

    def validate(self, data):
        try:
            user = User.objects.get(activation_token=data['token'])
            if user.is_active:
                raise serializers.ValidationError('account_already_active')
            email_address = EmailAddress.objects.filter(user=user, email=user.email).first()
            if not email_address:
              raise serializers.ValidationError('email_not_found')
            if email_address.verified:
                raise serializers.ValidationError('email_already_verified')
        except User.DoesNotExist:
            raise serializers.ValidationError('invalid_token')
        data['user'] = user
        data['email_address'] = email_address
        return data

    def save(self):
        user = self.validated_data['user']
        email_address = self.validated_data['email_address']
        user.is_active = True
        user.activation_token = user.generate_activation_token()
        user.save()
        email_address.verified = True
        email_address.save()
        return {"message": 'account_activated'}