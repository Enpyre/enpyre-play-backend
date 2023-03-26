from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):  # type: ignore
    picture = models.URLField(blank=True, null=True)
