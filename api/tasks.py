from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(username, email):
    send_mail(
        'Welcome!',
        f'Hello {username}, thank you for registering.',
        'from@example.com',
        [email],
        fail_silently=False,
    )

# This task sends a welcome email to the user after registration.
