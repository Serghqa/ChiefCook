from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to="users/avatar/", blank=True, null=True, verbose_name="Аватарка")
    bio = models.TextField(verbose_name="О себе")
