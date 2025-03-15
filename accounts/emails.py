from django.core.mail import send_mail
import random 
from django.conf import settings
from .models import User

def send_otp_via_email(email):
    subject = "Your account verified email"
    otp = random.randint(1000, 9999)
    msg = f"Your OTP is: {otp}"
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, msg, email_from, [email])
    user_obj = User.objects.get(email = email)
    user_obj.otp = otp
    user_obj.save()