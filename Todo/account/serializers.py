from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    @staticmethod
    def validate_email(value):
        if not value:
            raise serializers.ValidationError("The email field is required.")
        else:
            return value

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)

        return user


class CustomLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError('Invalid Credentials')

        return {
            'user': user
        }
