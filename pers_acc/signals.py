from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import *
from django.contrib.auth.models import User

@receiver(post_save, sender=OneTimeCode)
def otc_send(sender, instance, **kwargs):
    html_content = render_to_string(
        'otc.html',
        {
            'instance': instance,
        }
    )
    msg = EmailMultiAlternatives(
        subject=f'Registration on Ads Portal',
        body=f'{instance}',
        from_email='arahna.aurum@yandex.ru',
        to=[f'{instance.email}'],
    )
    msg.attach_alternative(html_content, "text/html")

    msg.send()