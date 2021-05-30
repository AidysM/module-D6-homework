from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver  # импортируем нужный декоратор
from django.core.mail import mail_managers, mail_admins
from .models import Post


# создаём функцию обработчик с параметрами под регистрацию сигнала
# в декоратор передаётся первым аргументом сигнал, на который будет реагировать эта функция, и
# в отправители надо передать также модель
@receiver(post_save, sender=Post)
def notify_managers_post(sender, instance, created, **kwargs):
    if created:
        subject = f'{instance.post_name} {instance.post_date.strftime("%d %m %Y")}'
    else:
        subject = f'Post changed for {instance.post_name} {instance.post_date.strftime("%d %m %Y")}'

    mail_managers(
        subject=subject,
        message=instance.content,
    )

    mail_admins(
        subject=subject,
        message=instance.content,
    )


@receiver(post_delete, sender=Post)
def notify_managers_post_canceled(sender, instance, **kwargs):
    subject = f'{instance.post_name} has canceled his post!'
    mail_managers(
        subject=subject,
        message=f'Canceled post for {instance.post_date.strftime("%d %m %Y")}',
    )

    print(subject)
