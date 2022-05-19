from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """модель профиля, расширение юзера"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField('phone:', max_length=15)
    file = models.ImageField(upload_to='files/%Y/%m/%d/', null=True, blank=True)

    class META:
        verbose_name = 'Profiles'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user.username
