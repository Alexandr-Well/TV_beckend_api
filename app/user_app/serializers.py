from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    """сериалацзер для расширения юзера профилем"""
    class Meta:
        model = Profile
        fields = ('phone', 'file')


class UserSerializer(serializers.ModelSerializer):
    """сериалацзер для юзера"""
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ("is_active",
                  "is_staff",
                  "is_superuser",
                  "email",
                  "profile",
                  "last_name",
                  "first_name",
                  "last_login",
                  "username",
                  'pk',
                  # 'password'
                  )

