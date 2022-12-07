from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=127)
    birthdate = serializers.DateField()
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)
    is_employee = serializers.BooleanField()
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
