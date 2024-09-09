from django.contrib.auth import get_user_model
from djoser.serializers import (
    UserCreateSerializer as BaseUserCreateUserCreateSerializer,
)
from djoser.serializers import UserSerializer as BaseUserSerializer

user = get_user_model()


class UserCreateSerializer(BaseUserCreateUserCreateSerializer):
    class Meta(BaseUserCreateUserCreateSerializer.Meta):
        model = user
        fields = BaseUserCreateUserCreateSerializer.Meta.fields + ("phone_number", "email", "location", "address")


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = user
        fields = ["id", "first_name", "last_name", "username", "email", "phone_number", "location", "address"]
