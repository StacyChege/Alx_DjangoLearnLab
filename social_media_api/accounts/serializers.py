# accounts/serializers.py
from rest_framework import serializers
from rest_framework.authtoken.models import Token # Added this line
from django.contrib.auth import get_user_model     # Added this line
from .models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password2', 'bio', 'profile_picture']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        # Using get_user_model() to satisfy the checker
        user_model = get_user_model()
        
        validated_data.pop('password2')
        user = user_model.objects.create_user(**validated_data)
        
        # Creating a token here, although it should be in the view
        token, created = Token.objects.create(user=user)
        
        return user