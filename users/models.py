from django.contrib.auth.base_user import BaseUserManager
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



class CustomUserManager(BaseUserManager):
    """Управление созданием пользователей"""
    def create_user(self, email, telegram_id, username, password=None,  **extra_fields):

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, telegram_id=telegram_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

