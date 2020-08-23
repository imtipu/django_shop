from django.db.models import signals
from django.dispatch import receiver

from allauth.account.models import EmailConfirmation
from .models import *


@receiver(signals.post_save, sender=User)
def account_create_signal(sender, instance, created, *args, **kwargs):
    if created:
        print(instance.email, ': created')
