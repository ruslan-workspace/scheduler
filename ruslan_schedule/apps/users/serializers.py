from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password' : {'write_only' : True}}

    def validate_password(self, password):
        validate_password(password=password)
        return password
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    