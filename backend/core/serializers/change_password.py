from rest_framework import serializers
from core.validators.password import validate_password

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_new_password = serializers.CharField(write_only=True, required=True)

    def validate_old_password(self, old_password):
        user = self.context['user']
        if not user.check_password(old_password):
            raise serializers.ValidationError('old_password_incorrect')
        return old_password

    def validate(self, data):
        user = self.context['user']
        self.validate_old_password(data['old_password'])
        if data['new_password'] != data['confirm_new_password']:
            raise serializers.ValidationError({"confirm_new_password": 'password_mismatch'})
        if user.check_password(data['new_password']):
            raise serializers.ValidationError({"new_password": 'password_same_as_old'})
        return data