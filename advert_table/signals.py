from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import *
from django.contrib.auth.models import User

@receiver(post_save, sender=Comments)
def new_comment_notify(sender, instance, created, **kwargs):
    if created:
        for user in User.objects.all():
            if user == instance.to_post.author.identity:
                html_content = render_to_string(
                    'notification.html',
                    {
                        'instance': instance,
                        'username': user.username,
                    }
                )
                msg = EmailMultiAlternatives(
                    subject=f'New comment to post {instance.to_post}',
                    body=f'{instance.text}',
                    from_email='arahna.aurum@yandex.ru',
                    to=[f'{user.email}'],
                )
                msg.attach_alternative(html_content, "text/html")

                msg.send()
    else:
        for user in User.objects.all():
            if user == instance.from_user:
                html_content = render_to_string(
                    'comment_accepted.html',
                    {
                         'instance': instance,
                    }
                )

                msg = EmailMultiAlternatives(
                    subject=f'Your comment to post {instance.to_post} was accepted',
                    body=instance.text,
                    from_email='arahna.aurum@yandex.ru',
                    to=[f'{instance.from_user.email} '],
                )
                msg.attach_alternative(html_content, "text/html")  # добавляем html

                msg.send()