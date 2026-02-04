from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(unique=True, max_length=50, verbose_name='Username')
    email = models.EmailField(unique=True, verbose_name='Email')
    telegram_id = models.IntegerField(unique=True, verbose_name='Telegram ID')




    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'