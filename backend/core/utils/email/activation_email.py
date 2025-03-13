from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

def send_activation_email(user):
    subject = "Activate Your Account"
    url = settings.REACT_APP_API_URL
    activation_url = f"{url}/auth/activate/?token={user.activation_token}"

    html_message = render_to_string("activation_email.html", {
        "username": user.username,
        "activation_url": activation_url,
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