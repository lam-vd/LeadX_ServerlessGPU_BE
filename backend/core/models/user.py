from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from datetime import timedelta
from django.utils.timezone import now
import uuid
import os

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

def user_avatar_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"user_{instance.id}_{uuid.uuid4().hex}.{ext}"
    return os.path.join('avatars', now().strftime('%Y/%m'), filename)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True, null=True, unique=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    billing_address = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to=user_avatar_upload_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    activation_token = models.UUIDField(default=uuid.uuid4, unique=True, null=True, blank=True)
    reset_password_token = models.UUIDField(default=None, null=True, blank=True, unique=True)
    reset_password_expiry = models.DateTimeField(default=None, null=True, blank=True)
    stripe_id = models.CharField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def generate_activation_token(self):
        self.activation_token = uuid.uuid4()
        self.save()
    def generate_reset_password_token(self):
        self.reset_password_token = uuid.uuid4()
        self.reset_password_expiry = now() + timedelta(hours=1)
        self.save()