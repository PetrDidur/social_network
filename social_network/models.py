from django.conf import settings
from django.db import models

from users.models import NULLABLE


class Post(models.Model):
    header = models.CharField(max_length=150, verbose_name='header', **NULLABLE)
    text = models.TextField(verbose_name='text')
    image = models.ImageField(upload_to='posts/', verbose_name='image', **NULLABLE)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='author', **NULLABLE)
    comment = models.TextField(verbose_name='comment', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at', **NULLABLE)
    edited_at = models.DateTimeField(auto_now=True, verbose_name='edited_at', **NULLABLE)

    def __str__(self):
        return f"{self.header} - {self.author}"

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='author', **NULLABLE)
    text = models.TextField(verbose_name='text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at', **NULLABLE)
    edited_at = models.DateTimeField(auto_now=True, verbose_name='edited_at')

    def __str__(self):
        return f"{self.text} - {self.author}"

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'


