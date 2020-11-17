from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField

import os
import uuid


def user_avatar_path(instance: 'Profile', filename: str):
    """
    Generates the path to save the user avatar file.
    The path is 'users/user_{uuid}/avatar{ext}',
    where {uuid} is the universally unique identifier of the user, and {ext} is the file extension.

    :param instance: Profile: An instance of the user profile.
    :param filename: str: The original name of the file.
    :return: str
    """
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
    """
    The function creates a Profile instance every time a User instance is created.

    :param sender:
    :param instance: User
    :param created:
    :param kwargs:
    :return:
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    The function saves a Profile instance every time a User instance is saved.

    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    instance.profile.save()
