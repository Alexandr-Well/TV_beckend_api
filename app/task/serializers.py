from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """сериалацзер для задачь"""
    class Meta:
        model = Task
        fields = ('date', 'title', 'pk', 'name')
