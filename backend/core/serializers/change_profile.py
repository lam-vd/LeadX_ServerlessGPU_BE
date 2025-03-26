from rest_framework import serializers
from core.models.user import User
from core.validators.username import validate_username
from core.validators.profile_validators import validate_phone_number, validate_avatar
from django.conf import settings
import os

class UpdateProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=False,
        validators=[validate_username],
    )
    phone_number = serializers.CharField(
        required=False,
        allow_blank=True,
        validators=[validate_phone_number],
    )
    avatar = serializers.ImageField(
        required=False,
        validators=[validate_avatar],
    )

    class Meta:
        model = User
        fields = ['username', 'phone_number', 'avatar']
        extra_kwargs = {
            'username': {'required': False},
            'phone_number': {'required': False, 'allow_blank': True},
            'avatar': {'required': False},
        }

    def delete_old_avatar(self, avatar_path):
        if avatar_path and os.path.isfile(avatar_path):
            if os.path.basename(avatar_path) != settings.DEFAULT_AVATAR_PATH:
                os.remove(avatar_path)

    def update(self, instance, validated_data):
        if 'avatar' in validated_data:
            self.delete_old_avatar(instance.avatar.path if instance.avatar else None)
            instance.avatar = validated_data['avatar']
        if 'username' in validated_data:
            instance.username = validated_data['username']
        if 'phone_number' in validated_data:
            instance.phone_number = validated_data['phone_number']
        instance.save()
        return instance