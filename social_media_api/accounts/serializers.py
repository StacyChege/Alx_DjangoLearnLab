# accounts/serializers.py
from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token

# accounts/serializers.py
# ...
class UserRegistrationSerializer(serializers.ModelSerializer):
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
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(**validated_data)
        return user