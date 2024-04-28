from rest_framework import serializers
from account.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    # we are writin to conform password 2 in registration request
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model= User
        fields= ['email', 'name', 'tc', 'password', 'password2']
        extra_kwargs= {
            'password': {'write_only': True}
        }

    # receiving and validating password and confirm password while registration
    # this validate funtion run when is_valid get execute in view.py
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError('password and confirm password doesnot match')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=200)
    class Meta:
        model = User
        fields = ["email", "password"]