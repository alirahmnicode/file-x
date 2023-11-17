from django.utils.translation import gettext_lazy as _
from rest_framework import serializers, exceptions

from users.models import User
from .exceptions import UserExistsError


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(label=_("Username"), write_only=True)

    password = serializers.CharField(
        label=_("Password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )

    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        if not username or not password:
            raise exceptions.ValidationError("username and password must be set.")

        user = User.objects.filter(username=username).exists()
        if user:
            raise UserExistsError()

        return attrs

    def create(self, validated_data):
        username = validated_data.get("username")
        password = validated_data.get("password")

        user = User.objects.create_user(username=username, password=password)
        return user
