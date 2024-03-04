from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    login = models.CharField(max_length=100, **NULLABLE, verbose_name='login', unique=True)
    username = models.CharField(max_length=100, **NULLABLE, verbose_name='username')
    number = models.CharField(max_length=100, **NULLABLE, verbose_name='number')
    birthdate = models.DateField(**NULLABLE, verbose_name='birthdate')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at', **NULLABLE)
    password = models.CharField(max_length=100, **NULLABLE, verbose_name='password')

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

