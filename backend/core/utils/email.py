from django.core.mail import send_mail
from django.conf import settings

def send_activation_email(user):
    subject = "Activate Your Account"
    activation_url = f"http://localhost:8001/api/auth/activate/?token={user.activation_token}"
    message = f"Hi {user.username},\n\nYour activation code is: {user.activation_code}\n\nPlease use this code to activate your account to link:\n{activation_url}\n"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)