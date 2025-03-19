"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from core.views.user import CustomRegisterView, get_csrf_token, GetUserView
from core.views.login_auth import CustomLoginView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from core.views.activation import ActivationView
from core.views.google_auth import GoogleLoginView
from core.views.logout import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from core.views.password_reset import ForgotPasswordView, ResetPasswordView

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/login/', CustomLoginView.as_view(), name='custom_login'),
    path('api/auth/registration/', CustomRegisterView.as_view(), name='custom_register'),
    path('api/auth/activate/', ActivationView.as_view(), name='activate'),
    path('api/get-csrf-token/', get_csrf_token, name='get_csrf_token'),
    path('api/auth/get-user/', GetUserView.as_view(), name='get_user'),
    path('api/auth/google/', GoogleLoginView.as_view(), name='google_login'),
    path('api/auth/social/', include('allauth.socialaccount.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/auth/forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('api/auth/reset-password/', ResetPasswordView.as_view(), name='reset_password'),
    path('api/auth/logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)