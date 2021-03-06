from django.contrib.auth import authenticate

from rest_framework_jwt.settings import api_settings
from rest_framework import serializers

from .models import *

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=50)
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(max_length=300, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)

        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email':user.email+' '+str(user.id),
            'token': jwt_token
        }


class UserListAndDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'email',
            'gender',
            'type'
        )