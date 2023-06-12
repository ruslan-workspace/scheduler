from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=150, primary_key=True)
    telegram_id = models.PositiveIntegerField(blank=True, null=True, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.username} | {self.email} | {self.get_full_name()} "
