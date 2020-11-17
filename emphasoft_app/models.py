from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField

import os
import uuid


def user_avatar_path(instance: 'Profile', filename: str):
    _, ext = os.path.splitext(filename)
    return "users/user_{uuid}/avatar{ext}".format(
        uuid=instance.user.profile.uuid,
        ext=ext,
    )


class Profile(models.Model):
    """
    The model extends the standard Django's user model with "avatar" and "bio" fields.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bio = models.TextField(max_length=1000, blank=True)
    avatar = ImageField(upload_to=user_avatar_path, null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
