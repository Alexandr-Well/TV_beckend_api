from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    """модель для задачь"""
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', verbose_name='user:')
    title = models.TextField(default="", verbose_name="task")
    date = models.CharField(max_length=256, verbose_name="crated at")
