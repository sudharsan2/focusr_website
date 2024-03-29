from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.models import User  
from django.conf import settings
from .models import enquery,apply
import time

@receiver(post_save, sender=enquery)
def send_email_on_new_object(sender, instance, created, **kwargs):
    if created:
        # Send email when a new object is created
        subject = 'New Object Added'
        message = f"New object added with the following details:\n\n"
        message+= f"name: {instance.full_Name}\n"
        message += f"email id: {instance.email}\n"
        message += f"about: {instance.about}\n"
        # Add more fields as needed
        email_ad = instance.email
        html_message = render_to_string('app1/clientResponse.html', {'instance': instance})

        to_email = 'sudharsanselvam2@gmail.com'  # replace with the recipient's email address

        # Send the email
        send_mail(subject, message, 'sudharsanmac02@gmai.com', [to_email])
        send_mail(subject, '', 'sudharsanmac02@gmai.com', [email_ad],html_message=html_message)


@receiver(post_save, sender=apply)
def send_email_on_new_object(sender, instance, created, **kwargs):
    if created:
        # Send email when a new object is created
        subject = 'New Object Added'
        message = f"New object added with the following details:\n\n"
        message+= f"name: {instance.first_Name} {instance.last_Name}\n"
        message += f"email id: {instance.email}\n"
        message += f"about: {instance.mobile}\n" 
        message += f"about: {instance.notice_Period}\n" 
        message += f"about: {instance.years_Of_Experience}\n" 
        message += f"about: {instance.skills}\n" 
        
        # Add more fields as needed
        email_ad = instance.email
        html_message = render_to_string('app1/employeeResponse.html', {'instance': instance})
        to_email = 'sudharsanselvam2@gmail.com'  # replace with the recipient's email address

        # Send the email
        send_mail(subject, message, 'sudharsanmac02@gmai.com', [to_email])
        send_mail(subject, '', 'sudharsanmac02@gmai.com', [email_ad],html_message=html_message)

