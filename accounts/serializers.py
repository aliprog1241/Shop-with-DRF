
from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ("username", "email", "password")

    def validate_username(self, value):
        if " " in value:
            raise serializers.ValidationError("نام کاربری نباید فاصله داشته باشد.")
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
