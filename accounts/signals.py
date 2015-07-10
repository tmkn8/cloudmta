from django.dispatch import receiver
from django.db.models.signals import post_save, pre_init
from django.contrib.auth import get_user_model
from .models import Member

@receiver(pre_init, sender=Member)
def ensure_user_for_member_exists(sender, **kwargs):
    # Uruchom aktualizację użytkownika Django przy wywołaniu użytkownika z forum
    kwargs.get('instance').save_django_user()
