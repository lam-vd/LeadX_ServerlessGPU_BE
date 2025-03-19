from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from urllib.parse import urljoin

def send_reset_password_email(user):
    subject = "Reset Your Password"
    base_url = settings.REACT_APP_API_URL
    reset_password_path = f"/reset-password/?token={user.reset_password_token}"
    reset_password_url = urljoin(base_url, reset_password_path)
    html_message = render_to_string("reset_password_email.html", {
        "username": user.username,
        "action_url": reset_password_url,
    })

    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]

    send_mail(
        subject,
        "",
        from_email,
        recipient_list,
        html_message=html_message,
    )