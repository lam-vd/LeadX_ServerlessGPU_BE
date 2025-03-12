from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from core.models.user import User
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from core.utils.email import send_activation_email

class CustomRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("A user is already registered with this email address.")
        return email

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()

        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.set_password(self.cleaned_data["password"])
        user.save()

        user.generate_activation_code()
        user.generate_activation_token()
        send_activation_email(user)
        setup_user_email(request, user, [])
        return user

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'email': self.validated_data.get('email', ''),
            'password': self.validated_data.get('password', ''),
        }